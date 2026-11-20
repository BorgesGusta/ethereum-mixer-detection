# EXP-05 — Parecer técnico de adjudicação preliminar das quatro divergências

**Data:** 20/11/2026. **Estado:** parecer técnico com evidências adicionais, **não adjudicação humana final**.

## 1. Escopo e independência

Casos: R001, R002, R004 e R005. Em todos, a ficha A, redigida com apoio de IA e ainda não assinada caso a caso, usou `indeterminado`; a ficha B, produzida pelo Bruno, usou `negativo_confirmado`. As fichas A e B originais foram preservadas e houve comparação previamente autorizada. Como o conteúdo de B já foi aberto, qualquer decisão posterior deve ser nomeada **adjudicação pós-confronto**.

A classe operacional predefinida é *mixer de pool com desvinculação entre depósito e saque*. Funções de ponte/roteamento/mensageria observadas fornecem indícios de **não mixer**, mas não provam por si sós a implementação histórica completa nem ausência de comportamento misturador. O protocolo exige evidência referente à função, endereço e bloco/época para um `negativo_confirmado`. Sob esse critério estrito, conservamos o rótulo formal **`indeterminado` nos quatro casos até aprovação de evidência adicional**; isso não equivale a dizer que sejam mixers.

## 2. Evidências independentes do modelo

Foram reabertos os artefatos já gerados no EXP-02B:
- `amostras_tx_api.csv`: [fonte Drive](https://drive.google.com/file/d/17S6xCYOng7Fk21cYZGq5k1yKzNn3kqGq/view); **SHA-256 `83f42e349d25cbbcded99784ba9eb4c148b64c9d91eb3190aab00a76c5f3ea8d`**.
- `eventos_amostras.csv`: [fonte Drive](https://drive.google.com/file/d/1NwJFLTrrMtpLndn2vMV7fLzy9oQJMlH6/view); **SHA-256 `b4442151e64a86722aed72caf15a785f6da800fc139d8befa8e50a41bd143571`**.
- [Manifesto EXP-02B](https://drive.google.com/file/d/1uM3FQlaJQXXMKuTuACO6BI2oLU1_qVE7/view) descreve API Blockscout e máximo de 3 amostras por contrato. Os dados foram obtidos anteriormente e estão preservados. **Não houve nova coleta RPC, novo treinamento, seleção de score ou ampliação de amostra**.
- Fonte externa de documentação funcional: [LayerZero OFTAdapter (repositório oficial)](https://github.com/LayerZero-Labs/LayerZero-v2/blob/main/packages/layerzero-v2/evm/oapp/contracts/oft/OFTAdapter.sol), [Wormhole — endereços oficiais](https://github.com/wormhole-foundation/xdapp-book/blob/main/src/reference/contracts.md), [Chainlink CCIP CLI — exemplo com endereço do Router](https://github.com/smartcontractkit/ccip-tools-ts/blob/main/ccip-cli/README.md), e [ABI SwappableBridge apresentada no Etherscan](https://etherscan.io/address/0x57bedd7eb4c3118669f4f33a3cae4d4b554f24b7#code). Esses documentos ajudam a identificar a arquitetura, mas **não substituem a prova do bytecode ativo no bloco**.

## 3. Resultado por divergência

| Caso | Método nos 3 exemplos | Sucessos/reversões | Logs amostrados | Interpretação funcional | Rótulo formal conservador |
|---|---|---:|---:|---|---|
| R001 — ApeCoin OFT Adapter | `send` | 3/0 | 36 | OFT entre redes | `indeterminado` |
| R002 — SwappableBridgeUniswapV3 | `swapAndBridge` | 3/0 | 30 | troca e ponte entre redes | `indeterminado` |
| R004 — Wormhole Standard Relayer | `deliver` | 3/0 | 15 | entrega de mensagens entre redes | `indeterminado` |
| R005 — Chainlink CCIP Router | `ccipSend` | 2/1 | 18 | roteamento de mensagens/tokens entre redes | `indeterminado` |


Os 12 registros amostrados são transações do dia **15/01/2026**, consultadas por API, com `recipient` e data correspondentes e páginas de logs capturadas conforme manifesto. A auditoria cobre **3 transações por caso**, não o universo diário nem a implementação histórica completa.

### R001 — ApeCoin OFT Adapter

A amostra contém três chamadas `send` bem-sucedidas, nos blocos **24236482**, **24241006** e **24243057**, 12 logs por amostra. O endereço é identificado como adaptador OFT, coerente com a arquitetura LayerZero. A ficha B registrou ABI de `send/quoteSend` e 15 chamadas no dia; essa afirmação é **evidência relatada por B** e não foi revalidada por leitura integral do dia nesta etapa. Os eventos denominados `Deposit` que apareçam em logs podem vir de **outros contratos emissores** (por exemplo, staking); o nome isolado de um evento não comprova atividade de mixer no endereço analisado.

**Parecer:** evidências favorecem função de interoperabilidade, não pool de mixing. A verificação histórica do código ainda é pendente. [Transação amostrada](https://eth.blockscout.com/tx/0x4993015929168f220dce49534b99776f91383ca98cef7f4d9c8fe6681843ef36).

### R002 — SwappableBridgeUniswapV3

Três chamadas `swapAndBridge` bem-sucedidas (blocos **24236890**, **24241576**, **24242207**), 10 logs cada. O ABI publicado para o endereço inclui as funções `bridge` e `swapAndBridge`. A ficha B também descreve conversão ETH/WETH e devolução de troco em uma operação. Trata-se de indício consistente de troca com ponte entre redes, não de um pool de desvinculação de depósitos e saques.

**Parecer:** forte candidato a contrato não mixer dentro do recorte; falta conferir integralmente o código histórico e a cobertura de transações. [Transação amostrada](https://eth.blockscout.com/tx/0x05a13f0bf7165711a497b933cff0260febcd0b568f6c347e712e878e2d9a8ace).

### R004 — Wormhole Standard Relayer

Três chamadas `deliver` bem-sucedidas (blocos **24236673**, **24239948**, **24243108**) com 4, 5 e 6 logs. A documentação oficial da Wormhole identifica este endereço como relayer na Ethereum. A ficha B relata ter resolvido o proxy e identificado a implementação histórica **`0x90995dbd1aae85872451b50a569de947d34ac4ee`** por eventos `Upgraded`, mas essa reconstrução **não foi reexecutada com leitura histórica independente** neste parecer.

**Parecer:** forte indício de relayer de mensagens, com pendência essencial de validação da implementação em 15/01/2026. [Transação amostrada](https://eth.blockscout.com/tx/0xa253e2e8c46f2a2fda83609d6233951dd6ee4a47fa755872c3732976e3035e2d).

### R005 — Chainlink CCIP Router

Três chamadas `ccipSend` (blocos **24236450**, **24240630**, **24243406**); a primeira foi revertida e as duas seguintes tiveram sucesso. Foram registrados 0, 7 e 11 logs, respectivamente. A documentação oficial e o repositório de ferramentas da Chainlink associam o endereço a seu router da Ethereum. Mesmo nos dois casos com logs de `Deposit`, o emissor é outro contrato (por exemplo, WETH) e a operação externa é uma mensagem CCIP: não é evidência de mixer de pool.

**Parecer:** forte indício de função de mensageria/roteamento entre redes. Para confirmar o negativo segundo o protocolo, checar versão e função histórica no bloco e fontes técnicas correspondentes. [Transação amostrada](https://eth.blockscout.com/tx/0x66516e1b3fa6a80778db1753521bcf5f867f6e6960fa490c995f53705269217c).

## 4. Resultado da adjudicação técnica preliminar

**Quatro divergências receberam documentação complementar e parecer funcional de não mixer; nenhuma foi convertida automaticamente em rótulo formal negativo confirmado.** As três referências Tornado Cash R006/R008/R009 permanecem positivas conhecidas, e R003/R007 continuam indeterminados. A ficha A, preparada com auxílio de IA, não pode ser contada como aprovação humana independente.

**Condição de fechamento:** Gustavo ou adjudicador designado deve examinar as evidências dos quatro casos e decidir, de modo fundamentado e **em registro novo pós-confronto**, se as provas de ABI, implementação histórica e transações atendem à regra de suficiência. Quando não atenderem, manter `indeterminado`. Não editar retroativamente os pareceres A/B.

## 5. O que pode entrar no artigo

Formulação permitida: “Uma auditoria documental piloto de nove alertas identificou três pools de referência e seis contratos de função diversa ou ainda indeterminada. O confronto de duas fichas mostrou quatro divergências, todas entre parecer negativo e indeterminado; três amostras de chamadas de cada contrato divergente foram verificadas em artefatos de auditoria já coletados. A análise reforça a necessidade de verificar funções e versões históricas antes de classificar alertas.”

**Não afirmar** que os quatro contratos sejam falsos positivos definitivamente demonstrados, nem usar os nove alertas para estimar precision, recall, F1, kappa de dois humanos, ou generalização entre protocolos.

## 6. Fontes e integridade

- O dossiê B é a [ficha do Bruno](https://docs.google.com/spreadsheets/d/1g4mqfuxOewrfBgVIJY2q_lfkzctuG_sztGWEkTSETpw/edit), consultada depois de autorização de comparação.
- A ficha A foi previamente pré-preenchida com IA; aprovação humana e data estão ausentes.
- O CSV anexo registra o método, blocos, hashes e pendências de cada um dos quatro casos.
- Não se obtiveram bytecodes históricos independentes nem execução RPC nova nesta etapa; fontes externas foram usadas para **corroborar nomes e funções**, não para provar ausência de todo comportamento possível.
