# EXP-06 — Inventário de candidatos a conjunto de referência de múltiplos protocolos

**Data:** 18/11/2026. **Estado:** pesquisa documental preliminar, NÃO executado como classificador/rotulagem ou experimento de desempenho. Caderno prévio à seleção de contratos e períodos. Não reusar os testes de 2020/2026 como holdout cego.

## Objetivo e definição de classe

Investigar se existem **contratos independentes do protocolo Tornado Cash** com mecanismo documentado de depósito em pool e retirada com vínculo origem-destino obscurecido, na **Ethereum mainnet**, em período verificável. Uma família de privacidade pode conter funções distintas e não ser tecnicamente equivalente. **Rótulo positivo exige**: identificação da implementação e endereço em Ethereum, contrato implantado no bloco/data estudado, evidência funcional de depósito/retirada e aderência à definição pré-registrada. Não bastam documentação atual, associação por nome ou saída do RF.

Não expandir a definição estreita de mixer retroativamente. Se necessário, abrir **uma segunda tarefa e classes hierárquicas**: (a) mixer de pool estrito, (b) outros pools de privacidade/escudos, (c) rollup/bridge de privacidade, (d) funções econômicas distintas, (e) inconclusivo. Revisão humana independente antes de binarização.

## Inventário com fontes primárias e próximos gates

| Família/candidato | Evidência documental consultada | Proposta de uso | Pendência / motivo de não inclusão imediata |
|---|---|---|---|
| Tornado Cash Classic ETH 0.1, 1, 10, 100 | [Deployments](https://docs.tornado.ws/general/deployments.html), [docs de funcionamento](https://docs.tornadoeth.cash/) e [repositório core](https://github.com/tornadocash/tornado-core) | Referência de comportamento de pool com depósito/saque; verificar pool 100 ETH e versões sem chamar de novo protocolo | Três pools já aparecem nos testes legados; 100 ETH é **mesma família/protocolo**, NÃO prova generalização a outro protocolo. Reconferir endereço em bloco e transações |
| Privacy Pools v1 (0xbow) | [Anúncio da desenvolvedora v2, com histórico de lançamento v1 em março/2025](https://0xbow.io/blog/privacy-pools-v2-is-live), [código oficial](https://github.com/0xbow-io/privacy-pools-core), [configuração oficial do site](https://github.com/0xbow-io/privacy-pools-website/blob/main/src/config/chainData.ts) | **Candidato prioritário de família distinta**, para conferir presença e função antes/depois de 15/01/2026 e se atende à classe operacional | Identificar contrato/pool exato e implantação histórica, eventos, versão/proxy ativa e critérios de associação set; **não rotular automaticamente** e não tomar endereço da versão atual como histórico |
| Privacy Pools v2 | [Deployments mainnet v2](https://docs.privacypools.com/deployments/mainnet), [anúncio oficial](https://0xbow.io/blog/privacy-pools-v2-is-live) | Candidato para janela temporal **posterior** ao deployment documentado em 2026, se desenhada nova avaliação | **Não elegível ao recorte 15/01/2026** se implantado apenas posteriormente. Confirmar bloco de implantação antes de selecionar período |
| RAILGUN Ethereum | [Documentação do shield](https://docs.railgun.org/developer-guide/wallet/transactions/shielding), [unshield](https://docs.railgun.org/developer-guide/wallet/transactions/unshielding), [deployments oficiais](https://github.com/Railgun-Community/deployments) | **Família comparativa em arquitetura distinta** de privacidade; possível classe separada/controle taxonômico | Shield/unshield e transações privadas não equivalem automaticamente à definição estreita de mixer de pool. Endereço/versão/ativo no período não foram validados nesta etapa |
| Aztec Connect histórico | [Repositório de contratos](https://github.com/AztecProtocol/aztec-connect-contracts), [rollup e bridge](https://aztecprotocol.github.io/aztec-connect/rollup_contract.html), [sunset](https://docs.aztec.network/aztec_connect_sunset) | Contraste de arquitetura rollup/bridge, não baseline positivo estrito | Depreciação/sunset e fase histórica distinta; não presumir 2026 nem equiparar função econômica |
| zkBob | [Repositório oficial de documentação](https://github.com/zkBob/docs) | Candidato adicional somente se houver deployment suportado na Ethereum mainnet | Documentação consultada destaca Polygon e Optimism, portanto **não foi confirmada elegibilidade na Ethereum mainnet**. Não transferir endereços de outras redes |

## Avaliação por contrato: requisitos antes da primeira coleta

Para cada candidato, preencher **antes da inferência do modelo**: `familia`, `rede_chainid`, `endereco`, `fonte_deployment`, `bloco_deployment`, `primeira_transacao`, `periodo_elegivel`, `classe_hipotese`, `revisor`, `evidencia_deposito`, `evidencia_retirada`, `estado_de_proxy_no_periodo`, `limite_de_cobertura`, `status` (candidato/indeterminado/elegível/fora do escopo), `sha256_dos_artefatos`.

Critério de inclusão **ainda não satisfeito** para família independente: endereço do contrato **validado historicamente**, aderência funcional da arquitetura, amostra de eventos e decisão de revisores. Não interpretar elegibilidade documental como rótulo.

## Regras metodológicas

1. **Não usar EXP-05 (9 alertas selecionados pelo RF) como teste confirmatório**, apenas como piloto de rotulagem de alertas. Revisores EXP-05 não devem receber scores nem as pré-classificações desta investigação antes de entregar suas fichas.
2. **Não escolher modelos, classes, limiares ou período com base nos outputs de 2020/15-01-2026.** Um futuro período independente precisa ser selecionado antes de observar sua classificação.
3. Separação por **família/protocolo e contrato**, sem misturar pools ou dias do mesmo protocolo entre treino e teste e chamar o resultado de generalização para protocolo inédito.
4. Negativos devem ser contratos legítimos **auditados no mesmo período e com função comparável**, nunca 'todos os outros endereços'; os seis alertas sem rótulo do EXP-05 não viram negativos automaticamente.
5. Registrar cobertura de transações diretas, traces e eventos; a falta de archive RPC continua restrição explícita, não evidência de ausência de contrato.
6. Métricas somente após ground truth independente, critérios de exclusão definidos e conjunto de teste congelado.

## Decisão inicial e backlog de execução

**Prioridade de pesquisa:** confirmar o **Privacy Pools v1 (0xbow)** como família de pools potencialmente distinta do Tornado, sem assumir que sua política de associação/abstração o torne equivalente. Em seguida conferir RAILGUN apenas como **categoria taxonômica distinta**. Tornado 100 ETH é controle adicional da **mesma** família. Privacy Pools v2 fica **fora de janeiro/2026**, sujeito a teste temporal posterior.

- [x] Fontes primárias/documentação de famílias candidatas consultadas.
- [x] Restrição taxonômica e temporal pré-definida.
- [ ] Confirmar endereço, chainId e bloco histórico do Privacy Pools v1 em fontes oficiais e explorador on-chain.
- [ ] Produzir registro de evidência funcional de depósito/retirada no período alvo, com hashes/versões.
- [ ] Submeter elegibilidade a revisão independente **fora** do processo cego do EXP-05.
- [ ] Criar controles não mixer com correspondência contratual e temporal, antes de qualquer cálculo de F1.
- [ ] Protocolo de divisão por protocolo e janela cronológica congelado antes de execução.

**No artigo:** inventário e motivação são proposta; nenhum candidato adicional recebeu rótulo e nenhum resultado novo de ML foi produzido aqui. Sem PDF.
