# Padrão didático dos notebooks canônicos

**Definido em:** 17/11/2026. **Aplicar nos notebooks 01–04 e próximos ajustes.**

## Objetivo

Ser legível pelo estudante e por um professor com conhecimento técnico da área, permitindo explicar **o que foi executado, por quê, como interpretar e quais limitações permanecem**. Notebooks não devem virar repositórios de funções gigantescas.

## Estrutura editorial

1. Pergunta científica em duas frases.
2. Conceito teórico em linguagem natural e unidade de análise.
3. Fontes e proveniência dos datasets, incluindo o recorte temporal.
4. Poucas células de execução, com título claro e parâmetros destacados.
5. Gráficos e tabelas com **explicação do que cada eixo representa**.
6. Interpretação: o que observamos, o que inferimos e o que não podemos concluir.
7. Registro de execução e próximo passo; preservar artefatos originais.

## Regra de código

- Preferir **3–6 células de código** por notebook quando isso não sacrificar clareza ou reprodutibilidade.
- Agrupar inicialização e download em uma célula; análise em outra; gráficos em outra; persistência numa última.
- Extrair código repetido de cálculo e modelagem para `src/ethmix/`, versionado e testado.
- Usar o **Drive próprio** `Projeto_Mixers_Ethereum` como fonte de dados; não depender de caminho `/content/drive/MyDrive` nem do atalho de Bruno.
- Criar apenas novas subpastas de resultados com manifestos; não sobrescrever dados e modelos antigos.
- Deixar cada etapa funcional também como **aula**: exercícios curtos e perguntas de interpretação.
- Testar sintaxe e, quando possível, regressões de métricas; **não declarar execução Colab como validada sem outputs efetivos**.

## Distinção metodológica

- **Reprodução:** aplica protocolo especificado a fontes previamente obtidas.
- **Auditoria de evidência:** confronta CSVs/manifests existentes, mas não refaz todos os cálculos dos dumps.
- **Auditoria independente:** refaz etapas desde inputs e compara hashes/saídas.
- **Exploração:** experimenta escolhas à luz de resultados já vistos.
- **Teste confirmatório:** usa protocolo pré-registrado e dados não usados para o ajuste.

A precisão/recall de 100% numa validação por linha com janelas positivas do mesmo contrato **não prova generalização entre contratos**.

## Primeiro notebook com esse padrão

[04_auditoria.ipynb](../notebooks/04_auditoria.ipynb) e [cópia operacional no Google Drive](https://drive.google.com/file/d/1qsqTiOHSdJhSIiK1xGXAp83IpO-T0oq8/view): 11 células, 4 de código, gráficos de atribuição direta/Router, status de paridade e F1 de validação cruzada por fold. O botão de salvar é opcional; a execução ainda está pendente.
