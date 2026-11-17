# EXP-01E — Auditoria histórica de features de três contratos (29/10/2020)

**Execução registrada:** 17/11/2026, Colab notebook canônico `01_reproducao.ipynb`, etapa 10.

**Pasta de evidências:** https://drive.google.com/drive/folders/18bBPWlILDm-nvd_rCAP3oikzsnFyBHjq

## Artefatos verificados

- [comparacao_features_3.csv](https://drive.google.com/file/d/1dI87wickD3v0xyP_d61CStqsLR1ADtrl/view)
- [resumo_transacoes_3.csv](https://drive.google.com/file/d/1NWnaZQbB95oeKx5TaZ5h5hoDVK1dip1j/view)
- [delta_features_3.png](https://drive.google.com/file/d/1KrIXDN0cEHYzHrinD9r8rZAs-UyVRvjC/view)
- [manifesto.json](https://drive.google.com/file/d/1zmLOPsa0tUoqy7zYB8H1NxsgLEFWo5om/view)

Entradas: `data/interim/test_20201029.parquet`, cópia no Drive (file id `1Ei7sCgYdFfX-AjrK6uazOvbrf28d1Px7`), e referência `data/processed/features_teste_20201029.parquet` (file id `1g22eCccxC4v_S2RmxPhFZyzfF1ARuzPk`). Sem reprocessamento independente do dump bruto.

## Resultado observado

| Endereço | Identificação documental | n_tx | Remetentes distintos | call_count_mean | value_entropy | fee_entropy | internal_value_entropy | Paridade |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 0x5e60fcca904753a31f9df7d7f6b7856b6ec27aa9 | AdminUpgradeabilityProxy | 53 | 27 | 40.56603773584906 | 0.5369622967963086 | 5.7279204545632 | 0.802152982320766 | sim |
| 0x98f1858c9740b9c5f2cd8abea67948873d38dc39 | SmartEther / SMARTE | 10 | 10 | 25.4 | 1.0 | 3.3219280948873626 | 1.0 | sim |
| 0xe113d58a4cb4dbac8a0da608ed7232785c1f2c18 | DSProxy | 10 | 1 | 40.6 | 0.7219280948873623 | 3.3219280948873626 | 1.5709505944546687 | sim |

Todas as **12 features** (3 endereços × 4) foram recomputadas com **delta absoluto = 0**, assim como `n_tx` nos três casos. `paridade_numerica=True` para os três.

## Interpretação e limites

- A rotina `preparar()/calcular_features()` aplicada ao intermediário do próprio projeto reproduz fielmente as features do parquet processado nesses três casos.
- Trata-se de **paridade interna** com a mesma cadeia de dados e metodologia. **Não é** uma auditoria independente de completude das transações na Ethereum e tampouco valida o número de endereços sinalizados pelos autores (63 versus nossos 9).
- Os três endereços são contratos segundo metadados Blockscout; funções econômicas das operações em 2020 não foram demonstradas.
- Em especial, o `AdminUpgradeabilityProxy` tinha implementação inicial descrita no construtor distinta da implementação atual segundo relatório Blockscout anterior. Falta recuperar os eventos históricos `Upgraded` para determinar quando ocorreram as mudanças.
- `DSProxy` teve dez transações de apenas um remetente; `SmartEther`, dez transações de dez remetentes. As features existentes não incluem diretamente essa diversidade de remetentes, o que é hipótese para estudo futuro, **sem acrescentá-la silenciosamente à reprodução do artigo**.

## Próximos passos

1. Auditar identidade econômica e histórico de eventos on-chain na janela de 29/10/2020, inclusive impl. do proxy por bloco.
2. Fazer rastreamento de proveniência desde o `raw`, não apenas comparar `interim` vs `processed`.
3. Diagnosticar 63 vs 9 com amostras negativas, filtros, engenharia das features, regras de inferência e resposta dos autores quando houver.
4. Só depois iniciar experimentos confirmatórios temporais em holdout por período/contrato.
