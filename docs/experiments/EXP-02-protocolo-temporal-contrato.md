# EXP-02 — Protocolo prévio de avaliação temporal e por contrato

**Versão:** 17/11/2026 — **Planejado, NÃO EXECUTADO.** Este protocolo define critérios antes de novos testes para evitar escolher retrospectivamente o experimento com resultado mais atraente.

## Perguntas e hipóteses

- **Q1 (reprodutibilidade):** qual parcela dos 63×9 alertas é sensível a reamostragem, semente e filtro de elegibilidade, sem ajustar o limiar para alcançar 63? Evidência preliminar virá da etapa 13 do notebook 01.
- **Q2 (generalização):** um classificador treinado em um grupo de contratos/períodos reconhece **contratos inteiramente ausentes do treino**?
- **Q3 (deriva temporal):** o desempenho muda ao aplicar uma configuração treinada em 2025 a dias de 2020/2026, respeitando a disponibilidade real das fontes?
- **Q4 (validade das features):** o tratamento de transações diretas e Router, a cobertura de chamadas internas e a discretização da entropia produzem diferenças sistemáticas?

## Critérios de prontidão (bloqueios explícitos)

1. **Rótulos positivos independentes**, com nome, endereço, contrato, versão e intervalo histórico; não basta que o próprio modelo sinalize.
2. **Rótulos negativos auditados** (protocolo conhecido, função econômica, evidências de que não integra a classe definida). Um rótulo vazio **não equivale** a negativo.
3. Múltiplos contratos positivos distintos para tornar possível testar *holdout por contrato*. As atuais 23 janelas positivas de um **único** pool são insuficientes para esse experimento.
4. Dados por período e fontes com metadados de cobertura; registrar quais janelas/atributos não possuem observação suficiente.
5. Congelamento do conjunto de teste e das métricas **antes** da seleção final do modelo.

## Separações e prevenção de vazamento

- **Por período:** períodos completos separados, sem janelas de uma mesma transação em treino e teste. Se aplicar treino 2025→teste 2020, descrever explicitamente como *transferência retrospectiva de padrões*, **não** como previsão prospectiva.
- **Por contrato:** um endereço-contrato não pode aparecer em treino e teste na mesma avaliação de generalização. Considerar agrupamento por protocolo/implementação quando pools do mesmo protocolo compartilham código e comportamento.
- **Reamostragem/normalização:** somente dentro do fold de treino; nunca ajustar transformações usando observações do teste.
- **Router:** política única pré-especificada e harmonizada entre períodos, ou cenários de ablação explicitamente separados.

## Modelos de comparação planejados

- Random Forest do artigo (baseline: 100 árvores; max_depth 5; limiar 0,50), preservado sem calibragem usando teste.
- Um baseline interpretável, por exemplo regressão logística, com pré-processamento ajustado somente no treino.
- Extra Trees como alternativa exploratória, com orçamento de busca e critérios iguais entre modelos.
- Não declarar um método melhor sem métricas externas comparáveis.

## Métricas e evidências

- Em dados com **ground truth**: matriz de confusão, precision, recall, F1, PR-AUC; taxa de falsos alertas em universo validamente rotulado; incerteza por reamostragem **agrupada por contrato/período**, quando factível.
- Em população **não rotulada**: apenas quantidade de alertas, distribuição de scores, sobreposição de conjuntos e auditoria manual, sem precisão/falso positivo fabricado.
- Rastreabilidade: SHA-256, fonte Blockchair/Blockscout, configuração da coleta, commit, notebook, seeds, relatório de cobertura, manifestações dos provedores, data da execução.
- Controles de integridade e qualidade **não** são métrica substituta de robustez adversarial, segurança criptográfica ou capacidade de mitigação de fraudes.

## Forma prevista de relatar resultados

- **Se 63×9 continuar sem causa resolvida:** declarar reprodução parcial, descrever quais contagens coincidiram, natureza das escolhas não documentadas e referência ao pedido de esclarecimento aos autores **somente quanto à situação real no fechamento do manuscrito**.
- **Se houver novos resultados de avaliação:** apresentar resultados separados dos 63/9, com amostras, splits, métricas e limitações próprias.
- **Se um provedor não retornar dados históricos:** marcar inconclusivo e não substituir por rótulo negativo.

## Próxima ação após EXP-01I

Inventariar quantos contratos positivos **distintos** existem em 2020, 2025 e 2026 com cobertura auditada; inventariar negativos verificáveis por data e protocolo. Somente então decidir quais divisões por contrato/período são factíveis.
