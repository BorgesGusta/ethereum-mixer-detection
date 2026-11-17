# EXP-01D — Triagem on-chain dos três alertas pendentes (17/11/2026)

## Execução e proveniência

- [Pasta no Drive do pesquisador](https://drive.google.com/drive/folders/1nx4JGAkaurP6Nvry_3B03iQYd8Q_KhdH)
- [CSV de metadados](https://drive.google.com/file/d/13jmytV0X3JrnfW_hzmJfdh4j95qQgdCD/view)
- [JSON de respostas completas da API](https://drive.google.com/file/d/1oE693nsSOJaXf3X6AsFUpp0GKGN0nvly/view)
- Horário UTC dos metadados: 2026-11-17T13:34:15.631370+00:00.
- Fonte: Blockscout Ethereum Mainnet, endpoints `/api/v2/addresses/{endereco}` e `/api/v2/smart-contracts/{endereco}`.
- Ambas as consultas de cada um dos três endereços retornaram HTTP 200. Os dados originais ficam no Drive; não sobrescrever arquivos de treino/teste.

## Identificações observadas diretamente

| Endereço | Score RF | is_contract | Nome Blockscout | is_verified | Observações na resposta |
|---|---:|---|---|---|---|
| `0x5e60fcca904753a31f9df7d7f6b7856b6ec27aa9` | 1,00 | true | AdminUpgradeabilityProxy | true | proxy_type=eip1967; implementação apontada `0xee2fCEcFb2075A85a31eE8676cE9Ae5f3c3be6D7`; **a identidade/função dessa implementação não foi auditada** |
| `0x98f1858c9740b9c5f2cd8abea67948873d38dc39` | 0,98 | true | SmartEther | false | token ERC-20; símbolo SMARTE; código não verificado na fonte consultada |
| `0xe113d58a4cb4dbac8a0da608ed7232785c1f2c18` | 0,76 | true | DSProxy | true | código-fonte verificado; estrutura genérica de execução de ações |

**Todos os três endereços foram identificados quanto à natureza geral de contrato**, mas não foram classificados definitivamente como mixer ou não mixer. Nos proxies, o nome de infraestrutura genérica não identifica a aplicação ou o protocolo de uso. A API retornou metadados contemporâneos à execução; é necessário auditar se e como se relacionam com as transações específicas de 29/10/2020, incluindo possível upgrade do proxy após essa data.

## Estado dos 9 alertas

- 3 pools Tornado de referência usados no artigo: 0,1 ETH, 1 ETH e 10 ETH.
- 1 pool Tornado adicional identificado no histórico: 100 ETH, sem rótulo no parquet do teste.
- 2 endereços associados documentalmente a outros protocolos: ForTube BANK e zkSync.
- 3 endereços agora identificados por metadados: AdminUpgradeabilityProxy, token SmartEther, DSProxy.

**Não usar a divisão 4/9 como precisão científica** nem declarar todos os outros cinco como falsos positivos. É necessário ground truth e auditoria independente. O achado não resolve por que o artigo reporta 63 alertas, ao passo que a reprodução reporta 9.

## Próximas ações

1. Determinar a identidade e evolução histórica do proxy upgradeable `0x5e60…`; inspecionar implementação, deploy e upgrades em 2020.
2. Inspecionar transações/eventos de 29/10/2020 de cada um dos três contratos para correlacionar as features de atividade com operações reais.
3. Estabelecer protocolo de rotulagem externa e confirmar classes negativas sem vazamento temporal.
4. Retomar comparação de filtros, amostragem, regras de features e treino com artigo, especialmente após eventual resposta dos autores.
