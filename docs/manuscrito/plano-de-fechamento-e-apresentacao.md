# Plano de fechamento — artigo Overleaf e apresentação

**Versão:** 17/11/2026. **Situação:** manuscrito **v0.1 redigido, não submetido**; roteiro de apresentação inicial preparado. Não confundir documento LaTeX existente com PDF compilado ou aprovado.

## Marco 1 — Validar a edição do artigo no Overleaf (próxima ação)

**Arquivos fonte:** [`main.tex`](../../artigo/overleaf/main.tex), [`referencias.bib`](../../artigo/overleaf/referencias.bib), [`figuras/sensibilidade.tex`](../../artigo/overleaf/figuras/sensibilidade.tex), [`README.md`](../../artigo/overleaf/README.md).

- [x] Rascunho LaTeX v0.1 com resumo, abstract, introdução, fundamentos, métodos, resultados, discussão, ameaças, conclusão e referências.
- [x] Tabelas de paridade 63×9, sensibilidade 49/14/9/7 e seis contratos 2026.
- [x] EXP-02C consta como executado: 3 transações MCT-XEN, 83/83/300 logs (466) e 18 transações amostradas completas.
- [ ] Abrir no Overleaf e **compilar com pdfLaTeX + BibTeX**; registrar log, número de páginas e mensagens de erro/overfull.
- [ ] Inspecionar o PDF resultante: português e acentos; tabelas dentro das margens; legendas; bibliografia e números corretos.
- [ ] Reestruturar para o template oficial **somente quando a conferência/trilha for escolhida**.
- [ ] Conferir autores e afiliações — e anonimização, se exigida.

**Atenção:** não foi gerado ZIP pronto nem verificado o build no Overleaf neste momento. Não afirmar compilação concluída.

## Marco 2 — Revisão científica do manuscrito com material existente

- [x] Descrever EXP-01J, EXP-02A, EXP-02B e EXP-02C como executados e com fontes rastreáveis.
- [x] Assinalar que 63 versus 9 é divergência **sem causa comprovada**, apesar de sensibilidade a critérios de elegibilidade ter sido demonstrada.
- [x] Apresentar as correspondências 20/20 (2020) e 18/18 (amostra 2026) sem extrapolar para toda a população.
- [x] Diferenciar três pools Tornado conhecidos de seis outros serviços apenas **identificados documental/funcionalmente**.
- [ ] Conferir bibliografia e DOI em cada PDF; ampliar trabalhos relacionados com referências completas.
- [ ] Preparar figura do fluxo metodológico em formato reproduzível e gráfico com fonte dos dados.
- [ ] Congelar versão do texto e dos resultados quando terminarem as revisões, registrando commit e hashes.

## Marco 3 — Experimentação adicional mínima (contribuição original)

- [x] Completar paginação dos logs da **amostra de 18 transações** no EXP-02C.
- [ ] Determinar implementação histórica dos proxies OKX, MCT-XEN e Wormhole em 15/01/2026, ou marcar cada caso inconclusivo.
- [ ] Expandir auditoria por política pré-definida e incluir amostra de **não alertas**, para reduzir viés de verificação.
- [ ] Construir rótulos negativos auditados com dois revisores e positivos de **outros protocolos mixer**.
- [ ] Predefinir RF original vs heurística funcional vs variante contextual; treino, validação e teste separados por **contrato e período**.
- [ ] Medir precision, recall, F1 e PR-AUC somente em teste com ground truth válido; registrar amostras e limites.
- [ ] Se testes adicionais se mostrarem inviáveis, manter foco de artigo **em reprodutibilidade, auditoria e sensibilidade de elegibilidade**, sem afirmar detector melhor.

## Marco 4 — Apresentação científica

[Roteiro inicial de 10 slides](../apresentacao/roteiro-cientifico-v0.md). A apresentação não precisa afirmar melhorias ainda não medidas.

| Slide | Título | Uma conclusão defendível |
|---|---|---|
| 1 | Pergunta do artigo | Mixer não é sinônimo de ilegalidade |
| 2 | Problema de classificação | DEX, bridge e mixer podem compartilhar estatísticas |
| 3 | Trabalho-base | Quatro features + Random Forest |
| 4 | Dados e rótulos | 23 positivos de um contrato, 100 negativos de um dia |
| 5 | Reprodução | 3/3 pools detectados; 63 vs 9 não resolvido |
| 6 | Sensibilidade | Mínimo de transações altera alertas 49/14/9/7 |
| 7 | Auditoria externa | 20/20 hashes em 2020 e 18/18 amostras em 2026 |
| 8 | Contexto funcional | send / swapAndBridge / ccipSend / batchClaimRank / deliver |
| 9 | Cobertura e rótulos | 466 logs nos 3 hashes MCT-XEN; 6 rótulos indeterminados |
| 10 | Conclusão | Auditoria e interpretação mais rigorosas, não maior acurácia demonstrada |

**Critérios:** adaptar número de slides e duração à chamada; conferir que gráficos/tabelas são legíveis; preparar falas e 6 perguntas difíceis; ensaiar com tempo real.

## Marco 5 — Submissão

- [ ] Selecionar conferência/trilha **com chamada oficial aberta ou calendário confirmado**, pesquisar escopo, extensão de páginas, template, anonimização, modalidade e prazos.
- [ ] Revisão por orientador/coautores; aprovação de autoria e versão.
- [ ] Conferir direitos de dados brutos e política de disponibilização/artefatos.
- [ ] Preparar PDF final, fontes LaTeX, repositório versionado, informações de reprodução e anexos permitidos.
- [ ] Submeter apenas após revisão final. **Aceite não pode ser prometido**.

## Ordem de execução recomendada

**Agora:** compilar o manuscrito v0.1 no Overleaf e corrigir apresentação gráfica. **Em paralelo:** revisar literatura e consolidar resultados do EXP-02C. **Depois:** escolher entre fechar artigo de auditoria/reprodutibilidade ou realizar avaliação contextual adicional, dependendo da disponibilidade de ground truth independente. **Só então:** formatar para a chamada escolhida e finalizar os slides.
