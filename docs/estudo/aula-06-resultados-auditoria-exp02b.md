# Aula 06 - Interpretando o EXP-02B: auditoria funcional de contratos Ethereum

**Data da análise:** 17/11/2026. **Dia de transações auditado:** 15/01/2026. **Referência:** [Relatório EXP-02B](https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02B-resultados-auditoria-amostral-2026.md). **Dados:** [Pasta de evidências no Drive](https://drive.google.com/drive/folders/1rV5mJ0rkINLML5aFUFnl0s7g1ybwrwOb).

## Objetivos de aprendizagem

Distinguir entre (1) contagem de transações no nosso dataset, (2) correspondência hash-a-hash com uma fonte externa, (3) interpretação de funções e eventos, (4) cobertura de logs, (5) identificação da implementação histórica e (6) atribuição independente de rótulos. Aprender a transformar um alerta estatístico em uma hipótese auditável sem chamá-lo automaticamente de falso positivo.

## 1. O que foi efetivamente medido

O classificador havia sinalizado nove endereços em 15/01/2026 com limiar 0,85. Três são pools Tornado Cash de referência. O EXP-02B analisou os seis outros contratos. As 315 transações **diretas** para os seis endereços no dataset intermediário coincidiram em quantidade com o ranking legado. Selecionamos a primeira, uma intermediária e a última transação de cada contrato: 18 no total. Todas as 18 foram encontradas no Blockscout com **hash, remetente, destinatário e dia iguais** aos do dataset.

| Serviço identificado documentalmente | Transações diretas no dia | Funções na amostra (3 tx) | Logs: páginas completas |
|---|---:|---|---:|
| OKX DEX / proxy | 83 | `0xec5b999d` (não decodificado; 1 revertida) | 3/3 |
| ApeCoin OFT Adapter | 16 | `send` | 3/3 |
| SwappableBridgeUniswapV3 | 66 | `swapAndBridge` | 3/3 |
| Chainlink CCIP Router | 119 | `ccipSend` (1 revertida) | 3/3 |
| MCT-XEN Batch Minter | 15 | `batchClaimRank` e `0x98190f47` | **0/3** |
| Wormhole Relayer / proxy | 16 | `deliver` | 3/3 |

Foram coletadas **270 linhas de evento**, mas não são necessariamente todas: três consultas ao MCT-XEN retornaram **50 logs na primeira página** e indicaram `next_page_params`. É incorreto declarar a cobertura completa enquanto houver páginas pendentes.

## 2. Por que essa distinção importa?

**315 transações no dataset** significa que o intermediário contém essa quantidade de chamadas externas endereçadas aos seis contratos. Não prova que inclui todas as chamadas internas ou as movimentações indiretas via Router.

**18/18 hashes confirmados** significa correspondência transacional para uma amostra **determinística, não aleatória**. Não significa 315/315 hashes verificados externamente, nem que cada contrato é de fato um mixer ou não mixer.

**15/18 páginas de logs completas** significa que não houve continuação indicada nessas consultas. As três restantes, todas MCT-XEN, exigem novas páginas. Uma transação revertida pode não produzir os eventos esperados; a ausência de logs não é prova de ausência da função tentada.

**`method_decoded`** é uma interpretação do explorador a partir de ABI/selector. Uma chamada como `ccipSend` ou `swapAndBridge` sustenta que a amostra executou ou tentou executar a função indicada, mas NÃO confirma sozinha a finalidade de todas as transações do contrato.

**Proxy upgradeable** exige conferir código/implementação **no bloco de interesse**, não apenas a implementação identificada em novembro/2026. A API sinalizou proxy EIP-1967 para OKX, MCT-XEN e Wormhole, mas nenhuma implementação histórica foi verificada nesta execução.

## 3. Hipótese científica e desenho de avaliação

**Hipótese atual:** quatro características puramente estatísticas (entropia dos valores, entropia de tarifas, entropia de transferências internas e média de chamadas) podem confundir comportamento de mixers com outros serviços inteligentes complexos, incluindo bridges, DEXs, roteadores, relayers e processamento em lote.

**Evidência inicial:** vários dos seis alertas mostram métodos de interoperabilidade ou lote em transações amostradas. **Não demonstrado:** melhoria de precisão, taxa geral de falsos positivos ou generalização a novos mixers. Antes de treinar modelo contextual: (a) completar paginação e verificar proxies; (b) criar rótulos com evidência e dupla revisão; (c) incluir controles não alertados; (d) obter contratos mixers de outro protocolo; (e) congelar avaliação por contrato e período para evitar vazamento.

## 4. Exercícios práticos

1. Um contrato recebeu 119 transações e você verificou 3 hashes no Blockscout. Que porcentagem desse conjunto teve identidade verificada externamente? Qual afirmação você NÃO pode fazer?
2. Três consultas de logs retornaram 50 entradas cada e campo `next_page_params`. O que é possível afirmar sobre os 150 eventos vistos? Qual passo falta?
3. A API informa `TransparentUpgradeableProxy` hoje. Podemos afirmar que essa era a implementação ativa em 15/01/2026? Qual seria a evidência necessária?
4. O modelo sinaliza o Chainlink Router com score alto; a amostra tem `ccipSend`. Isso prova um falso positivo? Como registrar a conclusão provisória?
5. Por que precisamos analisar também contratos que o modelo NÃO sinalizou antes de publicar recall ou F1 no universo de 2026?

## Gabarito comentado

1. **3/119, aproximadamente 2,52%**. Não declarar os 119 hashes verificados externamente, nem cobertura das chamadas internas.
2. **Foram capturados 150 logs da primeira página** das três transações. Falta seguir a paginação; o total pode ser maior.
3. **Não**. É preciso código/slot de implementação de blocos históricos ou sequência completa de upgrades até o bloco da transação.
4. **Não**. Há evidência funcional compatível com serviço de roteamento cross-chain, mas a rotulagem negativa exige auditoria da atividade histórica e evidência independente. Classe atual: **indeterminado**.
5. Porque verificar apenas os alertas produz **viés de verificação**. Sem conhecer as classes dos não alertados, falsos negativos e recall permanecem desconhecidos; F1 também depende de recall.

## Sugestão de estudo no NotebookLM

Adicione esta aula, o PDF `EXP-02B`, os artigos *Detecting Ethereum Mixers*, *FPTracer* e *MixGuard*. Peça: **"Crie um estudo guiado sobre como converter sinais estatísticos em evidências funcionais de smart contracts. Diferencie fonte interna, validação externa, rótulo e generalização. Faça oito questões graduais com explicação das respostas usando apenas estes documentos."**
