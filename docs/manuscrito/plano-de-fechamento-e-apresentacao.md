# Cronograma por marcos — Experimentos, artigo e apresentação

**Atualizado: 17/11/2026.** Planejamento sem promessa de prazo.

## Onde estamos

| Etapa | Situação | Documento |
|---|---|---|
| Reprodução do SBSeg 2025 | **Concluída parcialmente:** 3/3 pools, 9 vs 63 alertas | EXP-01J |
| Sensibilidade à elegibilidade | **Concluída:** 49/14/9/7 alertas para min_tx 1/5/10/20 | EXP-01J |
| Auditoria 2020/2026 | **Concluída nas amostras:** 20 hashes em 2020, 18 hashes em 2026 | EXP-01G e EXP-02B |
| Paginação MCT-XEN | **Concluída** para as 3 transações amostradas: 83+83+300 = 466 logs; 18/18 amostras com paginação completa | EXP-02C |
| Histórico de proxies e dois seletores | **Pendente:** dados insuficientes | EXP-02C |
| Ground truth independente | **Pendente:** seis contratos não são negativos confirmados | EXP-02B |
| Holdout por protocolo/tempo e ganho contextual | **Não executado:** depende de múltiplos positivos e negativos auditados | EXP-02 |
| Manuscrito editável | **Iniciado:** main.tex, referencias.bib e figura editável | artigo/overleaf |
| Apresentação científica | **Roteiro iniciado:** slides finais após congelar resultados | docs/apresentacao |

## Estratégia de publicação

**Rota A — auditoria/reprodutibilidade:** descreve os resultados demonstrados; escrevê-la **já**. Pode ser submetida a uma trilha adequada de métodos/estudos de caso se houver avaliação acadêmica, bibliografia validada e contribuição suficiente.

**Rota B — melhoria contextual:** exige ground truth externo e teste sem vazamento em contratos/protocolos novos. Não prometer desempenho superior antes dos dados; se houver resultados robustos, atualizar título, método e conclusões.

## O que escrever desde já

- [x] Introdução, fundamentação, método e limitações preliminares.
- [x] Tabelas de reprodução, sensibilidade e auditoria em LaTeX.
- [x] Resumo PT/EN provisório e bibliografia `.bib`.
- [ ] Conferir autores, instituições, referências e DOI exatos.
- [ ] Figuras finais adicionais com proveniência e legendas.
- [ ] Revisão por professor/orientador e autorizações.
- [ ] Conferir chamada/limite de páginas/template oficial do congresso escolhido.

## Experimentos restantes sem estender indefinidamente a pesquisa

1. Avaliar a viabilidade de obter implementação histórica dos três proxies; se não, registrar explicitamente como inconclusivo.
2. Elaborar rubrica de rótulos com duas revisões independentes e cobertura de transações. Incluir pelo menos amostra de não alertas sem seleção pelo score.
3. Tentar localizar positivos de mixers de outro protocolo, com contratos e período verificáveis.
4. Só então decidir **se** a comparação contextual é viável; caso negativo, concluir pela **rota A** com dados existentes e limitações.
5. Separar todas as métricas de população não rotulada (número de alertas) das métricas com ground truth.

## Apresentação

Roteiro interno já pode ser usado para seminário. A apresentação final deve usar exatamente os números do manuscrito congelado, sem transformar a hipótese contextual em resultado. Priorizar 3 figuras: pipeline auditável, sensibilidade de alertas, escada de evidências (hash → log → função → rótulo). Questões prováveis: 63 vs 9, filtro de elegibilidade, um único pool positivo no treino, falsos positivos não validados e o papel de proxies/Router.

## Links

- [Manuscrito editável para Overleaf](../../artigo/overleaf/main.tex)
- [Referências BibTeX](../../artigo/overleaf/referencias.bib)
- [Gráfico editável](../../artigo/overleaf/figuras/sensibilidade.tex)
- [Relatório EXP-02C](../experiments/EXP-02C-resultados-logs-e-seletores.md)
