# Guia final de estudo — Auditoria de detecção de mixers na Ethereum

**Base:** manuscrito de fechamento `docs/manuscrito/artigo_auditoria_mixers_sbc_2026.tex` e evidências auditadas dos EXP-01 a EXP-08, ramo `docs/consolidacao-oficial-2026-11-17`. **Estado:** guia pedagógico, não novo experimento ou nova fonte de métricas.

## A pergunta central do trabalho

Até que ponto um detector treinado com características estatísticas de um mixer conhecido identifica contratos realmente novos? Como usar previsões e evidências de execução para apoiar um processo de segurança sem produzir decisões automáticas injustificadas?

## Sequência cronológica e o que cada fase responde

1. **Reprodução do artigo de Leale e Sendin (SBSeg 2025).** Em 29/10/2020, os dados de transações e os três endereços Tornado Cash de referência foram reconstituídos. O original reportou 63 alertas, a reprodução consolidada apenas **9**. O principal achado é a divergência de contagem, não a conclusão de que os seis extras seriam necessariamente falsos positivos.
2. **Sensibilidade (EXP-01J).** Mínimo de 1, 5, 10 e 20 transações levou a **49, 14, 9 e 7 alertas**. O pré-processamento afeta fortemente os resultados.
3. **Auditoria de alertas em janeiro de 2026 (EXP-02).** Dentre 20.214 entidades elegíveis, nove alertas; três contratos Tornado Cash de referência e seis casos documentalmente associados a outras categorias. **Seis = indeterminados**, não rótulos negativos confirmados. Não se conhece precision/recall/F1 populacionais desse conjunto.
4. **Verificação histórica e integridade (EXP-03/04).** Controles não alertados e tentativas RPC históricas tiveram limitações; manifesto/hash de arquivos preserva cadeia de evidências; falhas HTTP em RPC não equivalem à ausência de contratos.
5. **Revisão cega (EXP-05).** Dois avaliadores independentes receberam protocolo de rotulagem. O trabalho entregue não deve usar rótulos sem ambas as fichas concluídas e verificadas.
6. **Protocolo distinto (EXP-06A/B/C).** Privacy Pools v1 da 0xbow: implantação via trace interno, depósitos e **quatro transações históricas de sucesso com log Withdrawn** (duas de 2025, duas de 2026). Isso não prova, por si só, anonimato, equivalência com Tornado Cash ou classe positiva.
7. **Comparação de algoritmos (EXP-07 v2).** Quatro modelos (Random Forest, regressão logística, árvore de decisão e Gradient Boosting) × três grupos de atributos × cinco folds = 60 medições internas. O maior F1 médio é **0,9778 (Random Forest)** nos três grupos. Porém, as **23 observações positivas são de um único contrato**, compartilhado por todos os folds de treino e teste. Resultado **exploratório**, não medição de generalização.
8. **Extensão de segurança (EXP-08).** Inventário de negativos difíceis e positivos independentes como candidatos **não rotulados**; protótipo **offline** de revisão humana e log JSONL com SHA-256 encadeado. Quatro testes locais aprovados. Não há integração com SIEM nem bloqueio automático.

## Termos que precisam ser entendidos

- **Mixer:** serviço de privacidade que procura enfraquecer o vínculo público entre depósito e retirada; existem arquiteturas diferentes.
- **Entropia:** medida estatística de diversidade de valores; sozinha não demonstra ofuscação de origem e destino.
- **Call count / trace:** número de chamadas e histórico de execução interna, importante para contratos Router e proxy.
- **Feature / atributo:** variável fornecida ao modelo; o estudo original utiliza quatro; o EXP-07 acrescentou `n_tx` para testar ablação.
- **Random Forest:** conjunto de árvores de decisão treinadas com subconjuntos amostrais e de atributos.
- **Precision:** entre previsões positivas, proporção efetivamente positiva; só calculável em amostra com rótulos válidos.
- **Recall:** entre positivos reais, proporção identificada; os três pools conhecidos não são a população inteira de mixers.
- **F1:** média harmônica de precision e recall; o valor 0,9778 é **média interna dos folds do EXP-07**.
- **Vazamento por identidade:** o mesmo contrato positivo aparece em treinamento e teste, com dias diferentes; favorece aprender a identidade em vez da classe generalizável.
- **Hard negatives:** negativos legítimos com comportamento parecido ao de positivos; precisam de evidência e confirmação independente.
- **Hash chain:** encadeamento de hashes de um log; detecta adulteração relativa a um hash terminal confiável armazenado fora da própria cadeia.

## Perguntas que o professor pode fazer

**“Por que 63 no artigo e 9 aqui?”** A seleção, os filtros e o processamento podem alterar o número de contratos elegíveis; o filtro foi testado e não resolveu sozinho toda a divergência. A diferença permanece documentada, sem alegar reprodução numérica exata.

**“Vocês podem dizer que o modelo acertou 97,78% dos mixers?”** Não. 0,9778 é o **F1 médio interno por linhas**; há apenas um contrato positivo em todos os folds e não existe holdout independente de protocolos.

**“Por que vocês não chamam os seis endereços de falsos positivos?”** Porque não há rótulos de verdade suficientemente confirmados e contextualizados na data; são casos indeterminados.

**“Por que testar outro protocolo?”** Para estudar diferenças funcionais da arquitetura e motivar um teste de generalização; as quatro transações de retirada verificadas não são rótulo de treino.

**“Qual é a contribuição prática de Segurança de Redes?”** O protótipo de triagem humana conserva a decisão como indeterminada, diferencia coleta de evidência de revisão e preserva registros de auditoria encadeados por SHA-256. Demonstra resposta prudente e integridade local, sem bloquear operações.

**“O que ainda falta para publicar um detector melhor?”** Múltiplos protocolos positivos confirmados, controles negativos difíceis revisados independentemente, períodos congelados e validação por contrato/família sem vazamento.

## Preparação do material de estudo

Este arquivo já está na biblioteca exclusiva do NotebookLM no Drive quando o link de entrega for apresentado. **A presença no Drive não garante importação automática no aplicativo NotebookLM.** Adicionar o arquivo como fonte manualmente, se necessário, e preferir a fonte LaTeX final ou PDF de revisão quando for autorizado e formatado oficialmente.

**Documentos-chave:**
- `docs/experiments/EXP-07-resultados-auditoria-2026-11-19.md`
- `docs/experiments/EXP-08-plano-seguranca-e-conjuntos.md`
- `docs/experiments/EXP-08-roteiro-demonstracao-seguranca.md`
- `docs/manuscrito/artigo_auditoria_mixers_sbc_2026.tex`
- `docs/manuscrito/CADERNO_CIENTIFICO_VIVO.md`
