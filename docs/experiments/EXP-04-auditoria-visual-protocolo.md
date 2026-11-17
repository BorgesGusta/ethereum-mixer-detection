# EXP-04 — Auditoria visual (protocolo, ainda não executado)

- **Objetivo:** explicar com evidências visuais a consistência da reprodução consolidada e da reconciliação direta/Router.
- **Notebook:** [04_auditoria.ipynb](../../notebooks/04_auditoria.ipynb)
- **Drive:** [abrir notebook operacional](https://drive.google.com/file/d/1qsqTiOHSdJhSIiK1xGXAp83IpO-T0oq8/view)
- **Status:** publicado e sintaticamente validado; execução Colab pendente.
- **Fontes:** resultados da auditoria 12.02B e execução consolidada 01, todos já copiados para o **Drive próprio**.
- **Integridade:** manifesta SHA-256 dos relatórios baixados; testes checam o número de registros com paridade, presença de uma combinação 2025 sem referência, ausência de colisões registradas e igualdade de F1 entre folds novos e legados.
- **Visualizações:** (a) transações diretas versus via chamadas por pool/dia em 2020 e 2026; (b) número de comparações com/sem paridade; (c) F1 em cinco folds, legado versus consolidado.
- **Persistência:** opcional (`SALVAR_NO_DRIVE=True`), cria subpasta de auditoria no `results` do Drive próprio; CSV, manifesto e 3 PNGs, sem sobrescrever originais.
- **Interpretação:** esta etapa é **auditoria documental das evidências**, não recálculo independente dos dumps e traces. Comparação das listas exatas de endereços e coleta temporal 2020–2026 continuam pendentes.
- **Próximo passo:** executar no Colab, ler manifesto e gráficos, ajustar conforme evidências e preparar protocolo histórico com cobertura harmonizada.
