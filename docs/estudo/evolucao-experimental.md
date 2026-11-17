# Linha do tempo e resultados — nossa pesquisa Ethereum mixers

**Atualizado:** 17/11/2026. Esta leitura distingue fatos demonstrados, hipóteses e verificações pendentes.

## A referência original

O artigo de Pedro Leale e Ivan da Silva Sendin no SBSeg 2025 reportou **63 endereços sinalizados** com Random Forest em dados da Ethereum de **29/10/2020**. Nossa reprodução, com **100 árvores**, `max_depth=5`, `random_state=42`, limiar >0,50 e `n_tx>=10`, sinalizou **9**, incluindo os três contratos Tornado Cash citados pelos autores. A diferença **63 × 9** permanece sem causa externa comprovada.

## A população do dia de 2020

- Transações no dump: **1.114.702**.
- Destinatários distintos: **230.658**.
- Destinatários com ≥10 transações: **4.038**.
- Contratos Tornado artigo: **0,1 ETH = 73**, **1 ETH = 55**, **10 ETH = 111**, somando **239 transações**.
- Os 9 alertas contêm ainda um pool Tornado de **100 ETH** e contratos com associações documentais a **ForTube, zkSync, proxy, token SmartEther e DSProxy**. Essas associações não tornam todos eles negativos verificados.

## A composição do treinamento

São **23 janelas positivas de um único contrato Tornado** ao longo de 23 dias e **100 janelas negativas de 100 endereços em um dia**. Ao balancear por oversampling chega-se a 100/100. Validação cruzada dividida por linha, sem reservar contratos/protocolos, não demonstra generalização para contratos desconhecidos.

## Os experimentos, em sequência

| Experimento | Pergunta | Conclusão sustentada |
|---|---|---|
| EXP-01B | Por que 63 × 9? | Curva de limiares mostra alta sensibilidade; não modificar limiar só para imitar 63 |
| EXP-01C/D | Quem são os 9 alertas? | Pistas documentais para contratos e protocolos; três casos exigiram consulta Blockscout |
| EXP-01E | As features batem com o dataset processado? | **12/12** paridades internas para três contratos; não é validação externa de traces |
| EXP-01F | Há cobertura externa das transações? | Dois contratos com 10 tx cada consultados; proxy não chegou a 29/10/2020 |
| EXP-01G | Os hashes conferem? | **20/20 hashes**, remetentes, destinatários e blocos coincidentes Blockchair × Blockscout |
| EXP-01H | Qual a implementação do proxy em 2020? | A consulta do slot histórico falhou em provedores; resultado **inconclusivo** |
| EXP-01I/J | Que mudanças afetam os alertas? | Filtro mínimo 1/5/10/20 tx produz **49/14/9/7** alertas com mesmo modelo e limiar; não explica 63 |
| EXP-02 | Como avaliar generalização? | Protocolo por período/contrato com ground truth auditável preparado |
| EXP-02A | Já existem resultados 2026? | **Sim, teste legado** em 15/01/2026: 20.214 elegíveis, 9 alertas e 3 pools Tornado conhecidos |
| EXP-02B | Como verificar 6 alertas extras em 2026? | Protocolo planejado para funções, eventos, transações e implementação de proxies; **não executado** |

## Entendendo o resultado de sensibilidade

O corte `n_tx>=10` remove 40 alertas que aparecem quando a mesma floresta classifica todos os destinatários com ao menos uma transação. Isso demonstra que **o universo classificado** afeta a quantidade de alertas. Todavia, mesmo com `n_tx>=1`, a reprodução produz **49**, não 63. Falta conhecer lista dos endereços originais, exemplos exatos de treinamento e detalhes de engenharia de features dos autores.

## O teste temporal de 2026

O modelo foi treinado em 2025, limiar **0,85** congelado por validação em 2020, e aplicado ao dia **15/01/2026**. Produziu **9 alertas** em **20.214** janelas elegíveis, incluindo os três pools Tornado do artigo. Seis alertas adicionais têm associações documentais a **OKX DEX, ApeCoin OFT Adapter/LayerZero, SwappableBridgeUniswapV3, Chainlink CCIP Router, MCT-XEN Batch Minter e Wormhole Relayer**.

A presença de nomes associados a serviços diferentes de mixers é uma hipótese de confusão estatística; **não são seis falsos positivos confirmados**. O pool Tornado 10 ETH foi usado no treino; assim, essa execução não prova reconhecimento de novo protocolo mixer.

## Evidência e limites, lado a lado

**Fatos demonstrados:** os três pools conhecidos são recuperados, a auditoria de dados produziu paridade em 20 hashes para dois contratos, o filtro mínimo altera o total de alertas, e o projeto tem manifestações de integridade e documentação reproduzível.

**Não demonstrado:** equivalência aos 63 alertas do artigo; precisão/recall na população total; estado de proxy em outubro/2020; seis negativos de 2026; generalização a Railgun/outros mixers; superioridade de segurança ou robustez.

## Repositório e documentos de origem

Checklist: https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/CHECKLIST_VIVO.md

EXP-01J: https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-01J-resultados-sensibilidade-63x9.md

EXP-02A: https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02A-inventario-e-triagem-2026.md

EXP-02B: https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02B-protocolo-auditoria-2026.md

## Perguntas de revisão

1. Por que “9 alertas” não significa “9 mixers verdadeiros”?
2. O que significa 20/20 hashes coincidentes e o que isso não significa?
3. Como a falta de archive RPC deve ser relatada?
4. Por que o teste 2026 é legado, não novo?
5. Qual seria o próximo experimento capaz de transformar hipótese de confusão com bridges em contribuição científica?
