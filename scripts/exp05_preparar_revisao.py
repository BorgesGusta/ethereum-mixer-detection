"""EXP-05: prepara revisão cega quanto aos scores para contratos de 2026.

NÃO atribui ground truth, não consulta APIs, não treina modelos.
Entradas são a lista de 9 alertas de 2026 e a matriz de 6 alertas EXP-04.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

SHA_RANKING = '5e989df3b50b2e5f84cab01af7fef4861dcb5eb63ecd0a2f5ae9f62ed9e8a260'
SHA_MATRIX = None  # expected hash recorded in manifest, never fabricate
SALT = 'EXP05-REV-INDEPENDENTE-2026-11-18|'
VALID = {'positivo_confirmado', 'negativo_confirmado', 'indeterminado'}


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for buf in iter(lambda: f.read(1 << 20), b''):
            h.update(buf)
    return h.hexdigest()


def readcsv(path):
    with open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def writecsv(path, records, cols):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader(); w.writerows(records)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ranking', type=Path, required=True)
    parser.add_argument('--matriz', type=Path, required=True)
    parser.add_argument('--saida', type=Path, required=True)
    args = parser.parse_args()
    if args.saida.exists() and list(args.saida.iterdir()):
        raise ValueError('Diretório não vazio: não sobrescrever')
    if sha(args.ranking) != SHA_RANKING:
        raise ValueError('Ranking de 2026 não corresponde ao previamente auditado')
    ranking, matrix = readcsv(args.ranking), readcsv(args.matriz)
    if len(ranking) != 9 or len({r['recipient'].lower() for r in ranking}) != 9:
        raise ValueError('Ranking não contém exatamente 9 alertas únicos')
    matrix_ids = {r['address'].lower() for r in matrix}
    if len(matrix) != 6 or len(matrix_ids) != 6:
        raise ValueError('Matriz EXP-04 não contém seis alertas únicos')
    ref = {r['recipient'].lower() for r in ranking if r['rotulo'] in ('0.1 ETH', '1 ETH', '10 ETH')}
    if len(ref) != 3 or ref & matrix_ids or (ref | matrix_ids) != {r['recipient'].lower() for r in ranking}:
        raise ValueError('Reconciliação 3 pools e 6 alertas falhou')
    sorted_ids = sorted([r['recipient'].lower() for r in ranking], key=lambda x: hashlib.sha256((SALT + x).encode()).hexdigest())
    cases = [{'case_id':f'R{i:03d}', 'endereco': addr, 'rede':'ethereum-mainnet', 'data_alvo':'2026-01-15', 'classificacao_legada_restrita':('referencia_tornado_existente' if addr in ref else 'alerta_adicional_sem_ground_truth')} for i, addr in enumerate(sorted_ids, 1)]
    blank = [{'case_id':row['case_id'], 'endereco':row['endereco'], 'data_alvo':row['data_alvo'], 'classe_proposta':'', 'tipo_entidade_historico':'', 'funcao_economica_historica':'', 'evidencia_primaria_url':'', 'tx_ou_bloco_referencia':'', 'arquivo_sha256':'', 'cobertura_analisada':'', 'confianca_qualitativa':'', 'justificativa_curta':'', 'lacunas':'', 'data_revisao_utc':''} for row in cases]
    args.saida.mkdir(parents=True, exist_ok=True)
    writecsv(args.saida/'indice_interno_nao_entregar_a_revisores.csv', cases, list(cases[0]))
    for reviewer in ('A','B'):
        writecsv(args.saida/f'revisao_independente_{reviewer}_PREENCHER.csv', blank, list(blank[0]))
    manifest = {
        'experimento':'EXP-05', 'status':'FORMULARIOS_GERADOS_SEM_ROTULAGEM',
        'created_utc':datetime.now(timezone.utc).isoformat(),
        'date_under_review':'2026-01-15', 'network':'ethereum-mainnet',
        'n_cases':len(cases),'n_documented_tornado_references':len(ref),
        'n_additional_alerts_without_independent_labels':len(matrix_ids),
        'reviewer_forms_do_not_contain':['prob','n_tx','rotulo_legado','associacao_documental_atual','modelo_predicao'],
        'selection_rule':'9 alertas já explorados, apenas amostra para estudo de caso; não holdout cego',
        'sources_sha256': {'ranking_original':sha(args.ranking),'matriz_exp04':sha(args.matriz)},
        'output_sha256':{p.name:sha(p) for p in sorted(args.saida.glob('*.csv'))},
        'limitations':['Nenhum rótulo atribuído','Seleção condicionada aos alertas: viés de verificação','3 pools não são protocolo independente do treino','Não usar para calcular métricas populacionais','Revisão A/B independente antes de adjudicação']
    }
    (args.saida/'manifesto_preparacao_exp05.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Preparados 9 casos, 2 formulários separados, 0 rótulos científicos. SHA-256 verificados.')

if __name__ == '__main__': main()
