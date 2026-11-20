# EXP-06B — Resultados auditados: criação interna do pool e amostra de logs

**Executado:** 19/11/2026 17:55:46 UTC. **Auditado:** 19/11/2026, por leitura direta dos dois arquivos no Drive e conferência SHA-256. **Status:** diagnóstico executado; criação interna observada no bloco 22.153.714; saques históricos na janela-alvo e equivalência à classe mixer **ainda não provados**.

## Rastreabilidade dos artefatos

- [Pasta oficial EXP-06B](https://drive.google.com/drive/folders/1-_iI6xOScAy0-a33Y2Rt94BdDFfBymyq).
- [`evidencias_exp06b.json`](https://drive.google.com/file/d/1tqOhpMwf_qce64d7-7F7YuO1H20naeAF/view) (55.724 bytes). SHA-256 recalculado: `61e60f28fd23af38e09f8ae2a6ae23d56699536e2667f7d0d1f875adebbc207f`.
- [`manifesto_exp06b.json`](https://drive.google.com/file/d/1dZby4_AxEFbuIzyOm8tG_krcQMaPcxGF/view) (866 bytes). **Hash do JSON de evidências coincide** exatamente com o manifesto.
- A execução exige `EXP-06A` de hash `f3e142a11e8a6d954d858c22df0dfa35b6a06e71234a75fa4cff03e9dadc3dda`, e o manifesto da execução registra a mesma entrada. A auditoria não reexecutou a consulta API, nem o RF.
- [Script](../../scripts/exp06b_validar_criacao_saques.py); [notebook](../../notebooks/19_EXP-06B_traces_criacao_e_retiradas_privacypools.ipynb); [protocolo previamente registrado](EXP-06B-protocolo-traces-e-retiro.md).

## R1 — Trace de criação do contrato (evidência forte de implantação)

A chamada `GET /api/v2/transactions/0x6e3e14d7bcdfa838a8f7918de81d7b233e40d3afd493a864285fad8b360bcf75/internal-transactions` retornou **HTTP 200; uma página; `status=completo`; um trace**:
- `type=create`, `success=true`;
- `created_contract=0xf241d57c6debae225c0f2e6ea1529373c9a9c9fb` (**igual ao pool ETH identificado na fonte oficial**);
- `block_number=22153714`, hash da transação igual à candidatura original.
- Metadata do endereço consultada via API: HTTP 200, `creator_address_hash=0xba5ed099633d3b313e4d5f7bdc1305d3c28ba5ed`, `is_contract=true` atual, `creation_tx_hash=null`. O endpoint `/addresses/{pool}/smart-contracts` retornou **HTTP 400**, sem confirmação de código-fonte verificado por essa rota.

**Conclusão sustentada:** a API disponibilizou uma evidência específica e coerente de **criação interna do pool na transação do bloco 22.153.714**, que explica por que o campo top-level `created_contract` do EXP-06A veio vazio. **Pendente:** por que a configuração da 0xbow declarava `deploymentBlock=22153707`, sete blocos antes. Não alterar um dos valores por conveniência. Uma causa possível é um bloco de referência da implantação de outro componente, mas isso é **hipótese**, não fato demonstrado.

## R2 — Amostra de logs (evidência de padrões de eventos; não período-alvo)

`GET /api/v2/addresses/{pool}/logs` retornou **HTTP 200 em duas páginas**; o script interrompeu após o limite pré-registrado, resultando `status=parcial_limite_paginas`. A amostra contém **100 registros**, entre os blocos **26.405.646 e 26.449.771**, portanto não constitui observação direta do período março/2025 ou 15/01/2026.

Contagem de nomes de evento **conforme decodificação retornada pela API atual**:

| Nome decodificado | Nº de logs |
|---|---:|
| `LeafInserted(...)` | 49 |
| `Withdrawn(...)` | **44** |
| `Deposited(...)` | 6 |
| `Ragequit(...)` | 1 |
| **Total** | **100** |

**Indicadores lexicais de saída:** 45 = 44 `Withdrawn` + 1 `Ragequit`; **não chamar de 45 retiradas confirmadas**. O script mostra até 50 candidatos. Há **48 hashes de transação distintos na amostra se contado campo vazio como valor**; identificam-se **42 hashes não vazios distintos entre os 45 eventos sugestivos**. Algumas linhas retornaram `tx_hash` vazio e `timestamp=null`. Consequentemente, a amostra precisa de revisão de esquema/atribuição do hash antes de verificar receipts individualmente. Não extrapolar frequência de eventos para toda a história do pool.

**Exemplo auditável sugerido, não prova histórica completa:** `0xd0e36312774288071e2a2746d743f2c9f846a3193f8f09403a328fa266d3f67f`, bloco 26.449.771, decodificado como `Withdrawn(address indexed _processooor, uint256 _value, uint256 _spentNullifier, uint256 _newCommitment)`, `topic0=0x75e161b3e824b114fc1a33274bd7091918dd4e639cede50b78b15a4eea956a21`. O evento combina campos relevantes à arquitetura de privacidade, **não é prova isolada de desvinculação depósito/saque** no período-alvo.

## Decisão de evidência, sem inferência excessiva

| Critério | Decisão |
|---|---|
| Identidade do pool criado internamente em março/2025 | **Evidência direta observada** no trace completo de sucesso |
| Bloco declarado na configuração versus bloco da transação | **Divergência de sete blocos ainda aberta** |
| Atividade do pool em março/2025 | Sustentada por EXP-06A e Etherscan; amostra pontual |
| Eventos decodificados como saques no pool | **Indícios fortes na amostra recente, sem validação histórica de ABI/receipts individuais** |
| Retiradas e mecanismo de anonimato no período 2025/2026 escolhido | **Ainda não comprovados** |
| Rótulo independente para RF / comparação externa / F1 | **Não atribuído / não calculado** |

## Próxima tarefa com maior valor (EXP-06C, ainda não executada)

1. Buscar **transação de retirada identificável no mesmo período histórico** e verificar *receipt* completo, endereço emissor, `topic0`, implementações/ABI e arquitetura on-chain, preferindo verificação por evento + função/trace no bloco correspondente.
2. Investigar o significado do `deploymentBlock=22153707` na configuração/versionamento; não retratar `22153714` como erro sem prova.
3. Resolver o problema de campo `tx_hash` vazio em algumas linhas retornadas por `/addresses/{pool}/logs` (rever esquema aninhado de `transaction_hash` no Blockscout). Qualquer novo filtro temporal ou amostragem será registrado antes da coleta.
4. Encaminhar elegibilidade funcional ao procedimento de revisão independente **fora do EXP-05**: o EXP-05 é cego ao score e não deve receber pré-classificações. Positivos de mesma família e famílias distintas separados por contrato e protocolo.

**Sem rerun de EXP-06A/06B, sem treino ou recálculo de métricas, sem PDF de artigo.**
