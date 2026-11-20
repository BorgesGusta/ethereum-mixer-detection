"""EXP-06C: busca limitada de logs Withdrawn historicos, sem atribuir rótulos.
A API V1 de logs usa topic0 e intervalos de blocos pre-registrados;
valida candidatos em transacao e receipt/logs V2, sem arquivo RPC.
"""
from __future__ import annotations
import argparse, hashlib, json, pathlib, requests
from datetime import datetime, timezone

POOL='0xf241d57c6debae225c0f2e6ea1529373c9a9c9fb'
WITHDRAW_TOPIC='0x75e161b3e824b114fc1a33274bd7091918dd4e639cede50b78b15a4eea956a21'
RAGEQUIT_TOPIC='0xd2b3e868ae101106371f2bd93abc8d5a4de488b9fe47ed122c23625aa7172f13'
EXP06B_SHA='61e60f28fd23af38e09f8ae2a6ae23d56699536e2667f7d0d1f875adebbc207f'
BASE='https://eth.blockscout.com'
# Recortes diagnosticos, escolhidos antes da coleta: nao sao holdout de ML.
WINDOWS=[('pos_implantacao_2025',22153714,22253714),('vizinhanca_dia_teste_2026',24233073,24240273)]
MAX_REQUESTS_PER_WINDOW=24
MAX_CANDIDATES_PER_WINDOW=2
CHUNK=10000

def sha(path):return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
def a(v):return str(v.get('hash','') if isinstance(v,dict) else v or '').lower()
def get(session,url,params=None):
    try:
        x=session.get(url,params=params,timeout=35,headers={'User-Agent':'AcademicAudit-EXP06C/1.0'})
        if x.status_code!=200:return {'ok':False,'http':x.status_code,'error':'HTTP_'+str(x.status_code)}
        try:body=x.json()
        except ValueError:return {'ok':False,'http':200,'error':'not_json'}
        return {'ok':True,'http':200,'body':body}
    except requests.RequestException as e:return {'ok':False,'http':None,'error':type(e).__name__}

def lookup_logs(s,lo,hi):
    params={'module':'logs','action':'getLogs','fromBlock':lo,'toBlock':hi,'address':POOL,'topic0':WITHDRAW_TOPIC}
    z=get(s,BASE+'/api',params)
    out={'from':lo,'to':hi,'http':z.get('http')}
    if not z['ok']:return {**out,'status':'api_error','error':z.get('error'),'items':[]}
    body=z['body']
    if not isinstance(body,dict):return {**out,'status':'schema_error','items':[]}
    result=body.get('result');message=str(body.get('message',''));status=str(body.get('status',''))
    if isinstance(result,list):
        if len(result)>=1000:return {**out,'status':'truncation_possible','n':len(result),'items':result}
        return {**out,'status':'ok','n':len(result),'items':result}
    if status=='0' and isinstance(result,str) and ('no record' in result.lower() or 'no log' in result.lower() or 'no transaction' in result.lower()):
        return {**out,'status':'empty','n':0,'items':[]}
    return {**out,'status':'ambiguous_response','message':message,'response_status':status,'error':str(result)[:200],'items':[]}

def txhash(item):
    return a(item.get('transactionHash') or item.get('transaction_hash') or item.get('tx_hash'))

def inspect_tx(s,tx_hash,expected_block):
    x=get(s,BASE+'/api/v2/transactions/'+tx_hash)
    row={'tx_hash':tx_hash,'api_http':x.get('http'),'tx_api_ok':x['ok'],'bloco_esperado':expected_block,'confirmed_withdraw_log':False}
    if not x['ok']:row['erro']=x.get('error');return row
    d=x['body'];row.update({'bloco_retornado':d.get('block_number'),'status_tx':d.get('status'),'to':a(d.get('to'))})
    if str(d.get('block_number'))!=str(expected_block) or str(d.get('status')).lower() not in ('ok','success'):
        row['erro']='tx_bloco_ou_status_divergente';return row
    z=get(s,BASE+'/api/v2/transactions/'+tx_hash+'/logs');row['logs_http']=z.get('http')
    if not z['ok']:row['erro']='logs_'+str(z.get('error'));return row
    body=z['body'];items=body.get('items') if isinstance(body,dict) else None
    if not isinstance(items,list):row['erro']='logs_schema';return row
    page_complete=not body.get('next_page_params')
    matches=[i for i in items if isinstance(i,dict) and a(i.get('address'))==POOL and
             isinstance(i.get('topics'),list) and i.get('topics') and str(i['topics'][0]).lower()==WITHDRAW_TOPIC]
    row.update({'logs_pagina_completa':page_complete,'logs_pagina_recebidos':len(items),'logs_withdraw_do_pool':len(matches),
                'confirmed_withdraw_log':page_complete and bool(matches)})
    if not page_complete:row['erro']='logs_tx_paginados_nao_completos'
    return row

def main():
    p=argparse.ArgumentParser();p.add_argument('--exp06b',type=pathlib.Path,required=True);p.add_argument('--saida',type=pathlib.Path,required=True);args=p.parse_args()
    if args.saida.exists() and any(args.saida.iterdir()):raise RuntimeError('Nao sobrescrever saida')
    if sha(args.exp06b)!=EXP06B_SHA:raise RuntimeError('EXP06B hash divergente')
    prev=json.loads(args.exp06b.read_text())
    if prev.get('referencias',{}).get('pool')!=POOL:raise RuntimeError('Endereco EXP06B inesperado')
    sess=requests.Session();reports=[]
    for label,start,end in WINDOWS:
        calls=[];found={};cutoff=False
        # earliest-first bounded historical scan; no skipping on errors
        for lo in range(start,end+1,CHUNK):
            if len(calls)>=MAX_REQUESTS_PER_WINDOW:cutoff=True;break
            hi=min(lo+CHUNK-1,end)
            z=lookup_logs(sess,lo,hi)
            # split only if result >=1000, to avoid API truncation silently
            if z['status']=='truncation_possible':
                if len(calls)+2>=MAX_REQUESTS_PER_WINDOW:cutoff=True;calls.append({k:v for k,v in z.items() if k!='items'});break
                mid=(lo+hi)//2
                split=[lookup_logs(sess,lo,mid),lookup_logs(sess,mid+1,hi)]
                calls.append({'from':lo,'to':hi,'status':'split_after_truncation','n':z['n']})
            else:split=[z]
            for zz in split:
                calls.append({k:v for k,v in zz.items() if k!='items'})
                if zz['status'] not in ('ok','empty'):continue
                for ev in zz['items']:
                    if not isinstance(ev,dict):continue
                    t=txhash(ev)
                    try:b=int(ev.get('blockNumber') or ev.get('block_number'),16) if str(ev.get('blockNumber') or ev.get('block_number')).startswith('0x') else int(ev.get('blockNumber') or ev.get('block_number'))
                    except (ValueError,TypeError):continue
                    if (len(t)==66 and t.startswith('0x') and start<=b<=end and
                        a(ev.get('address'))==POOL and isinstance(ev.get('topics'),list) and ev['topics'] and
                        str(ev['topics'][0]).lower()==WITHDRAW_TOPIC):found.setdefault(t,b)
            if len(found)>=MAX_CANDIDATES_PER_WINDOW:break
        keys=sorted(found.items(),key=lambda x:(x[1],x[0]))[:MAX_CANDIDATES_PER_WINDOW]
        checked=[inspect_tx(sess,t,b) for t,b in keys]
        complete_scan=(not cutoff and calls and all(c['status'] in ('ok','empty','split_after_truncation') for c in calls) and
                       bool(calls[-1].get('to',-1)>=end))
        reports.append({'janela':label,'blocos':[start,end],'status_cobertura':'janela_inteira_consultada' if complete_scan else 'parcial_ou_interrompida',
                        'criterio_parada':'max_2_candidatos_ou_fim_janela','consultas':calls,
                        'n_candidatos_encontrados_ate_parada':len(found),'transacoes_verificadas':checked})
    out={'experimento':'EXP-06C','executado_utc':datetime.now(timezone.utc).isoformat(),'status':'DIAGNOSTICO_HISTORICO_SEM_ROTULO',
         'fonte_api':BASE,'endereco_pool':POOL,'topic_withdraw_precongelado':WITHDRAW_TOPIC,
         'topic_ragequit_excluido':RAGEQUIT_TOPIC,'sha256_exp06b':EXP06B_SHA,'janelas':reports,
         'regras':['duas janelas fixas, sem holdout cego','amostras ate dois candidatos por janela: nao inventariar todos os saques',
                   'confirmacao de log e tx nao comprova desvinculacao por si so','nao equiparar Ragequit a saque privado',
                   'se API falhar nao converter a zero','sem rótulos negativos, sem F1 ou testes do RF']}
    args.saida.mkdir(parents=True,exist_ok=True)
    path=args.saida/'evidencias_exp06c.json';path.write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
    manifest={'experimento':'EXP-06C','entrada_sha256':{args.exp06b.name:sha(args.exp06b)},'saida_sha256':{path.name:sha(path)},'script_version':'v1','janelas':WINDOWS,'limites':out['regras']}
    (args.saida/'manifesto_exp06c.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps([{'janela':r['janela'],'candidatos':r['n_candidatos_encontrados_ate_parada'],'verificados':sum(t['confirmed_withdraw_log'] for t in r['transacoes_verificadas']),'cobertura':r['status_cobertura']} for r in reports],ensure_ascii=False))
if __name__=='__main__':main()
