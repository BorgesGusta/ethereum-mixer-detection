"""EXP-02C: completa as páginas de logs MCT-XEN e confere seletores por ABI.
Reexecuta só 3 transações já auditadas. Nenhum modelo ou rótulo é alterado.
"""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, time
from collections import Counter
import pandas as pd
import requests
from Crypto.Hash import keccak

API = 'https://eth.blockscout.com/api/v2'
FOURBYTE = 'https://www.4byte.directory/api/v1/signatures/'
ALVO_MCT = '0x2f848984984d6c3c036174ce627703edaf780479'
TARGET_ABI = {
  '0x7251febeabb01ec9de53ece7a96f1c951f886dd2': ['0xec5b999d'],
  ALVO_MCT: ['0x98190f47'],
}
MAX_PAGINAS_POR_TX = 30
MAX_LOGS_POR_TX = 4000
PAUSA = .35

def sha256(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as fd:
        for block in iter(lambda:fd.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()

def get_json(session, url, params=None, tentativas=3):
    last=''
    for k in range(tentativas):
        try:
            res = session.get(url,params=params,timeout=30,headers={'Accept':'application/json'})
            if res.status_code in (429,500,502,503,504) and k<tentativas-1:
                time.sleep(1.0*(k+1));continue
            try: payload = res.json()
            except ValueError: return res.status_code,{},'resposta_nao_json',res.url
            return res.status_code,payload,'' if res.ok else 'http_nao_ok',res.url
        except requests.RequestException as exc:
            last=f'{type(exc).__name__}: {str(exc)[:160]}'
            if k<tentativas-1:time.sleep(1.0*(k+1))
    return None,{},last,url

def log_summary(item,txhash,page,offset):
    logaddr=item.get('address') or ''
    if isinstance(logaddr,dict):logaddr=logaddr.get('hash','')
    decoded=item.get('decoded') or {}
    if not isinstance(decoded,dict): decoded={}
    topics=item.get('topics') or []
    return dict(tx_hash=txhash,pagina=page,posicao_na_pagina=offset,
                emissor=str(logaddr).lower(),topic0=str(topics[0]).lower() if topics else '',
                index_log=item.get('index'),metodo_evento_decodificado=str(decoded.get('method_call') or '')[:260],
                bloco=item.get('block_number'),hash_bloco=item.get('block_hash'),
                conteudo_sha256=hashlib.sha256(json.dumps(item,sort_keys=True,default=str,ensure_ascii=False).encode()).hexdigest())

def paginate_logs(session,txhash,anterior):
    url=f'{API}/transactions/{txhash}/logs'
    params=None;seen_cursors=set(); pages=[]; records=[]; reason=''; complete=False
    for page in range(1,MAX_PAGINAS_POR_TX+1):
        cursor=json.dumps(params,sort_keys=True,default=str)
        if cursor in seen_cursors:
            reason='cursor_repetido';break
        seen_cursors.add(cursor)
        status,data,error,real_url=get_json(session,url,params=params)
        if status!=200 or not isinstance(data,dict) or not isinstance(data.get('items'),list):
            reason=f'erro_api_pagina_{page}: HTTP {status} {error}';break
        items=data['items'];new_params=data.get('next_page_params')
        pages.append({'pagina':page,'http':status,'url':real_url,'itens':items,'next_page_params':new_params})
        for i,log in enumerate(items):
            if isinstance(log,dict):records.append(log_summary(log,txhash,page,i))
        if len(records)>MAX_LOGS_POR_TX:
            reason='limite_logs_excedido';break
        if new_params is None:
            complete=True;reason='fim_sem_next_page_params';break
        if not isinstance(new_params,dict) or not new_params:
            reason='next_page_params_invalido';break
        params=new_params
        time.sleep(PAUSA)
    else:
        reason='limite_paginas_alcancado'
    # Corroboração independente de que a nova primeira página é a mesma da coleta anterior.
    prev=anterior.loc[anterior.tx_hash.str.lower()==txhash]
    fresh=[r for r in records if r['pagina']==1]
    prev_pairs=[(str(r.emissor_evento).lower(),str(r.topic0).lower()) for r in prev.itertuples(index=False)]
    fresh_pairs=[(r['emissor'],r['topic0']) for r in fresh]
    first_page_ok=(prev_pairs==fresh_pairs) if len(prev_pairs)>0 else None
    # Sem descartar qualquer log. Índices duplicados entre páginas são sinalizados, não corrigidos silenciosamente.
    observed_indexes=[str(x['index_log']) for x in records if x['index_log'] is not None]
    duplicate_indexes=len(observed_indexes)-len(set(observed_indexes))
    return {'hash':txhash,'paginas':len(pages),'logs_capturados':len(records),
            'logs_primeira_pagina_reconfirmados':first_page_ok,
            'paginacao_completa':complete,'motivo_parada':reason,
            'indices_repetidos_entre_paginas':duplicate_indexes},pages,records

def full_type(inp):
    t=str(inp.get('type',''))
    if not t.startswith('tuple'):return t
    rest=t[len('tuple'):]
    return '('+','.join(full_type(c) for c in inp.get('components',[]))+')'+rest

def function_signature(item):
    return str(item.get('name'))+'('+','.join(full_type(x) for x in (item.get('inputs') or []))+')'

def selector_from_signature(signature):
    h=keccak.new(digest_bits=256);h.update(signature.encode('utf8'))
    return '0x'+h.digest()[:4].hex()

def inspect_selector(session,addr,selectors):
    url=f'{API}/smart-contracts/{addr}'
    status,body,err,real_url=get_json(session,url)
    abi=[]
    if status==200 and isinstance(body,dict):
        abi=body.get('abi') or []
        if isinstance(abi,str):
            try:abi=json.loads(abi)
            except ValueError:abi=[]
    if not isinstance(abi,list):abi=[]
    results=[]
    for sel in selectors:
        matches=[]
        for item in abi:
            if not isinstance(item,dict) or item.get('type')!='function':continue
            try:
                signature=function_signature(item)
                if selector_from_signature(signature)==sel:matches.append(signature)
            except Exception:continue
        # 4byte directory é fonte de candidatos e NÃO valida qual função um proxy executava em 2026.
        st4,dat4,err4,url4=get_json(session,FOURBYTE,{'hex_signature':sel})
        candidates=[]
        if st4==200 and isinstance(dat4,dict):
            candidates=[str(x.get('text_signature')) for x in dat4.get('results',[])[:20] if isinstance(x,dict)]
        results.append(dict(address=addr,selector=sel,http_abi_atual=status,
                            contrato_atual=body.get('name') if isinstance(body,dict) else None,
                            correspondencias_abi_atual=' | '.join(matches),total_funcoes_abi_atual=len(abi),
                            http_4byte=st4,candidatos_4byte=' | '.join(candidates),
                            historico_2026_verificado=False,
                            interpretacao='ABI atual nao comprova implementacao historica',
                            url_abi=real_url,url_4byte=url4,erro=err or err4))
    return results,{'status_abi':status,'body_abi_atual':body,'fonte_abi':real_url}

def run(out_dir:Path,samples_path:Path,old_logs_path:Path,session=None):
    out_dir=Path(out_dir);out_dir.mkdir(parents=True,exist_ok=True)
    s=pd.read_csv(samples_path,dtype={'tx_hash':str,'address':str});old=pd.read_csv(old_logs_path,dtype=str).fillna('')
    s['address']=s['address'].str.lower();s['tx_hash']=s['tx_hash'].str.lower()
    old['tx_hash']=old['tx_hash'].str.lower()
    pending=s.loc[(s.address==ALVO_MCT)&(~s.logs_complete.astype(str).str.lower().eq('true'))].copy()
    if len(pending)!=3:raise ValueError(f'Esperadas 3 transacoes de MCT-XEN pendentes, encontradas {len(pending)}; revisar a origem, sem alterar o universo')
    if pending.tx_hash.nunique()!=3:raise ValueError('Hashes de MCT-XEN repetidos')
    session=session or requests.Session()
    status=[];raw_pages={};all_logs=[]
    for txhash in sorted(pending.tx_hash):
        v,pages,logs=paginate_logs(session,txhash,old)
        status.append(v);raw_pages[txhash]=pages;all_logs.extend(logs)
        print(txhash[:18],v['paginas'],'pagina(s)',v['logs_capturados'],'logs','COMPLETA' if v['paginacao_completa'] else 'INCOMPLETA')
    lookup=[];current={}
    for addr,selectors in TARGET_ABI.items():
        rows,resp=inspect_selector(session,addr,selectors);lookup.extend(rows);current[addr]=resp
        time.sleep(PAUSA)
    pd.DataFrame(status).to_csv(out_dir/'status_paginacao.csv',index=False)
    pd.DataFrame(all_logs).to_csv(out_dir/'eventos_logs_coletados.csv',index=False)
    pd.DataFrame(lookup).to_csv(out_dir/'seletor_vs_abi_atual.csv',index=False)
    (out_dir/'paginas_blockscout.json').write_text(json.dumps({'consultado_utc':datetime.now(timezone.utc).isoformat(),'pages_by_hash':raw_pages},ensure_ascii=False,indent=2,default=str),encoding='utf8')
    (out_dir/'respostas_abi_atual.json').write_text(json.dumps(current,ensure_ascii=False,indent=2,default=str),encoding='utf8')
    manifest={'experimento':'EXP-02C','executado_utc':datetime.now(timezone.utc).isoformat(),
              'dia_da_ethereum':'2026-01-15','fonte_api':API,'fonte_logs_previa':'EXP-02B','n_transacoes':len(status),
              'paginacao_completa_em_todas':all(v['paginacao_completa'] for v in status),
              'sha256_amostras_EXP02B':sha256(samples_path),'sha256_logs_EXP02B':sha256(old_logs_path),
              'notas':['Nenhum modelo ou limiar modificado', 'As paginas adicionais verificam apenas 3 transacoes MCT-XEN previamente amostradas',
                       'ABI consultada é a atual; NÃO valida implementação EIP-1967 em 15/01/2026',
                       'Assinaturas 4byte sao candidatas globais, nao prova funcional do contrato',
                       'Rotulos de mixer/nao mixer permanecem indeterminados'],
              'status':status,'seletor_abi':lookup,
              'sha256_arquivos_saida':{p.name:sha256(p) for p in out_dir.glob('*') if p.is_file()}}
    (out_dir/'manifesto_EXP02C.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2,default=str),encoding='utf8')
    return status,lookup
