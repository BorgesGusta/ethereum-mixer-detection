# Painel da pesquisa

**Estado:** migração da pesquisa para um histórico versionado. Fonte dos dados pesados: [Drive](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj).

## Questões científicas

- **Reprodução:** que parte dos resultados do artigo de 2025 conseguimos reproduzir?
- **Robustez:** que decisões de amostragem, features e limiar modificam os alertas?
- **Generalização:** o modelo aprende padrões de mixers ou particularidades de um contrato?
- **Temporalidade:** quais variações são comportamento on-chain, quais são efeitos de cobertura/Router e como afetam a detecção?

## Estado histórico (16/11/2026) — preservado para rastreabilidade

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
- [x] Preparar estrutura LaTeX e bibliografia do artigo (v0.1 iniciada em 17/11; compilação pendente)

Consulte [[01_CRONOLOGIA]], [[02_EXPERIMENTOS]], [[03_DECISOES]], [[04_DADOS]] e [[05_PLANO]].


**Atualização de armazenamento (17/11/2026):** Drive próprio oficial: [Projeto_Mixers_Ethereum](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj). A pasta `mixers-ethereum` foi identificada como compartilhada por Bruno; o atalho foi removido do Meu Drive. Conferência integral da cópia por hash continua pendente.


## Checklist obrigatório para todas as sessões

Consulte e atualize o [CHECKLIST_VIVO.md](CHECKLIST_VIVO.md) antes de iniciar novo experimento. Para cada etapa informar objetivo, evidências, conclusão permitida e próximo passo. A reprodução do artigo ainda tem divergência quantitativa **63 alertas dos autores versus 9 alertas nossos** em 29/10/2020; **3/3 pools de referência recuperados** nas duas análises.


## Atualização operacional — 17/11/2026 (prevalece sobre pendências históricas acima)

- **EXP-01J executado:** RF e limiar 0,50 mantidos; `min_tx` 1/5/10/20 produziu 49/14/9/7 alertas no teste 2020, com 3/3 pools de referência. Demonstra sensibilidade de elegibilidade, **não** explica causalmente 63 versus 9. [Evidências](experiments/EXP-01J-resultados-sensibilidade-63x9.md).
- **EXP-02A:** análise legada de 15/01/2026 já conhecida (limiar 0,85, 20.214 elegíveis, 9 alertas, 3 pools de referência). Não é teste cego novo. [Inventário](experiments/EXP-02A-inventario-e-triagem-2026.md).
- **EXP-02B:** amostra de 18 transações entre seis contratos reconciliada externamente (18/18); contagens de transações diretas dos seis contratos totalizam 315. A verificação foi amostral, sem rótulos negativos finais. [Relatório](experiments/EXP-02B-resultados-auditoria-amostral-2026.md).
- **EXP-02C:** completada paginação dos logs de três transações MCT-XEN (83 + 83 + 300 = 466); junto dos 120 logs das demais 15 amostras, são 586 logs no conjunto de 18 transações. Não representa os logs de todas as 315 transações. Proxies históricos e dois seletores seguem inconclusivos. [Relatório](experiments/EXP-02C-resultados-logs-e-seletores.md).
- **Artigo:** `artigo/overleaf/` contém v0.1 editável com `.tex` e `.bib`; não há comprovação de compilação, aprovação ou submissão. [Plano de fechamento](manuscrito/plano-de-fechamento-e-apresentacao.md).
- **Pendências imediatas:** compilar/revisar manuscrito, conferir hashes integrais da cópia do Drive, amarrar versões de notebooks e resultados, reconciliar ADRs e obter rótulos independentes e dados por protocolo/período para validação nova.
- Documentação histórica pode conter itens ainda abertos ou já executados; para o estado operacional, prevalecem [CHECKLIST_VIVO](CHECKLIST_VIVO.md) e relatórios com manifestação de execução, sem apagar a cronologia.
