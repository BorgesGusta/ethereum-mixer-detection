# Registro de decisões — em reconciliação

Fonte histórica: `mixers-ethereum/docs/decisoes.md` no Drive. O original contém IDs repetidos e versões incompatíveis; **não deve ser apagado ou reescrito**.

## Pendências de reconciliação

| Tema | Registros observados | Situação |
|---|---|---|
| `MIN_TX` | 5 e 10 | Documentar quando cada valor foi usado; experimentos recentes usam >=10 |
| Positivos | Tornado 10 ETH direto / direto + Router | Identificar execução e origem de cada versão |
| Datas de validação/teste | múltiplos protocolos 2026 | Diferenciar propostas substituídas do protocolo efetivamente executado |
| Limiar | 0,85 selecionado a partir de 2020 para RF | Não reaproveitar como limiar calibrado de outros modelos |
| Rótulos de negativos | seleção manual de 100 endereços | Revisitar proveniência e critérios antes de afirmações confirmatórias |

## Nova convenção

Um documento por decisão: `ADR-0001-titulo.md` contendo: data, status (proposta/aceita/substituída), contexto, decisão, justificativa, consequências, experimentos afetados e evidências.

**Proibição metodológica:** não tratar mudança posterior do protocolo como se tivesse sido definida antes de observar os dados. A sequência de decisões deve aparecer no artigo.
