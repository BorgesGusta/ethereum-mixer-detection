"""EXP-06A: piloto de verificação on-chain de implantação e depósito Privacy Pools v1.

Não treina modelos, não atribui classes e não consulta estado histórico via archive.
Busca somente duas transações já identificadas por uma fonte secundária que referencia
Blockscout. Falhas de provedor geram resultado inconclusivo, nunca confirmação.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import requests

POOL = '0xf241d57c6debae225c0f2e6ea1529373c9a9c9fb'
ENTRYPOINT = '0x6818809eefce719e480a7526d76bd3e561526b46'
DECLARED_DEPLOY_BLOCK = 22153707
CREATION_TX = '0x6e3e14d7bcdfa838a8f7918de81d7b233e40d3afd493a864285fad8b360bcf75'
FIRST_DEPOSIT_TX = '0x55693706fddd4130a3b07fefa274c0b7730281c37e48725aa6aa8e1b7dca4948'
BASE = 'https://eth.blockscout.com/api/v2'
SOURCE = 'https://prifi.info/protocols/privacy-pools/'

def _addr(v):
    if isinstance(v, dict): v = v.get('hash')
    return str(v or '').lower()

def sha256(path):
    h=hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda:f.read(65536),b''):h.update(chunk)
    return h.hexdigest()

def fetch(session, url, params=None):
    try:
        r=session.get(url,params=params,timeout=35,headers={'User-Agent':'AcademicAudit-EXP06A/1.0'})
        if r.status_code != 200:
            return {'ok':False,'http_status':r.status_code,'error':f'HTTP_{r.status_code}'}
        try: body=r.json()
        except ValueError: return {'ok':False,'http_status':200,'error':'resposta_nao_json'}
        if not isinstance(body,dict): return {'ok':False,'http_status':200,'error':'json_sem_objeto'}
        return {'ok':True,'http_status':200,'data':body}
    except requests.RequestException as e:
        return {'ok':False,'http_status':None,'error':type(e).__name__}

def collect_logs(session, tx_hash, max_pages=12):
    rows=[];seen=set();params=None
    for page in range(max_pages):
        p=fetch(session,f'{BASE}/transactions/{tx_hash}/logs',params=params)
        if not p['ok']:return {'status':'inconclusivo_api','reason':p['error'],'pages':page,'rows':rows}
        data=p['data']; items=data.get('items')
        if not isinstance(items,list):return {'status':'inconclusivo_schema','pages':page,'rows':rows}
        rows.extend({'address':_addr(log.get('address')),'name':str(log.get('decoded',{}).get('method_call','') if isinstance(log.get('decoded'),dict) else ''),'topic0':str((log.get('topics') or [''])[0]) if isinstance(log.get('topics'),list) else '', 'tx_hash':str(log.get('transaction_hash','')).lower()} for log in items if isinstance(log,dict))
        next_params=data.get('next_page_params')
        if not next_params:return {'status':'completo','pages':page+1,'rows':rows}
        key=json.dumps(next_params,sort_keys=True)
        if key in seen:return {'status':'inconclusivo_cursor_repetido','pages':page+1,'rows':rows}
        seen.add(key); params=next_params
    return {'status':'inconclusivo_limite_paginas','pages':max_pages,'rows':rows}

def run(session):
    out={'experimento':'EXP-06A','status':'PILOTO_SEM_GROUND_TRUTH','coleta_utc':datetime.now(timezone.utc).isoformat(),'rede':'ethereum_mainnet','pool_oficial':POOL,'entrypoint_oficial':ENTRYPOINT,'deployment_block_declarado':DECLARED_DEPLOY_BLOCK,'fonte_indicacao_hashes':SOURCE,'transacoes':{},'regras':'não classificar sem prova em bloco e critérios de equivalência aprovados'}
    for label,tx_hash in [('criacao_pool',CREATION_TX),('deposito_inicial',FIRST_DEPOSIT_TX)]:
        fetch_tx=fetch(session,f'{BASE}/transactions/{tx_hash}')
        row={'tx_hash':tx_hash,'api_ok':fetch_tx['ok'],'http_status':fetch_tx.get('http_status')}
        if not fetch_tx['ok']:
            row.update({'status_verificacao':'inconclusivo_api','error':fetch_tx['error']})
        else:
            d=fetch_tx['data'];created=d.get('created_contract');block=d.get('block_number');status=d.get('status')
            row.update({'block_number':block,'tx_status':status,'from':_addr(d.get('from')),'to':_addr(d.get('to')),'created_contract':_addr(created),'timestamp':d.get('timestamp')})
            if label=='criacao_pool':
                match=_addr(created)==POOL
                row['status_verificacao']='confirmado_endereco_criado' if match and str(status).lower() in ('ok','success') else 'inconclusivo_ou_divergente'
                row['confere_bloco_declarado']=(str(block)==str(DECLARED_DEPLOY_BLOCK))
            else:
                if block is None: row['status_verificacao']='inconclusivo_bloco_ausente'
                else:
                    logs=collect_logs(session,tx_hash)
                    pool_logs=[z for z in logs['rows'] if z['address']==POOL]
                    row.update({'logs_status':logs['status'],'paginas':logs['pages'],'n_logs_recuperados':len(logs['rows']),'n_logs_pool':len(pool_logs),'enderecos_log_distintos':sorted({z['address'] for z in logs['rows']})})
                    # Eventos no pool + transação bem-sucedida = prova de interação; nome de evento ainda não confirmado sem ABI do período.
                    row['status_verificacao']='interacao_pool_com_logs_confirmada' if logs['status']=='completo' and pool_logs and str(status).lower() in ('ok','success') else 'inconclusivo_logs_ou_status'
                    row['eventos_nao_rotulados_historicamente']=True
        out['transacoes'][label]=row
    out['conclusoes_permitidas']=['transacao de criação refere-se ou não ao endereço pool','interação histórica com eventos, se respostas completas']
    out['conclusoes_proibidas']=['mixer de pool confirmado automaticamente','assinatura de função histórica confirmada apenas por nome atual','generalização do RF','F1/precision/recall']
    return out

def main():
    p=argparse.ArgumentParser();p.add_argument('--saida',type=Path,required=True);a=p.parse_args()
    if a.saida.exists() and any(a.saida.iterdir()):raise RuntimeError('Saída já existe: não sobrescrever')
    a.saida.mkdir(parents=True,exist_ok=True)
    result=run(requests.Session())
    data_path=a.saida/'verificacao_exp06a.json'
    data_path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    manifest={'experimento':'EXP-06A','resultado_status':'PILOTO','arquivo_sha256':{data_path.name:sha256(data_path)},'limites':['dados de recibos não substituem histórico de estado/proxy','não rotular mixer automaticamente','endereços/tx obtidos de fonte documental, confirmar na API']}
    (a.saida/'manifesto_exp06a.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:{'status':v.get('status_verificacao'),'bloco':v.get('block_number'),'http_status':v.get('http_status')} for k,v in result['transacoes'].items()},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
