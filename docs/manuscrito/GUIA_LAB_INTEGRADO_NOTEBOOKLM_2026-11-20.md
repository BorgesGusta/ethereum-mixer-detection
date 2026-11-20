# Estudo e demonstração: artigo LaTeX, gráficos e dois notebooks

**Data de consolidação:** 20/11/2026. Este material é um **guia didático**, não novo experimento ou novo ground truth. Ramo científico `docs/consolidacao-oficial-2026-11-17`.

## 1. Como navegar com poucos notebooks

**Notebook integrado 1 — Laboratório de detecção e gráficos:** https://drive.google.com/file/d/1qNKrre-8aa3aaJCFrV70LEAMUbQa3R7e/view

Importa artefatos oficiais EXP-01J/EXP-02A/EXP-07, valida cinco hashes SHA-256, desenha comparativo 63×9 e sensibilidade 49/14/9/7, heatmap dos 12 arranjos, boxplots das features, PCA exploratória, ranking de escores dos nove alertas de 2026, dispersão dos atributos e confusão interna do RF. Os boxplots/PCA usam matriz de treino original: 23 linhas positivas = 1 contrato, 100 linhas negativas = 100 contratos. Isso **não valida generalização a protocolos novos**. A visualização por PCA não representa transações em grafo nem é modelo GNN. As seis observações adicionais de 2026 são indeterminadas, não erros confirmados.

**Notebook integrado 2 — Demonstração defensiva:** https://drive.google.com/file/d/1Arsen3rjj2QYlxYc_X8jGXnFYMrsselV/view

Escreve script offline `triage.py`, roda quatro testes, registra dois exemplos em JSONL SHA-256 encadeado, verifica integridade e demonstra adulteração em cópia. Não consulta a blockchain automaticamente, não realiza bloqueios e não está conectado a SIEM. O hash terminal precisa ser preservado fora do registro para detectar reescrita de trilha.

Os notebooks antigos **não foram apagados**: EXP-01 a EXP-08 seguem rastreáveis e seus relatórios no GitHub são referência para reproduzir coleta, rotulagem, scripts e inferência. O notebook 1 é um **painel integrado de visualização**, não a execução de todas as coletas e protocolos originais.

## 2. Artigo LaTeX em duas colunas

**Fonte `main.tex`**: https://drive.google.com/file/d/1Be6eBVrUETvkQSZ_7DFXXQJwVkXqYEDA/view

**ZIP Overleaf com código e figuras `figures/*.tex`:** https://drive.google.com/file/d/1befPtgAnlzsXdEdkse6bv5Bpt056pboS/view

**GitHub — fonte e sete figuras vetoriais:** https://github.com/BorgesGusta/ethereum-mixer-detection/tree/docs/consolidacao-oficial-2026-11-17/docs/manuscrito/latex_2col

O layout padrão desta versão usa **duas colunas, 10 pt**, compacto para estudo e entrega se permitido. **O modelo SBC tradicional de conferências tem uma coluna e 12 pt**: se exigido, mudar `\SBCfalse` para `\SBCtrue` e conferir compilação e paginação oficial. O artigo em duas colunas compilou localmente com **4 páginas**, mas não foi validado com a classe SBC. Autores e afiliação ainda devem ser personalizados.

As sete figuras incluídas são: pipeline científico; alertas 63×9; sensibilidade `min_tx`; heatmap F1 interno 4×3; repetição do mesmo contrato positivo nos folds; escores dos nove alertas de 2026; triagem offline EXP-08. A oitava figura (dispersão dos nove alertas) está pronta em `.tex` como opção. Diagramas de fluxo são esquemáticos; não há prova de caminho de recursos por grafo on-chain nem aprendizado profundo testado.

## 3. Explicação oral resumida

**Reprodução:** refizemos referência de 2020, com 9 alertas versus 63, recuperando os três pools conhecidos; não sabemos a causa única da discrepância.

**Método:** diferentes limites de transações mudam elegibilidade e quantidade de alertas; auditoria de contratos, logs, traces e revisão humana são necessárias para interpretar casos ambíguos.

**Modelos:** 4 algoritmos × 3 grupos de features, F1 médio interno do RF 0,9778 nos três grupos; a validação por linhas compartilha 1 contrato positivo e não prova generalização.

**Segurança:** o protótipo não bloqueia ninguém. Ele organiza evidências fornecidas, exige revisão e cria histórico com verificação local de SHA-256; quatro testes passaram.

**Próximos estudos:** confirmar positivos de protocolos independentes e negativos difíceis com revisão independente, construir split por contrato/família e só então testar generalização externa e arquiteturas como MLP/GNN.

## 4. Condições para a entrega

Verificar autoria, referências, formato aprovado pelo professor e leitura dos gráficos; revisar a apresentação e executar os dois notebooks no Colab. O primeiro notebook foi **validado sintaticamente e seis dos gráficos foram executados localmente com os CSVs**, mas o carregamento de Parquet e sua execução integral no Colab ainda dependem da autorização da conta do grupo. O segundo está baseado em scripts com quatro testes locais aprovados. Não declarar que o notebook integrado inteiro já rodou no Colab antes de fazê-lo.
