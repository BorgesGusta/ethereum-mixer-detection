# Checklist de fechamento — estudo de mixers Ethereum

## Documentos preparados

- Manuscrito editável para SBC: `docs/manuscrito/artigo_auditoria_mixers_sbc_2026.tex` (fonte principal).
- EXP-07: 12 comparações/60 folds, relatório auditado, **apenas um contrato positivo**; F1 exploratório interno, sem generalização.
- EXP-08: protocolo de candidatos (não rotulados), código de triagem offline, quatro testes locais, roteiro de demonstração.
- Biblioteca NotebookLM: pasta exclusiva, com aulas e evolução dos experimentos, a atualizar quando a redação do manuscrito mudar.

## Checagens antes da entrega

- [ ] Identificar todos os autores, orientador, curso e afiliações corretas; remover placeholders.
- [ ] Conferir limite 4–6 páginas após compilação no template SBC **real**, não apenas no fallback local.
- [ ] Verificar figuras/tabelas, quebras, bibliografia e links.
- [ ] Não converter alertas 2026 indeterminados em falsos positivos (arquivos legados tinham métricas provisórias inválidas).
- [ ] Não usar F1 0,9778 como detecção de protocolos não vistos; nenhum teste externo por contrato foi feito.
- [ ] Verificar rótulos de EXP-05 apenas após revisão cega de ambos avaliadores; se pendente, omitir.
- [ ] Executar novamente `python3 -m unittest -v test_triage` no ambiente de apresentação.
- [ ] Alinhar datas, apêndices, repositório e fontes do NotebookLM.
- [ ] Compilar documento oficial e fazer inspeção visual; validar referências e formato pedido pelo professor.

## Histórico científico verificável

- Revisão e metodologia: `docs/manuscrito/CADERNO_CIENTIFICO_VIVO.md`.
- Resultados EXP-06C: `docs/experiments/EXP-06C-resultados-auditoria-2026-11-19.md`.
- Resultados EXP-07: `docs/experiments/EXP-07-resultados-auditoria-2026-11-19.md`.
- Plano EXP-08: `docs/experiments/EXP-08-plano-seguranca-e-conjuntos.md`.
- Evidências e manifestos no Drive da pesquisa.
