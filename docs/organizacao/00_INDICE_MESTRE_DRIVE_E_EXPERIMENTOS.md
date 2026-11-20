# 00 — Índice mestre da pesquisa: detecção de mixers na Ethereum

**Atualizado em 20/11/2026.** Esta é a porta de entrada para navegar os arquivos existentes. Não substitui os dados originais, não move os arquivos do Drive, não altera IDs/compartilhamentos e não incorpora fichas de revisão não finalizadas.

## 01 — Entrega e manuscrito

- [Artigo LaTeX (`main.tex`) no GitHub — fonte versionada](https://github.com/BorgesGusta/ethereum-mixer-detection/blob/docs/consolidacao-oficial-2026-11-17/docs/manuscrito/latex_2col/main.tex). **Conferir qual versão está atualmente sendo editada no Overleaf** antes de considerar esta a versão de entrega.
- [Pasta de fontes, PNGs e pacotes LaTeX no Drive](https://drive.google.com/drive/folders/1QV7SfiXA_56Z8zT6Pt3krL6RE6b0K8Mj).
- [Caderno científico vivo](https://github.com/BorgesGusta/ethereum-mixer-detection/blob/docs/consolidacao-oficial-2026-11-17/docs/manuscrito/CADERNO_CIENTIFICO_VIVO.md): cronologia, resultados e limitações.
- **Atenção:** em duas colunas, o manuscrito é uma adaptação; validar exigência exata de template antes da entrega.

## 02 — Base de dados e scripts

- [data/ — pasta mãe](https://drive.google.com/drive/folders/1gz191DH78K2NzIKbaTQ-IlCQUwUvPTwf) e suas pastas [raw](https://drive.google.com/drive/folders/1Nicyoz31MP_cahehl1XU2bBRCzgEGv3u), [interim](https://drive.google.com/drive/folders/1HF1ME_jEO_Fm-OuVVZ4eJ6matdT_WVY_), [processed](https://drive.google.com/drive/folders/18IeCuFcx5ka0OoJAxjJt3gey7JVX71ht).
- [src/ — scripts de coleta e auditoria](https://drive.google.com/drive/folders/1EtUuKDC85z3NWTLzJIcrIwW8__sUp7SN).
- Referências canônicas devem usar ID de arquivo + hash SHA-256; não usar apenas nome em pastas antigas.

## 03 — Notebooks para estudo e demonstração

- [notebooks/00_ATIVOS](https://drive.google.com/drive/folders/1VNdVfqmHt-csEcbh9M9SLaV_IgvpGwJ4).
- **Entrada principal 01:** [Laboratório integrado: dados, resultados e figuras](https://drive.google.com/file/d/1qNKrre-8aa3aaJCFrV70LEAMUbQa3R7e/view).
- **Entrada principal 02:** [Demonstração EXP-08: triagem e SHA-256](https://drive.google.com/file/d/1Arsen3rjj2QYlxYc_X8jGXnFYMrsselV/view).
- Notebooks numerados 13–21: **originais da coleta e dos testes**, necessários à rastreabilidade; não deletar ou renomear sem revisão das referências.
- [notebooks/99_LEGADO](https://drive.google.com/drive/folders/1GxbRUt4ZKQufiG_L8IsoBDYC2miZVY3r): 16 notebooks antigos. Preservar com rótulo de histórico.

## 04 — Resultados auditados e experimentos

- [results/ — pasta mãe](https://drive.google.com/drive/folders/1iZKAeZPEb6JOlH8KfqsR6-wqI1ygmojI). Os nomes atuais de algumas subpastas refletem a data/hora das execuções; a indexação científica deve ser feita pelo **ID do EXP**.
- EXP-01 / 01J — reprodução, comparação 63 × 9 e sensibilidade: [pasta EXP-01J](https://drive.google.com/drive/folders/1AFO6k3ShxdsZABU1OoFBXez7Dd8FngOx). Quatro pontos: `min_tx=1,5,10,20`.
- EXP-02A — alertas e auditoria documental de janeiro de 2026: [pasta](https://drive.google.com/drive/folders/15Do7dwtJgd4T7pkmXDptDfMKWn2NHkIE).
- EXP-02B — amostra de transações: [pasta](https://drive.google.com/drive/folders/1rV5mJ0rkINLML5aFUFnl0s7g1ybwrwOb).
- EXP-02C — logs/ABIs históricos parciais: [pasta](https://drive.google.com/drive/folders/13348CzioFtdQWc6snAEPQLroVBiAO_6T).
- EXP-03 / 03B / 03C — controles e limitações de RPC histórico: [EXP-03](https://drive.google.com/drive/folders/1SAdkZVyXcmYs02AYNZACE7h5DEDzPdzJ), [EXP-03B](https://drive.google.com/drive/folders/1WZ3tbWDY75Jmt_SBE8KX2EDbiUJzRKwu); 03C ficou diagnóstico opcional, não avaliação confirmatória.
- EXP-04 — triagem documental e integridade: [pasta](https://drive.google.com/drive/folders/1drM-F9LfePDFSYrGYzlNmySfy0dWQK_K).
- EXP-05 — **revisão independente pendente de A**: [pasta dos revisores](https://drive.google.com/drive/folders/11Ph9gtKlyR2q3jyLfehcOPlNHf2OBU38) e [protocolo](https://drive.google.com/file/d/1rN4LtgLXkzrybFTxL50mSRJeigcrMlQo/view). **Não consultar respostas B antes de finalizar A.** Arquivos internos de coordenação são separados, não incluídos neste índice de trabalho de revisores.
- EXP-06A / B / C — Privacy Pools v1: [EXP-06A](https://drive.google.com/drive/folders/1K83QFXRH_pGd5muiMNHhUxjNYdKwxt_l), [EXP-06B](https://drive.google.com/drive/folders/1-_iI6xOScAy0-a33Y2Rt94BdDFfBymyq), [EXP-06C](https://drive.google.com/drive/folders/1O9mAvAPx4HOER9Cn-GduUSCmriISVAnC). São evidências funcionais parciais, não rotulagem de novo protocolo para ML.
- EXP-07 v2 — 4 classificadores × 3 conjuntos: [resultados oficiais](https://drive.google.com/drive/folders/1iekmCwwXYnxzYNp7jJ6Ye5S4O56UN0b6). 123 observações, somente 1 contrato positivo; F1 **interno exploratório**.
- EXP-08 — candidatos a classes e protótipo de segurança: [inventário CSV](https://drive.google.com/file/d/1z2Oh1t9-OsbkqDxbXi3YXRVCoO3Bgsh5/view), [código do protótipo](https://drive.google.com/file/d/1XL6DHgfbC2Jbf0LPt88hSkPaar0RzoYz/view) e [testes](https://drive.google.com/file/d/1Tu7pIO1RlH8kbkOpSTB8jRduwJQAXR-t/view). **Sem novos rótulos confirmados e sem integração automática RPC/SIEM.**

## 05 — Revisão independente EXP-05: sequência correta

1. [Revisor A — Gustavo: preencher somente a ficha A](https://docs.google.com/spreadsheets/d/1zmaukMcbQSTemQL9eW8Oe9z68-9UF4Pedn4wR6jG2Jc/edit). Na conferência de 20/11, as **nove linhas ainda não tinham respostas**.
2. Revisor B — Bruno: o usuário informa que concluiu; **não consultar respostas até a ficha A ser congelada**. Há mais de uma cópia/versão B na pasta, e o adjudicador deverá identificar qual é a final.
3. Congelar as duas fichas, registrar data/hash/cópia imutável.
4. Comparar casos R001–R009 por decisão e evidências, registrar concordância descritiva.
5. Adjudicar divergências, preservar `indeterminado` quando faltarem evidências.
6. Só então atualizar relatório EXP-05 e considerar menção de resultados descritivos no artigo. **Não calcular F1 do classificador com esses nove alertas selecionados pelo próprio modelo**.

## 06 — Biblioteca exclusiva para NotebookLM

- [Biblioteca de Estudo e Pesquisa — NotebookLM](https://drive.google.com/drive/folders/1gnpcC5Y9yAZankjGSk5hIsW-nBXFmMYs): pastas já numeradas de `00_LEIA_PRIMEIRO` a `07_MANUSCRITO_E_SUBMISSAO`.
- O Drive contém **materiais preparados para servir como fontes do NotebookLM**, mas não há comprovação de que todos estejam importados no aplicativo. Não misturar fichas de revisão cega com material de estudo antes do fechamento.

## 90 — Estrutura histórica (não mexer sem mapa de dependências)

Na raiz coexistem antigos diretórios (`00_artigo`, `01_dados_brutos`, `02_dados_processados`, `03_features`, `04_modelos`, `05_resultados`, `99_notebooks`) e a organização atual (`data`, `notebooks`, `results`, `docs`, `src`, `temporal_2020_2026`). **Não deduplicar por nome, não apagar Parquet, não mover pastas usadas por notebook** antes de verificar ligações, scripts, IDs, SHA e versões.

## Regras de organização

- Prefixar novos artefatos com **`EXP-XX__tipo__data`**: por exemplo `EXP-05__revisao_A__2026-11-20`, `EXP-07__metricas__2026-11-20`.
- Resultados brutos, código, interpretação científica, figuras e materiais didáticos têm funções diferentes; manter o original e ligar pelo índice.
- Usar **dois notebooks de apresentação**; os experimentais originais continuam preservados.
- Nunca incluir o índice privado do coordenador no pacote dos revisores ou no material de estudo.
- Toda decisão de reorganização física deve ser acompanhada por tabela antes/depois com ID permanente, origem, destino, hash quando aplicável, autor e data.

### Atualização EXP-05 — confronto de pareceres (20/11/2026)

Após autorização, confronto documental realizado: 5/9 classificações iguais, quatro divergências (R001, R002, R004, R005); [relatório preliminar](../experiments/EXP-05-comparacao-A-B-preliminar-2026-11-20.md); [matriz CSV](../../data/exp05/EXP-05_matriz_pareamento_A_B_2026-11-20.csv). Cópias A e B e o relatório operacional estão em pasta restrita de coordenação, sem alteração das fichas originais. Ficha A com apoio de IA ainda não aprovada caso a caso. **Adjudicação pendente e sem novos indicadores do detector.**

### EXP-05 — parecer técnico das quatro divergências (20/11/2026)

[R001/R002/R004/R005 — parecer com evidências e links](../experiments/EXP-05-adjudicacao-tecnica-preliminar-2026-11-20.md), [CSV com 12 transações e contagem dos 99 logs](../../data/exp05/EXP-05_evidencias_das_quatro_divergencias.csv) e [pasta Drive da documentação pós-confronto](https://drive.google.com/drive/folders/19CorxL0x6CmPSeWK0HpIS7f51-DVHR4J). Todos exibem comportamento compatível com ponte/relayer/roteamento e, portanto, são **candidatos a negativos**, não casos negativos formalmente adjudicados. A aprovação humana pós-confronto permanece pendente. Fichas A e B originais preservadas.
