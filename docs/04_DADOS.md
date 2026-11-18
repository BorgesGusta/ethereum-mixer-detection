# Dados, proveniência e Drive

**Pasta principal oficial (própria):** https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj

**Fonte histórica compartilhada por Bruno:** https://drive.google.com/drive/folders/1VgyDm4okxLmt7GXf0diT560SAjYfgM9b — não usar como local padrão de execução.

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

## Histórico da migração preventiva para pasta de projeto separada (17/11/2026) — narrativa anterior à decisão final

Em resposta ao pedido de eliminar dependência de um atalho do colaborador Bruno, foi encontrada no Drive uma pasta alternativa `Segurança de Redes de Computadores/Projeto_Mixers_Ethereum` (ID `1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj`). Ela tinha sete subpastas organizacionais vazias.

Foi criada nela uma estrutura adicional compatível com o pipeline `data/raw`, `data/interim`, `data/processed`, `notebooks/00_ATIVOS`, `notebooks/99_LEGADO`, `results`, `docs`, `temporal_2020_2026/results`. Os arquivos foram **copiados** de `mixers-ethereum` (ID `1VgyDm4okxLmt7GXf0diT560SAjYfgM9b`), a pasta fornecida pelo usuário, sem remover arquivos originais.

**Conferência de presença em pastas de primeiro nível (origem → cópia):**
- Raw: 30 → 30, sem diferenças de nomes e tamanhos informados;
- Interim: 14 → 14, três planilhas nativas com tamanho informado divergente (não atestada equivalência de conteúdo);
- Processed: 4 → 4, sem diferenças de nomes e tamanhos informados;
- Notebooks legados: 16 → 16;
- Notebooks ativos: 1 → 1;
- Docs: 3 → 3, um documento nativo com tamanho informado divergente;
- Results raiz: 25 → 25. Pastas de benchmark e resultados temporais também foram copiadas, sujeitas a inventário recursivo final.

**Links da cópia:**
- [Projeto alternativo](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj)
- [Dados brutos](https://drive.google.com/drive/folders/1Nicyoz31MP_cahehl1XU2bBRCzgEGv3u)
- [Dados intermediários](https://drive.google.com/drive/folders/1HF1ME_jEO_Fm-OuVVZ4eJ6matdT_WVY_)
- [Dados processados](https://drive.google.com/drive/folders/18IeCuFcx5ka0OoJAxjJt3gey7JVX71ht)
- [Notebooks ativos](https://drive.google.com/drive/folders/1VNdVfqmHt-csEcbh9M9SLaV_IgvpGwJ4)
- [Notebooks legados](https://drive.google.com/drive/folders/1GxbRUt4ZKQufiG_L8IsoBDYC2miZVY3r)

**Pendências importantes:** (1) confirmar com o usuário qual pasta é efetivamente dele e qual é de Bruno — a propriedade não foi comprovada pelos metadados do conector; (2) conferir hashes SHA-256 dos arquivos binários copiados e revisar documentos nativos; (3) adaptar o notebook consolidado à pasta escolhida; (4) somente depois retirar o atalho do Drive, sem apagar a pasta ou dados de terceiros.

Até essa confirmação, o GitHub permanece a fonte de verdade para código; as duas pastas de dados do Drive devem ser consideradas como **origem e cópia em processo de validação**, sem designação definitiva de uma delas como canônica.


## Definição oficial confirmada — 17/11/2026

O usuário confirmou que `mixers-ethereum` é pasta **compartilhada pelo Bruno**, enquanto a pasta de trabalho própria será `Segurança de Redes de Computadores/Projeto_Mixers_Ethereum`.

- O atalho `mixers-ethereum` (ID `1G2LLuVFtRHGf1GdWd3nub-HsDOFkzGT0`) foi **removido apenas do Meu Drive do usuário**. A pasta original compartilhada e os arquivos do Bruno **não foram excluídos**.
- Cópias de dados da pasta do Bruno foram realizadas na pasta própria. Contagem de nomes e tamanho reportado dos arquivos comuns coincide no primeiro nível, mas falta conferir SHA-256 completo dos binários e equivalência de documentos nativos.
- A versão ativa de `01_reproducao.ipynb` foi corrigida para usar explicitamente o caminho da pasta própria no Google Colab. A cópia no Drive próprio está em https://drive.google.com/file/d/1ma1KHywnIF0lZ3LvsYEk7Ts-2h_J4W69/view.
- **Não apagar originais nem chamar a migração de integralmente validada** antes de inventário recursivo e hashes.


## Interpretação vigente da migração — consolidação documental 17/11/2026

A **definição oficial confirmada** acima prevalece sobre as instruções provisórias da seção histórica: a pasta `Projeto_Mixers_Ethereum` é o destino oficial de trabalho, e `mixers-ethereum` de Bruno é fonte histórica preservada. O notebook 01 ativo foi apontado para a pasta própria conforme registrado. **Não afirmar cópia plenamente íntegra** sem inventário recursivo e SHA-256 de todos os binários; divergências de metadados dos documentos nativos ainda requerem verificação de conteúdo. Esta atualização não executou uma nova cópia ou cálculo de hash.
