# Detecção de Mixers na Ethereum — Reprodução e Extensões

Pesquisa acadêmica em Segurança de Redes de Computadores: reprodução e investigação de extensões do artigo **“Uma Proposta de Algoritmo para a Detecção de Mixers na Ethereum”** (Leale e Sendin, SBSeg 2025).

> **Situação documental (17/11/2026):** reprodução parcial e auditorias EXP-01J, EXP-02B e EXP-02C executadas; manuscrito LaTeX v0.1 iniciado. **Não há validação independente de superioridade preditiva.** Os resultados são os documentados nas fichas de experimentos; nenhuma execução foi refeita nesta consolidação.

## Comece por aqui

- [Painel de pesquisa / memória Obsidian](docs/00_PAINEL.md)
- [Cronologia dos experimentos](docs/01_CRONOLOGIA.md)
- [Inventário de experimentos](docs/02_EXPERIMENTOS.md)
- [Registro de decisões](docs/03_DECISOES.md)
- [Dados, Drive e proveniência](docs/04_DADOS.md)
- [Plano de trabalho](docs/05_PLANO.md)
- [Artigo LaTeX v0.1 e instruções para Overleaf](artigo/overleaf/README.md)
- [Modelo de ficha de experimento](docs/experiments/TEMPLATE.md)

## Onde está cada coisa?

| Sistema | Responsabilidade |
|---|---|
| **Este GitHub** | Versões de scripts e notebooks, protocolos, decisões, notas, figuras e resultados leves |
| **[Google Drive — Projeto_Mixers_Ethereum (pasta oficial)](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj)** | Dados brutos, intermediários, processados, modelos binários, execuções completas e backups históricos |
| **Obsidian** | Abrir um clone deste repositório como cofre de notas Markdown; não criar outra fonte de verdade |
| **Overleaf** | Fontes LaTeX v0.1 versionadas em `artigo/overleaf/`; compilação e importação no Overleaf ainda não verificadas |

## Regras científicas e operacionais

1. Preservar arquivos e resultados legados; não sobrescrever dumps nem notebooks originais.
2. Separar **reprodução do artigo**, **melhorias exploratórias** e **validação confirmatória**.
3. Candidato adicional não é automaticamente falso positivo: confirmar rótulos.
4. Registrar por execução: protocolo, versão do código, período, hash dos dados, parâmetros, resultados e limitações.
5. Treino histórico de **2020 ainda não foi feito**: o treino legado tem positivos de março/2025, do mesmo contrato.
6. Os conjuntos de 2020 e janeiro/2026 já foram analisados; não são testes cegos para seleção posterior.
7. Não publicar dados pesados, credenciais, tokens, arquivos pessoais ou resultados não auditados no GitHub.

**Próximo marco:** conferir compilação do artigo v0.1, reconciliar a documentação com os relatórios EXP-01J/02B/02C e completar auditoria de integridade/migração; depois preparar rótulos e teste independente por protocolo/período. Nenhum resultado anterior foi recalculado nesta consolidação.


**Drive oficial:** [Projeto_Mixers_Ethereum (pasta própria)](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj). A pasta `mixers-ethereum` do Bruno é apenas fonte histórica compartilhada; não fazer novas execuções nela.


## Continuidade e fontes atuais (17/11/2026)

- **Estado operacional:** [checklist vivo](docs/CHECKLIST_VIVO.md) (verificar antes de iniciar experimentos).
- **Resultados prioritários:** [EXP-01J](docs/experiments/EXP-01J-resultados-sensibilidade-63x9.md), [EXP-02B](docs/experiments/EXP-02B-resultados-auditoria-amostral-2026.md), [EXP-02C](docs/experiments/EXP-02C-resultados-logs-e-seletores.md).
- **Manuscrito editável:** [`artigo/overleaf/`](artigo/overleaf/README.md); v0.1 é rascunho, não PDF compilado, revisão ou submissão.
- **Auditoria da consolidação:** [registro 17/11](docs/CONSOLIDACAO_2026-11-17.md).
- Em 29/10/2020, 3/3 pools de referência foram recuperados, mas **9 alertas da reprodução contra 63 do artigo** continuam sem explicação exata. Em 15/01/2026, seis alertas adicionais seguem sem rótulos negativos independentes. EXP-02C completou logs de **três transações MCT-XEN amostradas**, não de todas as 315 transações dos seis contratos.
