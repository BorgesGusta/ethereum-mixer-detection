# Guia de estudo e pesquisa — Detecção de mixers na Ethereum

**Projeto:** Segurança de Redes de Computadores — reprodução, auditoria e extensão experimental do trabalho de Leale e Sendin (SBSeg 2025).  
**Atualizado:** 17 de novembro de 2026.  
**Objetivo:** dominar fundamentos e experiências do projeto, preparar apresentação e transformar a investigação em um manuscrito cientificamente defensável.

## 1. Como organizar este material no NotebookLM

A pasta principal contém PDFs didáticos, cópias dos artigos científicos, o histórico de experimentos e um plano de publicação. Sugestão: crie **um notebook para fundamentos + exercícios** e **outro para revisão bibliográfica + artigo**. Carregue os PDFs das respectivas subpastas como fontes. Os arquivos não são uma reprodução automática do banco da Ethereum; neles há números e evidências provenientes dos experimentos já documentados no projeto. Para citações científicas, priorize o artigo original e os arquivos de evidências.

| Seção do Drive | O que estudar | Resultado esperado |
|---|---|---|
| 00 — Leia primeiro | Escopo, roteiro, perguntas | Saber apresentar problema, motivação e limites |
| 01 — Aulas e conceitos | Ethereum, mixers, estatística, segurança, validação | Saber explicar o funcionamento e as fórmulas |
| 02 — Evolução dos experimentos | Cronologia e achados verificados | Distinguir evidência de hipótese |
| 03 — Artigos enviados | Cinco artigos recebidos + artigo SBSeg 2025 | Compreender trabalhos relacionados |
| 04 — Artigos adicionais | Links para PDFs acadêmicos complementares | Ampliar referencial e buscar lacunas |
| 05 — Revisão bibliográfica | Matriz de trabalhos e oportunidades | Não comparar tarefas diferentes erroneamente |
| 06 — Exercícios e prática | Flashcards, roteiro de laboratório, gabaritos | Conseguir justificar e reproduzir decisões |
| 07 — Manuscrito e submissão | Questões de pesquisa, ablações e critérios de avaliação | Redigir e defender contribuições próprias |

## 2. Sequência de seis semanas (flexível)

**Semana 1 — Infraestrutura Ethereum.** Estude contas EOA/contrato, blocos, hash, transação externa, chamadas internas, logs, ABI, selectors e proxies. Pratique interpretando uma transação e distinguindo dado observado de dado ausente.

**Semana 2 — Mixers e privacidade.** Estude depósito, commitment, note, nullifier, retirada, Merkle Tree, zk-SNARK, relayers e Router. Explique por que um contrato de bridge não é automaticamente mixer e por que mixer não significa atividade ilícita.

**Semana 3 — Características e Random Forest.** Derive a entropia de Shannon, calcule exemplos pequenos, estude balanceamento, overfitting, vazamento entre janelas e calibração de scores.

**Semana 4 — Nossa evolução.** Reconstitua a auditoria 2020, os 63 × 9 alertas, a análise de elegibilidade e o teste legado de 2026. Explique limites com números exatos.

**Semana 5 — Literatura crítica.** Leia primeiro Akopova, taxonomia de Barbereau et al. e GNN/FPTracer; depois MixGuard, StealthLink e Tutela. Para cada artigo responda: o que ele classifica? Como cria rótulos? Como evita vazamento? Pode ser comparado com nosso RF?

**Semana 6 — Questão científica e artigo.** Elabore RQ, hipóteses, baselines, rótulos auditados, cenário com negativos difíceis, corte temporal e ablações. Escreva resultados preliminares com limitações claras.

## 3. Prompts úteis para o NotebookLM

1. “Explique como se eu fosse um aluno de Ciência da Computação a diferença entre transação externa, chamada interna, log ERC-20 e transferência econômica. Use somente as fontes.”
2. “Prepare uma aula progressiva com exemplos, oito questões e gabarito sobre entropia de Shannon usada na classificação de endereços Ethereum.”
3. “Construa uma linha do tempo dos EXP-01B a EXP-02B, com hipótese, experimento, arquivos de evidência e limitações.”
4. “Compare os artigos por **unidade de classificação**: contrato mixer, carteira suspeita, par depósito/saque e lavagem de dinheiro. Não compare F1 de tarefas distintas.”
5. “Faça uma banca simulada: dez perguntas difíceis sobre a divergência 63 × 9, risco de overfitting e ground truth, e depois avalie minhas respostas.”
6. “Mostre como uma transação pode interagir com Router, proxy, pool e bridge, e por que isso afeta a atribuição de features.”
7. “Com base apenas nos dados auditados, quais conclusões podemos publicar hoje? Quais dependem de novos experimentos?”

## 4. Regras permanentes de interpretação

- Score Random Forest não equivale automaticamente à probabilidade calibrada de que um endereço seja mixer.
- Uma identificação no Etherscan/Blockscout é **pista documental**; funções e transações da **data estudada** precisam ser verificadas antes de afirmar um rótulo histórico.
- “Não há rótulo” não significa “não mixer”. Sem ground truth não há precision, recall ou taxa de falsos positivos da população completa.
- A diferença **63 vs 9** deve permanecer como limitação de reprodutibilidade, caso não surjam código, dados ou esclarecimentos que comprovem a equivalência metodológica.
- O teste de 2026 **já existia**. Não descrevê-lo como avaliação inédita desta rodada nem reescolher limiar depois de conhecer seu resultado.
- Segurança e privacidade são objetivos diferentes: um mixer pode proteger a privacidade de usuários legítimos; analisar uso ilícito demanda evidência própria.

## 5. Fontes internas prioritárias

Projeto no Drive: https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj

Repositório: https://github.com/BorgesGusta/ethereum-mixer-detection

Relatório EXP-01J (sensibilidade): https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-01J-resultados-sensibilidade-63x9.md

EXP-02A (triagem 2026): https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02A-inventario-e-triagem-2026.md

EXP-02B (protocolo de rótulos): https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02B-protocolo-auditoria-2026.md

**Situação:** curso pronto para leitura; a verificação histórica de atividade de seis alertas de 2026 e a avaliação de novos protocolos de mixers continuam pendentes.
