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


## Síntese de decisões vigentes em 17/11/2026 — sem apagar decisões antigas

| Tema | Regra operacional atual | Evidência / situação |
|---|---|---|
| Reprodutibilidade 63 × 9 | Preservar divergência; não ajustar retrospectivamente limiar/filtro para coincidir com artigo | [EXP-01J](experiments/EXP-01J-resultados-sensibilidade-63x9.md): elegibilidade afeta alertas, causa exata desconhecida |
| Dados 2020/2026 | Já explorados; não chamar de holdout cego novo | [EXP-02](experiments/EXP-02-protocolo-temporal-contrato.md) e [EXP-02A](experiments/EXP-02A-inventario-e-triagem-2026.md) |
| Rótulos | Serviços identificados funcionalmente/documentalmente não equivalem a negativos confirmados | [EXP-02B](experiments/EXP-02B-resultados-auditoria-amostral-2026.md), [EXP-02C](experiments/EXP-02C-resultados-logs-e-seletores.md) |
| Cópia de dados | Pasta própria do projeto é destino de trabalho; preservar origem compartilhada; hashes da migração ainda pendentes | [Inventário de dados](04_DADOS.md) |
| Manuscrito | Fontes v0.1 existem em `artigo/overleaf/`; compilação/submissão não comprovadas | [Plano de fechamento](manuscrito/plano-de-fechamento-e-apresentacao.md) |

**Status de reconciliação:** a tabela acima não transforma registros antigos de `MIN_TX`, Router, limiar 0,85 e amostragem em ADRs retroativos. Devem ser criados ADRs específicos com evidência e status histórico após checagem dos notebooks efetivamente executados. Não inferir a data de decisão a partir da data de documentação.
