# Painel da pesquisa

**Estado:** migração da pesquisa para um histórico versionado. Fonte dos dados pesados: [Drive](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj).

## Questões científicas

- **Reprodução:** que parte dos resultados do artigo de 2025 conseguimos reproduzir?
- **Robustez:** que decisões de amostragem, features e limiar modificam os alertas?
- **Generalização:** o modelo aprende padrões de mixers ou particularidades de um contrato?
- **Temporalidade:** quais variações são comportamento on-chain, quais são efeitos de cobertura/Router e como afetam a detecção?

## Estado atual (16/11/2026)

- Treino legado: 123 janelas, 23 positivas, todas referentes ao pool Tornado Cash 10 ETH em dias de março/2025.
- Teste 29/10/2020: 4.038 janelas elegíveis (>=10 tx); recuperação dos 3 pools de referência depende do modelo e limiar.
- Teste 15/01/2026: 20.214 janelas elegíveis; RF no limiar 0,85 sinalizou 9 endereços incluindo 3 pools de referência. Outros alertas não são automaticamente falsos positivos.
- Exp. 10: Extra Trees F1 interno médio 0,9810 versus 0,9612 da RF, **sem generalização por contrato comprovada**.
- Exp. 11: Extra Trees no limiar 0,85 recuperou 0/3 pools em 2020 e 3/3 em 2026; RF recuperou 3/3 nos dois dias. O limiar não é calibrado igualmente para ambos.
- Exp. 12.00–12.02B: auditorias de inventário, viabilidade 2020, entropia interna e atribuição via Router concluídas; features conferidas nos quatro pools 2020 e três pools 2026.
- A coleta de chamadas intitulada 2025-03-15 abrange de 15 a 21/03/2025; documentar intervalo real.
- Treino exclusivo de 2020 e painel anual 2021–2024 **pendentes**.

## Próximas ações

- [ ] Vincular notebooks reais e versões de cada execução, sem sobrescrever originais
- [ ] Montar tabela de decisões vigentes versus substituídas
- [ ] Auditoria da disponibilidade de dados e contratos para treino de 2020
- [ ] Preparar plano de coleta temporal e protocolo de validação
- [ ] Preparar estrutura LaTeX e bibliografia do artigo

Consulte [[01_CRONOLOGIA]], [[02_EXPERIMENTOS]], [[03_DECISOES]], [[04_DADOS]] e [[05_PLANO]].


**Atualização de armazenamento (17/11/2026):** Drive próprio oficial: [Projeto_Mixers_Ethereum](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj). A pasta `mixers-ethereum` foi identificada como compartilhada por Bruno; o atalho foi removido do Meu Drive. Conferência integral da cópia por hash continua pendente.
