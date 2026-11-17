# Revisão bibliográfica anotada — Mixers, Ethereum e detecção em segurança

**Revisão inicial:** 17/11/2026. **Escopo:** identificação de serviços mixers em Ethereum, rastreamento de ativos, análise de privacidade, segurança de contratos e aprendizagem de máquina com rótulos limitados. **Importante:** uma parte dos textos está disponível somente como preprint (arXiv) no estado consultado; não tratar DOI placeholders em templates como publicações oficiais.

## 1. Qual problema científico cada trabalho realmente resolve?

A literatura contém **quatro tarefas distintas**, frequentemente confundidas:

1. **Identificação de contrato/serviço mixer:** dadas características e evidências de um endereço de contrato, decidir se funciona como mixer. É a tarefa mais próxima do artigo do SBSeg e da nossa reprodução.
2. **Identificação de carteiras suspeitas:** classificar uma conta por sua participação em fluxos de alto risco, phishing, fraude ou transações com mixers. Uma carteira que usou Tornado não é necessariamente o contrato mixer.
3. **Correlação depósito↔saque:** inferir relações entre contas ou eventos de depósito/retirada apesar da camada de privacidade. Não é classificação de mixer.
4. **Lavagem de dinheiro envolvendo mixer:** detectar operações ilícitas ou reconstruir casos e fluxos; exige evidência de atividade criminosa, não apenas identificação do serviço de privacidade.

**Regra de comparação:** não comparar métricas de F1/precision entre artigos de tarefas, rótulos, amostras, granularidades ou janelas temporais distintas como se estivessem no mesmo benchmark.

## 2. Cinco PDFs enviados pelo pesquisador — leitura orientada

| Trabalho | Unidade de análise | Técnica / contribuição | O que aproveitar | Limite para comparação |
|---|---|---|---|---|
| **Amanda Akopova — Detecting Ethereum Mixers** | Contrato mixer / atividade e função de contratos | Heurísticas `deposit(bytes32)`, retirada, verificação de provas e revisão de Solidity | **Muito próxima** da nossa questão: evidência funcional dos contratos e redução de alertas por contexto | Heurística do artigo não usa necessariamente o mesmo conjunto de treino/teste do RF; selector isolado não prova mixer |
| **Jeong & Yoon (BSCI 2025) — GNN-based Detection...** | Carteiras e subgrafos suspeitos relacionados a Tornado Cash | BFS + Account Relevance + GCN de três camadas | Baseline de grafos; diversidade de vizinhos; controles contra confundir DeFi com Tornado | Detecta comportamento suspeito de contas, não exatamente “endereço é contrato mixer”; scores não diretamente comparáveis |
| **Che et al. — StealthLink** (arXiv:2505.09892, 2025) | Pares de contas vinculadas / correlação de transações mixadas | Transferência de domínio, subgrafos e poucos rótulos | Método para lidar com **escassez de exemplos e shift de domínio**; reforça avaliação por grupos | Tarefa é associação entre endereços, não descoberta de contrato mixer; F1 não comparável diretamente |
| **Xing et al. — FPTracer** (arXiv:2610.32210, 2026) | Fluxos de ativos e transações de lavagem por múltiplos serviços | Context-Aware Transfer Tree, evidências de execução, bridges e pós-mixer | Fundamenta **limite das transferências superficiais** e valor de logs/traces/ABI | Sistema de rastreamento de ilícitos e fluxos; não baseline direto de RF contratual |
| **Fu et al. — MixGuard** (arXiv:2609.27807, 2026) | Transações de lavagem e agrupamento por incidente | Dataset MixLaunder com casos Tornado Cash/Railgun; múltiplas visões; holdout por caso | Evidência para **protocolo independente, mais de um mixer, validação por incidente** | Classe-alvo é lavagem, não existência de contrato mixer; resultados dependem de ground truth de casos |

**Leitura crítica de Akopova:** o artigo menciona 737 candidatos na heurística inicial, filtros por código e atividades de depósito/retirada, além de examinar contratos implantes de diferentes mixers. O trabalho ajuda a definir um **modelo de evidência de código** que complemente entropias. Números publicados nesse texto não devem ser reinterpretados como superioridade comprovada no dataset SBSeg 2025.

**Leitura crítica de FPTracer:** uma única transação em DeFi pode conter roteamento, swaps, transferências de tokens e chamadas aninhadas; inferir fluxo só de `from`/`to` pode induzir caminho incorreto. Isso dialoga com nosso problema de **Router** e com os alertas identificados como bridges/DEXs.

**Leitura crítica de MixGuard:** são reportadas 27 ocorrências de lavagem envolvendo Tornado Cash e Railgun, 9.300 transações associadas a casos e avaliação com separação por incidente. O achado relevante é **a necessidade de distinguir serviço de privacidade de uso criminoso**. O trabalho descreve uma tarefa mais específica e exige dados que nossa reprodução ainda não tem.

**Leitura crítica de StealthLink e GNN:** técnicas avançadas fazem sentido quando há dados e rótulos representativos; com 23 janelas positivas do mesmo contrato, a primeira prioridade do nosso estudo deve ser **qualidade da amostra e avaliação por protocolo**, não adicionar complexidade indiscriminadamente.

## 3. Trabalhos adicionais encontrados e fontes originais

### A. Taxonomia e prova de conceito funcional — prioridade muito alta

**Barbereau et al. (ICIS 2023), *Beyond a Fistful of Tumblers: Toward a Taxonomy of Ethereum-based Mixers*.** Estuda características e funções de contratos Ethereum mixers em camadas, incluindo arquitetura, denominação, depósito, retirada e taxas. Utilidade imediata: construir **rubrica de identificação funcional** e distinguir mixer de outras categorias. PDF: https://orbilu.uni.lu/bitstream/10993/57137/1/_ICIS__Toward_a_Taxonomy_of_Ethereum_based_Mixers__final_version_%20%281%29.pdf . Registro: https://orbilu.uni.lu/handle/10993/57137 .

### B. Heurísticas e privacidade — prioridade alta

**Wu et al. (2022), *Tutela: An Open-Source Tool for Assessing User-Privacy on Ethereum and Tornado Cash*.** Mostra que anonimato prometido pode ser reduzido por interações e hábitos; fornece perspectiva de **rastreabilidade e limites de heurísticas**. PDF: https://arxiv.org/pdf/2201.06811 ; registro: https://arxiv.org/abs/2201.06811 .

**On How Zero-Knowledge Proof Blockchain Mixers Improve, and Worsen User Privacy** (arXiv:2201.09035, 2022). Avalia empiricamente anonimato e padrões de uso de mixers. Útil para **privacidade legítima, avaliação dos riscos e limitações**. PDF: https://arxiv.org/pdf/2201.09035 ; registro: https://arxiv.org/abs/2201.09035 .

### C. Generalização entre cadeias e correlação — prioridade média

**Cristodaro, Kramer e Tessone (2025), *Clustering Deposit and Withdrawal Activity in Tornado Cash: A Cross-Chain Analysis*.** Utiliza heurísticas de relacionamento de depósito/retirada, incluindo tempo e outras redes EVM. Útil para discutir **limites de privacidade, temporalidade e transferência**, mas não para comparar F1 de contrato mixer. PDF: https://arxiv.org/pdf/2510.09433 ; registro: https://arxiv.org/abs/2510.09433 .

### D. Explicação interdisciplinar e enquadramento ético — prioridade média

**Federal Reserve Bank of St. Louis (2023), *Tornado Cash and Blockchain Privacy: A Primer for Economists and Policymakers*.** Explica trade-off entre anonimato, privacidade de usuários e supervisão financeira. Útil para **motivação sem demonizar usuários legítimos**. PDF: https://files.stlouisfed.org/files/htdocs/publications/review/2023/02/03/tornado-cash-and-blockchain-privacy-a-primer-for-economists-and-policymakers.pdf .

## 4. Mapa da lacuna que nosso projeto pode estudar

**Observação já demonstrada:** o RF com quatro features produz alertas em endereços que outros exploradores associam a bridges, relayers, DEXs, adapters e batch minters. Em 2026, os seis adicionais não têm rótulos negativos independentes. O mesmo contrato Tornado usado como positivo aparece no treino e no teste temporal legado.

**Hipótese de pesquisa:** a incorporação de **evidências funcionais e contexto de execução** poderá reduzir confusão entre contratos mixers e serviços não mixers de atividade semelhante em relação ao RF com quatro features, **mantendo a recuperação de mixers positivos em contratos e períodos novos**.

**Ablação mínima proposta:** RF baseline; RF + diversidade de contrapartes (se a fonte permitir); RF + características funcionais provenientes de eventos/ABI; auditoria por regras interpretáveis (sem retreinar); comparar somente após obter ground truth novo, negativo difícil e positivo de outro protocolo.

**Diferencial potencial, não realizado:** (i) exploração de confusão entre categorias DeFi e mixer com evidência histórica; (ii) metodologia de classificação explicável com cobertura de trace/ABI; (iii) protocolo rigoroso de holdout temporal e contratual; (iv) benchmark de RF vs heurística vs extensão contextual; (v) reprodutibilidade integral com manifestos e checagem cruzada de fontes.

## 5. Leituras por prioridade para elaborar o artigo

1. **Akopova + Barbereau:** evidências funcionais e definição de mixer.
2. **FPTracer + MixGuard:** contexto de execução, rotulagem robusta e separação do problema “lavagem” do problema “tipo de contrato”.
3. **GNN BSCI 2025:** features de grafo e baselines, com crítica da compatibilidade.
4. **Tutela + ZKP mixers:** privacidade, heurísticas, limites éticos.
5. **StealthLink:** estratégias futuras para poucos rótulos, não necessariamente baseline simples.
6. **Cristodaro et al. + Fed St. Louis:** temporalidade, cross-chain e discussão mais ampla.

## 6. Próximos passos de revisão científica

- Conferir *versão editorial e DOI definitivo* de cada pré-publicação antes de submetermos o manuscrito; arXiv não equivale a aceite em congresso.
- Tentar localizar datasets públicos e código-fonte. Não afirmar disponibilidade de dados só porque o resumo diz que “serão liberados”.
- Transcrever uma tabela técnica por artigo: **tarefa / unidade / dataset / split / rótulos / features / algoritmo / métricas / código / ameaça à validade**.
- Congelar uma hipótese e baseline antes de usar qualquer dia adicional como teste. Não transformar 2026 já analisado em holdout independente.

**Nota sobre anexo alheio ao tema:** o arquivo `10.1039-c3lc51171e_figure.pptx` trata de **mixer microfluídico de laboratório**, não de mixer de criptomoedas. Ele foi intencionalmente excluído da biblioteca temática para não contaminar o estudo.
