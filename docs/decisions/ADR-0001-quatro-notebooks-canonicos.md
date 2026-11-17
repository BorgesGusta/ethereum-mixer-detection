# ADR-0001 — Quatro notebooks canônicos

- **Data:** 2026-11-16
- **Status:** aceita para orientar a organização; implementação pendente
- **Contexto:** proliferaram notebooks independentes com código duplicado, datas, datasets e decisões incompatíveis; isso prejudica a compreensão e a redação do artigo.
- **Decisão:** preservar notebooks históricos em `notebooks/legacy`, consolidar trabalho novo em quatro notebooks (reprodução, avaliação, temporal, auditoria) e mover lógica para `src/ethmix`.
- **Justificativa:** separa apresentação/estudo do código compartilhado; facilita testar regressões e versionar protocolos; mantém experimentos separados mesmo quando executados pelo mesmo notebook.
- **Consequências:** refatoração gradual com testes de paridade antes de substituir fluxos; arquivos legados permanecem como referência, não são deletados.
- **Evidências:** inventário de múltiplas variantes dos experimentos 03 e 10 e acervo histórico no Drive; discussão de reorganização em 16/11/2026.
- **Risco:** refatoração pode alterar resultados se fórmulas e semântica de Router não forem preservadas; mitigação: testes com dados conhecidos e hashes.
- **Issues relacionadas:** #1 e #3.
