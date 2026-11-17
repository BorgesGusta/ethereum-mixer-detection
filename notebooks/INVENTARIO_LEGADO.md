# Inventário de notebooks legados (16/11/2026)

**Objetivo:** permitir rastrear a origem das implementações enquanto o trabalho ativo é consolidado em [quatro notebooks canônicos](../docs/06_ARQUITETURA_ENXUTA.md).

**Atenção:** estes são **arquivos arquivados**, não necessariamente versões finais executáveis. Preservamos células de saída e erros históricos, sem corrigir o legado. Apenas o código das versões consolidadas será submetido a testes de paridade.

| Notebook arquivado em `legacy/` | Origem no Drive | Estado / função |
|---|---|---|
| [01_teste_20201029.ipynb](legacy/01_teste_20201029.ipynb) | [Abrir](https://colab.research.google.com/drive/1ZzP24uCaRu2aKIZs4F1b3uSa1AJg6Rfk) | Coleta/reprodução de 2020 |
| [02_dados_marco_2025.ipynb](legacy/02_dados_marco_2025.ipynb) | [Abrir](https://colab.research.google.com/drive/18YHPEhp3e0r0uYdnodcD5gvXjl3oCLFp) | Dados positivos de 2025 |
| [03_negativos_features_treino.ipynb](legacy/03_negativos_features_treino.ipynb) | [Abrir](https://colab.research.google.com/drive/1GC5E-YLh4sp6wIDIhCVyhexzB0yeVVwi) | Construção do treino, versão anterior |
| [03_negativos_features_treino_v2.ipynb](legacy/03_negativos_features_treino_v2.ipynb) | [Abrir](https://colab.research.google.com/drive/10PCr9IrfKhb4E8oajzzsW6tJmNZqqW_A) | Variante v2; comparação pendente |
| [04_inferencia_analise.ipynb](legacy/04_inferencia_analise.ipynb) | [Abrir](https://colab.research.google.com/drive/1PqH_k-RVot4WM0Gi8ENjdztaX9TN3Vzk) | Inferência |
| [05_experimentos_ablacao_mixers.ipynb](legacy/05_experimentos_ablacao_mixers.ipynb) | [Abrir](https://drive.google.com/file/d/1zp5HwI7mWCo-ZSYO5s6F2ETpXS5M5zXe/view) | Ablação |
| [07b_teste_2026_validacao_2020.ipynb](legacy/07b_teste_2026_validacao_2020.ipynb) | [Abrir](https://colab.research.google.com/drive/1aFznNBj8eSg4JeyjvRLQSOEp-zgpAj0C) | Teste 2026 |
| [08_analise_features_candidatos_2026 (2).ipynb](legacy/08_analise_features_candidatos_2026%20(2).ipynb) | [Abrir](https://drive.google.com/file/d/1Qp4iKPIFW0zaLrrVlyUbLAqt08SdIPL5/view) | Análise exploratória de alertas |
| [10_benchmark_classificadores_mixers.ipynb](legacy/10_benchmark_classificadores_mixers.ipynb) | [Abrir](https://drive.google.com/file/d/176SN-v28fdn1bQa3E53jAloDG-DHJV7w/view) | Benchmark, variante inicial |
| [10_benchmark_classificadores_mixers_REFATORADO.ipynb](legacy/10_benchmark_classificadores_mixers_REFATORADO.ipynb) | [Abrir](https://colab.research.google.com/drive/1ycwlFxHDlLfTiWGidkQ48lprJAkSxIrc) | Benchmark, variante refatorada |
| [11_comparacao_externa_ensemble_mixers.ipynb](legacy/11_comparacao_externa_ensemble_mixers.ipynb) | [Abrir](https://colab.research.google.com/drive/1JSas45XSQhECI_oLz3O4WWECWt9GRA_k) | RF/ET/voting em períodos externos |
| [12_00_auditoria_inventario.ipynb](legacy/12_00_auditoria_inventario.ipynb) | [Abrir](https://colab.research.google.com/drive/1mwWUghRrysMQG-LkC_-KQRPqNpi-EA1p) | Auditoria do inventário |
| [12_01_diagnostico_viabilidade_treino_2020.ipynb](legacy/12_01_diagnostico_viabilidade_treino_2020.ipynb) | [Abrir](https://colab.research.google.com/drive/1aUqjwIEEH5xXIPPjh2QzrJ-fqQwVsl2E) | Viabilidade do treino histórico |

**Não incluídos ainda na pasta legacy:** os notebooks 12.02A e 12.02B, que foram entregues fora da pasta principal de notebooks e cujos resultados estão no Drive. Os notebooks 06 e 09 não foram localizados como arquivos independentes na pasta de notebooks auditada. O notebook utilitário 99_sync_github permanece no Drive e não é parte dos quatro canônicos.

**Critério de fechamento da Issue #1:** verificar as variantes, vincular suas saídas com hashes e identificar versões executadas, além da simples importação inicial.
