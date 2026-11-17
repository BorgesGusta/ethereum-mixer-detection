# EXP-04 — Auditoria visual (executada e conferida em 17/11/2026)

- **Objetivo:** explicar com evidências visuais a consistência da reprodução consolidada e da reconciliação direta/Router.
- **Notebook:** [04_auditoria.ipynb](../../notebooks/04_auditoria.ipynb)
- **Drive:** [abrir notebook operacional](https://drive.google.com/file/d/1qsqTiOHSdJhSIiK1xGXAp83IpO-T0oq8/view)
- **Status:** execução Colab concluída; arquivos e conteúdo do CSV de checks conferidos no Drive em 17/11/2026.
- **Fontes:** resultados da auditoria 12.02B e execução consolidada 01, todos já copiados para o **Drive próprio**.
- **Integridade:** manifesta SHA-256 dos relatórios baixados; testes checam o número de registros com paridade, presença de uma combinação 2025 sem referência, ausência de colisões registradas e igualdade de F1 entre folds novos e legados.
- **Visualizações:** (a) transações diretas versus via chamadas por pool/dia em 2020 e 2026; (b) número de comparações com/sem paridade; (c) F1 em cinco folds, legado versus consolidado.
- **Persistência:** opcional (`SALVAR_NO_DRIVE=True`), cria subpasta de auditoria no `results` do Drive próprio; CSV, manifesto e 3 PNGs, sem sobrescrever originais.
- **Interpretação:** esta etapa é **auditoria documental das evidências**, não recálculo independente dos dumps e traces. Comparação das listas exatas de endereços e coleta temporal 2020–2026 continuam pendentes.
- **Próximo passo:** implementar auditoria independente de cálculos desde as fontes, comparar endereços sinalizados por identidade e pontuação, depois planejar coleta temporal 2020–2026 com cobertura harmonizada.


## Execução observada — 17/11/2026

- **Horário UTC do manifesto:** 2026-11-17T12:50:40.005561+00:00.
- **Pasta efetivamente criada no Drive próprio:** https://drive.google.com/drive/folders/1_hnQANKXRyJ4kK6nvKdnYlS1JeFwGQ8t
- [Tabela de checks](https://drive.google.com/file/d/1TBmdXfd7U0AZeU3GilasMO9oafXoaYmB/view)
- [Manifesto](https://drive.google.com/file/d/17Z9yJckGvJ77QgfIQcP-2Ri-1uGHGr6W/view)
- [Gráfico 1 — atribuição direta vs chamadas](https://drive.google.com/file/d/1_c3cIfRaRcS6aH73xOe2VpdZxYLo3H0R/view)
- [Gráfico 2 — estado da paridade](https://drive.google.com/file/d/1xZXYQC1qyxOXRt-Z56VUv5RW6GyCgY7q/view)
- [Gráfico 3 — F1 por fold](https://drive.google.com/file/d/10kboZQskPjdI67aBwE0o6kFczzvjY3MF/view)

O `checks.csv` contém cinco verificações:

1. Paridade de n_tx e quatro features: 7/7 combinações **com referência**.
2. Março de 2025: um caso sem feature de referência e não comparável.
3. Colisões entre pools: nenhuma registrada na auditoria anterior.
4. CV: F1 correspondente nos cinco folds entre original e consolidado.
5. Inferência 2020, limiar 0,50: 9 alertas agregados, 3 pools conhecidos.

**Cuidado epistemológico:** o notebook valida consistência dos CSVs e dos manifestos existentes, não executa uma extração nova da blockchain e não audita rótulos de candidatos adicionais. Os gráficos são visualizações dos mesmos relatórios; não representam nova evidência independente. A equivalência exata das listas de endereços não foi verificada.
