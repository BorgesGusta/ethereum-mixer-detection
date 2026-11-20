# EXP-07 v2 — Comparação exploratória de classificadores e ablação de características

**Preparado em 19/11/2026, em face do prazo de entrega de 20/11/2026. STATUS: notebook publicado; execução com matriz real PENDENTE.** Não confundir testes sintéticos locais com resultados científicos.

## Hipótese e escopo

Verificar descritivamente se, sob **a mesma matriz de exemplos rotulados** e os mesmos folds, quatro classificadores apresentam desempenho interno diferente ao usar três conjuntos de características. A análise **não demonstra generalização para protocolos Ethereum novos**, especialmente se a classe positiva estiver concentrada em um só contrato.

### Modelos pré-fixados

1. Random Forest, `n_estimators=100`, `max_depth=5`, `random_state=20261119` (reentrenado, não o arquivo joblib original).
2. Regressão Logística com `class_weight=balanced`, normalização `StandardScaler` treinada apenas no fold de treinamento.
3. Árvore de Decisão `max_depth=5`.
4. Gradient Boosting do scikit-learn com parâmetros default e semente 20261119.

Todos usam `SimpleImputer(strategy='median')` **dentro** do Pipeline, por fold; o limiar de classe é o padrão do estimador (não ajustado posteriormente). Sem pesquisa de hiperparâmetros.

### Ablação pré-fixada

- `A_original_5`: `n_tx`, `value_entropy`, `fee_entropy`, `internal_value_entropy`, `call_count_mean`.
- `B_sem_volume_4`: quatro originais exceto `n_tx`.
- `C_entropias_3`: apenas as três entropias.

Essas 12 combinações usam *a mesma matriz* `features_treino.parquet` ID Drive `1jUHAq6H9FKSgptv4nsCoOmFILH4Py_2S`; **nenhuma característica nova é extraída** e não há rótulo adicional.

## Procedimento e controle de validade

1. Validar colunas, endereço, data, classes, duplicatas, faltantes e contagem de contratos por classe. Rótulo conflitante para mesmo contrato → interromper.
2. Se ≥2 contratos em **cada classe** e dois folds com ambas as classes: `StratifiedGroupKFold` com agrupamento por `recipient`.
3. Se não houver agrupamento viável: **StratifiedKFold por linhas somente como validação interna exploratória** com aviso explícito de possível vazamento de identidade e tempo. **Não apresentar seus F1/precision/recall como teste em contratos inéditos**.
4. Mesmas divisões para 12 configurações, mesma semente; salvar os índices de cada fold e overlap de contratos.
5. Computar `tp,tn,fp,fn,precision,recall,f1,balanced_accuracy` por fold; médias/desvios no resumo. Sem seleção de “melhor” a posteriori como evidência confirmatória.
6. Arquivos de auditoria: `auditoria_matriz.json`, `folds_congelados.json`, `metricas_12_combinacoes_por_fold.csv`, `resumo_12_combinacoes.csv`, `manifesto_exp07.json` (hash SHA-256 dos arquivos anteriores e da matriz), matriz original preservada na pasta de resultados; uploads na pasta oficial `results`.

Nenhum dado de 2020 ou 2026 é tratado como ground truth externo. Os alertas da revisão independente EXP-05 não são rótulos de treino ou teste.

## Recursos versionados

- [Notebook EXP-07 v2 no Drive](https://drive.google.com/file/d/1nKI1sM5pbY-UOAI6nxraTTSzkNFY8MHW/view?usp=drivesdk), pasta de notebooks ativos.
- [Notebook EXP-07 v2 no GitHub](../../notebooks/21_EXP-07_v2_comparacao_e_ablacao.ipynb), commit `33e6cc5296b64ff8ff8293b2ebb28136f634dc61`.
- Versão v1 do notebook preservada `notebooks/21_EXP-07_comparacao_quatro_classificadores.ipynb` (sem ablação).
- **Validação local:** as células Python compilam; execução simulada com 36 linhas sintéticas e **um contrato positivo** percorreu 12 combinações e ativou corretamente modo exploratório por linhas. **Este teste NÃO é análise do dataset real nem produz métricas publicáveis.** A leitura local de Parquet foi impedida por ausência de `pyarrow`; notebook instala a dependência no Colab.

## Uso acadêmico e decisão de publicação

- Artigo: seção curta “Comparação exploratória entre classificadores e ablação de atributos”, **somente após execução e auditoria dos arquivos reais**.
- Se matrizes revelarem único contrato positivo: apresentar a tabela de 12 combinações explicitamente como diagnóstico interno, sem qualquer afirmação de capacidade de reconhecer protocolos diferentes. Se resultados forem inconsistentes/insuficientes, dar prioridade a reprodução e auditoria on-chain já validadas.
- Não readequar os grupos de atributos ou classificadores após inspecionar os resultados sem registrar novo experimento.
- Entrega: 20/11/2026; **não aguardar novos datasets ou revisão EXP-05 para completar artigo**.
