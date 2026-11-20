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

## Diário de pesquisa — preparação EXP-03, 18/11/2026

**Status: implementação preparada, não executada.** O inventário do Drive e a inspeção do notebook legado 07b não localizaram exportação de scores completos para os não alertados. Confirmados os arquivos `features_2026-01-15.parquet`, `modelo_rf.joblib`, `sinalizados_teste_2026.csv` e o limiar previamente congelado 0,85. Foi versionado [script de seleção de controles](../../scripts/exp03_selecionar_controles.py) e [procedimento Colab](../experiments/EXP-03-como-executar-selecao-no-colab.md), com travas de paridade de elegíveis, endereços e scores. **A seleção ainda não foi executada**: ambiente local sem leitor Parquet, instalação indisponível. Não registrar número de controles escolhidos, comparações funcionais ou melhoria de classificador até a execução. Próxima ação é executar apenas esse script no Colab e auditar os novos arquivos, sem repetir o notebook 07b ou as coletas já concluídas.


### Notebook operacional publicado no Drive — 18/11/2026

O notebook [`15_EXP-03_selecao_controles_2026.ipynb`](https://drive.google.com/file/d/15pzH8sNmB8oNYnGRtk9WAiuztmRR5Mzv/view?usp=drivesdk) foi enviado e conferido em `Projeto_Mixers_Ethereum/notebooks/00_ATIVOS/`, arquivo de **8.010 bytes** e SHA-256 **`f6a0dfb38eed7afcc4e3406ee6dac149a55f82916369d523c558ad56c10e48df`**. Possui seis células e executa o script fixado no commit `360d351962ef7aff7db7dc957fbeecbd182058df`. **Não executado no Colab até este registro**. Para rodar: abrir o arquivo com Google Colaboratory e selecionar **Ambiente de execução → Executar tudo**. A pasta de resultados só será criada após a paridade comprovada pelo script; ao finalizar, registrar o link aqui e conferir os outputs/manifesto. Nenhum arquivo anterior foi movido, renomeado ou sobrescrito.

## Diário científico — 18/11/2026 UTC: EXP-03 seleção executada

**Evidência verificada:** [EXP-03 — resultados da seleção](../experiments/EXP-03-resultados-selecao-auditada-2026-11-18.md) e [Drive](https://drive.google.com/drive/folders/1SAdkZVyXcmYs02AYNZACE7h5DEDzPdzJ). Uma inferência de seleção usando modelo legado registrou identidade 9/9 alertas, diferença máxima de probabilidade 0,0, e seis pares alertado/controle na mesma banda de volume de transações. Os SHA-256 do output e três insumos foram reconciliados com bytes recuperados. **Resultado descritivo:** os seis controles provisórios ficaram com score zero, mas não há confirmação de que sejam contratos nem de que funcionem como negativos da mesma classe de entidades. Risco de controles triviais (EOA x contrato), viés de pareamento apenas por `n_tx` e endereço atípico `0xff000...0010` exigem auditoria histórica. **Não constitui melhoria do modelo nem validação de falso positivo.** Mantém o artigo em rascunho Markdown; nenhum PDF novo. Próximo resultado elegível para o artigo: cobertura e adequação histórica dos controles, caso verificada.

## Planejamento EXP-03B — 18/11/2026 (não executado)

Foi preparado e versionado o [notebook EXP-03B](../../notebooks/16_EXP-03B_verificacao_historica_controles_2026.ipynb), já [disponível no Drive oficial](https://drive.google.com/file/d/1xxJUpr3rrTjGdBnLcJwB6te9-ivqqy-U/view?usp=drivesdk), para verificar via `eth_getCode` o código **dos seis controles** no bloco da primeira transação já verificada do alertado associado (dia 15/01/2026). [Protocolo](../experiments/EXP-03B-protocolo-verificacao-tipo-historico.md). Outputs terão resposta por provedor, tipo observado no bloco, disponibilidade de dados históricos e status `indeterminado` para rótulos científicos. **Não é mais um teste de detecção; não reexecuta EXP-02B/02C ou retreina RF.** A execução pelo pesquisador e auditoria de resultados ainda estão pendentes. Risco fundamental: controles selecionados com score zero podem ser EOAs ou não comparáveis a smart contracts, invalidando uma comparação funcional ingênua.

## Diário científico — EXP-03B executado, 18/11/2026 UTC

[Relatório EXP-03B](../experiments/EXP-03B-resultados-verificacao-historica-2026-11-18.md), [outputs Drive](https://drive.google.com/drive/folders/1WZ3tbWDY75Jmt_SBE8KX2EDbiUJzRKwu). **Observado:** seis controles congelados e seis blocos-âncora de 15/01/2026; doze `eth_getCode` tentados com dois endpoints RPC, porém nenhum forneceu estado histórico (6×HTTP 403 e 6×HTTP 525). O Blockscout respondeu com metadados **atuais** em 6/6; um endereço está marcado `is_contract=true`, tipo `eip7702`, e os outros cinco `false`. **Não inferir tipo/estado no bloco passado a partir desses dados atuais.** Os quatro outputs/manifesto estão íntegros; seis casos permanecem com `rotulo_cientifico=indeterminado`. **Contribuição defensável:** evidência de falha de cobertura histórica de provedores consultados e importância da distinção entre estado atual e histórico. **Não demonstrado:** EOA/contrato na data, negativo confirmado, superioridade do RF ou generalização. Próxima opção: fonte histórica validada em consulta piloto de um bloco ou novo desenho de controles contratuais pré-registrado, sem substituir silenciosamente a amostra EXP-03 original. Nenhum novo PDF.

## Técnica de Segurança de Redes a explorar — 18/11/2026

**Proposta conceitual, não resultado:** enquadrar detecção estatística de mixers como um sistema de **detecção de anomalias com triagem e investigação de alertas (analogia a IDS)**: transações → extração de características → score do RF → alerta → verificação de contrato, função, eventos e cobertura → status confirmado/indeterminado. **Não tratar mixer como intrusão, nem alertado como ilícito.** Abordagem complementar: análise de falsos alertas, viés de verificação e logs auditáveis (forense digital). **Pendente** conferir a ementa/roteiros exatos da disciplina antes de afirmar que ela cobriu IDS ou esse método.

EXP-03B teve 12 respostas RPC HTTP sem estado histórico útil; a distinção entre `dados não disponíveis` e `código ausente` demonstra problema de **observabilidade e validade da evidência**, não desempenho do classificador. Novo [EXP-03C](../experiments/EXP-03C-protocolo-piloto-rpc-archive.md) foi **preparado, não executado**: rede chainId 1, WETH como referência de código no bloco histórico, depois apenas um controle congelado. Notebook [no Drive](https://drive.google.com/file/d/1V4u21nJV1gNuAv_7qhO6f1qLAkyJVMIl/view?usp=drivesdk). Não gerar novas métricas nem PDF do manuscrito.

## Alinhamento confirmado com a disciplina Segurança em Redes de Computadores — 18/11/2026

**Fonte:** PDFs fornecidos pelo pesquisador, slides do Prof. Hugo P. Kuribayashi, Unifesspa, 2026.4. São documentos locais recebidos na conversa; mantê-los com seus nomes originais e citar capítulo/página nos rascunhos. Não redistribuir slides do professor no GitHub sem autorização.

### Evidência diretamente presente no material didático

| Material | Páginas | Conteúdo comprovadamente ministrado/documentado | Relevância |
|---|---|---|---|
| `SRC-Cap0-Apresentação da Disciplina.pdf` | 6–8, 15–17 | Objetivos de CID, criptografia, firewalls/IDS; ementa cita IDS, NAT, VPN; estudo de caso com reprodução de artigo; entrega SBC 4–6 páginas via Overleaf | Requisitos acadêmicos e enquadramento; ementa **não** prova aula prática de IDS ministrada |
| `SRC Cap2 - Parte 1.pdf` | 3, 5–13 | Integridade por hash criptográfico, efeito avalanche e SHA-256 (inclui referência a blockchain) | **Técnica diretamente implementada**: hashes SHA-256 dos insumos/outputs, manifesto e auditabilidade |
| `SRC Cap4 - Parte 2.pdf` | 10–16 | Firewall por parâmetros de pacotes, filtro por conteúdo de aplicação, assinaturas/regex e WAF | **Analogia metodológica proposta**: triagem em camadas, features primeiro e evidência funcional depois; **não** chamar de firewall implementado |
| `SRC Cap3 - Parte 1 e Parte 2.pdf` | introduções e assinatura | Criptografia simétrica/assimétrica, autenticidade e assinatura digital | Possível aprofundamento sobre verificações criptográficas de transações e prova de origem, **não implementado** nesta pesquisa |
| `SRC Cap4 - Parte 1.pdf` | seções HTTPS, HMAC, X.509 | Protocolos de comunicação segura, integridade/autenticidade do canal | Potencial segurança de coleta RPC; não confundir HTTPS com autenticidade do estado histórico |

### Enquadramento responsável da contribuição

**Já feito:** (a) reprodução parcial do detector RF e suas limitações, (b) SHA-256 dos dados e evidências com manifesto, (c) triagem contextual qualitativa de alertas. **Proposto:** desenho de triagem em duas camadas, inspirado em filtros em níveis distintos, e eventual avaliação comparativa pré-registrada com ground truth independente. O fluxo pode ser relacionado ao ciclo de detecção/triagem de alertas de IDS **por analogia**, mas o pipeline atual **não é um IDS de rede** e não captura pacotes IP/TCP nem detecta invasões; mixer, por si, não caracteriza ataque ou crime.

**Precisamos evitar uma afirmação excessiva:** a ementa prevê IDS, mas os capítulos anexados até aqui não demonstram exercícios/implementação de IDS específicos. Já a função SHA-256 está explicitamente nos slides e **foi operacionalizada** na trilha experimental.

**Compromisso de entrega:** distinguir artigo acadêmico final da disciplina (resumo expandido 4–6 páginas formato SBC, Overleaf) da publicação científica mais longa que poderá resultar das extensões. **Não gerar PDF agora**, seguindo preferência expressa do pesquisador; continuar no caderno Markdown e reservar edição do artigo para a fase de consolidação.

## Registro de execução EXP-04 — 18/11/2026 (realizado)

O script [EXP-04](../../scripts/exp04_triagem_evidencias.py) foi **executado localmente sem nova consulta on-chain ou treinamento**, com [manifesto e matrizes no Drive](https://drive.google.com/drive/folders/1drM-F9LfePDFSYrGYzlNmySfy0dWQK_K) e [relatório de método/limitações](../experiments/EXP-04-resultados-triagem-por-evidencia.md). Reconciliou 6 alertas adicionais de 2026, 18 transações anteriormente validadas, 586 logs das amostras após EXP-02C e 6 controles históricos ainda inconclusivos (0 com estado histórico válido EXP-03B). **Contribuição imediata:** integridade SHA-256 e *qualidade de evidência por alerta*, em processo inspirado na filtragem em camadas (Capítulo 4 parte 2) e verificação de integridade (Capítulo 2 parte 1) dos slides do Prof. Hugo. **Não cria novo classificador nem rótulo de mixer/não mixer; não prova redução de falsos positivos ou maior performance.** Ideal para futura subseção 'Auditabilidade da triagem contextual', com tabela de cobertura, após revisão. Não gerar artigo em PDF ainda.


## Preparação do EXP-05 — rotulagem independente (18/11/2026)

**Status: protocolos e duas fichas em branco preparados, revisão ainda não executada.** [Protocolo EXP-05](../experiments/EXP-05-protocolo-rotulagem-independente.md), [gerador versionado](../../scripts/exp05_preparar_revisao.py), [fichas no Drive](https://drive.google.com/drive/folders/11Ph9gtKlyR2q3jyLfehcOPlNHf2OBU38), [índice interno separado](https://drive.google.com/drive/folders/1-U6awHaGi9-2N_n0V3_BbQHb-mZxZLcp). Conferidas as 9 identidades do ranking 2026: três referências do mesmo protocolo Tornado Cash e seis contratos adicionais sem rótulo independente. Dois formulários de 9 casos, sem scores ou rótulos legados, preparados para avaliação por revisores distintos. Nenhum novo rótulo foi atribuído.

**Decisão metodológica importante:** definir classe **estreita** de mixer por pool e desvinculação depósito→saque, exigindo evidência funcional e temporal; RAILGUN (shield/unshield) e Aztec Connect (privacidade de outra arquitetura) são **candidatos de famílias a investigar e/ou fora do escopo**, não exemplos positivos equivalentes por padrão. A fonte de identidade histórica/ABI/código em bloco é indispensável, principalmente para proxies. Dois revisores e eventual adjudicador precisam preservar casos indeterminados. A seleção condicionada aos alertas impede medir precisão/recall/F1 populacionais. A classe também não implica ilicitude.

**Próximos gates:** obter duas fichas de revisão fundamentadas e independentes; reconciliar discordâncias; construir separadamente conjunto fora dos alertas e de múltiplos protocolos, em período ainda não usado na escolha de método. Conexão com disciplina: SHA-256 para integridade das evidências e análise contextual em camadas. **Sem PDF/Overleaf por enquanto.**

## Diário científico — EXP-06, 18/11/2026: candidatos de outras famílias (somente documental)

[Inventário EXP-06](../experiments/EXP-06-inventario-candidatos-referencia-multiplos-protocolos.md). **Descoberta documental:** código/configuração oficiais da 0xbow identificam o **Privacy Pools v1 ETH pool** na Ethereum mainnet `0xF241d57C6DebAe225c0F2e6eA1529373C9A9C9fB`, Entrypoint `0x6818809EefCe719E480a7526D76bD3e561526b46` e `deploymentBlock=22153707` na configuração. A empresa informa lançamento em março/2025. **Sem verificação independente da transação de criação ou do bytecode no bloco** e sem consenso sobre enquadramento na classe estreita de mixer definida no EXP-05. Outros candidatos: RAILGUN (shield/unshield) e Aztec Connect (rollup/bridge) devem continuar categorias distintas; 100 ETH do Tornado é mesma família; Privacy Pools v2 é posterior ao recorte 15/01/2026. **Status: pesquisa documental, zero novas amostras/rótulos/treinos/scores.** Próxima etapa é verificação histórica e aprovação taxonômica antes de definir avaliação confirmatória; sem PDF.

## EXP-06A — evidência inicial de depósito e etapa preparada (18/11/2026)

Na investigação de protocolo distinto de Tornado Cash, uma [transação pública no Etherscan](https://etherscan.io/tx/0x495294c929babdbc035041904bb87d8fc2494c1c7841e2e6e074b84367a5dcef) foi verificada: bloco 22169054, 31/03/2025 19:42:59 UTC, `deposit(uint256)` ao Entrypoint da 0xbow e transferência interna de 0,1 ETH para o Privacy Pools v1 ETH pool, com evento `Deposited` na interface do explorador. **Isso sustenta a atividade de depósito observada nessa transação**, não prova funcionalidade de saque com anonimato no mesmo período, implantação histórica exata, comparação com RF ou novo rótulo mixer confirmado. [Protocolo com limitações](../experiments/EXP-06A-piloto-implantacao-eventos-privacypools.md), [notebook Colab na pasta ativa](https://drive.google.com/file/d/14so42iaP7joZ2OR5LkYLq20osUJE61Ha/view?usp=drivesdk). **Notebook preparado e versionado, ainda não executado.** Próxima ação: executar piloto de recibos/implantação Blockscout sem node archive; depois verificar retirada e passar por revisão funcional independente distinta do EXP-05. Sem PDF.

## Diário EXP-06A executado e auditado — 18/11/2026

[Relatório com evidências e SHA-256](../experiments/EXP-06A-resultados-auditoria-2026-11-18.md), [Drive de execução](https://drive.google.com/drive/folders/1K83QFXRH_pGd5muiMNHhUxjNYdKwxt_l). Duas transações Ethereum foram consultadas pelo Colab via Blockscout: a **candidata de criação** ocorreu no bloco 22.153.714, 29/03/2025, status OK, mas sem `created_contract`; a configuração da 0xbow declara `deploymentBlock=22.153.707`, divergência de 7 blocos **não resolvida**. Não inferir que não houve deploy, pois a chamada foi enviada a outro contrato e poderia envolver uma factory; isso **não foi provado**. A transação de **depósito inicial** do bloco 22.167.294, 31/03/2025, status OK, tem 3 logs paginados completos, 2 no endereço do pool ETH. Confirma interação histórica amostrada com pool, **não** a função definitiva nem saque/desvinculação. **Sem novo positivo, F1, treino ou teste independente.** Próxima tarefa EXP-06B: traces/criação interna e fonte de retirada histórica, sem repetir a coleta já validada. Nenhum PDF novo.

## EXP-06B — piloto complementar preparado (18/11/2026)

Após auditoria de EXP-06A (criação candidata em bloco 22.153.714, implantação declarada no 22.153.707 e depósito com dois logs do pool), foi preparado [protocolo EXP-06B](../experiments/EXP-06B-protocolo-traces-e-retiro.md), [script versionado](../../scripts/exp06b_validar_criacao_saques.py) e [notebook na pasta 00_ATIVOS](https://drive.google.com/file/d/1Pej3E3Nr65figYCEtZ2axC1Fal1D-NiJ/view?usp=drivesdk). **Não executado em Colab até este registro.** O piloto verifica metadados atuais e até quatro páginas de traces da transação candidata, além de apenas duas páginas de logs do pool. Os logs são amostrais e podem ser recentes: **não permitem concluir ausência de saques, nem provar desvinculação**. Qualquer trace de criação precisará de bloco, contrato e sucesso reconciliados. Nenhuma classe, métrica ou novo experimento de ML está declarado. Nenhum PDF de artigo.

## Diário EXP-06B executado e auditado — 19/11/2026

[Resultados EXP-06B auditados](../experiments/EXP-06B-resultados-auditoria-2026-11-19.md), [Drive da execução](https://drive.google.com/drive/folders/1-_iI6xOScAy0-a33Y2Rt94BdDFfBymyq); SHA-256 de `evidencias_exp06b.json` verificado contra o manifesto. **Fato novo:** um trace `CREATE` com `success=true` criou o pool `0xf241...9fb` internamente na transação candidata do bloco 22153714, completando a evidência de criação que o EXP-06A não conseguiu pela transação principal. A diferença de sete blocos em relação à configuração `deploymentBlock=22153707` **continua aberta**. A amostra limitada e parcial de 100 logs recentes (blocos 26405646–26449771) contém 44 nomes decodificados como `Withdrawn`, 1 como `Ragequit`, 49 `LeafInserted`, 6 `Deposited`; 45 indicadores lexicais **não equivalem a 45 saques com prova de desvinculação** nem representam a janela histórica original. Endpoint de fonte verificada retornou HTTP 400; várias linhas têm hash/timestamp ausentes. **Estado:** evidência forte da criação interna; indícios funcionais posteriores; falta uma transação de retirada de época, ABI/implementação histórica e revisão de taxonomia. Zero novos rótulos e métricas. Próximo: EXP-06C dirigido e pré-registrado, sem retreinar nem reconsultar EXP-06A/06B; sem PDF.


## EXP-06C — busca histórica de retiradas preparada (19/11/2026)

[Protocolo pré-registrado](../experiments/EXP-06C-protocolo-retiradas-historicas.md), [script](../../scripts/exp06c_retirada_historica.py), [notebook ativo no Drive](https://drive.google.com/file/d/1mtUxaTHxExTXBKUI5cUAGlCQCBVcN5zt/view?usp=drivesdk). **ESTADO: preparado, não executado no Colab.** A análise EXP-06B mostrou um trace CREATE do pool em bloco 22153714 e amostras recentes de eventos `Withdrawn`, mas não validou retiradas no período da implantação nem em janeiro/2026. O EXP-06C procura até 2 transações `Withdrawn` por janela, em **blocos predefinidos** 22153714–22253714 e 24233073–24240273, pela API legada de logs com filtro `address+topic0+fromBlock/toBlock`, depois confere status da transação e logs correspondentes na API v2. **Sem treino, classificação automática, comparação ou rótulos de mixer**. `Ragequit` deve permanecer separado de retirada privada; APIs parciais impedem afirmar inexistência. Testes locais de sintaxe e API simulada passaram, mas não se produziu evidência on-chain nova nesta preparação. Sem PDF.

## EXP-06C executado e auditado — 19/11/2026

[Relatório científico EXP-06C](../experiments/EXP-06C-resultados-auditoria-2026-11-19.md) e [artefatos no Drive](https://drive.google.com/drive/folders/1O9mAvAPx4HOER9Cn-GduUSCmriISVAnC). SHA-256 de `evidencias_exp06c.json` confere com manifesto: `f2c6243979fbb38266718f9ed28884abf4b9a7edf3439a1cf8cf1db606ba6922`. **Quatro transações históricas verificadas**, duas em 2025 (blocos 22167564, 22168311) e duas na janela de janeiro/2026 (24233404, 24234863), todas `status=ok`, logs completos e um log do pool com assinatura `Withdrawn`. A janela 2025 foi interrompida após 3 logs candidatos vistos e 2 transações checadas; a janela 2026 cobriu seus blocos predefinidos, encontrou 13 logs candidatos e checou apenas 2 transações. **Não são 16 saques verificados nem amostra representativa.** O mecanismo de desvinculação, ABI histórica e rótulo independente continuam pendentes; nenhum ML novo ou métrica foi calculado. Considerando entrega em 20/11/2026, a recomendação é concluir artigo SBC e avaliação documental antes de novos pilotos.

## EXP-07 v2 — quatro classificadores × três grupos de atributos (19/11/2026)

[Protocolo pré-registrado](../experiments/EXP-07-protocolo-comparacao-e-ablacao.md) e [notebook EXP-07 v2 no Google Drive](https://drive.google.com/file/d/1nKI1sM5pbY-UOAI6nxraTTSzkNFY8MHW/view?usp=drivesdk). Preparadas 12 combinações, com `A_original_5`, `B_sem_volume_4`, `C_entropias_3`; Random Forest, Regressão Logística, Árvore de Decisão e Gradient Boosting, folds idênticos para todos. O notebook audita contratos positivos e tenta separação por contrato; se inviável, faz validação **somente exploratória por linhas**, advertindo explicitamente sobre vazamento de identidade. Teste local com **dados sintéticos** passou e gerou 12 linhas, mas **nenhum resultado real do EXP-07 foi produzido** (leitor de Parquet indisponível localmente). Executar notebook Colab, auditar resultados antes de incluir qualquer tabela no artigo. Prazo de entrega 20/11; não reivindicar generalização a protocolos distintos. Sem PDF de artigo nesta etapa.

## EXP-07 v2 executado e auditado — 19/11/2026 (20/11 00:36 UTC)

[Relatório detalhado com hashes e 12 F1 médios](../experiments/EXP-07-resultados-auditoria-2026-11-19.md), [pasta real no Drive](https://drive.google.com/drive/folders/1iekmCwwXYnxzYNp7jJ6Ye5S4O56UN0b6), [guia de estudo na biblioteca NotebookLM](https://drive.google.com/file/d/1ErBf0-jmaA9Rf3C-eW3CQOCoEuxBMOps/view). A matriz tem **123 exemplos: 100 negativos de 100 contratos e 23 positivos de apenas 1 contrato, observados em 23 dias**. Cinco folds aleatórios por linhas compartilham sempre o contrato positivo entre treino/teste (1 contrato sobreposto em cada), portanto há **dependência contratual e validação EXCLUSIVAMENTE exploratória**, não generalização demonstrada. 4 algoritmos × 3 grupos de atributos × 5 folds produziram 60 avaliações reais e 12 resumos, com integridade SHA-256 de todos os cinco artefatos conferida. **F1 médio Random Forest = 0,9778** em todos os três grupos; árvores e boosting variaram de 0,8870 (A) a ~0,9156/0,9159 (B/C); Regressão Logística 0,8095 (A), 0,8170 (B), 0,5452 (C). 0,9778 não é estimativa de recall, precision, acurácia, taxa real de detecção na Ethereum ou generalização por protocolo. Não inferir causalidade da ablação. **Próxima prioridade: artigo SBC 4–6 páginas e revisão final para entrega 20/11, sem novos experimentos.**

## EXP-08 — Negativos difíceis, positivos independentes e protótipo defensivo (19/11/2026)

[Protocolo, auditoria dos limites e implementação](../experiments/EXP-08-plano-seguranca-e-conjuntos.md), [inventário de candidatos](../../data/exp08/candidatos_classes.csv), [implementação de triagem](../../scripts/security_triage/triage.py) e [testes](../../scripts/security_triage/test_triage.py). Diante do único contrato positivo do EXP-07, definimos três extensões científicas **sem afirmar novo resultado de classificação**: (1) seis famílias observadas no EXP-02A como **candidatos a negativos difíceis, todos indeterminados** (conjunto condicionado à seleção de alertas RF e, portanto, não holdout independente); (2) Privacy Pools v1 como **candidato independente sem rótulo**, RAILGUN como arquitetura diversa e Aztec Connect como contraste histórico, não positivos automaticamente aprovados; (3) protótipo didático offline de resposta de segurança baseado em **triagem humana, URLs de evidência, verificação de formato de hash/endereço e registros JSONL encadeados por SHA-256**. **Quatro testes unitários passaram**; duas entradas de demonstração geraram trilha verificável; adulteração de um campo é detectada. **Não há blockchain RPC, recebimento automático de logs, SIEM, bloqueio, auditoria de ABI histórica nem novos testes de RF nesse EXP-08**. SHA encadeado não é imutabilidade sem ancoragem externa. O projeto segue com prioridade de conclusão do artigo em 20/11/2026.
