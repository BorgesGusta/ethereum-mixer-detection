# Detecção de mixers na Ethereum — artigo LaTeX e laboratório integrado

**Data:** 20/11/2026. **Ramo de origem:** `docs/consolidacao-oficial-2026-11-17`.

## 1. Artigo (fonte exclusiva `.tex`)

- `main.tex`: manuscrito integral, editável, **duas colunas** por padrão. Use no Overleaf como arquivo principal.
- `figures/01_fluxo_metodologia.tex` a `figures/07_triagem.tex`: **sete figuras vetoriais TikZ/PGFPlots** incluídas automaticamente por `\input`; não dependem de PNG ou de fontes externas. A figura `08_dispersao_alertas_opcional.tex` é suplementar e não é inserida automaticamente para preservar o limite de páginas.
- Compile com `pdfLaTeX` (requer pacotes padrão `tikz`, `pgfplots`, `babel`, `geometry`, `times`). O artigo foi **compilado localmente com 4 páginas em modo duas colunas**, com verificação visual. Não foi entregue um PDF como artefato principal.
- `\SBCfalse` no topo habilita as **duas colunas**; `\SBCtrue` tenta o modelo tradicional **SBC de coluna única** (requer `sbc-template.sty` para máxima fidelidade; na falta, aplica margens aproximadas). **O modelo SBC tradicional é de coluna única, 12 pt, A4**. Duas colunas NÃO devem ser chamadas de “SBC oficial” sem autorização do professor.
- Há campos de autoria/afiliação a completar. A página de rosto é deliberadamente simples. **Não garantir 4–6 páginas no modo SBC de coluna única sem verificar a compilação real**.

### Figuras — o que é medido e o que é conceito

| Arquivo | Visual | Evidência e cuidado |
|---|---|---|
| 01 | Pipeline de metodologia | Diagrama conceitual próprio, inspirado na ideia do pipeline de Leale e Sendin; não é experimento de inferência |
| 02 | Barras 63 × 9 | Reprodução de 29/10/2020, não precisão |
| 03 | Curva de sensibilidade `min_tx` | EXP-01J: 49, 14, 9, 7; não F1 |
| 04 | Mapa F1 de 12 arranjos | EXP-07: F1 **interno**, 5 folds por linhas, só 1 contrato positivo |
| 05 | Contrato positivo repetido | Diagrama **esquemático** da limitação dos folds, não matriz de confusão |
| 06 | Scores dos 9 alertas de 2026 | 3 Tornado de referência + 6 **indeterminados**, não resultados de detecção de ilícito |
| 07 | Fluxo defensivo EXP-08 | Implementação demonstrativa **offline**, sem integração SIEM/Blockchain |
| 08 | Dispersão de atributos (opcional) | Dados dos nove alertas, taxa de chamadas média em escala log; **não é grafo on-chain** |

As figuras seguem uma **linguagem visual científica** comparável aos artigos de referência: esquema de fluxo (Leale e Sendin SBSeg 2025), arquitetura em estágios (GNN-based Detection ... 2025) e contextualização de casos (MixGuard). **Nenhuma figura, imagem ou métrica foi copiada dos artigos de referência**. Não foi treinada CNN/GNN neste projeto.

## 2. Apenas dois notebooks para apresentação

| Arquivo | O que faz | O que NÃO faz |
|---|---|---|
| `notebooks/01_LAB_INTEGRADO_DETECCAO_E_GRAFICOS.ipynb` | Busca arquivos oficiais do Drive, verifica 5 hashes EXP-07, reproduz gráficos de barras, linha, heatmap, boxplots, PCA, escores dos alertas, dispersão e matriz de confusão agregada, salva PNGs de alta qualidade | Não refaz os vários GB de coleta bruta nem demonstra generalização por contrato novo |
| `notebooks/02_DEMONSTRACAO_SEGURANCA_EXP08.ipynb` | Inclui o código real `triage.py` e `test_triage.py`, roda os quatro testes, produz log JSONL com SHA-256, verifica adulteração e exibe fluxo conceitual | Não consulta a blockchain, não integra SIEM e não bloqueia contas |

**Executar no Google Colab**: abrir o notebook, escolher “Abrir com Google Colaboratory”, `Ambiente de execução → Executar tudo`. O primeiro notebook pede permissão de leitura do Drive e coleta resultados por IDs já conhecidos; por padrão não envia novos arquivos ao Drive. Para publicar os PNGs, usar a célula `EXPORTAR_PARA_DRIVE=True`.

### Reprodutibilidade completa e versões históricas

**Os notebooks antigos NÃO foram apagados, mesclados de forma irreversível nem alterados.** Todos os experimentos EXP-01..EXP-08 e seus registros continuam nos caminhos originais. O **EXP-07 v2** é o registro autoritativo do treinamento 12 × 5; os novos notebooks consolidam a **consulta e demonstração dos resultados**, não substituem a coleta e os treinamentos originais.

- Coleta e inferência base 2020/março 2025: notebooks históricos `01` a `04` da pasta original.
- EXP-02 (avaliação janeiro 2026): scripts e relatórios experimentais originais.
- EXP-03, 03B e 03C: investigação de controles e limitação do RPC histórico.
- EXP-04: integridade de hashes e triagem de evidências.
- EXP-05: revisão cega independente, sem expor decisões dos revisores neste laboratório.
- EXP-06A/B/C: implantação e retiradas históricas do Privacy Pools v1, sem novo rótulo de mixer confirmado.
- EXP-07 v2: matriz real, cinco folds, 12 modelos/configurações, com separação exploratória por linhas.
- EXP-08: inventário de candidatos sem rótulo e protótipo defensivo offline.

A versão viva, os resultados auditados e as ressalvas ficam em `docs/manuscrito/CADERNO_CIENTIFICO_VIVO.md` e `docs/experiments/` no ramo do projeto.

## 3. Estudos e apresentação

1. **2 min**: mostrar Fig. 1 e explicar o pipeline.
2. **2 min**: mostrar 63×9, sensibilidade e observação de 3/3 pools conhecidos.
3. **2 min**: abrir heatmap do EXP-07, enfatizar 1 único contrato positivo e vazamento entre folds.
4. **2–3 min**: notebook 02, rodar testes e adulteração intencional em cópia do log.
5. **1 min**: limites, propostas de negativos difíceis e novos protocolos, sem métricas inventadas.

**Notas de rigor:** nenhum dos seis contratos associados aos alertas de 2026 foi validado como falso positivo; Privacy Pools não foi incluído como novo positivo; os gráficos PCA e dos escores são ilustrativos, não provas de comportamento ilícito. A capacidade de generalização a novos protocolos permanece não demonstrada.
