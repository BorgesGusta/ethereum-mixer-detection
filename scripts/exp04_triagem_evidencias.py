"""EXP-04: matriz de qualidade das evidencias existentes, sem novos rótulos.
Reusa amostras EXP-02B, paginação EXP-02C e estado histórico EXP-03B.
Sem acesso à blockchain, treinamento ou recalibração. Python pandas.
"""
import argparse, hashlib, json
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd

EXPECTED = {
'amostras_tx_api.csv':'83f42e349d25cbbcded99784ba9eb4c148b64c9d91eb3190aab00a76c5f3ea8d',
'eventos_amostras.csv':'b4442151e64a86722aed72caf15a785f6da800fc139d8befa8e50a41bd143571',
'status_paginacao.csv':'42db4ef99505297d916f8aa9906f80f97a225ef2ca919eaf566cddc2dd9e5bc3',
'seletor_vs_abi_atual.csv':'a722f447214a578fc7901eed100be0161ebac9362f128b1dab05b0645840e4ad',
'controles_estado_historico.csv':'0db4e36948edc8a261d6031355657b2fe7814a4dfba30bb4e97a50850caf72eb',
}

def sha(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()

def validate(tx, pages, controls):
 if tx.shape[0]!=18 or tx.address.nunique()!=6 or tx.tx_hash.nunique()!=18:raise ValueError('Amostra EXP02B inesperada')
 if set(pages['hash'])-set(tx['tx_hash']):raise ValueError('Hash da paginação não está na amostra')
 if len(pages)!=3 or not pages['paginacao_completa'].astype(bool).all():raise ValueError('EXP02C incompleto')
 if len(controls)!=6 or not (controls.status_codigo_historico=='inconclusivo_sem_resposta_historica').all():raise ValueError('Mudança de status EXP03B, reavaliar protocolo')
 flags=['hash_confere','sender_confere','recipient_confere','dia_confere','valida_para_dia']
 if not tx[flags].eq(True).all().all():raise ValueError('Paridade amostral não é integral')


def main():
 p=argparse.ArgumentParser();p.add_argument('--entrada',type=Path,required=True);p.add_argument('--saida',type=Path,required=True);a=p.parse_args()
 if a.saida.exists() and any(a.saida.iterdir()):raise ValueError('Não sobrescrever outputs')
 for name,digest in EXPECTED.items():
  f=a.entrada/name
  if not f.is_file() or sha(f)!=digest:raise ValueError('SHA-256 divergente: '+name)
 tx=pd.read_csv(a.entrada/'amostras_tx_api.csv');ev=pd.read_csv(a.entrada/'eventos_amostras.csv');pages=pd.read_csv(a.entrada/'status_paginacao.csv');selectors=pd.read_csv(a.entrada/'seletor_vs_abi_atual.csv');controls=pd.read_csv(a.entrada/'controles_estado_historico.csv')
 validate(tx,pages,controls)
 page_map={str(r['hash']).lower():r for _,r in pages.iterrows()}
 details=[]
 for _,r in tx.iterrows():
  h=str(r.tx_hash).lower(); extra=page_map.get(h); complete=bool(extra.paginacao_completa) if extra is not None else bool(r.logs_complete)
  nlogs=int(extra.logs_capturados) if extra is not None else int(r.n_logs_captured)
  details.append({'address':str(r.address).lower(),'tx_hash':h,'dia':'2026-01-15','paridade_hash_from_to_data':True,'logs_completos_na_amostra':complete,'logs_observados':nlogs,'metodo_reportado':str(r.method_decoded),'seletor':str(r.selector),'houve_reversao':str(r.status).lower() in ('error','reverted','failed'),'tipo_evidencia':'tx_amostrada_e_logs' if complete else 'tx_amostrada_logs_parciais','nao_prova_ausencia_mixer':True})
 d=pd.DataFrame(details)
 if not d.logs_completos_na_amostra.all() or d.logs_observados.sum()!=586:raise ValueError('Não reconciliou os 586 logs das 18 amostras')
 manifest_02b=json.loads((a.entrada/'manifesto.json').read_text()) if (a.entrada/'manifesto.json').exists() else None
 doc_assoc={str(x['recipient']).lower():x['associacao_documental'] for x in (manifest_02b or {}).get('contagens',[])}
 address_unknown=set(selectors.address.astype(str).str.lower())
 rows=[]
 for addr,g in d.groupby('address',sort=True):
  n_unknown=sum(m.lower()==s.lower() for m,s in zip(g.metodo_reportado,g.seletor))
  rows.append({'address':addr,'associacao_documental_atual':doc_assoc.get(addr,'nao_informada'), 'transacoes_amostradas':len(g),'amostras_hash_from_to_data_verificados':len(g),'amostras_logs_completos':int(g.logs_completos_na_amostra.sum()),'logs_em_transacoes_amostradas':int(g.logs_observados.sum()),'amostras_com_reversao':int(g.houve_reversao.sum()),'amostras_metodo_nao_decodificado':int(n_unknown),'historico_proxy_verificado':False if addr in address_unknown else None,'cobertura_tempo':'somente_tres_amostras_de_2026_01_15','tipo_qualidade_evidencia':'transacoes_e_logs_amostrados_completos','rotulo_cientifico':'indeterminado','acao_recomendada':'revisao_humana_e_validacao_historica'})
 summary=pd.DataFrame(rows)
 if summary.logs_em_transacoes_amostradas.sum()!=586 or len(summary)!=6:raise ValueError('Falha de reconciliação por contrato')
 # Estes são os controles NEGATIVOS AO SCORE (não rótulos negativos), e sem prova histórica.
 ctrl=controls[['alertado','controle','block_ancora','status_codigo_historico','rotulo_cientifico']].copy()
 ctrl['observabilidade_historica']='indisponivel_nos_dois_rpc_EXP03B';ctrl['comparabilidade_contratos']='nao_verificada';ctrl['ausencia_de_codigo_comprovada']=False
 a.saida.mkdir(parents=True,exist_ok=True)
 for name,data in [('matriz_amostras.csv',d),('matriz_alertas.csv',summary),('matriz_controles.csv',ctrl)]:data.to_csv(a.saida/name,index=False)
 manifest={'experimento':'EXP-04','fase':'triagem_de_qualidade_da_evidencia_sem_classificacao','executado_em_utc':datetime.now(timezone.utc).isoformat(),'dados_historicos':'2026-01-15','entradas_sha256':EXPECTED,'fontes_reutilizadas':['EXP-02B','EXP-02C','EXP-03B'],'resumo':{'alertas_adicionais':len(summary),'transacoes_verificadas':len(d),'logs_amostrados_completos':int(d.logs_observados.sum()),'controles_com_estado_historico_valido':0,'rotulos_positivos_ou_negativos_novos':0},'limites':['18 transacoes não equivalem ao universo de 315','586 logs referem-se somente às 18 amostras','tipagem atual e função de ABI atual não provam código histórico','controles não alertados não são negativos verificados','não há métrica de precisão/recall nem novo detector'],'saidas_sha256':{p.name:sha(p) for p in a.saida.iterdir()}}
 (a.saida/'manifesto_exp04.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(manifest['resumo'],indent=2,ensure_ascii=False))

if __name__=='__main__':main()
