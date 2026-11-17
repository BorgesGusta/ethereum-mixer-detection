# EXP-02A — Inventário de 2026 e triagem documental dos nove alertas

**Data do inventário:** 17/11/2026. **Data dos dados analisados:** 15/01/2026. **Status:** análise de artefatos **já executados**, com nova checagem documental pública; **não houve retreinamento, nova inferência, alteração do limiar nem reexecução do teste de 2026**.

## Proveniência da avaliação antiga

- [CSV original dos nove alertas](https://drive.google.com/file/d/11kWohs3VvdDGVjwsN_t-S8EQVix6n9mf/view), acompanhado de [resumo](https://drive.google.com/file/d/1Tk9h9f3ymfjLlkzRBSpsk3OR3FnyzoQP/view), [resultado por dia](https://drive.google.com/file/d/1WCeQSCmTZR-X04CG8JgJehudO5XJ6VnF/view), [limiar congelado](https://drive.google.com/file/d/1rVq1bPOvy1pxtQVmuXOFKecfGcFRPd_d/view) e [protocolo de teste único](https://drive.google.com/file/d/1XOqdl9WsDxjLLbVfyWgveFjjT7CVOmd4/view).
- [Notebook legado executado `07b_teste_2026_validacao_2020.ipynb`](../../notebooks/07b_teste_2026_validacao_2020.ipynb) descreve modelo `modelo_rf.joblib` de março/2025, sem retreino, `MIN_TX=10`, seleção do limiar pela validação de 29/10/2020 e teste de 15/01/2026, com marca de execução anterior.
- [Matriz da triagem e manifesto no Drive](https://drive.google.com/drive/folders/15Do7dwtJgd4T7pkmXDptDfMKWn2NHkIE). Os mesmos arquivos estão versionados nesta pasta do repositório.

Os resultados **originais** do teste já realizado em 2026 foram: **20.214** janelas elegíveis; limiar **0,85**, congelado antes da execução do teste, mas escolhido com base na validação de 2020 que já havia sido explorada; **9 endereços sinalizados**; **3/3 pools de referência Tornado Cash recuperados**; **6 outros sem rótulo binário independente**. A alternativa com limiar 0,50 tinha 15 alertas no mesmo dia, mas não é um resultado de novo teste.

O CSV antigo contém campos chamados `falsos_positivos` e `precisao` (6; 0,333). **Esses números contam como negativos todos os endereços fora dos três pools de referência**; dado que a referência é incompleta, **não devem ser apresentados como FPs ou precisão estimada com ground truth independente**. Também não se deve apresentar 2026 como teste novo/corroborativo realizado durante a presente auditoria.

## Resultado do novo cruzamento documental

| Endereço | Score 2026 | Nome/identificação pública | Status no nosso inventário |
|---|---:|---|---|
| `0x12d66f87…b8fc` | 1,00 | Tornado Cash 0,1 ETH | Pool positivo de referência |
| `0x47ce0c6e…2936` | 1,00 | Tornado Cash 1 ETH | Pool positivo de referência |
| `0x910cbd52…b39dbf` | 1,00 | Tornado Cash 10 ETH | Pool positivo de referência, **mesmo endereço usado no treino** |
| `0x7251febe…6dd2` | 1,00 | **OKX DEX: TransparentUpgradeableProxy**, segundo explorador Routescan (associação ao protocolo, estado histórico ainda não auditado) | Outro serviço identificado documentalmente; sem rótulo negativo independente |
| `0x5182fede…2370` | 0,99 | **ApeCoin OFT Adapter / LayerZero**, segundo Etherscan e funções `send`/endpoint | Outro serviço identificado documentalmente; sem rótulo negativo independente |
| `0x57bedd7e…24b7` | 0,98 | **SwappableBridgeUniswapV3**, segundo código verificado no Etherscan | Outro serviço identificado documentalmente; sem rótulo negativo independente |
| `0x80226fc0…f7d` | 0,98 | **Chainlink CCIP Router**, segundo transações rotuladas no Etherscan | Outro serviço identificado documentalmente; sem rótulo negativo independente |
| `0x2f848984…0479` | 0,91 | **MCT-XEN Batch Minter**, segundo Etherscan | Outro serviço identificado documentalmente; sem rótulo negativo independente |
| `0x27428dd2…4911` | 0,86 | **Wormhole Standard Relayer**, **endereço Ethereum listado na documentação do próprio Wormhole** | Outro serviço identificado documentalmente; sem rótulo negativo independente |

**Fontes externas detalhadas para auditoria:**

1. OKX DEX, registro do endereço no Routescan: https://ethereum.routescan.io/tx/0xed563d8e8f48852da5789a52b4c35ffff3cdeb10340e474ad375edae0123c0b0?chainid=1 ; endereço no Etherscan: https://etherscan.io/address/0x7251febeabb01ec9de53ece7a96f1c951f886dd2 .
2. ApeCoin OFT Adapter: https://etherscan.io/address/0x5182fede730b31a9cf7f49c5781214b4a99f2370 ; fonte da implementação OFTAdapter: https://github.com/LayerZero-Labs/LayerZero-v2/blob/main/packages/layerzero-v2/evm/oapp/contracts/oft/OFTAdapter.sol .
3. SwappableBridgeUniswapV3: https://etherscan.io/address/0x57bedd7eb4c3118669f4f33a3cae4d4b554f24b7 .
4. Chainlink CCIP Router: https://etherscan.io/tx/0x7a355470a742e8aaa9b331c60a4f636ba7ce71dd79f56b2bf3060cdcf0368bdf ; ver também https://cryptoskills.dev/skills/chainlink .
5. MCT-XEN Batch Minter: https://etherscan.io/address/0x2f848984984d6c3c036174ce627703edaf780479 .
6. Wormhole Standard Relayer — documentação oficial e endereço na rede Ethereum: https://github.com/wormhole-foundation/xdapp-book/blob/main/src/reference/contracts.md .

**Avanço em relação ao inventário legado:** três dos seis casos antes `indeterminado` passaram a ter uma **associação documental verificável** (OKX DEX, ApeCoin OFT Adapter e Chainlink CCIP Router). A identificação pública do protocolo não demonstra, por si só, que todas as **transações de 15/01/2026** pertencessem à atividade descrita, especialmente para um proxy atualizável. Nenhum desses seis foi convertido silenciosamente para classe negativa definitiva.

## Implicações metodológicas e para segurança de redes

- A presença de bridges, relayers, roteadores cross-chain, DEXs e operações em lote entre os alertas **sugere uma hipótese plausível de confusão estatística** quando se consideram apenas entropias e média de chamadas internas; **não é comprovação quantitativa de falsos positivos**.
- Os três pools Tornado de 2026 são do **mesmo protocolo**; o endereço do pool de 10 ETH aparece também no treino (23 janelas). Dessa forma, a avaliação em 2026 mostra recuperação temporal dos pools conhecidos, mas **não constitui holdout integral por contrato nem teste de novos protocolos de mixer**.
- O teste 2026 já era conhecido/inspecionado antes do presente inventário. **Não selecionar limiar, features, filtros ou novos hiperparâmetros usando esse resultado e depois reportar desempenho confirmatório nele.**
- Trata-se de melhoria comprovável de **auditabilidade e rastreabilidade**, e de um achado relevante para desenho de controles contra falsas classificações. Ainda não há prova de maior acurácia, recall, robustez adversarial ou segurança operacional.
- O tratamento de Router é outra escolha de protocolo potencialmente relevante. O notebook legado exclui o endereço de infraestrutura Router do ranking, mas associa operações ao pool Tornado. O confronto com 2020 requer harmonização da cobertura de chamadas antes de comparar valores absolutos.

## O que falta antes do experimento confirmatório

1. Auditar **hashes, calldata/funções e eventos executados em 15/01/2026** dos seis contratos adicionais; quando houver proxies, verificar a implementação válida na época e não apenas o nome atual.
2. Revisão de pelo menos dois avaliadores independentes para rótulos negativos; quando não houver evidência suficiente, manter **indeterminado** e excluir de métricas que exijam ground truth.
3. Obter positivos de **outros contratos/protocolos mixers** além de um único pool Tornado; fazer validação holdout por protocolo/contrato.
4. Se não houver ground truth adicional, apresentar apenas **recuperação 3/3 de referência** e resultados descritivos de um teste temporal já executado, mais a distribuição dos candidatos auditados; sem precision/recall gerais inventados.

A próxima coleta deve priorizar rótulos com função econômica verificável e um **período novo que não tenha orientado decisões de desenvolvimento**. Ver protocolo predefinido [EXP-02](EXP-02-protocolo-temporal-contrato.md).
