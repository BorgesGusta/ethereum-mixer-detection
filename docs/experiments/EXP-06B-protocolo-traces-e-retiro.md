# EXP-06B — Piloto complementar de traces e eventos do Privacy Pools v1

**Preparado:** 18/11/2026. **Estado: NOTEBOOK PUBLICADO NO DRIVE E NO GITHUB; EXECUÇÃO REAL PENDENTE.** Este protocolo complementa EXP-06A, não o substitui e não reexecuta suas duas consultas de transação.

## Perguntas

1. A transação candidata à criação `0x6e3e14d7bcdfa838a8f7918de81d7b233e40d3afd493a864285fad8b360bcf75`, bloco 22.153.714, contém algum trace que criou internamente o pool `0xF241d57C6DebAe225c0F2e6eA1529373C9A9C9fB`?
2. Por que a configuração oficial indica `deploymentBlock=22.153.707` (sete blocos antes)? A resposta **não** pode ser fabricada de um trace ausente: ausência em API parcial não comprova ausência de implantação.
3. Há indicadores de eventos cujo nome decodificado sugere retirada entre uma **amostra limitada** de logs do pool? Não concluir que houve desvinculação sem prova funcional do contrato e período.

## Entradas e prova de integridade

- [EXP-06A: verificação anterior](https://drive.google.com/file/d/1vAiHf6_ui9-SIrfuoQaIV2xWEFkALJYj/view), SHA-256 `f3e142a11e8a6d954d858c22df0dfa35b6a06e71234a75fa4cff03e9dadc3dda` — conferido pelo script antes de qualquer consulta.
- Script: [`scripts/exp06b_validar_criacao_saques.py`](../../scripts/exp06b_validar_criacao_saques.py), commit `2b2a1f0e7c0f030f942a74acf7496ef8ff617108`, SHA-256 `17d2aab3ad5e55ddb63af78d3a3e5afba542661b57e8de35cc82f374c6865bf9`.
- [Notebook operacional no Drive](https://drive.google.com/file/d/1Pej3E3Nr65figYCEtZ2axC1Fal1D-NiJ/view?usp=drivesdk), em `Projeto_Mixers_Ethereum/notebooks/00_ATIVOS/`. [Cópia no GitHub](../../notebooks/19_EXP-06B_traces_criacao_e_retiradas_privacypools.ipynb), commit `a1ec7bde4a98da8f0b78c30c1cd850f5ca499d7f`.
- **Verificações locais:** arquivo Python compilou com sucesso; notebook JSON válido e 11 células. **Não é execução do piloto real.**

## Método predefinido

- Consultar via Blockscout `GET /api/v2/addresses/{pool}` e `GET /api/v2/addresses/{pool}/smart-contracts`, explicitamente **metadados atuais**.
- Consultar `GET /api/v2/transactions/{hash_factory}/internal-transactions` com no máximo **4 páginas**. Identificar `created_contract.hash == pool` e `success == true` somente quando devolvidos. **Se ausência com API parcial/erro, classificar inconclusivo.**
- Consultar `GET /api/v2/addresses/{pool}/logs` com no máximo **2 páginas**; manter bloco, hash e tópico dos eventos. **A API pode listar logs recentes primeiro** e as duas páginas não são recorte representativo de março/2025 ou janeiro/2026.
- Nomes decodificados que contenham termos como `withdraw`, `unshield`, `exit` ou `ragequit` são **pistas lexicais**, não prova histórica de retirada, anonimato ou desvinculação.
- Salvar `evidencias_exp06b.json` e `manifesto_exp06b.json` com SHA-256 em uma **nova pasta** `results/EXP-06B_traces_e_logs_*`, sem sobrescrever EXP-06A.

A API de *internal transactions* e endereços segue [especificação Swagger Blockscout](https://github.com/blockscout/blockscout-api-v2-swagger/blob/main/swagger.yaml). O suporte efetivo no explorador Ethereum deve ser demonstrado na execução, não presumido.

## Critérios de interpretação

- Trace de CREATE/CREATE2 com `created_contract` igual ao pool e `success=true`: evidência de **criação interna naquela transação**, se campos confiáveis e paginação adequada. Confrontar número do bloco com configuração.
- Nenhum trace retornado: **não concluir inexistência**, sobretudo se HTTP não 200, paginação incompleta ou escopo de endpoint limitado.
- Evento sugestivo de retirada: abrir transação específica, verificar receipt, endereço, ABI/bytecode histórico e mecanismo funcional. Não atribuir automaticamente `positivo_confirmado`.
- Nenhum evento sugestivo nas duas páginas: **não concluir inexistência de saques**.
- **Ground truth permanece pendente**; EXP-06B não calcula score, F1, precision, recall e não interfere na revisão independente EXP-05.

## Estado

- [x] Código do piloto versionado, entrada congelada com SHA, notebook publicado no Drive.
- [ ] Pesquisador executar notebook via **Ambiente de execução → Executar tudo**.
- [ ] Conferir saída do Drive e hashes contra manifesto.
- [ ] Investigar apenas lacunas específicas remanescentes, sem ampliar coleta ou conclusões retroativamente.

**Regra:** este protocolo é diagnóstico, não comprovação automática de rótulo.

## Resultado após execução — 19/11/2026

**EXECUTADO E AUDITADO:** [Relatório EXP-06B](EXP-06B-resultados-auditoria-2026-11-19.md), [pasta real de resultados](https://drive.google.com/drive/folders/1-_iI6xOScAy0-a33Y2Rt94BdDFfBymyq), JSON SHA-256 coincidente com manifesto. A transação candidata continha **1 trace interno CREATE de sucesso** criando o pool ETH no bloco **22153714**. O campo `deploymentBlock=22153707` da configuração permanece divergente e sem explicação comprovada. A amostra limitada de **100 logs** é parcial, dos blocos 26405646–26449771, com **44 `Withdrawn`**, **1 `Ragequit`**, 49 `LeafInserted` e 6 `Deposited` decodificados pela API atual. Nenhum desses registros é prova direta de saque em 2025/15-01-2026. Nenhum rótulo ou score novo.
