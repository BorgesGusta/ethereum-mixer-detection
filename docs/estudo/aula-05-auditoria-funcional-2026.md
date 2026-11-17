# Aula 05 — Auditoria funcional e rotulagem de contratos Ethereum

**Projeto:** Segurança de Redes — Detecção de Mixers na Ethereum
**Etapa:** EXP-02B (preparada, ainda não executada)
**Data do estudo:** 17/11/2026

## 1. Por que este experimento existe?

Na reprodução do artigo do SBSeg 2025, o Random Forest encontrou 9 alertas em 29/10/2020, enquanto os autores relataram 63. O filtro de transações é um fator importante de sensibilidade, mas não explica a equivalência com a lista não publicada do artigo. Mantemos essa diferença como limitação metodológica, sem alterar artificialmente o modelo para obter 63.

No teste legado de 15/01/2026, 20.214 endereços-janelas eram elegíveis e 9 foram sinalizados usando limiar congelado de 0,85. Três eram pools Tornado Cash de referência e outros seis apresentavam associações documentais a DEX, pontes, roteadores ou minter. Associação documental não é prova de que o contrato não seja mixer.

## 2. O que é um rótulo (label)?

Rótulo é o valor de referência usado para determinar se a previsão do modelo estava correta. As categorias científicas adotadas para a auditoria são: mixer confirmado, não mixer confirmado e indeterminado. Na ausência de provas suficientes, o rótulo deve permanecer indeterminado. Não vale converter ausência de evidência em prova negativa.

## 3. Contrato, transação e função são coisas diferentes

- Contrato: endereço com bytecode executado na Ethereum Virtual Machine.
- Transação: chamada com hash próprio, remetente, destino, bloco e timestamp.
- Selector: primeiros quatro bytes do calldata, usados para identificar a função quando a assinatura/ABI é conhecida; colisões e proxies exigem cautela.
- Log/evento: registro emitido durante a execução. Um evento é evidência de atividade mas não descreve necessariamente todo o fluxo financeiro.
- Proxy atualizável: a lógica executada pode ter sido substituída em outra data, portanto o código atual não comprova o que estava ativo no dia histórico.
- Trace: sequência de chamadas internas; pode ser necessária para inferir o fluxo real de fundos em transações complexas.

## 4. Como realizaremos a auditoria EXP-02B

1. Preservar o CSV original dos 9 alertas e o parquet intermediário do dia 15/01/2026.
2. Selecionar os seis endereços adicionais e extrair todas as transações **registradas no intermediário** que tenham cada um como destinatário naquele dia.
3. Ordenar cronologicamente os hashes e selecionar uma amostra reproduzível de três por contrato: primeira, central e última.
4. Consultar cada hash no Blockscout, cruzando hash, remetente, destinatário e dia UTC.
5. Recuperar os logs da transação e o selector do calldata; registrar se a paginação de logs estiver incompleta.
6. Consultar metadados atuais do contrato como pistas, **sem chamar de auditoria histórica do proxy**.
7. Salvar CSVs e manifesto com SHA-256 das entradas, resultados e falhas HTTP.
8. Submeter as evidências à revisão por dois avaliadores e decidir se cabe um rótulo independente. Esta revisão **não faz parte** da execução automática.

## 5. Os seis candidatos de 2026

- 0x7251febe...6dd2: OKX DEX (proxy; exigir histórico de implementação).
- 0x5182fede...2370: ApeCoin OFT Adapter / LayerZero.
- 0x57bedd7e...24b7: SwappableBridgeUniswapV3.
- 0x80226fc0...f7d: Chainlink CCIP Router.
- 0x2f848984...0479: MCT-XEN Batch Minter.
- 0x27428dd2...4911: Wormhole Standard Relayer.

Esses nomes são **hipóteses documentais** a verificar nas transações de 15/01/2026.

## 6. Exercícios para estudar e discutir

**Exercício 1.** Se o explorador confirma 3 de 3 hashes amostrados de um endereço com 119 transações, quais afirmações são legítimas?

**Exercício 2.** Uma transação de um contrato atualizável mostra método `swap` e evento de swap. Isso prova que o contrato não é um mixer?

**Exercício 3.** Se o modelo emitiu 9 alertas, 3 pools Tornado estão confirmados e 6 estão indeterminados, qual é a precisão do modelo?

**Exercício 4.** Por que comparar as funções de um bridge e de um mixer pode fornecer novas variáveis explicativas ao nosso Random Forest?

## 7. Respostas comentadas

**1.** Podemos afirmar que os três hashes pertencem ao endereço e à data, se destinatário/remetente/data coincidirem. Não podemos afirmar que as outras 116 transações foram auditadas na API.

**2.** Não. São evidências da atividade da amostra. Faltam a versão histórica do contrato e a avaliação do conjunto completo de operações. Proxies podem alterar a implementação.

**3.** A precisão global **não é conhecida**: seis alertas não têm ground truth. Só é correto informar recuperação de 3/3 positivos de referência e seis resultados indeterminados entre os alertas.

**4.** Porque mixers, bridges e DEXs podem ter entropias e volume de chamadas parecidos, mas sinais funcionais diferentes, como eventos de troca, ponte, depósito com compromisso e retirada com prova. Isso é uma **hipótese para um experimento controlado**, não uma melhoria já demonstrada.

## 8. Critério de sucesso e próximos passos

A etapa EXP-02B será considerada executada quando o Colab produzir CSVs, manifesto, relatório de cobertura e registro de falhas, com os números da fonte intermediária conferidos contra a referência legada. A auditoria independente dos seis rótulos, a busca de mixers de outros protocolos e a comparação predefinida entre modelos são fases futuras.

## Fontes de consulta

- Protocolo EXP-02B: https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02B-protocolo-auditoria-2026.md
- Relatório EXP-02A: https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02A-inventario-e-triagem-2026.md
- Documentação Blockscout: https://github.com/blockscout/blockscout-api-v2-swagger/blob/main/swagger.yaml
- Artigo Akopova, *Detecting Ethereum Mixers* (PDF na biblioteca enviada pelo pesquisador).
- Artigo Xing et al., *Tracing Money Laundering Across DeFi, Bridges, and Mixers on Ethereum* (PDF na biblioteca).
