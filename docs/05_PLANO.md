# Plano de trabalho

## Etapa A — Consolidar evidências (pendências que permanecem)
- [ ] Identificar versão executada de cada notebook e associar resultado ao Drive
- [ ] Registrar ambientes, parâmetros, hashes e métodos
- [ ] Revisar lacunas na cronologia 01–09
- [ ] Reconciliar decisões antigas contraditórias por ADR, sem apagar histórico

## Etapa B — Pipeline reproduzível
- [ ] Extrair funções de features para `src/` e adicionar testes de paridade
- [ ] Diferenciar transação direta e atribuição por chamada/Router
- [ ] Manifestos por execução, schemas e checagens de integridade
- [ ] Congelar protocolos antes de executar novos testes

## Etapa C — Pesquisa temporal 2020–2026
- [ ] Planejar amostragem e cobertura das chamadas históricas
- [ ] Construir exemplos positivos de múltiplos contratos e dias de 2020
- [ ] Auditar negativos, não assumir 'todo outro contrato = não mixer'
- [ ] Comparar modelos estáticos e atualizados em períodos posteriores
- [ ] Medir drift com cobertura e atribuição harmonizadas

## Etapa D — Artigo
- [ ] Consolidar perguntas, hipóteses e limitações
- [ ] Extrair tabelas/figuras rastreáveis das execuções
- [ ] Preparar manuscrito e referências no Overleaf
- [ ] Conferir reprodutibilidade para acesso do professor

**Princípio:** nenhum novo resultado vira conclusão do artigo sem protocolo, dados, código e interpretação vinculados.


## Atualização de prioridades — 17/11/2026

1. **P0 documentação:** reconciliar índice, painel, cronologia e decisões com [CHECKLIST_VIVO](CHECKLIST_VIVO.md) e EXP-01J/02B/02C; distinguir resumos de evidência original.
2. **P1 artigo v0.1:** compilar `artigo/overleaf/main.tex` com pdfLaTeX + BibTeX e revisar tabelas, citações, margens, dados e limitações; **fontes já existem**, build ainda não verificado.
3. **P1 integridade:** inventário recursivo e SHA-256 da cópia do Drive; vincular execução ↔ notebook/commit ↔ manifesto/outputs; não sobrescrever legados.
4. **P2 revisão histórica:** investigar implementação de proxies na data de referência e seletores sem identificação; preservar casos inconclusivos e cobertura parcial.
5. **P2 estudo independente:** obter rótulos negativos auditados e positivos de outros protocolos, predefinir splits e métricas e usar período não selecionado anteriormente; **não alegar superioridade até executar avaliação válida**.
6. **P3 submissão:** verificar bibliografia/DOI e chamada oficial; revisão por orientador antes de fechamento.

**Correção de status:** já há protocolo [EXP-02](experiments/EXP-02-protocolo-temporal-contrato.md), resultados [EXP-01J](experiments/EXP-01J-resultados-sensibilidade-63x9.md), [EXP-02B](experiments/EXP-02B-resultados-auditoria-amostral-2026.md), [EXP-02C](experiments/EXP-02C-resultados-logs-e-seletores.md) e manuscrito LaTeX v0.1; nenhuma nova validação confirmatória por protocolo foi executada nesta consolidação.
