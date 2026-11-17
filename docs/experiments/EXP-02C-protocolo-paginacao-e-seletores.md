# EXP-02C — Fechamento de logs e verificação de assinaturas (15/01/2026)

**Preparação:** 17/11/2026. **Estado:** notebook e script desenvolvidos e validados quanto à sintaxe e paginação com resposta simulada; **AINDA NÃO EXECUTADO contra a API real nesta etapa**.

## Pergunta de pesquisa

No EXP-02B, todas as 18 transações amostradas foram confirmadas na API Blockscout e as contagens locais dos seis contratos somaram 315 transações diretas em 15/01/2026. Porém, **três transações do MCT-XEN receberam 50 logs na primeira página e `next_page_params` não nulo**, ou seja, **150 logs inicialmente coletados não correspondem à coleção completa**. Além disso, dois seletores de funções permaneceram sem decodificação: **`0xec5b999d` no OKX/TransparentUpgradeableProxy** e **`0x98190f47` no MCT-XEN**.

## Estratégia e controle experimental

1. Reutilizar apenas dois arquivos pequenos da execução anterior: `amostras_tx_api.csv` (Drive ID `17S6xCYOng7Fk21cYZGq5k1yKzNn3kqGq`) e `eventos_amostras.csv` (Drive ID `1NwJFLTrrMtpLndn2vMV7fLzy9oQJMlH6`). **Não baixar o Parquet de ~369 MB**; não classificar nenhum endereço novo.
2. Selecionar exatamente as **três transações MCT-XEN cuja página de logs está incompleta**; se o arquivo não contiver três, abortar explicitamente em vez de modificar silenciosamente a seleção.
3. Reconsultar a primeira página da API `GET /api/v2/transactions/{hash}/logs` e **passar o objeto `next_page_params` inalterado como parâmetros da página seguinte**. Limites predefinidos: no máximo 30 páginas e 4.000 logs por transação, com pausas entre consultas e tratamento de HTTP 429/5xx.
4. Confrontar emissor e `topic0` da primeira página obtida novamente com os logs preservados no EXP-02B; detectar repetição de cursor ou índices de log. **Não deduplicar automaticamente dados que divergem.**
5. Obter a **ABI atual** de dois contratos no Blockscout e calcular os identificadores com **Keccak-256** (não `SHA3-256` da biblioteca padrão). Conferir se algum seletor possui correspondência na ABI atual; opcionalmente obter sugestões globais do `4byte.directory`, que não são prova do contrato de origem.
6. Preservar todas as páginas JSON retornadas, as ABIs atuais, CSV de status por transação, CSV consolidado dos logs, correspondências dos seletores e manifesto com SHA-256 das entradas/saídas.

## O que a execução poderá concluir

- **Se `next_page_params = null` ao final das três transações**, a paginação dos logs **dessas três transações** foi concluída. Isso não comprova exaustividade de todas as transações do contrato no dia, nem de logs relativos a outras cadeias.
- **Se não chegar ao fim**, registrar `paginacao_completa=false` e motivo de parada (HTTP, cursor repetido, limite).
- **Se uma assinatura aparecer na ABI atual**, pode ser relatada como **candidata compatível com o código/ABI atual**. Para o proxy atualizado, ela **não comprova** qual implementação ou função estava ativa em 15/01/2026.
- **Se o 4byte.directory sugerir assinaturas**, são hipóteses não verificadas de decodificação; podem existir colisões de 4 bytes. Não atribuir função histórica com base somente nesses resultados.
- Nenhum resultado implica `nao_mixer_confirmado`, `mixer_confirmado` ou melhor desempenho do classificador. Os seis rótulos do EXP-02B permanecem indeterminados até revisão independente e cobertura histórica adequada.

## Arquivos e links operacionais

- [Notebook EXP-02C no GitHub](../../notebooks/14_EXP-02C_logs_MCT_XEN_e_abi.ipynb)
- [Script Python versionado](../../scripts/exp02c_logs_abi.py)
- [Relatório EXP-02B (executado)](EXP-02B-resultados-auditoria-amostral-2026.md)
- [Resultados EXP-02B no Drive](https://drive.google.com/drive/folders/1rV5mJ0rkINLML5aFUFnl0s7g1ybwrwOb)

## Próximas dependências após o EXP-02C

- Investigar `eth_getStorageAt` do slot EIP-1967 ou sequência completa de eventos de upgrade no bloco **das transações** para OKX, MCT-XEN e Wormhole, com provedor com estado histórico válido; consultas sem arquivo não confirmam ausência de upgrade.
- Expandir amostragem e incluir endereços não sinalizados por seleção prévia ao acesso aos scores; executar revisão independente de rótulos.
- Construir positivos de outro protocolo de mixers para avaliação por protocolo/contrato; só então medir melhoria de detecção contextual com baseline Random Forest inalterado.
