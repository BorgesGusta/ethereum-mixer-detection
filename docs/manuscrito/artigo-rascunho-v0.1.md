# Rascunho científico v0.1 — Auditoria reprodutível e limites da detecção estatística de mixers na Ethereum

**Data:** 17/11/2026. **Estado:** manuscrito de trabalho, **não submetido**, com resultados já executados e análises futuras claramente separadas. **Autores, instituição, afiliação, e-mail e evento:** preencher com pesquisadores responsáveis. **Formato final:** a definir após escolha da chamada oficial e de seu template (p.ex., SBC/SBSeg ou outra trilha). **Texto sujeito à revisão por orientador(a) e coautores.**

**Título de menor risco científico (atual):** *Auditoria Reprodutível da Detecção de Mixers na Ethereum: Sensibilidade Metodológica e Evidências Funcionais de Contratos Sinalizados*.

**Título alternativo, SOMENTE se o futuro experimento demonstrar ganho:** *Além da Entropia: Evidências Funcionais para Distinguir Mixers de Outros Serviços Ethereum*.

## Resumo — versão baseada somente em resultados observados

A identificação de contratos inteligentes que implementam serviços de mistura de ativos na Ethereum é relevante para análise forense de blockchain, mas padrões transacionais semelhantes também podem ocorrer em aplicações descentralizadas legítimas. Este estudo investiga a reprodutibilidade e os limites de um classificador Random Forest para detecção de possíveis mixers, proposto em trabalho anterior, utilizando quatro características transacionais. A reprodução aplicada a 1.114.702 transações de 29 de outubro de 2020 recuperou os três contratos Tornado Cash de referência, mas identificou nove endereços acima do limiar de 0,50, frente aos 63 reportados pelo estudo-base. Uma análise controlada demonstrou que, mantendo o mesmo modelo e limiar, a variação do filtro de elegibilidade de uma a vinte transações alterou o número de alertas de 49 para sete. A investigação de um teste temporal legado, referente a 15 de janeiro de 2026, reuniu evidências documentais e funcionais em contratos associados a bridges, roteadores cross-chain e operações em lote. Em auditoria externa amostral, 18 de 18 transações apresentaram correspondência de hash, remetente, destinatário e data; posteriormente, completou-se a paginação dos eventos dessas 18 amostras. Os resultados demonstram sensibilidade à definição da população analisada e a importância de evidências funcionais e controles de cobertura para interpretar alertas. A divergência em relação ao artigo-base permanece sem causa comprovada, e a insuficiência de rótulos negativos independentes impede estimar precisão e generalização para protocolos mixers inéditos.

**Palavras-chave provisórias:** Ethereum; mixer; análise forense de blockchain; aprendizado de máquina; reprodutibilidade; contratos inteligentes; auditoria.

## Abstract (provisório, traduzir e revisar depois do fechamento)

[Traduzir o resumo revisado, preservando exatamente escopo, limitações, contagens e caráter amostral das evidências. Não traduzir como improved detection accuracy sem ensaio comparativo.]

## 1. Introdução

Blockchains públicas possibilitam auditoria das transações e, simultaneamente, criam tensões entre transparência, privacidade legítima e análise forense de serviços usados para dificultar o rastreamento de ativos. Na Ethereum, mecanismos de privacidade podem recorrer a contratos inteligentes, compromissos criptográficos e provas de conhecimento zero para dissociar depósito e retirada de fundos. Entretanto, nem toda atividade transacional complexa — como uso de bridges, DEXs, roteadores ou processamento em lote — corresponde a um serviço de mistura. Consequentemente, identificar um possível mixer com base exclusivamente em estatísticas de movimentação representa uma tarefa de classificação sujeita a ambiguidades semânticas.

Leale e Sendin (SBSeg 2025) propuseram um classificador Random Forest com quatro características derivadas de transações para identificar possíveis contratos mixers. Seu teste principal, em 29/10/2020, reportou 63 endereços sinalizados, incluindo os três contratos Tornado Cash associados às denominações de 0,1, 1 e 10 ETH. O próprio estudo discute confusão com aplicações como mercados, pools de liquidez e jogos. Nosso estudo parte dessa proposta para responder a duas necessidades metodológicas: (i) distinguir recuperação de contratos de referência de equivalência experimental estrita; e (ii) qualificar alertas mediante evidências de função, execução e cobertura temporal.

As seguintes questões orientam a investigação:

- **RQ1 — Sensibilidade:** qual o efeito de regras explícitas de elegibilidade e escolhas do treinamento sobre quantidade e composição dos alertas?
- **RQ2 — Evidência funcional:** o que é possível afirmar sobre as funções efetivamente observadas nos contratos sinalizados em um dia específico, sem inferir rótulos binários a partir de nomes de serviços?
- **RQ3 — Generalização contextual (ainda não testada):** atributos de funções/eventos/contrapartes podem reduzir confusão entre mixers e serviços não mixers, preservando recuperação de mixers em protocolos e contratos ausentes do treino?

**Contribuições já demonstradas:** (a) reprodução parcial e auditoria do pipeline com rastreabilidade; (b) quantificação da sensibilidade do classificador ao filtro `n_tx`; (c) comparação externa de hashes de transações de duas datas; (d) triagem funcional e declaração explícita de lacunas de observabilidade (paginação, proxy histórico e cobertura de dados).

**Contribuição ainda hipotética:** melhoria de desempenho preditivo por engenharia de características contextuais. Não reportá-la como contribuição concluída.

## 2. Fundamentação e trabalhos relacionados

### 2.1. Mixer não é sinônimo de atividade ilícita

Um mixer é caracterizado pela **função de privacidade** que oferece, e não pela presunção de que toda utilização seja criminosa. Na arquitetura de referência Tornado Cash, compromissos e provas criptográficas sustentam processos de depósito e retirada. O objetivo deste artigo é identificar e qualificar serviços do tipo mixer, **não** determinar a legalidade de uma transação individual.

### 2.2. Evidências estatísticas e funcionais

As quatro características transacionais de referência são `value_entropy`, `fee_entropy`, `internal_value_entropy` e `call_count_mean`. São resumos de dispersão dos valores e de atividade de chamadas. Um vetor semelhante de características pode corresponder a serviços com finalidades distintas. Além dessas estatísticas, logs, seletores de funções, ABIs verificadas, implementações de proxies e cobertura histórica constituem indícios sobre o que foi executado em um bloco. Por sua vez, uma assinatura identificada na ABI **atual** não comprova a função histórica em um contrato atualizável.

### 2.3. Delimitação de tarefas na literatura

Diferenciam-se quatro tarefas que **não** podem ser comparadas por F1 como se fossem o mesmo benchmark: classificação de **contratos mixers**; classificação de **carteiras** que interagem com mixers; **correlação** de depósitos/retiradas; e investigação de **lavagem de dinheiro** entre serviços.

A discussão de evidências de código/funcionamento pode se apoiar em Akopova (*Detecting Ethereum Mixers*) e Barbereau et al. (*Beyond a Fistful of Tumblers*). FPTracer fornece contexto sobre a complexidade de fluxos envolvendo DeFi e bridges; MixGuard aborda análise de lavagem por incidente; StealthLink estuda correlação entre contas e aprendizado com poucos rótulos; trabalhos GNN investigam padrões em grafos. **Esses estudos fundamentam escolhas de auditoria, mas não constituem baselines diretamente comparáveis ao nosso classificador de contratos.** Conferir autoria/ano/DOI/versão final antes da submissão. Ver [revisão bibliográfica versionada](../literatura/revisao-bibliografica-2026.md).

## 3. Materiais e métodos

### 3.1. Repositório, unidade experimental e dados

O repositório do estudo mantém código de extração de características, notebooks, relatórios e manifestos de integridade, com origem dos dados e SHA-256. A unidade operacional usada pela reprodução é a janela de transações recebidas por um endereço ao longo de um dia UTC.

O conjunto de treino da reprodução contém **123 janelas:** 23 positivas associadas a **um mesmo pool Tornado Cash 10 ETH** em 23 dias de março/2025, e 100 negativas associadas a 100 endereços em um dia de março/2025. Essa seleção não demonstrou identidade com a amostra exata dos autores do artigo-base. A divisão estratificada por linha pode agrupar observações do mesmo contrato positivo entre treino e validação e, portanto, não demonstra generalização para contratos inéditos.

O teste de 29/10/2020 contém 1.114.702 transações e **230.658 endereços destinatários**. Após o critério `n_tx>=10`, a implementação avalia 4.038 endereços. A avaliação de **15/01/2026** foi executada previamente, com 20.214 janelas elegíveis e limiar 0,85 estabelecido a partir da validação em 2020. Esse teste **não deve ser reclassificado como teste futuro virgem** nem usado novamente para selecionar atributos/limiares como se permanecesse independente.

### 3.2. Classificador de referência

O classificador utiliza Random Forest com 100 árvores, profundidade máxima de cinco níveis, balanceamento por reamostragem, pesos automáticos e limiar `p>0,50` na reprodução do protocolo 2020. As quatro features são extraídas de valores, taxas, valores internos e contagem de chamadas. O código de reprodução documenta discretizações por arredondamento não especificadas com a mesma granularidade no artigo-base. As pontuações do Random Forest não são probabilidades calibradas de atividade ilícita.

### 3.3. Análise controlada de sensibilidade

A partir do mesmo modelo e de limiar 0,50 fixo, modificou-se apenas `min_tx` na população de teste em 2020 (1, 5, 10 e 20). Outros cenários controlados variaram reamostragem/pesos e sementes aleatórias mantendo `min_tx>=10`. Não houve otimização para alcançar retrospectivamente os 63 endereços do artigo-base.

### 3.4. Auditoria cruzada de fontes e funções

Na auditoria de 2020, os hashes de 20 transações referentes a SmartEther e DSProxy foram comparados diretamente entre o dump Blockchair e o Blockscout, verificando emissor, destinatário e bloco.

Na avaliação legada de janeiro/2026, seis endereços fora dos três pools de referência foram associados documentalmente a outras categorias de serviços. O EXP-02B selecionou, de forma determinística, primeira, central e última transação de cada contrato para consulta à API do Blockscout. Verificaram-se hash, remetente, destinatário, data, seletor e logs. O EXP-02C completou a paginação de três transações de MCT-XEN inicialmente truncadas, preservando todas as páginas. Nenhum rótulo binário foi automaticamente modificado.

### 3.5. Protocolo previsto para validação do classificador contextual

**Ainda não executado.** Para avaliar eventual melhoria, o estudo exigirá positivos de mais de um protocolo mixer, negativos de serviços distintos com função histórica verificada, amostragem de não alertas, separação temporal e por contrato/protocolo, e revisão independente de rótulos. O comparativo deverá conter baseline RF original, abordagem contextual de baixa complexidade e ablações. Somente conjuntos rotulados independentemente poderão produzir precision, recall, F1 e PR-AUC representativos.

## 4. Resultados experimentais

### 4.1. Reprodução parcial em 29/10/2020

| Métrica | Artigo-base | Reprodução |
|---|---:|---:|
| Transações do dia | 1.114.702 | 1.114.702 |
| Endereços do universo reportado / destinatários na reprodução | 230.658 | 230.658 |
| Transações destinadas aos 3 pools Tornado Cash | 239 | 239 |
| Pools de referência detectados | 3 | 3 |
| Endereços sinalizados | **63** | **9** |
| Endereços elegíveis após `n_tx>=10` | Não explicitado para teste | 4.038 |

O artigo-base publicou 63 endereços suspeitos, dos quais três são os pools de referência. A nossa implementação recuperou os mesmos três pools, mas não a mesma quantidade total de alertas. A divergência **não está explicada causalmente**. Diferenças plausíveis incluem amostras negativas e positivas não idênticas, unidade de agregação, discretização e políticas de Router/eligibilidade. **Não** é correto declarar que o estudo-base estava errado ou que houve 60 falsos positivos verificados.

### 4.2. Filtro de elegibilidade e políticas de treinamento

| `min_tx` | Candidatos efetivamente avaliados | Alertas acima de 0,50 | Pools de referência |
|---:|---:|---:|---:|
| 1 | 230.658 | 49 | 3/3 |
| 5 | 7.865 | 14 | 3/3 |
| 10 | 4.038 | 9 | 3/3 |
| 20 | 2.464 | 7 | 3/3 |

O filtro aplicado à nossa população excluiu **40 dos 49 alertas** identificados ao avaliar destinatários com ao menos uma transação. Mudanças de sementes ou de políticas de balanceamento mantiveram os mesmos nove endereços elegíveis, exceto a variante apenas com pesos balanceados (dez). Esses achados evidenciam sensibilidade a uma decisão de pré-processamento, mas **não provam que o filtro seja a causa do resultado 63 do artigo**. Fonte: [EXP-01J](../experiments/EXP-01J-resultados-sensibilidade-63x9.md).

### 4.3. Auditoria externa de transações em 2020

Vinte transações referentes a dois contratos examinados tiveram correspondência **20/20** de hash, remetente, destinatário e bloco entre Blockchair e Blockscout. Já a investigação de um terceiro contrato proxy permaneceu sem cobertura histórica completa, inclusive por respostas inválidas ou acesso recusado a provedores de estado de arquivo. A comparação confirma **essas 20 identidades**, não valida as quatro características com fonte independente para toda a população. Fonte: [EXP-01G](../experiments/EXP-01G-auditoria-hashes-blockchair-blockscout.md) e [EXP-01H](../experiments/EXP-01H-estado-proxy-historico-inconclusivo.md).

### 4.4. Avaliação temporal legada e auditoria funcional em 2026

Na avaliação pré-existente de 15/01/2026, houve nove endereços sinalizados em 20.214 janelas elegíveis, incluindo os três pools Tornado Cash de referência, a limiar 0,85. Os outros seis foram associados documentalmente a OKX DEX, ApeCoin OFT Adapter, SwappableBridgeUniswapV3, Chainlink CCIP Router, MCT-XEN Batch Minter e Wormhole Relayer.

| Associação documental | Transações diretas no intermediário | Método observado na amostra |
|---|---:|---|
| OKX DEX / proxy | 83 | seletor `0xec5b999d`, não identificado |
| ApeCoin OFT Adapter | 16 | `send` |
| SwappableBridgeUniswapV3 | 66 | `swapAndBridge` |
| Chainlink CCIP Router | 119 | `ccipSend` |
| MCT-XEN Batch Minter | 15 | `batchClaimRank`; também seletor `0x98190f47` não identificado |
| Wormhole Relayer | 16 | `deliver` |
| **Total** | **315** | **18 transações auditadas externamente (3 por contrato)** |

As contagens diretas do intermediário coincidiram com o ranking legado. As **18/18** amostras tiveram hash, remetente, destinatário e data compatíveis entre o intermediário e o Blockscout. A primeira coleta obtivera 15/18 páginas de logs completas; no EXP-02C, as três transações MCT-XEN foram paginadas até `next_page_params=null`, recuperando **83, 83 e 300 logs** (466 nos três hashes). Com os 120 logs das demais amostras já completos, há **586 eventos recuperados** nas 18 transações amostradas. A ABI atual e a consulta à base 4byte não produziram identificação confirmada dos dois seletores pendentes. As implementações históricas de três proxies permanecem sem validação.

**Não resulta desses achados** que todos os seis endereços sejam negativos, que o modelo tenha precisão de 33,3% ou que os 315 hashes tenham sido verificados individualmente fora da fonte local. Fontes: [EXP-02B](../experiments/EXP-02B-resultados-auditoria-amostral-2026.md) e [EXP-02C](../experiments/EXP-02C-resultados-logs-e-seletores.md).

## 5. Discussão

Os resultados mostram que, dentro da reprodução, decisões sobre quem é elegível para avaliação afetam fortemente o número de alertas, mesmo com classificador e limiar constantes. Também demonstram o valor operacional de uma auditoria que distinga verificação da identidade da transação, completude dos logs, identificação de função e validação do rótulo do contrato. As amostras funcionais de 2026 sustentam a hipótese de que padrões estatísticos de contratos de interoperabilidade e operações em lote podem ser confundidos com padrões de mixers. No entanto, **a presença de funções como `ccipSend` não prova a ausência de outras funções, nem a natureza de todas as atividades do endereço**.

Essa diferenciação é relevante para segurança de redes e análise forense: um alerta de modelo é um mecanismo de priorização e investigação, **não uma acusação**. Um classificador empregável exigiria desempenho aferido em conjunto não enviesado, limitações explícitas de cobertura, tratamento de proxies e possibilidade de revisão humana.

## 6. Ameaças à validade

1. **Validade de construto e ground truth:** classes negativas não verificadas independentemente para seis alertas de 2026; outros mixers/protocolos positivos ausentes do treino.
2. **Viés de seleção:** a auditoria amostrou **endereços já alertados**, e não amostra representativa da população de 20.214.
3. **Vazamento entre grupos:** treino possui 23 janelas positivas de um único contrato; CV por linha não mede holdout por contrato.
4. **Validade temporal:** o modelo treinou com março/2025, aplicou-se retrospectivamente a 2020 e foi usado no dia de 2026, com limiar selecionado a partir de 2020 já explorado. A avaliação 2026 não pode ser recuperada como teste novo após ajustes.
5. **Cobertura e versões:** transações diretas do intermediário não representam necessariamente traces internos completos, e ABIs atuais não provam implementação vigente no bloco histórico.
6. **Reprodutibilidade do estudo-base:** não há confirmação de igualdade do treino, regras completas de seleção e lista integral dos 63 alertas. A solicitação de esclarecimentos aos autores foi enviada em 17/11/2026. **Somente declarar falta de resposta se ainda for verdadeiro no fechamento do artigo.**
7. **Tamanho e alcance:** 18 transações amostradas não equivalem a 315 conferidas na API. A auditoria não mede robustez adversarial ou segurança criptográfica do detector.

## 7. Conclusão — provisória

A reprodução recuperou os três contratos de referência do estudo-base, mas a contagem total de alertas diferiu. Evidenciou-se que a regra de elegibilidade modifica fortemente a quantidade de endereços sinalizados e que a integração de evidências funcionais e controles de cobertura fornece uma interpretação mais cuidadosa dos contratos selecionados. O conjunto de resultados favorece procedimentos auditáveis de qualificação de alertas em análise forense de blockchain; **não** sustenta, até aqui, superioridade de detecção ou generalização a protocolos mixers inéditos. Como trabalho futuro e pré-requisito de eventual modelo contextual, propõe-se construir rótulos externos independentes, revisar implementações históricas e comparar classificadores sob divisões temporais e contratuais sem vazamento.

## Referências e transparência

- **Leale, P.; Sendin, I. S.** *Uma Proposta de Algoritmo para a Detecção de Mixers na Ethereum*. SBSeg 2025, WTICG. [PDF arquivado no Drive](https://drive.google.com/file/d/1FflHcOmD3lsO6HeGOp4D85RQbQz7c4EG/view).
- **Breiman, L.** (2001). *Random Forests*. Machine Learning 45:5–32. [Referência presente no estudo-base].
- **Akopova, A.** *Detecting Ethereum Mixers* — conferir metadados editoriais na versão anexa.
- **Barbereau et al.** (2023). *Beyond a Fistful of Tumblers: Toward a Taxonomy of Ethereum-based Mixers*. [Registro e PDF na revisão bibliográfica].
- **FPTracer**, **MixGuard**, **StealthLink** e **GNN/Tornado Cash** — **inserir referências bibliográficas completas e conferidas**, sem inventar DOI/anais antes da submissão. Consulte [revisão bibliográfica](../literatura/revisao-bibliografica-2026.md).
- **Dados, parâmetros, scripts e evidências:** [repositório](https://github.com/BorgesGusta/ethereum-mixer-detection), [checklist](../CHECKLIST_VIVO.md), [EXP-01J](../experiments/EXP-01J-resultados-sensibilidade-63x9.md), [EXP-02B](../experiments/EXP-02B-resultados-auditoria-amostral-2026.md) e [EXP-02C](../experiments/EXP-02C-resultados-logs-e-seletores.md).

## Campos em aberto antes da submissão

- [ ] Adicionar autores, afiliações, orientador, autorização dos coautores.
- [ ] Revisão de literatura com metadados/DOIs e discussão crítica suficiente.
- [ ] Escolher **trilha e template da chamada real**; adequar resumo e extensão.
- [ ] Congelar protocolo de rótulos e executar avaliação confirmatória **ou** explicitar escopo de artigo de reprodução/auditoria.
- [ ] Auditar seletores/proxies históricos e descrever o que permaneceu inconclusivo.
- [ ] Gerar figuras finais a partir de CSVs versionados com títulos/legendas, não só prints de notebook.
- [ ] Revisão técnica externa, revisão de linguagem e normas de anonimização da chamada.
- [ ] Aprovar versão final e preparar slides, artefatos reprodutíveis e ensaio oral.
