# Detecção de Mixers na Ethereum — Reprodução e Extensões

Pesquisa acadêmica em Segurança de Redes de Computadores: reprodução e investigação de extensões do artigo **“Uma Proposta de Algoritmo para a Detecção de Mixers na Ethereum”** (Leale e Sendin, SBSeg 2025).

> **Situação (16/11/2026):** organização e auditoria de um acervo experimental pré-existente. Ainda não existe um resultado confirmatório independente que prove superioridade de um novo algoritmo.

## Comece por aqui

- [Painel de pesquisa / memória Obsidian](docs/00_PAINEL.md)
- [Cronologia dos experimentos](docs/01_CRONOLOGIA.md)
- [Inventário de experimentos](docs/02_EXPERIMENTOS.md)
- [Registro de decisões](docs/03_DECISOES.md)
- [Dados, Drive e proveniência](docs/04_DADOS.md)
- [Plano de trabalho](docs/05_PLANO.md)
- [Orientações para artigo/Overleaf](manuscript/README.md)
- [Modelo de ficha de experimento](docs/experiments/TEMPLATE.md)

## Onde está cada coisa?

| Sistema | Responsabilidade |
|---|---|
| **Este GitHub** | Versões de scripts e notebooks, protocolos, decisões, notas, figuras e resultados leves |
| **[Google Drive — mixers-ethereum](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj)** | Dados brutos, intermediários, processados, modelos binários, execuções completas e backups históricos |
| **Obsidian** | Abrir um clone deste repositório como cofre de notas Markdown; não criar outra fonte de verdade |
| **Overleaf** | Manuscrito em LaTeX, tabelas e referências sincronizadas de forma controlada, futuramente |

## Regras científicas e operacionais

1. Preservar arquivos e resultados legados; não sobrescrever dumps nem notebooks originais.
2. Separar **reprodução do artigo**, **melhorias exploratórias** e **validação confirmatória**.
3. Candidato adicional não é automaticamente falso positivo: confirmar rótulos.
4. Registrar por execução: protocolo, versão do código, período, hash dos dados, parâmetros, resultados e limitações.
5. Treino histórico de **2020 ainda não foi feito**: o treino legado tem positivos de março/2025, do mesmo contrato.
6. Os conjuntos de 2020 e janeiro/2026 já foram analisados; não são testes cegos para seleção posterior.
7. Não publicar dados pesados, credenciais, tokens, arquivos pessoais ou resultados não auditados no GitHub.

**Próximo marco:** catalogar notebooks e resultados históricos, reconciliar decisões contraditórias e planejar coleta longitudinal 2020–2026. Nenhum resultado anterior foi recalculado por esta documentação.


**Drive oficial:** [Projeto_Mixers_Ethereum (pasta própria)](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj). A pasta `mixers-ethereum` do Bruno é apenas fonte histórica compartilhada; não fazer novas execuções nela.
