# EXP-02B — Resultado da auditoria funcional amostral em 15/01/2026

**Executado no Colab:** 17/11/2026, 16:10:57 UTC. **Data da blockchain:** 15/01/2026 (Ethereum mainnet, `chainId=1`). **Status:** coleta e comparação amostral **concluídas**; rótulos binários e auditoria exaustiva **pendentes**.

## Evidências originais e proveniência

[Pasta da execução no Drive](https://drive.google.com/drive/folders/1rV5mJ0rkINLML5aFUFnl0s7g1ybwrwOb)

- [`resumo_6.csv`](https://drive.google.com/file/d/1faYPTBUFBfAmInYFsnrXnq9tXm4KOwUR/view): comparação das contagens do ranking legado com o parquet intermediário e resultado das amostras.
- [`transacoes_locais_6_20260115.csv`](https://drive.google.com/file/d/1ebQZfUB9K1lrtYclrlxgGwowvnoaT4yD/view): transações diretas para os seis contratos presentes no intermediário.
- [`amostras_tx_api.csv`](https://drive.google.com/file/d/17S6xCYOng7Fk21cYZGq5k1yKzNn3kqGq/view): 18 hashes consultados diretamente no Blockscout.
- [`eventos_amostras.csv`](https://drive.google.com/file/d/1NwJFLTrrMtpLndn2vMV7fLzy9oQJMlH6/view): **270 linhas de log capturadas**, incluindo apenas a primeira página de três transações com paginação adicional.
- [`metadados_atuais.csv`](https://drive.google.com/file/d/1A7LTZR3AE95go8hzgdxRJgtZ5TTUBgpI/view): nomes, contrato e estado de verificação **atuais**, não código de 2026.
- [`manifesto.json`](https://drive.google.com/file/d/1uM3FQlaJQXXMKuTuACO6BI2oLU1_qVE7/view): SHA-256 dos dois insumos e dos cinco CSVs, parâmetros e advertências.

**SHA-256 do intermediário:** `9537f05d29044991f9a4750de1ea1b2dc5a466c4155826d53d14c4957cbbd143`.

**SHA-256 do ranking legado:** `5e989df3b50b2e5f84cab01af7fef4861dcb5eb63ecd0a2f5ae9f62ed9e8a260`.

**Implementação técnica:** [notebook `13_EXP-02B_auditoria_funcional_2026.ipynb`](../../notebooks/13_EXP-02B_auditoria_funcional_2026.ipynb) e [script `exp02b_auditoria_2026.py`](../../scripts/exp02b_auditoria_2026.py). A amostra foi determinística: primeira, central e última transação, em ordem cronológica, de cada endereço. Não houve retreino, reavaliação de scores ou mudança de limiar.

## Quadro sintético por contrato

| Endereço | Associação atual/documental | Tx no ranking | Tx no intermediário | Hash, from, to e dia na API | Chamadas no dia na amostra | Páginas de logs completas | Logs capturados |
|---|---|---:|---:|---:|---|---:|---:|
| `0x7251febeabb01ec9de53ece7a96f1c951f886dd2` | OKX DEX / TransparentUpgradeableProxy | 83 | 83 | 3/3 | seletor `0xec5b999d`, não decodificado; **1 revertida** | 3/3 | 21 |
| `0x5182fede730b31a9cf7f49c5781214b4a99f2370` | ApeCoin OFT Adapter | 16 | 16 | 3/3 | `send` ×3, sucesso | 3/3 | 36 |
| `0x57bedd7eb4c3118669f4f33a3cae4d4b554f24b7` | SwappableBridgeUniswapV3 | 66 | 66 | 3/3 | `swapAndBridge` ×3, sucesso | 3/3 | 30 |
| `0x80226fc0ee2b096224eeac085bb9a8cba1146f7d` | Chainlink CCIP Router | 119 | 119 | 3/3 | `ccipSend` ×3, **1 revertida** | 3/3 | 18 |
| `0x2f848984984d6c3c036174ce627703edaf780479` | MCT-XEN Batch Minter | 15 | 15 | 3/3 | `batchClaimRank` ×2; seletor `0x98190f47` não decodificado ×1; sucesso | **0/3** | **150 (50 por tx, páginas restantes não capturadas)** |
| `0x27428dd2d3dd32a4d7f7c497eaaa23130d894911` | Wormhole Standard Relayer / SimpleProxy | 16 | 16 | 3/3 | `deliver` ×3, sucesso | 3/3 | 15 |
| **Total** | **6 contratos** | **315** | **315** | **18/18** | **18 amostras** | **15/18** | **270 capturados; não o total real** |

### Controles efetivamente confirmados

- Todos os seis endereços obtiveram **HTTP 200** em `/addresses` e `/smart-contracts`, com `is_contract=true` e `is_verified=true`. A identificação da API **é atual**.
- Para **18/18** transações amostradas houve igualdade de hash, remetente, destinatário e data entre Parquet e API.
- Para **6/6** contratos, o número de transações **diretas recebidas** no intermediário é igual à contagem do ranking legado. **Isso não demonstra exaustividade de transações internas ou chamadas por Router**, nem igualdade hash-a-hash de todas as 315 com fonte externa.
- Os nomes de método provenientes do campo `method` decodificado pelo explorador sustentam associação **funcional** para pelo menos ApeCoin (`send`), SwappableBridge (`swapAndBridge`), CCIP (`ccipSend`), MCT-XEN (`batchClaimRank`) e Wormhole (`deliver`) **somente nas transações amostradas**.
- O OKX proxy usa seletor `0xec5b999d`, não mapeado nesta coleta. Três contratos com metadados `proxy_type=eip1967`: OKX, MCT-XEN e Wormhole. Nenhum deles possui **implementação histórica** verificada em 15/01/2026.
- **Duas chamadas amostradas reverteram** (uma OKX e uma CCIP), portanto evento ausente numa transação revertida não demonstra comportamento benigno nem malicioso.
- **150 de 270 logs** pertencem ao MCT-XEN, apenas suas primeiras páginas (50 por transação); `next_page_params` foi retornado nas três. Logo, **há lacuna mensurável de cobertura de eventos**, embora os três hashes das transações tenham sido confirmados.
- Não se observou evidência de transferência `deposit`/`withdraw` típica de mixer nas amostras decodificadas, **mas a ausência em 18 transações selecionadas não é evidência de ausência nos contratos ou no dia**.

## Discussão científica

**Achado novo:** a fonte externa corrobora o funcionamento de infraestruturas de interoperabilidade, DEX/bridge e operações em lote entre os endereços que o classificador estatístico sinalizou em 2026. Isso oferece **suporte empírico inicial à hipótese** de que entropias transacionais e média de chamadas, isoladas, não distinguem adequadamente contratos mixers de outros contratos com execução complexa.

**Não está demonstrado:** que os seis sejam necessariamente **não mixers** em toda a sua história, que sejam seis falsos positivos independentes, que o detector tenha precisão de 33,3%, que tenhamos identificado chamadas internas completas, ou que um modelo enriquecido já aumente desempenho. A própria amostra foi escolhida **entre alertas já conhecidos**, de modo que métricas gerais sofreriam viés de verificação.

## Próximos passos controlados

1. **Fechar a paginação dos logs das três transações MCT-XEN**, preservando `next_page_params` e terminando somente quando a API não devolver próxima página ou quando o limite máximo documentado for atingido. Registrar eventual lacuna.
2. **Documentar a função do seletor `0xec5b999d`** (OKX) e `0x98190f47` (MCT-XEN) por ABI ou implementação histórica; **não confiar em inferência apenas pelo nome**.
3. Obter evidência de **implementação ativa em 15/01/2026** dos proxies OKX, MCT-XEN e Wormhole, por bloco de cada amostra ou histórico de upgrades confiável. Caso indisponível, manter `inconclusivo_proxy_historico`.
4. Expandir para transações adicionais por endereço, com política predefinida, e complementar auditoria com endereço não alertado selecionado **sem conhecer o score**, para evitar validação enviesada.
5. Submeter rótulos a **dois revisores independentes**; somente classes com evidência independente e cobertura suficiente podem compor conjunto de verdade-terreno.
6. A melhoria contextual permanece **hipótese de engenharia**; exige features disponíveis em ambos os períodos, avaliação por contrato/protocolo, robustez temporal e métricas comparáveis em dados rotulados.

**Decisão:** preservar a reprodução e a avaliação 2026 já realizadas. Continuar na trilha de **qualidade do rótulo, cobertura de dados e contexto funcional**, sem ajustar retrospectivamente o limiar para obter resultado favorável.
