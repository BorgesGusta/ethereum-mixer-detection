# Cronologia auditável

| Data / fase | Marco | Evidência / pendência |
|---|---|---|
| Set.–out. 2026 | Reproduções iniciais: coleta, features, treino, inferência, ablação e robustez | Notebooks 01–06, dados e resultados no Drive |
| 14/11/2026 | Protocolo e teste externo de 15/01/2026 | Notebook 07b; limiar RF 0,85; outputs no Drive |
| 15/11/2026 | Experimentos 08–09: auditoria e sensibilidade | Outputs e notebooks legados; revisão de rótulos necessária |
| 15/11/2026 | Exp. 10: benchmark RF, Extra Trees, HGB e Regressão Logística | 5 sementes × 5 folds; validação por linha, apenas exploratória |
| 15/11/2026 | Exp. 11: comparação 2020/2026 e soft voting | Não confirmou superioridade externa do Extra Trees no limiar 0,85 |
| 15/11/2026 | Exp. 12.00: inventário e SHA-256 de 11 arquivos | Resultados em temporal_2020_2026/results no Drive |
| 15/11/2026 | Exp. 12.01: quatro pools elegíveis em um único dia de 2020 | Apenas quatro janelas positivas; insuficiente para treino definitivo |
| 15/11/2026 | Exp. 12.02A: paridade das quatro features em 2020 | internal_value_entropy = 0 em cada pool no dia examinado |
| 15/11/2026 | Exp. 12.02B: reconciliação por hash | 2026: 74+171+43 transações via chamadas; hashes de março/2025 abrangem sete dias |
| 16/11/2026 | Repositório oficial e organização da memória | Fase atual: documentação, migração controlada e preparação do estudo temporal |

**Nota:** a data acima é o marco de atividade registrado; arquivos legados ainda precisam de vínculos a commit, hash e execução específica. A cronologia é versionada, nunca reescrita para apagar decisões anteriores.
