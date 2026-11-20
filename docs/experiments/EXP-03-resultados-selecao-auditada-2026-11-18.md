# EXP-03 — Resultado auditado da seleção de controles (execução 18/11/2026)

**Status:** SELEÇÃO EXECUTADA E AUDITADA QUANTO A ARQUIVOS/MANIFESTO; **NÃO** auditoria contextual, rotulagem ou validação independente. Análise documental dos outputs originais, **sem reexecutar o modelo nesta conferência**.

## Proveniência

- [Pasta de resultados no Drive](https://drive.google.com/drive/folders/1SAdkZVyXcmYs02AYNZACE7h5DEDzPdzJ), em `Projeto_Mixers_Ethereum/results/EXP-03_selecao_controles_20261118T024057Z/`.
- [Manifesto de seleção](https://drive.google.com/file/d/1CXid67uMShljJBb2dftm8cRPzRleQb2B/view), 1.350 bytes.
- [CSV de controles provisórios](https://drive.google.com/file/d/1qgMy6Yy1UEGm6JgEQqkgrkoyjDHTCz-1/view), 1.168 bytes.
- **Execução registrada:** 2026-11-18T02:40:55.271307+00:00 (23:40:55 de 17/11, UTC-03).
- Script de seleção [`scripts/exp03_selecionar_controles.py`](../../scripts/exp03_selecionar_controles.py), com download fixado no notebook ao commit `360d351962ef7aff7db7dc957fbeecbd182058df`.
- Rede/dia de referência: Ethereum mainnet, **15/01/2026**. Limiar legado **0,85**, `min_tx=10`. Dados **já explorados**, não teste cego.

## Integridade e travas

| Verificação | Valor do manifesto / conferência | Estado |
|---|---|---|
| Elegíveis de referência | 20.214 | Declarado e protegido por falha explícita no script |
| Alertas de referência | 9; mesmas identidades | `paridade_identidades_alertas=true` no manifesto |
| Máxima diferença de scores dos 9 alertas | 0.0 | `diferenca_maxima_scores_alertas=0.0` |
| Amostra de controles | 6 pares; 6 alertados e 6 controles distintos | Conferido diretamente no CSV |
| Correspondência de bandas de `n_tx` | Distância de banda 0 em todos os seis pares | Conferido diretamente no CSV |
| SHA-256 do CSV | `ea01869f2b776246578c1bd7c78253634704714b5d013853505657de34d890d5` | Recalculado sobre bytes baixados; coincide com manifesto |
| SHA-256 do Parquet de features | `6d3da4a245778d707319cec8cde7a420a91166f01cd6373691fe1e8fac9d4294` | Recalculado sobre bytes da cópia oficial previamente baixada; coincide |
| SHA-256 do modelo RF | `012bdf45a70fe04e4ee32d2d9c48c548c2e43d3d9615837573bdfa22f6bd6863` | Recalculado sobre bytes da cópia oficial previamente baixada; coincide |
| SHA-256 do ranking legado | `5e989df3b50b2e5f84cab01af7fef4861dcb5eb63ecd0a2f5ae9f62ed9e8a260` | Recalculado sobre bytes da cópia oficial previamente baixada; coincide |

**Limite da verificação:** paridade do modelo foi constatada pelo manifesto e pelas travas implementadas, não por reexecução independente da inferência nesta auditoria. Os arquivos de entrada foram comparados com cópias oficiais do Drive, não com a pasta externa original do Bruno.

## Pares selecionados

| Alerta adicional | n_tx alertado | score alertado | Candidato a controle | n_tx controle | score controle |
|---|---:|---:|---|---:|---:|
| `0x27428dd2d3dd32a4d7f7c497eaaa23130d894911` | 16 | 0.86 | `0xbd70bb67c90ea7d01abcf5b0c973a3830c7cff88` | 10 | 0.0 |
| `0x2f848984984d6c3c036174ce627703edaf780479` | 15 | 0.91 | `0x18d1b124044e028511875cfdb380c240f6f87035` | 10 | 0.0 |
| `0x5182fede730b31a9cf7f49c5781214b4a99f2370` | 16 | 0.99 | `0xf7de94d35d6a28563b66506ec4e7a9826b583ac1` | 18 | 0.0 |
| `0x57bedd7eb4c3118669f4f33a3cae4d4b554f24b7` | 66 | 0.98 | `0xac345edaa698ba22f0db05a73209e4373c2d3120` | 68 | 0.0 |
| `0x7251febeabb01ec9de53ece7a96f1c951f886dd2` | 83 | 1.0 | `0x99dcb46e59971c30f860f451e8e05c3084be03dd` | 56 | 0.0 |
| `0x80226fc0ee2b096224eeac085bb9a8cba1146f7d` | 119 | 0.98 | `0xff00000000000000000000000000000000000010` | 316 | 0.0 |

Todos têm `status=provisorio_aguardando_verificacao_tipo_de_endereco` e `contrato_controle_historicamente_confirmado=false`.

### Achados relevantes e limites

1. **Todos os seis controles têm score 0,0.** Seleção estratificada por volume de transações, **não pareada por score**, tipo de endereço, setor econômico ou grau de dificuldade. Pode ser trivial para o modelo distinguir casos; não utilizar como prova de valor de atributos contextuais.
2. **Todos estão na mesma faixa de atividade**, mas quantidade de transações pode diferir significativamente dentro da faixa: ex. 119 vs 316 e 83 vs 56. Não afirmar pareamento fino.
3. `0xff00000000000000000000000000000000000010` tem estrutura de endereço atípica e **exige verificação on-chain**, sem presumir sua função, natureza ou legitimidade.
4. A seleção **não comprova que seis controles sejam smart contracts**. Alguns podem ser EOAs; não cabe comparação funcional DEX/mixer x EOA sem estratificação adequada.
5. Identidades dos seis alertados coincidem com casos de EXP-02A/B/C e **não precisam ser auditadas de novo** até haver justificativa específica.
6. Nenhum desses resultados produz ground truth, falso positivo confirmado, precision, recall, F1 ou teste de generalização.

## Decisão de gate

- **Gate 1-A: PASSOU** — CSV gerado, paridade registrada, dados/manifesto/6 pares íntegros e rechecados documentalmente.
- **Gate 1-B: PENDENTE** — verificar na data histórica se os controles são contratos (e/ou se são EOAs), interface econômica e representatividade; sem isto não há comparação contextual válida.
- **Gate 2 (coleta externa): NÃO INICIADO**. Priorizar consulta de metadados e `eth_getCode` no bloco histórico para os seis controles e comparadores. Registrar erros de arquivo RPC, provedor, período e tipo de endereço. Não executar retroativamente seleção alternativa só para obter resultado favorável.
- **Gate 3 (rótulos): NÃO INICIADO**; revisão independente necessária.

## Próxima etapa proposta, sem reexecução

Projetar **EXP-03B** como validação de elegibilidade dos controles, preservando o CSV congelado e registrando endereços não comparáveis como `excluido_por_tipo` ou `inconclusivo`, não trocando silenciosamente por novos. Caso um grupo tenha menos de 6 pares aptos, reportar redução amostral ou emitir adendo prévio com regras de reposição e *sensibilidade* separado. Primeiro avaliar se a amostra pode ser uma comparação entre contratos inteligentes, depois recolher logs de controles aptos. Se inexistirem controles válidos, declarar piloto inviável, sem métricas fabricadas.

**Uso no artigo:** apenas descrever seleção e integridade como metodologia executada, não como experimento confirmatório. Não gerar PDF.
