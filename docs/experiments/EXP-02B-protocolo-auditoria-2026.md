# EXP-02B — Protocolo de validação de rótulos negativos em 15/01/2026

**Criado em:** 17/11/2026. **Estado atualizado:** **execução amostral concluída no Colab em 17/11/2026**, com 18/18 hashes e contagens 315/315 conferidos; logs do MCT-XEN incompletos e rótulos ainda indeterminados. [Resultados EXP-02B](EXP-02B-resultados-auditoria-amostral-2026.md). Não altera limiar, modelo, amostras ou rótulos de `features_2026-01-15.parquet`.

## Universo e finalidade

Conjunto de investigação: **seis endereços não rotulados** sinalizados no teste legado de **15/01/2026** (limiar 0,85). Fonte canônica: [EXP-02A](EXP-02A-inventario-e-triagem-2026.md), [CSV](EXP-02A-matriz-triagem-2026.csv). Três pools Tornado Cash de referência são considerados positivos conhecidos pelo protocolo. **Não selecionar apenas endereços cujo nome sugira falso positivo para medir a precisão geral do modelo.**

## Procedimento por endereço

1. **Proveniência:** fixar rede Ethereum mainnet (`chainId=1`), endereço exato, hash SHA-256 dos registros de entrada, período UTC (00:00:00 a 23:59:59 de 15/01/2026) e dados/serviço do explorador.
2. **Atividade do dia:** extrair todos os hashes de transações externas dirigidas ao endereço na data, método (selector + ABI verificada), remetentes, blocos, `value`, recebedores de eventos e principais eventos de protocolo. Registrar **quantas transações existem na fonte** e se foi possível consultar a população completa da data (não inferir ausências de paginação incompleta).
3. **Proxies:** extrair implementação histórica para o(s) bloco(s) da data ou histórico verificável de upgrade. Em caso de indisponibilidade da prova, marcar como `inconclusivo_proxy_historico` em vez de assumir código atual.
4. **Identificação econômica:** confrontar funções/ABI e eventos efetivamente observados com documentação de protocolo, transações verificadas e, quando cabível, repositório oficial. **Um nome de contrato ou uma interação isolada com token não bastam para concluir não-mixer.**
5. **Revisão independente:** dois revisores registram evidência, juízo e possíveis conflitos sem conhecer o score, quando possível. Classes possíveis: `mixer_confirmado`, `nao_mixer_confirmado`, `indeterminado`. Falta de evidência → indeterminado.
6. **Rastreabilidade:** salvar `fonte_url`, `hash_tx`, `bloco`, `dia_utc`, `selector`, `evento`, `status_cobertura`, `codigo_historico_verificado`, `revisor_1`, `revisor_2`, `decisao_final`, `justificativa`. Incluir erros de API e data de consulta.

## Hipóteses por contrato a serem confirmadas **no dia**

| Endereço | Associação documental inicial | Verificação histórica específica |
|---|---|---|
| `0x7251febeabb01ec9de53ece7a96f1c951f886dd2` | OKX DEX: TransparentUpgradeableProxy | Implementação vigente em 15/01/2026; operações roteadas a DEX e eventos do proxy |
| `0x5182fede730b31a9cf7f49c5781214b4a99f2370` | ApeCoin OFT Adapter / LayerZero | Chamadas `send`, `lzReceive` e eventos de transferências cross-chain |
| `0x57bedd7eb4c3118669f4f33a3cae4d4b554f24b7` | SwappableBridgeUniswapV3 | Seletores de `swapAndBridge` e eventos de swap/bridge |
| `0x80226fc0ee2b096224eeac085bb9a8cba1146f7d` | Chainlink CCIP Router | `ccipSend`, mensagens/recebimento e evidências do CCIP |
| `0x2f848984984d6c3c036174ce627703edaf780479` | MCT-XEN Batch Minter | Funções e eventos de minting/batch mint |
| `0x27428dd2d3dd32a4d7f7c497eaaa23130d894911` | Wormhole Relayer | `sendPayloadToEvm`, relaying e logs de entrega |

Os nomes acima são **pistas para auditoria**, não afirmações de que todas as funções foram executadas no dia ou de que os seis são definitivamente negativos.

## Critérios para publicação de métricas

- Se todos os seis tiverem **revisão negativa independente e cobertura completa**, é válido calcular a **proporção de positivos confirmados entre os nove sinalizados auditados**, com amostra/escopo explícitos. Isso **não** caracteriza, por si só, a precisão em todas as 20.214 janelas avaliadas, nem recall/F1 gerais.
- Se houver rótulo `indeterminado`, apresentar contagem de confirmados e indeterminados, **intervalos conservadores** de proporção e referência à cobertura. Não denominá-los falsos positivos.
- Não calcular recall/precision/F1 em **toda a população** sem rótulos de positivos e negativos para uma avaliação corretamente amostrada e independente; evitar **verification bias** (apenas casos alertados auditados).
- Este protocolo é **exploratório/confirmatório de rótulos**, não um novo teste de generalização. Para robustez de novos mixers, observar EXP-02 com holdout de contratos/protocolos distintos e dados inéditos.

## Próxima execução

Primeiro, coletar uma amostra com hashes e funções de **15/01/2026** em fonte com cobertura de data garantida; priorizar os seis alvos acima. Não aumentar limites de paginação sem controle, não exigir novos tokens desnecessários, nem alterar o modelo por causa das evidências obtidas.

## Implementação técnica preparada em 17/11/2026 (não executada em dados reais)

- [Notebook EXP-02B de auditoria funcional](../../notebooks/13_EXP-02B_auditoria_funcional_2026.ipynb) — cópia [no Drive, para abrir no Colab](https://drive.google.com/file/d/1hKW2YgMYi86u2YKUs-l-4NOvTHmMN9La/view).
- [Script Python de auditoria](../../scripts/exp02b_auditoria_2026.py) — amostra determinística de até três hashes por endereço, metadados atuais e detalhes da transação/log na API v2 Blockscout.
- [Aula 05 e exercícios](../estudo/aula-05-auditoria-funcional-2026.md) — cópia [PDF no NotebookLM](https://drive.google.com/file/d/1RDNhyOZSxTmZvFytyFlFitlgLH7CtL_p/view).
- O notebook baixa pelo ID no Drive **somente** o `data/interim/dia_20260115.parquet` (arquivo histórico intermediário de ~369 MB) e `sinalizados_teste_2026.csv`, selecionando os seis destinatários no dia de teste.
- Extrai contagens locais por endereço, salva **todas as linhas locais dos seis**, e consulta **até 3 transações de cada um** com verificações de hash, destinatário, remetente e dia. `/transactions/{hash}/logs` é consultado na primeira página; paginação incompleta fica registrada, sem inferência por ausência.
- Cria pasta exclusiva em `results/` para `transacoes_locais_6_20260115.csv`, `resumo_6.csv`, `amostras_tx_api.csv`, `eventos_amostras.csv`, `metadados_atuais.csv` e `manifesto.json`, com SHA-256 das entradas e saídas.
- **Testes realizados nesta preparação:** sintaxe dos quatro blocos executáveis do notebook validada, e pipeline com seis endereços verificado por respostas simuladas da API. **A coleta on-chain e o processamento real do parquet ainda NÃO foram executados.**
- **Limite:** verificar 3/119 transações, por exemplo, não significa auditar todas as 119. Não conceder rótulo negativo independente nem calcular nova precisão geral nesta etapa.

**Próxima ação:** executar as quatro etapas no Colab; conferir CSVs e manifesto, identificar erros reais, selecionar endereços para coleta histórica completa e revisão de rótulos por dois avaliadores.


## Adendo pós-execução — 17/11/2026

A seção de preparação acima registra historicamente o estado **anterior à execução**. O notebook foi executado no Colab e salvou seis arquivos em [pasta própria do Drive](https://drive.google.com/drive/folders/1rV5mJ0rkINLML5aFUFnl0s7g1ybwrwOb). Todos os seis contratos tiveram contagens iguais ao ranking (total **315 transações diretas no dia**). As **18/18 transações amostradas** coincidem entre API Blockscout e arquivo intermediário quanto a hash, remetente, destinatário e data. **15/18 páginas de logs estão completas**; as outras três, todas MCT-XEN, trouxeram 50 logs cada e continuação da paginação. Todas as seis identidades seguem com `rotulo_cientifico=indeterminado`; nenhum código de proxy foi validado no bloco de janeiro/2026. [Resultados detalhados](EXP-02B-resultados-auditoria-amostral-2026.md).
