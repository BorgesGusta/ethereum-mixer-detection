# Caderno científico vivo — itens para o futuro artigo

**Atualização inicial:** 18/11/2026. **Natureza:** rascunho de pesquisa em Markdown, **não** versão final do artigo; não gerar PDF nem realizar formatação editorial nesta etapa. **Fonte de resultados:** fichas e manifestos originais, não este resumo. Registro cumulativo, com decisões e lacunas explícitas.

## 1. Pergunta de pesquisa e recorte

**Pergunta central atual:** quão reproduzível é um classificador estatístico de possíveis mixers na Ethereum quando variam os critérios de elegibilidade, e quais evidências funcionais e de cobertura são necessárias para interpretar os alertas?

**Hipóteses futuras, NÃO confirmadas:** (H1) padrões agregados podem conflitar com funções legítimas de DEX, bridges e relayers; (H2) adicionar evidências contextuais pode melhorar a interpretação/triagem; (H3) separar por protocolo e período poderá revelar fragilidade de generalização da validação por linha.

**Escopo:** identificação de contratos/serviços por dados on-chain; não declarar ilicitude, rastreio individual de usuários nem superioridade preditiva sem testes.

## 2. Evidências que já podem entrar no artigo

| ID | Afirmação apoiada | Fonte/artefato | Limite obrigatório |
|---|---|---|---|
| A01 | Treino da reprodução: 123 janelas, 23 positivas de **um pool Tornado Cash (23 dias)** e 100 negativas de 100 endereços (um dia) | [EXP-01J](../experiments/EXP-01J-resultados-sensibilidade-63x9.md) | Dependência entre linhas; CV por linha não demonstra generalização |
| A02 | Teste 29/10/2020: 1.114.702 transações, 239 aos três pools de referência; 3/3 recuperados; 9 alertas próprios versus 63 no artigo | [EXP-01J](../experiments/EXP-01J-resultados-sensibilidade-63x9.md); [artigo base](https://drive.google.com/file/d/1FflHcOmD3lsO6HeGOp4D85RQbQz7c4EG/view) | **Reprodução parcial**, causa da divergência não identificada |
| A03 | RF/limiar 0,50 fixos, elegibilidade mínima de 1/5/10/20 transações: 49/14/9/7 alertas; 3/3 pools em todos os cenários | [EXP-01J](../experiments/EXP-01J-resultados-sensibilidade-63x9.md) | Alterar população não explica por si só os 63, mesmo min_tx=1 dá 49 |
| A04 | Paridade externa por 20/20 hashes de SmartEther/DSProxy na amostra 2020 | [EXP-01G](../experiments/EXP-01G-auditoria-hashes-blockchair-blockscout.md) | Não é auditoria exaustiva de 2020 |
| A05 | Teste **legado** 15/01/2026: 20.214 elegíveis, limiar 0,85, 9 alertas e 3/3 Tornado referência | [EXP-02A](../experiments/EXP-02A-inventario-e-triagem-2026.md) | Já analisado; não é novo holdout cego; 6 restantes sem rótulo negativo independente |
| A06 | Seis contratos adicionais: 315 transações **diretas** no intermediário; 18/18 hashes amostrados validados quanto a hash, from, to, data via Blockscout | [EXP-02B](../experiments/EXP-02B-resultados-auditoria-amostral-2026.md) | 18 amostras ≠ 315 transações externamente verificadas |
| A07 | EXP-02C fechou paginação de três transações MCT-XEN: 83+83+300=466 logs; somando outras 15 amostras = 586 logs em **18 transações amostradas** | [EXP-02C](../experiments/EXP-02C-resultados-logs-e-seletores.md) | Não representa totalidade dos logs de 315 transações |
| A08 | Identificações documentais: OKX DEX, ApeCoin OFT Adapter, SwappableBridge, Chainlink CCIP Router, MCT-XEN, Wormhole; funções amostradas `send`, `swapAndBridge`, `ccipSend`, `batchClaimRank`, `deliver` | [EXP-02A](../experiments/EXP-02A-inventario-e-triagem-2026.md), [EXP-02B](../experiments/EXP-02B-resultados-auditoria-amostral-2026.md) | Identidade/ABI atual não prova implementação histórica nem rótulo negativo |
| A09 | Scripts EXP-02B/02C idênticos nas cópias Drive/GitHub; 4 saídas de auditoria conferidas por SHA-256 com os manifestos | [Auditoria dirigida](../AUDITORIA_DRIVE_D1-4_2026-11-18.md) | Migração integral não certificada; não mede desempenho do modelo |
| A10 | Cinco testes unitários de funções do pipeline passaram em ambiente local | [Relatório de testes](../TESTES_D1-3_2026-11-18.md) | Não comprova paridade com datasets nem classificação independente |

## 3. Limitações e ameaças à validade a preservar

- Divergência **63 × 9** sem reprodução estritamente equivalente do universo e da seleção de treino dos autores; contato aos autores registrado em 17/11/2026, status de resposta a reconferir no fechamento.
- Semântica de `MIN_TX`, discretização das entropias, Router/transações diretas e abrangência de traces exige comparação precisa por execução e data.
- Positivos do treino advêm de um contrato; vazamento por contrato/protocolo na validação por linha pode superestimar desempenho de generalização.
- Seis contratos 2026 continuam com rótulo **indeterminado**, não seis falsos positivos.
- Proxies/seletores sem validação histórica no bloco da execução; HTTP 200 e ABI atual não são prova de código executado no passado.
- Amostragem de somente alertas causa viés de verificação; EXP-03 deve incluir controles de **não alertas**, com plano registrado antes da análise.
- Dataset 2026 e dia de 2020 já explorados; não reutilizar como testes cegos de um novo método.
- Acurácia, F1/precision/recall populacionais e superioridade do modelo contextual **não foram demonstrados**.

## 4. Contribuições científicas possíveis

**Já sustentadas:** reprodução parcial documentada, análise de sensibilidade controlada, reconciliação externa de amostras, cobertura detalhada de eventos, rastreabilidade e limites metodológicos explicitados.

**Em construção:** protocolo de auditoria contextual com controle de seleção e análise de não-alertas; matriz de verificação por contrato, data, função e cobertura; ground truth por revisão independente.

**Condicionais (somente após execução):** diferença estatística de comportamento entre classes com rótulos independentes; desempenho comparativo RF versus método contextual em split por protocolo/período; generalização para mixers de outros protocolos.

## 5. Elementos a preparar mais tarde para Overleaf

- Tabela de composição do treino/validade externa, usando EXP-01J.
- Tabela de reprodução com 63 e 9 **sem** chamar a diferença de erro do artigo.
- Gráfico 49/14/9/7 com elegíveis e limiar fixo, vinculando CSV/manifesto.
- Diagrama do fluxo de auditoria: entrada → triagem estatística → transação/trace → ABI e proxy histórico → evidência/rotulagem por dois revisores → limites de inferência. **Conceitual até execução do EXP-03.**
- Matriz dos seis contratos 2026: associação documental, n_tx, amostras, método, eventos, proxy histórico e status `indeterminado`.
- Comparação de cobertura entre alertas e não alertas **somente após EXP-03**.
- Referências bibliográficas com autoria, DOI, status editorial e data de acesso verificados. O artigo v0.1 foi compilado tecnicamente, mas a revisão editorial continua pendente.

## 6. Backlog científico do texto

- [ ] Atualizar RQ e redação após resultados adicionais sem antecipar conclusões.
- [ ] Verificar completa autoria e referência editorial de Leale/Sendin e Barbereau; conferir os trabalhos FPTracer, MixGuard, StealthLink, GNN e Akopova nas fontes primárias.
- [ ] Conferir metodologia/contagens do artigo-base no PDF durante revisão final, não substituir pelo resumo.
- [ ] Completar tabela de proveniência: execução ↔ notebook/hash/commit ↔ insumo/manifesto ↔ saída.
- [ ] Adicionar seção de amostragem e análise do EXP-03 **apenas se executado**, distinguindo plano de resultado.
- [ ] Debater se contribuição principal será **reprodutibilidade e auditoria** (já sólida) ou detector melhorado (depende de teste independente).
- [ ] Só então revisar o texto final e formatar no Overleaf.

## 7. Diário de decisões redacionais

- **18/11/2026 — Aceita:** manter **este caderno Markdown** como rascunho científico vivo; **não gerar novos PDFs de artigo** automaticamente. O `artigo/overleaf/` continua preservado como fonte histórica v0.1, mas não é prioridade de edição enquanto experiências e interpretação estiverem em aberto.
- **18/11/2026 — Aceita:** o experimento EXP-03 deve aproveitar todos os artefatos EXP-02A/B/C; não coletar de novo os logs já completos sem razão registrada.
- **18/11/2026 — Proposta:** investigação contextual de alertas e não alertas para reduzir o viés de verificação. Não deve ser descrita como experimento executado até conter outputs novos e manifestos.

**Regra de atualização:** toda entrada nova incluir data, autor/revisor quando houver, status `ideia / planejado / executado / auditado / refutado`, link de evidência e o que o resultado NÃO prova. Nunca apagar um registro histórico; corrigir por adendo datado.
