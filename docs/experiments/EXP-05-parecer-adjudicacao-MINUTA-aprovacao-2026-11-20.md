# EXP-05 — Parecer de adjudicação dos nove alertas

MINUTA PARA APROVAÇÃO | 20/11/2026 | NÃO HOMOLOGADO

## 1. Objetivo e método

Registrar uma proposta de decisão para nove contratos sinalizados na Ethereum em 15/01/2026. A definição positiva predefinida é um mixer de pool com desvinculação entre depósito e saque. As classificações se limitam ao endereço e recorte histórico estudados. Não permitem afirmar ilegalidade de usuários.

A ficha A foi elaborada com auxílio de IA e não tem aprovação humana caso a caso nem data UTC de revisão. A ficha B foi preenchida pelo Bruno em 19/11/2026. A leitura comparada ocorreu com autorização em 20/11/2026. Qualquer avaliação posterior é adjudicação pós-confronto e não substitui uma segunda revisão humana cega. As fichas originais não devem ser alteradas.

Critério conservador: confirmar positivo quando houver documentação e comportamento compatível com um pool; confirmar negativo somente com evidência histórica suficiente de função diferente, implementação correta e escopo temporal definido; manter indeterminado diante de implementação proxy não confirmada, código histórico incompleto ou evidência apenas amostral.

## 2. Propostas de classificação por caso

R001 — ApeCoin OFT Adapter | A: indeterminado | B: negativo_confirmado | PROPOSTA: indeterminado. No EXP-02B, três chamadas send de 15/01/2026 foram confirmadas com 36 logs. Isso favorece transferência de tokens entre redes. Falta verificar de modo independente o código ativo no bloco da data-alvo.

R002 — SwappableBridgeUniswapV3 | A: indeterminado | B: negativo_confirmado | PROPOSTA: indeterminado. Três chamadas swapAndBridge no dia e 30 logs sustentam função de troca e ponte. A cobertura é amostral e o código histórico integral não foi confirmado.

R003 — OKX DEX proxy | A: indeterminado | B: indeterminado | PROPOSTA: indeterminado. B descreveu operações com WETH e uma possível implementação 0x85461e163c64f99a8709dff3bab0db808c358bd6, mas não comprovou o código da implementação do período.

R004 — Wormhole Standard Relayer | A: indeterminado | B: negativo_confirmado | PROPOSTA: indeterminado. Três chamadas deliver no dia e 15 logs são compatíveis com entrega de mensagens entre redes. B relatou implementação 0x90995dbd1aae85872451b50a569de947d34ac4ee, cuja validade histórica ainda não foi reexecutada de modo independente.

R005 — Chainlink CCIP Router | A: indeterminado | B: negativo_confirmado | PROPOSTA: indeterminado. Três chamadas ccipSend no dia, duas bem-sucedidas e uma revertida, com 18 logs. Evidência de roteamento entre redes, mas sem revalidação histórica integral da implementação no bloco analisado.

R006 — Tornado Cash, pool de 1 ETH | A: positivo_confirmado | B: positivo_confirmado | PROPOSTA: positivo_confirmado, REFERÊNCIA CONHECIDA. A identificação do contrato e as evidências de depósitos e retiradas relatadas em B são compatíveis com um pool de mixer; não representa novo protocolo nem validação externa.

R007 — MCT-XEN proxy | A: indeterminado | B: indeterminado | PROPOSTA: indeterminado. B descreveu chamadas em lote e implementação sugerida 0xce2ae22de7d45558c5feaededd828dfd22c6d7a2, mas não identificou de forma verificável o código/função histórica completa.

R008 — Tornado Cash, pool de 10 ETH | A: positivo_confirmado | B: positivo_confirmado | PROPOSTA: positivo_confirmado, REFERÊNCIA CONHECIDA. A ficha B documentou exemplos de depósito de 10 ETH e retirada via Router; trata-se do mesmo protocolo do treinamento.

R009 — Tornado Cash, pool de 0,1 ETH | A: positivo_confirmado | B: positivo_confirmado | PROPOSTA: positivo_confirmado, REFERÊNCIA CONHECIDA. B descreveu depósitos, retiradas e elementos de migração. É referência do Tornado Cash, não outro protocolo.

## 3. Evidências e limites da investigação

O material do EXP-02B contém 12 transações amostradas em 15/01/2026 para R001, R002, R004 e R005, três por caso. Foram capturados 99 registros de logs nessas amostras. Os métodos observados foram send, swapAndBridge, deliver e ccipSend. As evidências foram reanalisadas a partir dos arquivos preservados e não constituem nova coleta on-chain ou auditoria exaustiva.

As quatro divergências decorrem de B propor negativo_confirmado enquanto A mantinha indeterminado. A análise funcional favorece a hipótese de não mixer, mas o protocolo pré-registrado exige confirmação histórica suficiente para atribuir negativo. Em R003 e R007 faltam verificações decisivas de implementações de contratos proxy. Nenhum dos seis casos adicionais deve ser automaticamente chamado de falso positivo confirmado.

Integridade dos arquivos EXP-02B: SHA-256 de amostras_tx_api.csv = 83f42e349d25cbbcded99784ba9eb4c148b64c9d91eb3190aab00a76c5f3ea8d. SHA-256 de eventos_amostras.csv = b4442151e64a86722aed72caf15a785f6da800fc139d8befa8e50a41bd143571. Esses hashes se referem aos arquivos de coleta, não aos anexos individuais das fichas A e B.

## 4. Síntese proposta e alcance científico

Resultado conservador proposto: três positivos conhecidos do Tornado Cash e seis indeterminados, quatro dos quais com indícios fortes de função não mixer. As duas fichas apresentam cinco classificações nominais iguais e quatro divergentes. Como A foi preparada com apoio de IA e não está assinada, esses números NÃO medem concordância entre dois revisores humanos independentes.

Os nove contratos foram escolhidos por terem sido alertados pelo detector. A amostra não permite estimar precisão, recall, F1, falsos negativos, taxa geral de falso positivo nem generalização para protocolos diferentes. Estas propostas também não autorizam atualizar rótulos de treino ou treinar novamente o modelo.

## 5. Texto sugerido para o manuscrito

Realizamos uma auditoria documental piloto de nove alertas da Ethereum em 15 de janeiro de 2026. Três endereços correspondem a pools conhecidos do Tornado Cash. Os seis casos adicionais permaneceram indeterminados segundo os critérios históricos de rotulagem, embora quatro apresentassem operações características de troca, ponte, entrega de mensagens ou roteamento entre redes. A comparação documental de duas fichas revelou quatro divergências entre classificações negativa e indeterminada. Como uma ficha foi preparada com apoio de IA e a adjudicação humana permanece pendente, esses resultados são apresentados apenas qualitativamente, sem estimativa de desempenho do classificador.

## 6. Registro de aprovação humana — PENDENTE

[  ] APROVAR as decisões propostas     [  ] APROVAR com alterações registradas     [  ] SOLICITAR INVESTIGAÇÃO ADICIONAL

Adjudicador responsável: __________________________________________

Data e hora UTC de aprovação: _____________________________________

Observações, mudanças e fontes adicionais: ______________________________

A assinatura ou aprovação deverá ocorrer depois de conferidos os endereços, evidências e limites. Alterações posteriores devem ser registradas em versão nova do parecer, não nas fichas A ou B originais.

## 7. Fontes de auditoria

Protocolo EXP-05: https://drive.google.com/file/d/1rN4LtgLXkzrybFTxL50mSRJeigcrMlQo/view

Confronto A/B: https://drive.google.com/file/d/1eJdgSiZJPa-8uM3CFH6se0TKlIl4BUhd/view

Parecer técnico das divergências: https://drive.google.com/file/d/13qCv7HHIhXE4iOyEES6grQIe_raepGr4/view

Amostras EXP-02B: https://drive.google.com/file/d/17S6xCYOng7Fk21cYZGq5k1yKzNn3kqGq/view

Logs EXP-02B: https://drive.google.com/file/d/1NwJFLTrrMtpLndn2vMV7fLzy9oQJMlH6/view

Manifesto EXP-02B: https://drive.google.com/file/d/1uM3FQlaJQXXMKuTuACO6BI2oLU1_qVE7/view

Documentação do protocolo Tornado Cash: https://github.com/tornadocash/tornado-core

Cópias das fichas A e B preservadas na coordenação: https://drive.google.com/drive/folders/1qW94S6wuT1nwV-Hukc-8mjsYUqzAvZvy

