# EXP-06C — Protocolo prévio de busca por retirada histórica no Privacy Pools v1

**Preparado em 19/11/2026. Status: notebook publicado; execução on-chain pelo pesquisador PENDENTE.** Complementa EXP-06A e EXP-06B; não refaz esses experimentos nem aplica RF.

## Pergunta científica

Podemos demonstrar uma transação individual de retirada no ETH pool da 0xbow **em período histórico relevante**, com assinatura de evento, hash, bloco, transação com sucesso e log do contrato? Tal constatação fortalece a evidência de atividade funcional, mas não prova, sozinha, a desvinculação depósito→saque nem a equivalência ao Tornado Cash.

## Fontes e decisão metodológica

- [Documentação técnica oficial da 0xbow](https://github.com/0xbow-io/privacy-pools-core/blob/main/packages/contracts/README.md): fluxo de **withdrawal privado** com prova ZK via relayer é distinto do **ragequit**, no qual o depositante original saca diretamente. Portanto, não misturar eventos `Withdrawn` e `Ragequit`.
- [Especificação de API Blockscout-compatible](https://explorer.unit0.dev/api-docs): endpoint `/api?module=logs&action=getLogs&fromBlock=...&toBlock=...&address=...&topic0=...`, com limitação potencial de 1.000 logs. A disponibilidade da API no host Ethereum deve ser demonstrada na execução; não presumida.
- Pool `0xf241d57c6debae225c0f2e6ea1529373c9a9c9fb`, tópico `Withdrawn` `0x75e161b3e824b114fc1a33274bd7091918dd4e639cede50b78b15a4eea956a21`; tópico `Ragequit` `0xd2b3e868ae101106371f2bd93abc8d5a4de488b9fe47ed122c23625aa7172f13`. Esses tópicos provêm do **EXP-06B**, mas sua semântica será confrontada com ABI/contrato da época.

## Janelas congeladas ANTES da execução

| Janela | Blocos (ambos inclusivos) | Função |
|---|---|---|
| `pos_implantacao_2025` | **22.153.714–22.253.714** | Encontrar até 2 exemplos iniciais de `Withdrawn` após implantação observada |
| `vizinhanca_dia_teste_2026` | **24.233.073–24.240.273** | Busca exploratória em torno de bloco legado da data de teste de 15/01/2026 (janela aproximada, **não** declaração de dia inteiro) |

**Não são amostras aleatórias nem holdout cego**. A janela 2026 já é parte de pesquisa explorada e não será usada para afirmar nova validação de generalização. Os limites são por número de blocos, não por timestamp UTC exato; o relatório deverá aferir datas reais dos blocos/tx.

## Procedimento técnico

1. Verificar SHA-256 da entrada original EXP-06B: `61e60f28fd23af38e09f8ae2a6ae23d56699536e2667f7d0d1f875adebbc207f`.
2. Baixar script versionado no commit `9a922526196bdc0face23858d1923f7b834c9a28`, SHA-256 `fdd82442ca69b8af77cfd8840d7f70d56571e8a0e336b6b20539d4a6a7bebd6a`.
3. Para cada janela: consultar `getLogs` com address + topic0 e partições de até **10.000 blocos**; no máximo **24 consultas**; se houver 1.000 eventos, dividir a partição uma vez e marcar inconclusiva qualquer continuação não resolvida.
4. Parar depois de **2 hashes candidatos por janela** ou no fim da janela. Salvar status por partição para que busca interrompida não seja relatada como exame exaustivo.
5. Para até 2 hashes por janela, consultar `/api/v2/transactions/{hash}` e `/api/v2/transactions/{hash}/logs`. Exigir hash com 32 bytes, transação `ok`, bloco igual, log emitido pelo pool e topic0 igual. **Se logs de uma tx ainda paginam, marcar não confirmado**; a coleta não faz essa paginação para preservar limite.
6. Preservar `evidencias_exp06c.json` e `manifesto_exp06c.json` em pasta **nova** do Drive, com SHA-256 e restrições.

## Interpretação e limites

- `confirmed_withdraw_log=true` significa **somente** que uma transação de sucesso possui log `topic0` do contrato pool com o tópico atribuído a `Withdrawn`. Ainda é preciso verificar ABI/implementação histórica e o mecanismo de desacoplamento por código/documentos na data.
- Falta de eventos ou falha da API significa **inconclusivo quanto a ausência histórica**; duas retiradas encontradas não formam amostra representativa.
- `Ragequit` é outro caminho funcional, não substituir `Withdrawn` sem justificativa.
- Reconciliação da divergência de bloco **22.153.707 vs 22.153.714** continua investigação distinta; a evidência de CREATE do EXP-06B permanece válida, sem corrigir número arbitrariamente.
- Este piloto **não atribui novo rótulo positivo**, não usa endereços da revisão cega EXP-05, não modifica treino/limiar, não testa RF, não produz precision, recall ou F1.
- Após resultado auditado, decidir se há base para obter parecer de revisores **distintos** do EXP-05 sobre equivalência funcional.

## Artefatos

- [Notebook EXP-06C no Drive](https://drive.google.com/file/d/1mtUxaTHxExTXBKUI5cUAGlCQCBVcN5zt/view?usp=drivesdk), em `notebooks/00_ATIVOS/`; [versão GitHub](../../notebooks/20_EXP-06C_retiradas_historicas_privacypools.ipynb), commit `6dff6980805c48c0d024c5f6d604366db9800f8b`.
- [Script GitHub](../../scripts/exp06c_retirada_historica.py) commit `9a922526196bdc0face23858d1923f7b834c9a28`; [cópia Drive](https://drive.google.com/file/d/1p7yWyNo8NlMzS5Mk0-B2DX2SC-Wj1UfI/view).
- **Testes locais:** sintaxe Python e cenários simulados de API/recibo passaram, sem consulta on-chain real. Notebook JSON válido (11 células).

**Status final desta preparação:** pronto para executar no Colab, nenhum resultado on-chain do EXP-06C ainda foi gerado. Não gerar PDF/Overleaf nesta etapa.
