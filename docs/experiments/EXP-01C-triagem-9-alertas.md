# EXP-01C — Triagem dos 9 alertas de 29/10/2020

**Data:** 17/11/2026. **Natureza:** auditoria documental, não confirmação on-chain completa nem rótulos de verdade-terreno.

## Objetivo

Separar **predições do modelo** de **rótulos de referência usados no experimento** e de **identificações externas independentes**. Esta distinção evita calcular uma precisão enganosa em um problema de detecção de mixers.

## Fontes

- [Scores dos 4.038 candidatos elegíveis](https://drive.google.com/file/d/1ZC-iBEmYvLxTN6IZR8aTOqfQ3cm5wJwG/view)
- [CSV legado com os 9 alertas](https://drive.google.com/file/d/1TFkoAKXVjM4jAxjS75lrilxhWzMEiRkH/view)
- [Paridade e identificação dos quatro pools Tornado 2020](https://drive.google.com/file/d/1Vuo98PnMKRoL1t4j9MHmkQz4s8bGfbfS/view)
- [Repositório ForTube que declara BANK](https://github.com/thefortube/fortube), endereço `0xde7b3b2Fe0E7b4925107615A5b199a4EB40D9ca9`
- [Blockchain Research Lab, lista zkSync](https://www.blockchainresearchlab.org/wp-content/uploads/2020/05/BRL-Working-Paper-29-Transaction-Fees-and-Economic-Activity.pdf), endereço `0xabea9132b05a70803a4e85094fd0e1800777fbef`

## Resultado da triagem

| Situação | Quantidade | Observação |
|---|---:|---|
| Tornado Cash de referência artigo (0,1/1/10 ETH) | 3 | Detectados e rotulados no dataset |
| Tornado Cash 100 ETH adicional | 1 | Aparece sem `tornado` no parquet; identificado no relatório histórico |
| Protocolos externos identificados documentalmente | 2 | ForTube BANK e zkSync; **não equivalem automaticamente a negativos verificados** |
| Sem identificação corroborada suficiente nesta rodada | 3 | `0x5e60…`, `0x98f1…`, `0xe113…` |
| **Total de alertas do nosso modelo (>0,50)** | **9** | Somente 4.038 endereços elegíveis receberam predição |

**Separação de evidências:** a lista original de nove do legado tem campos `categoria`, `rotulo_etherscan` e `observacao` vazios. O arquivo de classificação externa criado hoje não altera esse legado e não atribui classes binárias de modo definitivo.

## Cinco candidatos não rotulados no parquet

1. `0x5e60fcca904753a31f9df7d7f6b7856b6ec27aa9`, score 1,00, 53 tx — **não identificado nesta pesquisa**.
2. `0x98f1858c9740b9c5f2cd8abea67948873d38dc39`, score 0,98, 10 tx — **não identificado nesta pesquisa**.
3. `0xde7b3b2fe0e7b4925107615a5b199a4eb40d9ca9`, score 0,91, 52 tx — **ForTube BANK**, com referência ao repositório público do protocolo.
4. `0xe113d58a4cb4dbac8a0da608ed7232785c1f2c18`, score 0,76, 10 tx — **não identificado nesta pesquisa**.
5. `0xabea9132b05a70803a4e85094fd0e1800777fbef`, score 0,59, 25 tx — **zkSync**, documentado como ponte/proxy em estudo do Blockchain Research Lab.

Esses cinco devem permanecer **fora do cálculo de falsos positivos confirmados** até definição de classes de referência e auditoria independente.

## Perguntas para aprender e explicar

**Por que 4 conhecidos entre 9 e não apenas 3?** Porque o artigo incluiu no teste referenciado três pools, mas o acervo expandido contém um quarto pool 100 ETH, igualmente sinalizado. O rótulo vazio de um dataset não é prova de ausência de mixer.

**Por que identificar ForTube e zkSync não prova dois falsos positivos?** Porque identificar a função do contrato com evidência externa é uma etapa de rotulagem, mas precisamos validar pertinência à classe usada, intervalo do experimento e critérios completos; não equivale a rótulo verificado de não mixer.

**A descoberta explica 63 vs 9?** Não. Esclarece a *interpretação dos nossos nove*, não diferenças de treinamento e critérios com o artigo.

## Próximo passo

Auditar os três endereços ainda não identificados com fontes primárias (Etherscan verificação de contrato, histórico de eventos, código e transações em 29/10/2020). Depois comparar amostras de treino, filtros e procedimentos exatos do artigo, sem mudar limiar por conveniência.
