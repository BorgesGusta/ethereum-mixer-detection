"""EXP-06B: complementa EXP-06A com metadata/trace de factory e triagem LIMITADA de logs.
Nao classifica mixer, nao usa scores/modelo, nao reconsulta as duas tx do EXP-06A.
"""
import argparse, hashlib, json, pathlib, requests
from datetime import datetime, timezone

POOL='0xf241d57c6debae225c0f2e6ea1529373c9a9c9fb'
TX_FACTORY='0x6e3e14d7bcdfa838a8f7918de81d7b233e40d3afd493a864285fad8b360bcf75'
BLOCK_DECLARED=22153707
BLOCK_TX=22153714
ORIGINAL_SHA='f3e142a11e8a6d954d858c22df0dfa35b6a06e71234a75fa4cff03e9dadc3dda'
API='https://eth.blockscout.com/api/v2'


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def address(value):
    if isinstance(value,dict): return str(value.get('hash','')).lower()
    return str(value or '').lower()


def request(session,path,params=None):
    try:
        r=session.get(API+path,params=params,headers={'User-Agent':'AcademicAudit-EXP06B/1.0'},timeout=30)
        if r.status_code!=200:
            return {'ok':False,'http':r.status_code,'error':'HTTP_'+str(r.status_code)}
        body=r.json()
        if not isinstance(body,dict):return {'ok':False,'http':200,'error':'resposta_nao_objeto'}
        return {'ok':True,'http':200,'body':body}
    except requests.RequestException as exc:
        return {'ok':False,'http':None,'error':type(exc).__name__}
    except ValueError:
        return {'ok':False,'http':200,'error':'json_invalido'}


def pages(session,route,limit):
    cursor=None;seen=set();allrows=[];evidence=[]
    for n in range(1,limit+1):
        x=request(session,route,cursor)
        evidence.append({'pagina':n,'http':x.get('http'),'ok':x['ok'],'erro':x.get('error')})
        if not x['ok']:return {'status':'inconclusivo_api','paginas':evidence,'items':allrows}
        body=x['body']; data=body.get('items')
        if not isinstance(data,list):return {'status':'inconclusivo_schema','paginas':evidence,'items':allrows}
        allrows+=data
        cursor=body.get('next_page_params')
        if not cursor:return {'status':'completo','paginas':evidence,'items':allrows}
        key=json.dumps(cursor,sort_keys=True)
        if key in seen:return {'status':'inconclusivo_cursor_repetido','paginas':evidence,'items':allrows}
        seen.add(key)
    return {'status':'parcial_limite_paginas','paginas':evidence,'items':allrows}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--exp06a',required=True,type=pathlib.Path)
    ap.add_argument('--saida',required=True,type=pathlib.Path)
    args=ap.parse_args()
    if args.saida.exists() and any(args.saida.iterdir()):raise RuntimeError('Saida ocupada; nao sobrescrever')
    if sha(args.exp06a)!=ORIGINAL_SHA:raise RuntimeError('SHA do EXP-06A divergente; interrompido')
    prev=json.loads(args.exp06a.read_text())
    if prev['transacoes']['criacao_pool']['block_number']!=BLOCK_TX or prev['transacoes']['criacao_pool']['tx_hash']!=TX_FACTORY:
        raise RuntimeError('EXP-06A nao condiz com referencia congelada')
    s=requests.Session()
    meta=request(s,'/addresses/'+POOL)
    creator=request(s,'/addresses/'+POOL+'/smart-contracts')
    traces=pages(s,'/transactions/'+TX_FACTORY+'/internal-transactions',4)
    trace_summary=[]
    for x in traces['items']:
        if not isinstance(x,dict):continue
        created=address(x.get('created_contract'))
        trace_summary.append({'tipo':x.get('type'),'created_contract':created,'criou_pool':created==POOL,
                              'bloco':x.get('block_number'),'hash_tx':x.get('transaction_hash'),
                              'sucesso':x.get('success')})
    creation_match=[x for x in trace_summary if x['criou_pool'] and x['sucesso'] is True]
    # O endpoint de logs de enderecos costuma entregar itens mais recentes primeiro;
    # coletar APENAS 2 paginas, sem concluir que nao existem saques no intervalo.
    log_scan=pages(s,'/addresses/'+POOL+'/logs',2)
    log_sample=[]
    for x in log_scan['items']:
        if not isinstance(x,dict):continue
        topics=x.get('topics') or []
        decoded=x.get('decoded')
        log_sample.append({'tx_hash':x.get('transaction_hash'),
                           'block_number':x.get('block_number'),
                           'timestamp':x.get('timestamp'),
                           'topic0':topics[0] if topics else None,
                           'decoded_event':(decoded.get('method_call') or decoded.get('name')) if isinstance(decoded,dict) else None})
    withdrawal_keywords=['withdraw','unshield','ragequit','exit']
    candidate_logs=[x for x in log_sample if x['decoded_event'] and any(k in str(x['decoded_event']).lower() for k in withdrawal_keywords)]
    report={'experimento':'EXP-06B','executado_utc':datetime.now(timezone.utc).isoformat(),
            'status':'DIAGNOSTICO_SEM_ROTULO','referencias':{'pool':POOL,'transacao_factory_candidata':TX_FACTORY,
            'bloco_configuracao':BLOCK_DECLARED,'bloco_transacao':BLOCK_TX,'sha256_exp06a':ORIGINAL_SHA},
            'metadados_pool':{'http':meta.get('http'),'ok':meta['ok'],'erro':meta.get('error'),
                'creation_tx_hash':(meta.get('body') or {}).get('creation_tx_hash'),
                'creator_address_hash':address((meta.get('body') or {}).get('creator_address_hash')),
                'is_contract_atual':(meta.get('body') or {}).get('is_contract')},
            'smart_contract_atual':{'http':creator.get('http'),'ok':creator['ok'],'erro':creator.get('error'),
                'is_verified_atual':(creator.get('body') or {}).get('is_verified')},
            'traces_candidata':{'status':traces['status'],'paginas':traces['paginas'],
                'total_traces_observados':len(trace_summary),'traces_criacao_pool_sucesso':creation_match,
                'resumo_traces':trace_summary[:75]},
            'amostra_logs_pool':{'status':log_scan['status'],'paginas':log_scan['paginas'],
                'total_logs_observados':len(log_sample),'eventos_amostra':log_sample[:100],
                'eventos_nome_sugere_retirada':candidate_logs[:50],
                'aviso':'nomes atuais decodificados sao pistas, nao prova de ABI historica ou retirada desvinculada'},
            'limites':['API de traces pode ser parcial/indisponivel','nao inferir ausencia de CREATE de lista vazia',
                'log scan limitado a duas paginas, possivelmente recentes, nao demonstra ausencia de saques',
                'metadados atuais nao provam estado historico','nenhum rotulo mixer foi atribuido',
                'nenhuma conclusao de desempenho do Random Forest']}
    args.saida.mkdir(parents=True,exist_ok=True)
    path=args.saida/'evidencias_exp06b.json'
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    manifesto={'experimento':'EXP-06B','resultado':'DIAGNOSTICO',
        'entrada_sha256':{args.exp06a.name:sha(args.exp06a)},
        'saida_sha256':{path.name:sha(path)},'urls_consultadas':[API+'/addresses/'+POOL,API+'/addresses/'+POOL+'/smart-contracts',API+'/transactions/'+TX_FACTORY+'/internal-transactions',API+'/addresses/'+POOL+'/logs'],
        'restricao':'nenhum resultado automatiza rotulo mixer, sem comparacao de modelo'}
    (args.saida/'manifesto_exp06b.json').write_text(json.dumps(manifesto,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps({'traces':traces['status'],'criacao_interna_observada':len(creation_match),
                      'logs':log_scan['status'],'n_logs_amostra':len(log_sample),'possiveis_eventos_retirada':len(candidate_logs)},ensure_ascii=False))

if __name__=='__main__':main()
