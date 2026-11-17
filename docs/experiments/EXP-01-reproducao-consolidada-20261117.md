# EXP-01 — Reprodução consolidada verificada em 17/11/2026

**Estado:** execução concluída; paridade parcial com o legado confirmada. **Categoria:** reprodução exploratória, não teste confirmatório independente.

## Evidências

- [Pasta da execução no Drive próprio](https://drive.google.com/drive/folders/1Cykyn2M8BGj5mDxfnXHkyv7x0cBrBkWe)
- [Manifesto](https://drive.google.com/file/d/1hSPj9SiG-iRo-ENEXniBuSVkVEyI4Yxx/view)
- [CV por fold](https://drive.google.com/file/d/1_fXFj9Glynv3OFFCSfXPDxwA6UAFXg2Q/view)
- [Resumo 2020](https://drive.google.com/file/d/1giUxsAxWG-YFuTX6UuXL4QvN4NXu6aMB/view)
- Notebook: [01_reproducao.ipynb](../../notebooks/01_reproducao.ipynb)
- Módulos: `src/ethmix/features.py` e `src/ethmix/models.py`. Manifesto registra SHA-256 individuais e hashes dos datasets.

## Metodologia efetivamente aplicada

- Treino legado com 123 janelas contrato-dia (23 positivas do pool Tornado 10 ETH em março/2025, 100 negativas selecionadas).
- RandomForest de 100 árvores, profundidade máxima 5, `class_weight='balanced'`, seed 42 e oversampling nos folds de treino.
- Teste em dados já previamente examinados de 29/10/2020; somente janelas com `n_tx >= 10`; limiares exploratórios 0,50 e 0,85.
- Datasets e módulos carregados da pasta própria no Drive por IDs com checagem de hashes.

## Resultados confirmados pelos CSVs da execução

| Etapa | Resultado |
|---|---|
| CV 5 folds: precision média | 1,000 |
| CV 5 folds: recall médio | 0,960 |
| CV 5 folds: F1 médio | 0,9777777778 |
| Limiar >0,50: endereços sinalizados | 9 |
| Limiar >0,50: pools de referência recuperados | 3 de 3 |
| Limiar >0,50: alertas adicionais sem rótulo verificado | 6 |
| Limiar >0,85: endereços sinalizados | 7 |
| Limiar >0,85: pools de referência recuperados | 3 de 3 |
| Limiar >0,85: alertas adicionais sem rótulo verificado | 4 |

**Paridade observada:** 5 folds correspondem linha a linha às métricas salvas em `cv_metricas.csv` no acervo legado; no limiar de 0,50 a saída agregada corresponde ao `comparacao_artigo_20201029.csv` do legado (9 alertas, três pools recuperados).

**Não confirmado nesta execução:** igualdade dos IDs dos nove alertas com a lista legada, reconstrução integral das features desde dumps brutos, paridade do modelo salvo `.joblib`, validade externa dos rótulos negativos, equivalência ao protocolo completo do artigo publicado e generalização entre contratos.

## Conclusão científica permitida

A refatoração preservou as métricas de CV por linha e os totais agregados de inferência histórica no limiar de 0,50. Isso é **paridade parcial do pipeline consolidado**, não prova da capacidade de generalização. A precisão de CV de 100% não deve ser extrapolada: exemplos positivos provêm de um único contrato e a validação divide janelas de modo estratificado, podendo compartilhar o mesmo contrato entre treino e validação. Alertas fora dos pools conhecidos não devem ser classificados como falsos positivos sem evidência externa.

## Próximo passo

Priorizar `04_auditoria.ipynb` para testes automatizados de features, hash/Router, integridade e comparação exata dos endereços sinalizados. Depois construir protocolo histórico 2020–2026 com conjuntos independentes e coleta harmonizada.
