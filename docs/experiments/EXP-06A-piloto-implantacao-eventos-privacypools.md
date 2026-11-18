# EXP-06A — Verificação de implantação e evidências de depósito (piloto)

**Preparado em:** 18/11/2026. **STATUS: NOTEBOOK DISPONÍVEL; NÃO EXECUTADO NO COLAB.** É verificação de provas de implantação e de eventos, sem novos modelos, rótulos ou estimativas de desempenho.

## Evidências antes do piloto

- A [documentação oficial da 0xbow](https://0xbow.io/blog/getting-started-with-privacy-pools) identifica Pool ETH `0xF241d57C6DebAe225c0F2e6eA1529373C9A9C9fB` e Entrypoint `0x6818809EefCe719E480a7526D76bD3e561526b46`.
- A [configuração oficial do site](https://github.com/0xbow-io/privacy-pools-website/blob/main/src/config/chainData.ts) declara `deploymentBlock=22153707`; **esse valor não foi validado por consulta à transação de criação**.
- Um [inventário externo](https://prifi.info/protocols/privacy-pools/) aponta como possíveis referências a transação de criação do pool `0x6e3e14d7bcdfa838a8f7918de81d7b233e40d3afd493a864285fad8b360bcf75` e a primeira transação de depósito `0x55693706fddd4130a3b07fefa274c0b7730281c37e48725aa6aa8e1b7dca4948`. A API Blockscout não respondeu nesta consulta web; esses dois hashes **ainda são candidatos não validados diretamente**.
- **Evidência de transação independente já consultada no Etherscan:** [transação `0x495294c929babdbc035041904bb87d8fc2494c1c7841e2e6e074b84367a5dcef`](https://etherscan.io/tx/0x495294c929babdbc035041904bb87d8fc2494c1c7841e2e6e074b84367a5dcef), bloco **22169054** de **31/03/2025 19:42:59 UTC**, sucesso, chamada `deposit(uint256)` ao Entrypoint, transferência interna de **0,1 ETH** ao pool e evento **`Deposited`** nos logs do endereço do pool. A exibição de evento decodificado depende da interpretação do explorador/ABI, embora o hash, o bloco, o destinatário, o registro do log e a movimentação estejam disponíveis na página de transação. **Apenas demonstra uma operação de depósito observada, não saída desvinculada nem equivalência taxonômica ao Tornado Cash.**
- Para completar o critério de equivalência é necessário demonstrar retirada e o mecanismo de desvinculação por fontes oficiais e dados históricos, além de análise por revisores independente do EXP-05.

## Notebook operacional

- [`18_EXP-06A_validacao_implantacao_privacypools_v1.ipynb` no Drive](https://drive.google.com/file/d/14so42iaP7joZ2OR5LkYLq20osUJE61Ha/view?usp=drivesdk), na pasta `notebooks/00_ATIVOS`.
- [Notebook versionado no GitHub](../../notebooks/18_EXP-06A_validacao_implantacao_privacypools_v1.ipynb), commit `d7d4422addae8cb41b07a279dea65bbeeddcaf2c`. SHA-256 da versão publicada `350f8e22f4a6444400a6e2129e51191a6555c81346b790e5afb9a04bfc793ccd`.
- [Script de verificação versionado](../../scripts/exp06_validar_implantacao.py), commit `c28e9ad9b129e0e0deb2433ded5509630b4ac479`, SHA-256 `64d05561e236b91b53f57271421dce012e9268bb152af1dddb0dca4d3c961a21`. Cópia do script também preservada no [Drive](https://drive.google.com/file/d/1LE2-9zV3Aadpmmx2e2AxXy6BMSbKFL6j/view).
- **Teste local executado:** compilação do Python e teste sintético com respostas simuladas para criação e depósito passaram. **Não houve consulta real à API via Python local** nem inferência. Isso não é uma execução do EXP-06A.
- Ao executar no Colab: autenticar Drive, baixar script pelo commit fixo, verificar hash, chamar API Blockscout para as duas transações predefinidas, consultar logs paginados do depósito, gerar `verificacao_exp06a.json` + `manifesto_exp06a.json` em **nova pasta** sob `results`. Não sobrescreve artefatos existentes.

## Gates de validação

1. **GO evidência da implantação:** a transação de criação deve ter status de sucesso, `created_contract` igual ao pool e bloco de implantação coerente com referência declarada; divergências permanecem abertas, não ajustar valores retroativamente.
2. **GO evidência de depósito:** transação em bloco identificado, conclusão de logs, ao menos um log do pool e status bem-sucedido. A nomenclatura de evento/função deve ser confirmada na implementação histórica para rótulo funcional.
3. **NO-GO API:** HTTP não 200, resposta sem campos, paginação inconclusiva, ou endereço divergente => `inconclusivo`, sem inferir ausência de implantação/atividade.
4. **Rótulo científico:** exige evidência adicional de retiradas e mecanismo de privacidade, revisão independente, definição da classe; **não atribuído automaticamente**.

**Restrições:** não há ground truth novo, nem teste do Random Forest, nem avaliação de generalização para protocolo externo; artigo PDF suspenso.
