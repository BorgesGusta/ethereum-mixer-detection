import gzip,csv,hashlib,json,os
from collections import defaultdict
from datetime import datetime,timezone
base='/mnt/data'
raw=f'{base}/blockchair_ethereum_transactions_20201029.tsv.gz'
api=f'{base}/transacoes_20201029_api.csv'
addrs={
'0x5e60fcca904753a31f9df7d7f6b7856b6ec27aa9':'AdminUpgradeabilityProxy',
'0x98f1858c9740b9c5f2cd8abea67948873d38dc39':'SmartEther',
'0xe113d58a4cb4dbac8a0da608ed7232785c1f2c18':'DSProxy'}
norm=lambda x:'0x'+str(x).lower().removeprefix('0x')
with open(api,newline='') as f:
    ext=list(csv.DictReader(f))
assert len(ext)==20, f'expected 20 API rows got {len(ext)}'
api_hashes={norm(e['hash']):e for e in ext}
assert len(api_hashes)==len(ext),'duplicate hashes API'
targets=defaultdict(list)
all_hashes={}
raw_rows=0
with gzip.open(raw,'rt',encoding='utf-8',newline='') as f:
    reader=csv.DictReader(f,delimiter='\t')
    for row in reader:
        raw_rows+=1
        address=norm(row['recipient']) if row['recipient'] else ''
        txhash=norm(row['hash'])
        if address in addrs:
            targets[address].append({'hash':txhash,'recipient':address,'sender':norm(row['sender']) if row['sender'] else '', 'block':row['block_id'],'time':row['time'],'failed':row['failed']})
        if txhash in api_hashes:
            all_hashes[txhash]={'hash':txhash,'recipient':address,'sender':norm(row['sender']) if row['sender'] else '', 'block':row['block_id'],'time':row['time'],'failed':row['failed']}
print('total raw rows:',raw_rows,'matched API hashes:',len(all_hashes))
fields=['endereco','protocolo_documental','tx_hash','na_fonte_blockchair','mesmo_destinatario','mesmo_remetente','mesmo_bloco','hash_externo','hash_raw','remetente_externo','remetente_raw','bloco_externo','bloco_raw']
audit=[]
for extrow in ext:
    h=norm(extrow['hash']);a=norm(extrow['endereco']);orig=all_hashes.get(h)
    audit.append(dict(endereco=a,protocolo_documental=addrs.get(a,''),tx_hash=h,na_fonte_blockchair=bool(orig),mesmo_destinatario=bool(orig and orig['recipient']==a),mesmo_remetente=bool(orig and orig['sender']==norm(extrow['de'])),mesmo_bloco=bool(orig and str(orig['block'])==str(extrow['bloco'])),hash_externo=h,hash_raw=orig['hash'] if orig else '',remetente_externo=norm(extrow['de']),remetente_raw=orig['sender'] if orig else '',bloco_externo=extrow['bloco'],bloco_raw=orig['block'] if orig else ''))
with open(f'{base}/auditoria_hashes_20.csv','w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(audit)
summ=[]
for addr,name in addrs.items():
    al={norm(x['hash']) for x in ext if norm(x['endereco'])==addr}
    ar={x['hash'] for x in targets[addr]}
    matching=al&ar
    summ.append({'endereco':addr,'nome_documental':name,'tx_raw':len(ar),'tx_api':len(al),'hashes_em_comum':len(matching),'somente_raw':len(ar-al),'somente_api':len(al-ar),'api_data_cobertura': 'incompleta' if name=='AdminUpgradeabilityProxy' else 'completa'})
with open(f'{base}/resumo_auditoria_hashes.csv','w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(summ[0]));writer.writeheader();writer.writerows(summ)
manifest={'executado_em_utc':datetime.now(timezone.utc).isoformat(),'origem_raw':'Drive próprio data/raw/blockchair_ethereum_transactions_20201029.tsv.gz','origem_api':'Blockscout dataset exportado em 17/11/2026','sha256_raw':hashlib.sha256(open(raw,'rb').read()).hexdigest(),'sha256_api_csv':hashlib.sha256(open(api,'rb').read()).hexdigest(),'linhas_total_raw':raw_rows,'quantidade_hashes_externos':len(ext),'todos_hashes_encontrados':all(x['na_fonte_blockchair'] for x in audit),'todos_destinatarios_conferem':all(x['mesmo_destinatario'] for x in audit),'todos_remetentes_conferem':all(x['mesmo_remetente'] for x in audit),'todos_blocos_conferem':all(x['mesmo_bloco'] for x in audit),'ressalvas':['O arquivo bruto e o parquet de referência derivam do mesmo dump Blockchair','Esta auditoria confirma os hashes externos recuperados pela API; não confirma paridade do proxy porque cobertura Blockscout foi incompleta','Requer exame da semântica da API de transações para concluir quais operações são consideradas.']}
with open(f'{base}/manifesto_auditoria_hashes.json','w') as f:json.dump(manifest,f,ensure_ascii=False,indent=2)
print(json.dumps(summ,indent=2));print({k:manifest[k] for k in ['todos_hashes_encontrados','todos_destinatarios_conferem','todos_remetentes_conferem','todos_blocos_conferem']})
