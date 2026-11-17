"""EXP-02B - auditoria de seis alertas do dia 2026-01-15.

Nenhuma modificação do modelo. Funções reutilizáveis. Executar main() apenas
com acesso ao arquivo intermediário Parquet de 2026 e internet da API Blockscout.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path
import hashlib
import json
import time
from typing import Any

import pandas as pd
import requests

DIA = date(2026, 1, 15)
API = 'https://eth.blockscout.com/api/v2'
ALVOS = {
    '0x7251febeabb01ec9de53ece7a96f1c951f886dd2': 'OKX DEX / proxy (documental)',
    '0x5182fede730b31a9cf7f49c5781214b4a99f2370': 'ApeCoin OFT Adapter (documental)',
    '0x57bedd7eb4c3118669f4f33a3cae4d4b554f24b7': 'SwappableBridgeUniswapV3 (documental)',
    '0x80226fc0ee2b096224eeac085bb9a8cba1146f7d': 'Chainlink CCIP Router (documental)',
    '0x2f848984984d6c3c036174ce627703edaf780479': 'MCT-XEN Batch Minter (documental)',
    '0x27428dd2d3dd32a4d7f7c497eaaa23130d894911': 'Wormhole Standard Relayer (documental)',
}
SLOT_EIP1967 = '0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc'


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def normalize_hash(value: Any) -> str:
    t = str(value).strip().lower()
    return t if t.startswith('0x') else '0x' + t


def obj_hash(obj: Any) -> str:
    return (obj.get('hash') or '').lower() if isinstance(obj, dict) else (str(obj).lower() if obj else '')


def sha256_json(data: Any) -> str:
    return hashlib.sha256(json.dumps(data, ensure_ascii=False, sort_keys=True, default=str).encode()).hexdigest()


def chosen_samples(rows: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Amostra cronológica determinística: primeira, central, última."""
    rows = rows.sort_values(['time_utc', 'hash'], kind='mergesort').reset_index(drop=True)
    if len(rows) == 0:
        return rows
    if n <= 0:
        raise ValueError('n deve ser positivo')
    if len(rows) <= n:
        return rows
    if n == 1:
        idx = [0]
    else:
        idx = [round(i * (len(rows) - 1) / (n - 1)) for i in range(n)]
    return rows.iloc[sorted(set(idx))].copy()


def extract_local_transactions(path: Path) -> pd.DataFrame:
    """Lê apenas 4 colunas, em batches; não carrega parquet inteiro em RAM."""
    import pyarrow.parquet as pq
    parser = pq.ParquetFile(str(path))
    expected = {'hash', 'sender', 'recipient', 'time'}
    missing = expected - set(parser.schema.names)
    if missing:
        raise ValueError(f'Parquet sem campos obrigatórios: {sorted(missing)}')
    pieces = []
    for batch in parser.iter_batches(batch_size=100_000, columns=['hash','sender','recipient','time']):
        data = batch.to_pandas()
        data['recipient'] = data['recipient'].astype(str).str.lower()
        selected = data.loc[data.recipient.isin(ALVOS)].copy()
        if selected.empty:
            continue
        selected['time_utc'] = pd.to_datetime(selected['time'], utc=True, errors='coerce')
        selected = selected[selected.time_utc.dt.date == DIA]
        if selected.empty:
            continue
        selected['hash'] = selected['hash'].map(normalize_hash)
        selected['sender'] = selected['sender'].astype(str).str.lower()
        pieces.append(selected[['recipient','hash','sender','time_utc']])
    if not pieces:
        return pd.DataFrame(columns=['recipient','hash','sender','time_utc'])
    full = pd.concat(pieces, ignore_index=True)
    duplicated = full.duplicated(['recipient','hash']).sum()
    if duplicated:
        raise ValueError(f'{duplicated} hashes duplicados no parquet: investigar antes de concluir contagens')
    return full.sort_values(['recipient','time_utc','hash'],kind='mergesort').reset_index(drop=True)


def get_json(session: requests.Session, url: str, tries: int=2) -> tuple[int | None, Any, str]:
    """Não mascara HTTP erros nem respostas JSON inválidas."""
    for i in range(tries):
        try:
            r = session.get(url, timeout=25, headers={'Accept': 'application/json'})
            if r.status_code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(1.5 * (i+1))
                continue
            try:
                payload = r.json()
            except ValueError:
                return r.status_code, {}, 'json_invalido'
            return r.status_code, payload, '' if r.ok else 'http_nao_ok'
        except requests.RequestException as e:
            if i < tries - 1:
                time.sleep(1.5 * (i+1))
                continue
            return None, {}, type(e).__name__ + ': ' + str(e)[:160]
    return None, {}, 'falha_nao_identificada'


def compact_transaction(tx: Any, target: str, tx_expected: str, sender_expected: str) -> dict:
    if not isinstance(tx, dict):
        return {'valida_para_dia': False, 'erro': 'transacao_nao_dict'}
    actual_to = obj_hash(tx.get('to'))
    actual_from = obj_hash(tx.get('from'))
    got = str(tx.get('hash') or '').lower()
    timestamp = str(tx.get('timestamp') or '')
    input_data = tx.get('raw_input') or tx.get('input') or ''
    if not isinstance(input_data, str):
        input_data = ''
    iso_date = timestamp[:10]
    method = tx.get('method') or ''
    return {
        'hash_api': got,
        'hash_confere': got == tx_expected,
        'sender_api': actual_from,
        'sender_confere': actual_from == sender_expected,
        'recipient_api': actual_to,
        'recipient_confere': actual_to == target,
        'dia_api': iso_date,
        'dia_confere': iso_date == DIA.isoformat(),
        'block_number': tx.get('block_number'),
        'selector': input_data[:10].lower() if input_data.startswith('0x') else '',
        'method_decoded': str(method)[:180],
        'result': tx.get('result'),
        'status': tx.get('status'),
        'value_wei': tx.get('value'),
        'decoded_input_present': bool(tx.get('decoded_input')),
        'valida_para_dia': got == tx_expected and actual_to == target and actual_from == sender_expected and iso_date == DIA.isoformat(),
    }


def collect_one_tx(session: requests.Session, target: str, row: pd.Series, n_log_pages: int = 1) -> tuple[dict, list[dict]]:
    txhash = row['hash']
    url = f'{API}/transactions/{txhash}'
    status, info, err = get_json(session, url)
    res = {
        'address':target,'tx_hash':txhash,'time_local':str(row['time_utc']),
        'source_url':url,'http_tx':status,'error_tx':err,'sample_only':True,
        'logs_complete':False, 'n_logs_captured':0,
    }
    if status != 200 or not isinstance(info, dict):
        res['valida_para_dia'] = False
        return res, []
    res.update(compact_transaction(info,target,txhash,row['sender']))
    log_url = f'{url}/logs'
    page_status, logdata, logerr = get_json(session, log_url)
    logs = []
    if page_status == 200 and isinstance(logdata, dict) and isinstance(logdata.get('items'),list):
        logs = logdata['items']
        res['logs_complete'] = logdata.get('next_page_params') is None
        res['n_logs_captured'] = len(logs)
        res['http_logs'] = page_status
        res['error_logs'] = '' if res['logs_complete'] else 'paginacao_pendente'
    else:
        res['http_logs'] = page_status
        res['error_logs'] = logerr or 'logs_sem_items'
    event_rows=[]
    for i,item in enumerate(logs):
        if not isinstance(item,dict):continue
        topics=item.get('topics') or []
        item_address = item.get('address')
        if isinstance(item_address,dict):item_address=item_address.get('hash')
        event_rows.append({
            'address_alvo':target,'tx_hash':txhash,'numero_log_pagina_1':i,
            'emissor_evento':str(item_address or '').lower(),
            'topic0':str(topics[0] if isinstance(topics,list) and topics else ''),
            'decoded_event':str(item.get('decoded') or '')[:500],
            'source_url':log_url,'paginacao_completa':res['logs_complete'],
        })
    return res,event_rows


def run(data_path: Path, ranking_csv_path: Path, output_dir: Path, per_address: int = 3, pause_s: float = .3, session=None):
    out=Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    signal=pd.read_csv(ranking_csv_path,dtype={'recipient':str})
    signal['recipient']=signal['recipient'].str.lower()
    tx=extract_local_transactions(data_path)
    tx.to_csv(out/'transacoes_locais_6_20260115.csv',index=False)
    session = session or requests.Session()
    summary=[];rows=[];events=[];metadata=[]
    for address,name in ALVOS.items():
        local=tx.loc[tx.recipient==address].copy()
        exp=signal.loc[signal.recipient==address,'n_tx']
        exp_n=int(exp.iloc[0]) if len(exp) else None
        status_addr,api_addr,error_addr=get_json(session,f'{API}/addresses/{address}')
        status_sc,api_sc,error_sc=get_json(session,f'{API}/smart-contracts/{address}')
        metadata.append({'recipient':address,'doc_associacao':name,'http_address':status_addr,
                         'http_contract':status_sc,'is_contract':api_addr.get('is_contract') if isinstance(api_addr,dict) else None,
                         'blockscout_name_atual':api_addr.get('name') if isinstance(api_addr,dict) else None,
                         'contract_name_atual':api_sc.get('name') if isinstance(api_sc,dict) else None,
                         'is_verified_atual':api_addr.get('is_verified') if isinstance(api_addr,dict) else None,
                         'proxy_type_atual':api_addr.get('proxy_type') if isinstance(api_addr,dict) else None,
                         'implementation_historica_verificada':False,'error_address':error_addr,'error_contract':error_sc,
                         'url':f'{API}/addresses/{address}'})
        sample=chosen_samples(local,n=per_address)
        n_ok=0;n_log_complete=0
        for _,row in sample.iterrows():
            detail,logs=collect_one_tx(session,address,row)
            rows.append(detail);events.extend(logs)
            n_ok+=int(detail.get('valida_para_dia',False))
            n_log_complete+=int(detail.get('logs_complete',False))
            time.sleep(pause_s)
        full_count=(exp_n == len(local)) if exp_n is not None else False
        summary.append({'recipient':address,'associacao_documental':name,'n_tx_legado':exp_n,'n_tx_interim':len(local),
                        'contagens_batem':bool(full_count),'amostras_programadas':len(sample),'amostras_tx_confirmadas':n_ok,
                        'paginas_log_amostra_completas':n_log_complete,
                        'cobertura_parquet_dia': 'parquet_intermediario_local_20260115',
                        'cobertura_externa_dia': 'amostral_nao_exaustiva',
                        'codigo_historico_verificado':False,
                        'rotulo_cientifico':'indeterminado',
                        'revisao_humana_pendente':True})
        print(f'{address[:12]} | local {len(local)} / legado {exp_n} | tx verificadas {n_ok}/{len(sample)}')
    for file_name,records in [('resumo_6.csv',summary),('amostras_tx_api.csv',rows),('eventos_amostras.csv',events),('metadados_atuais.csv',metadata)]:
        pd.DataFrame(records).to_csv(out/file_name,index=False)
    manifest={
        'experimento':'EXP-02B', 'data_corte_utc':DIA.isoformat(), 'executado_utc':datetime.now(timezone.utc).isoformat(),
        'chainId':1, 'fonte_2026_interim':str(data_path),'sha256_interim':sha256_file(data_path),
        'sha256_ranking_legado':sha256_file(ranking_csv_path),
        'api_base':API, 'max_amostras_por_endereco':per_address,
        'status':'coleta_amostral_exploratoria', 'houve_retreamento':False,'limiar_modificado':False,
        'limites':['Os dados internos cobrem apenas transacoes diretamente enderecadas aos alvos',
                  'A consulta externa e amostral; nao audita todas as transacoes de cada contrato',
                  'Metadados de contrato atuais nao comprovam codigo historico de janeiro/2026',
                  'Nenhum rotulo negativo definitivo foi atribuido; exige revisao humana e ground truth independente',
                  'Sem amostra representativa de nao-alertas, nao permite estimar precision/recall gerais'],
        'contagens':summary
    }
    manifest['sha256_arquivos_saida']={p.name:sha256_file(p) for p in sorted(out.glob('*.csv'))}
    (out/'manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
    return pd.DataFrame(summary)
