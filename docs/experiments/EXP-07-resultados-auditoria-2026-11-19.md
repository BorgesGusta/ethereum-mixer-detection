# EXP-07 v2 — Auditoria e interpretação da comparação exploratória e ablação

**Execução:** 20/11/2026 00:36:45 UTC (19/11 no horário UTC-3). **Estado: EXECUTADO E AUDITADO.**
**Decisão:** conjunto contém **1 único contrato positivo**, portanto comparação é **validação interna por linhas**, sem validação independente por contrato ou protocolo.

## Fontes e integridade

- [Pasta oficial de execução no Google Drive](https://drive.google.com/drive/folders/1iekmCwwXYnxzYNp7jJ6Ye5S4O56UN0b6).
- [Auditoria da matriz](https://drive.google.com/file/d/1Ghgugyo8U0Mhn4GAsZlaOmnJ5Clq4nUe/view), [resumo dos 12](https://drive.google.com/file/d/1h8dC2pmki_TteMGXKLHaVAEmVK8duKTO/view), [métricas por fold](https://drive.google.com/file/d/1TB1oy9ZwzYL_EMggYTvZqY3ENHXZj0Uh/view), [folds congelados](https://drive.google.com/file/d/1cg1fkkmFudgY-eqej__5euY_gI5Yac_g/view), [manifesto](https://drive.google.com/file/d/1rAwtsQbsX5rhmgI-OLn8GBmJxy0rgGAo/view), [cópia da matriz](https://drive.google.com/file/d/1_Sry0K0JusRL3PcxEweyC_9hnaP1vdRy/view).
- **SHA-256 recalculados sobre os bytes efetivamente recuperados do Drive e conferidos com manifesto: todos os 5 artefatos coincidem**:
  - `auditoria_matriz.json` `a3470f0a912e2324522bace456db41170df527e17873d958562512201ee18005`
  - `features_treino_original.parquet` `0a8baa11cee97d338d7a8d92b984f38192ba1a10ec915cc4a06d67ec94ad5c32`
  - `folds_congelados.json` `0b23f3b7749dee4ed541c5ac98f2c77c4ddb0ab9e6a2e66b9e7423bf1bba67f7`
  - `metricas_12_combinacoes_por_fold.csv` `ae7e2eeab6882bdf7739fd36784ca87ccc1a9800c17239582acbfae01d584b86`
  - `resumo_12_combinacoes.csv` `f1b2da3a9916c298a3d0731b781955ec05c7defd2f83455163fcf2eb68dda6e6`
- [Protocolo predefinido](EXP-07-protocolo-comparacao-e-ablacao.md); [notebook v2](../../notebooks/21_EXP-07_v2_comparacao_e_ablacao.ipynb), commit `33e6cc5296b64ff8ff8293b2ebb28136f634dc61`. Resultados auditados sem reexecução da inferência.

## Auditoria de composição e vazamento de identidade

| Campo | Observado |
|---|---:|
| Exemplos (linhas) | **123** |
| Classe 0 | **100** |
| Classe 1 | **23** |
| Contratos distintos no dataset | **101** |
| Contratos negativos distintos | **100** |
| Contratos positivos distintos | **1** |
| Dias positivos | **23** |
| Dias negativos | **1** |
| Duplicatas contrato-dia | **0** |
| Faltantes nas cinco features | **0** |
| Método | **StratifiedKFold por linhas, exploratório** |
| Número de folds | **5** |
| Folds com contrato compartilhado treino/teste | **5/5**, 1 contrato por fold |

Como os **23 positivos** vêm de um único contrato em 23 dias, **não há como criar folds de teste com positivos de contrato inédito sem perder classe positiva em treino ou teste**. Separação por linhas faz com que a mesma identidade apareça em ambos. Portanto, uma métrica interna elevada é compatível com aprendizado de traços do único contrato/protocolo, e não valida generalização. Dias negativos todos iguais e dias positivos distintos também representam fator de confusão temporal/coleta. É inadequado usar F1 interno como medição populacional da Ethereum.

## Comparação de F1 médio em cinco folds (dados reais)

| Modelo | A: 5 features | B: sem n_tx | C: entropias |
|---|---:|---:|---:|
| Random Forest | **0,9778** | **0,9778** | **0,9778** |
| Decision Tree | 0,8870 | 0,9156 | 0,9159 |
| Gradient Boosting | 0,8870 | 0,9156 | 0,9159 |
| Regressão Logística | 0,8095 | 0,8170 | 0,5452 |

As métricas acima são médias aritméticas das medidas por fold, não F1 de uma base externa ou por contrato. A versão comparativa do Random Forest é **reentrenada**, não prova identidade de predictions com o modelo `modelo_rf.joblib` legado.

### Métricas da configuração original (A)

| Modelo | Precision média | Recall médio | F1 médio | Balanced accuracy média |
|---|---:|---:|---:|---:|
| Random Forest | 1,0000 | 0,9600 | 0,9778 | 0,9800 |
| Regressão Logística | 0,6833 | 1,0000 | 0,8095 | 0,9450 |
| Decision Tree | 0,9600 | 0,8300 | 0,8870 | 0,9100 |
| Gradient Boosting | 0,9600 | 0,8300 | 0,8870 | 0,9100 |

**Ablação:** retirar `n_tx` não alterou o F1 médio do RF na amostra e folds atuais; a versão só entropias manteve RF igual, mas Regressão Logística caiu para 0,5452. Isso não comprova irrelevância causal/geral de `n_tx` nem superioridade em dados externos. Árvores e boosting apresentaram métricas idênticas neste arranjo, sem implicar equivalência universal.

## Orientações para o artigo SBC

- Denominar **“Comparação exploratória e ablação de atributos”** (4 modelos × 3 grupos, 5 folds), não “comprovação de generalização” ou “classificador com 97,78% de precisão em mixer novo”.
- O número **97,78% corresponde a F1 médio interno**, não à precisão (`precision` foi 1,0 nesse conjunto e também não é estimativa externa).
- **Não apresentar alertas 2026 como falsos positivos/negativos** se a revisão EXP-05 ainda não estiver concluída.
- Contrastar resultado EXP-07 com EXP-01J (sensibilidade de volume), EXP-02 (9 alertas 2026, seis não rotulados) e EXP-06 (evidência on-chain de protocolo distinto **sem rótulo de treino**).
- Limites de validade: apenas 1 contrato positivo, identidade nos dois lados do fold, um dia de negativos e 23 dias positivos, exemplos não representativos, ausência de teste por protocolo externo.
- **Não adicionar mais coletas/modelos antes da entrega de 20/11**. Caso EXP-05 concluído, incluir somente depois de auditoria independente das duas planilhas.

## Estado

- [x] Execução real dos 12 arranjos.
- [x] 60 registros de métricas por fold e 12 registros de resumo.
- [x] Composição da matriz e overlaps auditados.
- [x] Todos os hashes conferidos.
- [ ] Transpor resultados à seção do manuscrito formatada SBC e validar o limite 4–6 páginas.
- [ ] Adicionar guia didático à biblioteca de estudo NotebookLM.
