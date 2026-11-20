# EXP-06A — Auditoria dos resultados de implantação e depósito (Privacy Pools v1)

**Executado no Colab:** 18/11/2026 17:35:20 UTC (declarado no resultado). **Auditado:** 18/11/2026, por conferência do JSON e SHA-256 a partir do arquivo real baixado do Drive. **Estado científico: implantação inconclusiva, interação histórica com pool confirmada na transação de depósito. Sem rotulagem de mixer.**

## Artefatos oficiais e integridade

- [Pasta de resultados EXP-06A no Drive](https://drive.google.com/drive/folders/1K83QFXRH_pGd5muiMNHhUxjNYdKwxt_l)
- [verificacao_exp06a.json](https://drive.google.com/file/d/1vAiHf6_ui9-SIrfuoQaIV2xWEFkALJYj/view) — 2205 bytes
- [manifesto_exp06a.json](https://drive.google.com/file/d/1G-I4MiOHlN0494uSN8rL_500XiRO-J24/view) — 382 bytes
- SHA-256 de `verificacao_exp06a.json` **recalculado** sobre os bytes baixados: `f3e142a11e8a6d954d858c22df0dfa35b6a06e71234a75fa4cff03e9dadc3dda`, **idêntico** ao manifesto.
- [Script versionado](../../scripts/exp06_validar_implantacao.py) e [notebook](../../notebooks/18_EXP-06A_validacao_implantacao_privacypools_v1.ipynb). Conferência de versão de execução ainda baseada no notebook publicado, não em hash do script no próprio manifesto (melhoria de proveniência pendente).
- O programa consultou a API de transações do Blockscout, não um RPC archive; a auditoria posterior não repetiu consultas on-chain.

## Duas transações: fatos e limites

| Item | Criação candidata | Depósito inicial |
|---|---|---|
| Hash | `0x6e3e14d7bcdfa838a8f7918de81d7b233e40d3afd493a864285fad8b360bcf75` | `0x55693706fddd4130a3b07fefa274c0b7730281c37e48725aa6aa8e1b7dca4948` |
| API de transação | HTTP 200 | HTTP 200 |
| Status | `ok` | `ok` |
| Bloco | **22.153.714** | **22.167.294** |
| Data UTC | 29/03/2025 16:20:59 | 31/03/2025 13:47:59 |
| Destinatário | `0xba5ed099633d3b313e4d5f7bdc1305d3c28ba5ed` | Entrypoint `0x6818809eefce719e480a7526d76bd3e561526b46` |
| `created_contract` | vazio | vazio |
| Logs paginados | não consultados por esse script | **3**, 1 página completa, **2 logs do pool** |
| Status do script | `inconclusivo_ou_divergente` | `interacao_pool_com_logs_confirmada` |

A configuração da desenvolvedora informa `deploymentBlock=22153707`, **sete blocos antes** da transação candidata (`22153714`). Esse campo foi obtido de configuração oficial e o bloco real foi obtido da API; o confronto demonstra a divergência **mas não identifica a razão**. A transação candidata foi enviada a outro contrato, e o campo `created_contract` vazio **não exclui** implantação por chamada interna de fábrica/factory. Não chamar essa transação de criação comprovada sem traces, eventos `CREATE/CREATE2`, verificação do criador ou fonte histórica equivalente.

A transação inicial de depósito foi direcionada ao Entrypoint oficial e registrou 2 logs emitidos pelo endereço ETH Pool `0xf241d57c6debae225c0f2e6ea1529373c9a9c9fb`. Os três logs foram recuperados até `next_page_params=null`, sob a semântica da API. **Isso confirma interação bem-sucedida com logs do pool naquele bloco**, não prova automaticamente o nome funcional dos eventos, o mecanismo de desvinculação depósito→saque nem um rótulo de positivo do classificador.

## Decisões científicas

- **GO apenas para evidência parcial de atividade histórica:** status `interacao_pool_com_logs_confirmada` em transação amostrada. A evidência anterior do Etherscan de 31/03/2025 (outra transação, bloco 22.169.054) continua separada.
- **NO-GO para criação comprovada:** divergência de bloco e nenhum `created_contract` exposto; investigar criação interna e definir por qual conceito o arquivo de configuração chama `deploymentBlock`.
- **NO-GO para novo rótulo positivo:** não foram verificados withdrawal/unshield e mecanismos de desvinculação na versão histórica nem concluída revisão independente.
- **NO-GO para generalização do RF:** EXP-06A não treinou nem aplicou RF e não estabeleceu holdout.
- Nenhuma evidência de ilicitude é inferida; anonimato/privacidade não equivalem a ataque.

## Próxima ação (ainda não realizada)

**EXP-06B, exclusivamente diagnóstico de implantação:** (1) conferir metadata de contrato criado/creator e *internal transactions/traces* da transação `0x6e3e14...` no Blockscout/Etherscan; (2) reconciliar `22153707` versus `22153714` por registros de deploy e versão; (3) investigar eventos/documentação de withdrawal, com hashes reais e versão da ABI na época; (4) preservar todos os registros com fonte, URL, bloco, horário, hash e limites. **Não repetir EXP-06A por inteiro** e não promover rótulos até completar esse gate. 

**No caderno/artigo:** apenas evidência parcial e discrepância verificável, não nova acurácia, falso positivo ou melhoria confirmada. Sem PDF.
