# EXP-02C — Resultado real: logs completos do MCT-XEN e consulta de seletores

**Execução em Colab:** 17/11/2026, 17:25:57 UTC. **Recorte histórico das transações:** Ethereum mainnet, 15/01/2026. **Estado:** a paginação das três transações MCT-XEN amostradas está concluída; **não** estão concluídas a auditoria de todas as 315 transações, a implementação histórica dos proxies ou a rotulagem independente.

## Evidências da execução

[Pasta da execução](https://drive.google.com/drive/folders/13348CzioFtdQWc6snAEPQLroVBiAO_6T)

- [`status_paginacao.csv`](https://drive.google.com/file/d/1uyeomb9MIBuXWlvswDii1boP_70O2hkE/view)
- [`seletor_vs_abi_atual.csv`](https://drive.google.com/file/d/1F2SD_Wu6CtbZg_sxrUPtKsvlOTq6E-5N/view)
- [`eventos_logs_coletados.csv`](https://drive.google.com/file/d/1MWfcHSfn7dIpp_xKv0IUlAPbKn6XYJpA/view)
- [`paginas_blockscout.json`](https://drive.google.com/file/d/1C4tjqeb8dQ9pNDCIqG2qrO0zKZnE51X_/view)
- [`respostas_abi_atual.json`](https://drive.google.com/file/d/1vPmlLjow-5JB2hDJtNFW6Z6aCyqfVXr4/view)
- [`manifesto_EXP02C.json`](https://drive.google.com/file/d/1AM7PnVWFb5lFSBhuOYwkofBoEZ3xVXsW/view)

Os hashes SHA-256 das **entradas** EXP-02B foram preservados no manifesto: `83f42e349d25cbbcded99784ba9eb4c148b64c9d91eb3190aab00a76c5f3ea8d` (`amostras_tx_api.csv`) e `b4442151e64a86722aed72caf15a785f6da800fc139d8befa8e50a41bd143571` (`eventos_amostras.csv`). Não houve mudança de modelo, limiar ou rótulos.

## Paginação: resultados observados

| Hash da transação | Páginas | Logs recuperados | Primeiro lote igual ao EXP-02B? | Paginação completa? | Índices repetidos |
|---|---:|---:|---|---|---:|
| `0x16f0f1fbc11069f78f9c249ddfd9da36781b3beb90b9bc00b299c9bebbd71409` | 2 | 83 | Sim | Sim | 0 |
| `0x7c3ddc32a73033bf2e76f9f1bf0ffbdd513d311b0f0c6200024a4aa2c148e885` | 2 | 83 | Sim | Sim | 0 |
| `0xe7c05731842cfdf2491457806e27f5349b79b0d0fb2c5caf5cb0ee03a7233d8a` | 6 | 300 | Sim | Sim | 0 |
| **Total** | **10** | **466** | **3/3** | **3/3** | **0** |

O EXP-02B havia capturado apenas 150 logs desses três hashes (50 por transação). Foram obtidos **316 eventos adicionais**, perfazendo **466 logs** completos para as três transações amostradas. Considerados os **120 logs** já completos das outras 15 amostras no EXP-02B, o conjunto das 18 transações amostradas soma **586 logs recuperados**, sob a semântica de `next_page_params=null` informada pelo Blockscout. Esse total não representa os logs de todas as transações recebidas pelos contratos no dia.

## Identificação por seletor

| Contrato | Seletor | ABI atual HTTP | Match na ABI atual | 4byte HTTP | Candidatos 4byte | Histórico janeiro/2026 validado |
|---|---|---:|---|---:|---|---|
| OKX DEX / TransparentUpgradeableProxy | `0xec5b999d` | 200 | nenhum | 200 | nenhum | **não** |
| MCT-XEN / MctXenMinter | `0x98190f47` | 200 | nenhum | 200 | nenhum | **não** |

A ausência de correspondência nas fontes consultadas **não autoriza** inferir que as chamadas eram não reconhecíveis, maliciosas ou próprias de mixer. A ABI retornada é contemporânea à consulta, não necessariamente a implementação histórica do bloco.

## Estado científico e prioridades

- **Concluído:** paridade das páginas iniciais com o EXP-02B, paginação dos três hashes MCT-XEN até `next_page_params=null`, ausência de índices repetidos e preservação de respostas.
- **Pendente:** interpretar as funções dos seletores à luz de implementação histórica; reconstruir histórico de upgrades dos proxies OKX, MCT-XEN e Wormhole; expandir auditoria para todo o dia e incluir amostra não alertada; submeter rótulos a dois revisores independentes; reunir positivos de mais de um protocolo mixer.
- **Proibido inferir:** seis falsos positivos verificados, precision 33,3%, melhoria demonstrada por modelo contextual ou segurança operacional superior.
- **Próxima fase:** [protocolo EXP-02](EXP-02-protocolo-temporal-contrato.md) e [plano de artigo](../manuscrito/plano-de-publicacao.md). Iniciar a **escrita do artigo imediatamente**, mantendo resultados novos como pendentes até execução, sem selecionar retrospectivamente limiar/features em teste 2026 já explorado.

**Relação com [EXP-02B](EXP-02B-resultados-auditoria-amostral-2026.md):** complementa a coleta inicial e **não** substitui seus limites de amostragem nem a insuficiência de ground truth.
