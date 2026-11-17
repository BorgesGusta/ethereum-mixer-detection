# Guia de estudo e defesa do projeto

Cada estudo começa com três perguntas:

1. **O que tentamos reproduzir?** O artigo SBSeg 2025 propõe detectar mixers na Ethereum por características de transações e aprendizado supervisionado.
2. **Qual é a unidade de análise?** Neste projeto, agrupamos transações por contrato destinatário e dia UTC (janela endereço-dia), sujeitos a regras de elegibilidade; verificar se esse agrupamento coincide exatamente com as escolhas descritas no artigo.
3. **Como sabemos se o modelo funciona?** Métricas internas sozinhas não bastam; devemos controlar vazamento por contrato, reconhecer rótulos desconhecidos, medir cobertura da fonte e testar em períodos ainda não usados para ajustes.

## Glossário essencial

- **Mixer:** mecanismo que busca dificultar a associação entre origem e destino de ativos.
- **Pool:** contrato de denominação específica, por exemplo Tornado Cash 1 ETH, usado no estudo.
- **Router:** contrato intermediário que pode encaminhar chamadas aos pools; filtragem somente por destinatário de topo pode perder atividade.
- **Transação de topo:** transação registrada no bloco, com remetente, destinatário e hash.
- **Chamada interna (trace):** interação entre contratos produzida na execução de uma transação.
- **Hash:** identificador da transação; usado para conciliar chamada interna com transação de topo.
- **Feature:** valor numérico que descreve uma janela, como entropia ou média de chamadas.
- **Entropia de Shannon:** mede diversidade dos valores discretizados; zero quando todas as observações são iguais.
- **False positive:** predição positiva cuja classe verdadeira foi **verificada** como negativa. Endereço não rotulado não é automaticamente falso positivo.
- **Data leakage:** informação de teste, ou informação correlacionada entre treino e teste, que vaza para seleção, treino ou calibração.
- **Concept drift:** mudança na relação entre as características e o alvo ao longo do tempo; simples mudança das distribuições de entradas é *data drift* e não prova concept drift.

## Perguntas de apresentação
- Por que os quatro pools em 29/10/2020 produzem apenas quatro exemplos positivos? **Porque uma janela por contrato-dia é uma linha; milhões de transações não equivalem a milhões de exemplos positivos.**
- Por que `internal_value_entropy` pode ser zero em 2020? **Nos quatro pools inspecionados naquele dia, o valor interno foi constante; o cálculo foi reproduzido exatamente.**
- Qual foi a divergência de 2025? **Um CSV denominado 15/03 contém chamadas de 15–21/03; comparar com dump somente de 15/03 deixa hashes de outros dias sem correspondência.**
- O que temos para afirmar sobre 2026? **A atribuição por chamadas foi reproduzida para três pools na data 15/01/2026, mas isso não equivale a comprovar generalização temporal em todos os anos.**

Atualizar esta aula somente com conclusões apoiadas por um experimento identificável e suas evidências.
