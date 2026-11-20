# EXP-03C — Piloto mínimo de consulta a estado histórico Ethereum

**Preparado:** 18/11/2026 UTC. **Status: NOTEBOOK DISPONÍVEL; NÃO EXECUTADO.** Não reexecutar EXP-03B em seis controles até uma fonte histórica funcionar em uma referência conhecida.

## Motivação e relação com Segurança de Redes

O piloto usa **verificação de evidência e controle positivo de observabilidade**, etapa típica de uma investigação forense e de sistemas de detecção baseados em alertas. A pesquisa como um todo pode ser interpretada pela ótica de **detecção de anomalias + triagem de alertas**, análoga ao encadeamento IDS → alerta → validação contextual, sem igualar mixers a intrusões. A confirmação de que o assunto pertence ao **conteúdo específico da disciplina cursada** depende da ementa ou slides do professor; não foi verificada.

## Fontes de referência

- [API Ethereum: eth_getCode](https://ethereum.github.io/execution-apis/next/api/methods/eth_getCode/) especifica código de uma conta em um bloco; saída é estado depois da execução do bloco.
- [Ethereum: archive nodes](https://ethereum.org/developers/docs/nodes-and-clients/archive-nodes/) explica necessidade de estados históricos.
- [Infura: archive data](https://docs.infura.io/concepts/archive-data/) documenta consultas históricas de estado, incluindo eth_getCode; exige endpoint de projeto.
- [Chainstack: archive node](https://chainstack.com/what-is-an-archive-node/) informa archive no plano Growth; plano Developer grátis sem archive (conforme página consultada em 18/11/2026).
- Outros fornecedores podem variar a disponibilidade por plano e região. Nenhum provedor novo foi testado nesta etapa; **compatibilidade real do endpoint precisa ser comprovada experimentalmente**.

## Notebook pronto no Drive

- [17_EXP-03C_diagnostico_rpc_historico.ipynb](https://drive.google.com/file/d/1V4u21nJV1gNuAv_7qhO6f1qLAkyJVMIl/view?usp=drivesdk), na pasta oficial `notebooks/00_ATIVOS/`.
- [Cópia versionada no GitHub](../../notebooks/17_EXP-03C_diagnostico_rpc_historico.ipynb), commit `b6442e3aaf3b1afb0cb523cbaf51c6f5073fd0fb`.
- SHA-256 do notebook (criação local antes do upload): `16c17454421fac848afc3904cc15d9f01ef11c83c07fc7e8008516976e654c7e`. Arquivo do Drive conferido em listagem e conteúdo; evitar afirmar paridade de SHA do Drive sem cálculo posterior.

## Protocolo pré-registrado

1. Usar **endpoint HTTPS autenticado de archive RPC da rede Ethereum mainnet** obtido pelo pesquisador; entrar via `getpass` no Colab. **Nunca registrar a URL tokenizada em resultados, notebooks, GitHub ou mensagens.** Não pedir que o usuário cole token no chat.
2. Checar `eth_chainId=0x1`; se diferente, `NO_GO_WRONG_NETWORK`.
3. Checar `eth_getCode` do contrato WETH (`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`) no bloco `24236673`. Código não vazio: valida capacidade de consultar **um** estado histórico conhecido (não prova disponibilidade global).
4. **Somente se passar:** consultar um controle congelado `0xbd70bb67c90ea7d01abcf5b0c973a3830c7cff88` no mesmo bloco; registrar código presente/vazio/inconclusivo, comprimento e SHA-256 do código. Um código vazio demonstra somente o estado desse endereço **nesse bloco**.
5. Salvar `diagnostico_archive.json` numa nova pasta `results/EXP-03C_diagnostico_archive_*` do Drive oficial, sem sobrescrever arquivos.
6. Só ampliar para os demais cinco controles depois de inspecionar a evidência de êxito e as limitações. Mesmo provedor funcionando não cria rótulos independentes.

**Cautela:** `NO_GO_ARCHIVE` significa **o provedor consultado** não comprovou acesso na referência, não que a rede Ethereum não contenha o histórico nem que o endereço seja uma EOA.

## Dependências e critérios de fechamento

- [x] Protocolo e notebook disponíveis, fonte verificada documentalmente.
- [ ] Provedor autenticado selecionado pelo pesquisador e consulta piloto executada.
- [ ] Conferência dos outputs/hashes no Drive e registro do status experimental.
- [ ] Só se `PILOT_RPC_OK`, preparar etapa seguinte de no máximo cinco controles sem alterar a amostra.

**Nenhuma alteração do detector RF; nenhuma métrica F1/recall/precision, nenhum PDF de artigo.**
