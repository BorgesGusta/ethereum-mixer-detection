# Dados, proveniência e Drive

**Pasta principal:** https://drive.google.com/drive/folders/1VgyDm4okxLmt7GXf0diT560SAjYfgM9b

## Inventário essencial confirmado

| Arquivo | Papel |
|---|---|
| `data/raw/blockchair_ethereum_transactions_20201029.tsv.gz` | dump 29/10/2020 |
| `data/raw/blockchair_ethereum_transactions_20250315.tsv.gz` | dump 15/03/2025 |
| `data/raw/blockchair_ethereum_transactions_20260115.tsv.gz` | dump 15/01/2026 |
| `data/processed/features_treino.parquet` | 123 janelas (23 positivas de 1 pool em 2025) |
| `data/processed/features_teste_20201029.parquet` | features 2020 |
| `data/processed/features_2026-01-15.parquet` | features 2026 |
| `data/processed/modelo_rf.joblib` | RF treinada anteriormente |

As auditorias 12.00–12.02B guardam SHA-256 e schema dos arquivos em [resultados do Drive](https://drive.google.com/drive/folders/1twHP6i1jwSemx59-Uc8C1N2nVlDabmCh).

## Política

- Originais no Drive são somente leitura lógica: novas transformações recebem **novos caminhos**, versões e hashes.
- Em GitHub somente amostras pequenas auditadas, scripts, notebooks, relatórios e manifestos.
- `raw` > `interim` > `processed` > `results`: registrar inputs, scripts, datas e dependências.
- Jamais afirmar que dados de 2021–2024 já foram coletados: ainda não constam deste inventário.
- Classificações de endereços sem verificação são `unverified`, não `negative`.
- Dados de 2020 e 2026 foram explorados; criar teste futuro ainda não inspecionado para alegações confirmatórias.
