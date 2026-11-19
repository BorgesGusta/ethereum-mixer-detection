# EXP-06C — Auditoria das retiradas históricas (19/11/2026)

**Execução do Colab:** 19/11/2026 18:21:50 UTC. **Status: EXECUTADO E AUDITADO.** Conclusão limitada: **4 transações históricas bem-sucedidas verificadas** com logs emitidos pelo pool ETH e topic0 previamente identificado como `Withdrawn`. **Não demonstra por si só desvinculação entre depositante e sacador, não atribui rótulo do dataset, não avalia modelo.**

## Proveniência e integridade

- [Pasta oficial](https://drive.google.com/drive/folders/1O9mAvAPx4HOER9Cn-GduUSCmriISVAnC), [`evidencias_exp06c.json`](https://drive.google.com/file/d/1GAxZBNyOROeZhJEelZeIct338924tjXX/view), [`manifesto_exp06c.json`](https://drive.google.com/file/d/1BmaLC5ICARuEMoaERGGd_hd_375FVYSc/view).
- SHA-256 de `evidencias_exp06c.json` **recalculado sobre bytes baixados**: `f2c6243979fbb38266718f9ed28884abf4b9a7edf3439a1cf8cf1db606ba6922`; **igual ao manifesto**. SHA de entrada EXP-06B `61e60f28fd23af38e09f8ae2a6ae23d56699536e2667f7d0d1f875adebbc207f`.
- [Protocolo congelado antes da execução](EXP-06C-protocolo-retiradas-historicas.md), [script](../../scripts/exp06c_retirada_historica.py), [notebook](../../notebooks/20_EXP-06C_retiradas_historicas_privacypools.ipynb).
- Os registros abaixo provêm **da consulta à API Blockscout feita no Colab**, analisada pelo JSON; não houve segunda consulta independente à blockchain nesta auditoria. Os timestamps UTC exatos dos quatro blocos não foram obtidos neste JSON.

## Evidências auditadas

| Janela | Bloco | Tx de sucesso | Log do pool com `topic0` Withdrawn | Paginação tx completa |
|---|---:|---|---|---|
| Pós-implantação 2025 | 22167564 | [`0x51fdc6cf55af6598544db3cef441e405df9a24d17d7ca9e47a287828839aa786`](https://eth.blockscout.com/tx/0x51fdc6cf55af6598544db3cef441e405df9a24d17d7ca9e47a287828839aa786) | 1 de 3 logs | sim |
| Pós-implantação 2025 | 22168311 | [`0x3980801e0e16345198639eddd4b3caef9100b5370e6ec9aaf08855b5fa171304`](https://eth.blockscout.com/tx/0x3980801e0e16345198639eddd4b3caef9100b5370e6ec9aaf08855b5fa171304) | 1 de 3 logs | sim |
| Vizinhança de janeiro/2026 | 24233404 | [`0x8d32089f4533096bc23e8f94ba4d12e0e30324948431dcb6bc84678b1b1c4410`](https://eth.blockscout.com/tx/0x8d32089f4533096bc23e8f94ba4d12e0e30324948431dcb6bc84678b1b1c4410) | 1 de 3 logs | sim |
| Vizinhança de janeiro/2026 | 24234863 | [`0x119ee6fa2175cfd2dad4a9843f0141bc3e9a5e0ddbc1c58e188fe1ed44bbaffc`](https://eth.blockscout.com/tx/0x119ee6fa2175cfd2dad4a9843f0141bc3e9a5e0ddbc1c58e188fe1ed44bbaffc) | 1 de 3 logs | sim |

Todos os hashes foram conferidos via `/api/v2/transactions/{hash}` (HTTP 200, `status=ok`, bloco correto, `to=Entrypoint 0x6818809eefce719e480a7526d76bd3e561526b46`) e `/api/v2/transactions/{hash}/logs` (HTTP 200, 3 logs, ausência de `next_page_params`, 1 log do pool com `topic0=0x75e161b3e824b114fc1a33274bd7091918dd4e639cede50b78b15a4eea956a21`).

## Cobertura e interpretação

- Janela 2025 predefinida 22153714–22253714: consultas de dois lotes 22153714–22163713 sem eventos e 22163714–22173713 com **3 candidatos vistos**; validação dos 2 primeiros e parada antecipada. **Não dizer que varremos toda a janela.**
- Janela 2026 predefinida 24233073–24240273: consulta única retornou **13 candidatos de log**, porém **somente 2 inspecionados como transações individuais**; toda a janela configurada foi consultada, não os 13 receipts. Não relatar 13 saques validados.
- A API v1 foi usada para localizar logs pelo topic0 já definido, com API v2 para confirmação individual. A assinatura e nomes vêm de registros observados anteriormente, **sem auditoria independente da ABI/implementação histórica**. Eventos `Ragequit` foram propositalmente excluídos.
- A janela de 2026 é **diagnóstico sobre recorte já explorado**, não validação cega nem teste de generalização.
- **Nenhum ground truth, recall, precision ou F1 novo.** A confirmação on-chain de logs de retirada não basta para classificar a arquitetura como mixer equivalente à classe binária de Tornado Cash.

## Decisão e próximo fechamento

EXP-06A: atividade de depósito; EXP-06B: trace interno `CREATE` de sucesso no bloco 22153714 (divergência com bloco declarado 22153707 ainda aberta); EXP-06C: quatro transações de retirada verificadas em 2025/2026. **Triangulação documental significativa**, mas protocolo distinto ainda **candidato sem rótulo**. A principal lacuna de metodologia é a equivalência funcional à definição estreita do detector e revisão de evidência histórica de contrato. Como prazo de entrega é 20/11/2026, recomenda-se **não abrir novos experimentos de coleta**; integrar como estudo de caso exploratório e priorizar o artigo e, se dados permitirem, pequena comparação de modelos EXP-07 sem inventar métricas.
