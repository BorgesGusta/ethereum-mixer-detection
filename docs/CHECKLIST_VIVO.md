# Checklist vivo — Detecção de Mixers na Ethereum

**Atualizado:** 2026-11-17  
**Fonte acadêmica:** Pedro Leale e Ivan da Silva Sendin, *Uma Proposta de Algoritmo para a Detecção de Mixers na Ethereum*, SBSeg 2025 (PDF original arquivado no Drive do projeto, em `00_artigo/`).

> Toda atualização de pesquisa deve manter: **o que foi feito**, **por que**, **evidência**, **o que o resultado NÃO demonstra** e **próxima ação**. As caixas aqui são estado de execução; não significam aprovação científica sem evidência.

## Estado do projeto

**Comunicação científica:** [x] E-mail enviado aos dois autores em 17/11/2026 solicitando detalhes metodológicos, dados/código e lista dos 63 endereços. [ ] Resposta recebida e analisada. O envio não implica concordância ou resposta dos autores.


### A — Organização e rastreabilidade
- [x] Repositório oficial GitHub criado e conectado
- [x] Drive próprio `Projeto_Mixers_Ethereum` adotado; atalho da pasta de Bruno removido, originais preservados
- [x] Copiar acervo central de dados, notebooks e relatórios para Drive próprio
- [x] Separar notebooks ativos e legados
- [x] Definir quatro notebooks canônicos e padrão didático/visual
- [ ] Auditar **hash SHA-256 completo** de todos os dados binários copiados, manifestos e resultados
- [ ] Vincular cada notebook legado à versão executada, protocolo e resultados exatos

### B — Reprodução do artigo
- [x] Recuperar e conferir PDF do artigo dos autores
- [x] Recriar pipeline central RF com as quatro features, 100 árvores, max_depth=5, class_weight balanced e limiar 0,50
- [x] Treinar com conjunto de março/2025 e executar inferência em 29/10/2020
- [x] Identificar 3/3 pools Tornado de referência e 239 transações associadas a 0.1/1/10 ETH
- [x] Executar notebook consolidado 01, salvar CSVs e comparar CV fold a fold com o legado
- [ ] Explicar **por que artigo identificou 63 endereços, mas nossa reprodução identificou 9**, mesmo com três pools corretos
- [x] Publicar etapa didática de diagnóstico no próprio notebook 01 (gráficos de probabilidade, curva de limiares e exportação dos scores por endereço)
- [x] Executar o diagnóstico no Colab e conferir os cinco artefatos produzidos em 17/11/2026 (4.038 elegíveis; nove alertas no limiar 0,50)
- [x] Identificar um pool adicional de **100 ETH (0xa160…f291)** entre os nove alertas, com score 0,87, sem rótulo `tornado` no parquet; cruzamento com relatório anterior confirma o pool conhecido. **Referência artigo: 3/3; referência expandida: 4 conhecidos entre 9**.
- [x] Auditar documentalmente os nove alertas: 3 pools de referência + pool 100 ETH conhecido + 2 contratos identificados externamente (ForTube BANK e zkSync) + 3 ainda não identificados
- [ ] Verificar independentemente na blockchain a identidade e atividade dos três restantes, além de validar rótulos negativos sem presumir falsos positivos
- [ ] Auditar a rotulagem da classe de referência e os critérios de negativos
- [x] Conferir que 1.114.702 transações e as 239 do Tornado Cash coincidem com o artigo no recorte 2020
- [x] Localizar diferença de contagem de endereços: **230.658 destinatários únicos**, exatamente o número publicado; 294.232 remetentes únicos e 377.296 na união. Verificar no artigo se 'endereços distintos' corresponde à projeção de destinatários.
- [ ] Conferir identificação exata e scores dos nove endereços versus os relatórios legados
- [ ] Reconstituir equivalência de amostragem/rotulagem dos 100 negativos e 23 positivos e das regras de elegibilidade
- [ ] Auditar toda diferença de protocolo, features e limiares em relação ao artigo **sem afirmar identidade não demonstrada**

### C — Auditoria
- [x] Auditoria 12.02A/B: relatório de paridade em 7/7 combinações de 2020/2026 com referência
- [x] Evidenciar diferença de atribuição direta em 2020 e via Router em 2026; 2025 possui descompasso temporal 15–21/03
- [x] Executar notebook 04 com verificações documentais e três gráficos, salvar manifesto e PNGs
- [ ] Implementar e executar **auditoria independente desde dados brutos**, com chamadas completas e janelas equivalentes
- [ ] Executar suíte de testes dos módulos `src/ethmix`

### D — Contribuição científica
- [ ] Definir hipóteses de generalização para novos contratos e períodos **antes** dos próximos experimentos
- [ ] Criar treino histórico 2020 com múltiplos dias/pools e negativos auditados
- [ ] Harmonizar traces/Router, cobertura e datas em 2020–2026
- [ ] Treinar e testar com separação por tempo e contrato, evitando vazamento
- [ ] Executar comparação justa de RF, Extra Trees e modelos adicionais
- [ ] Redigir manuscrito no Overleaf com tabelas/figuras rastreáveis

## Por que essa reprodução ainda não é exata?

**Checagem adicional no texto original (17/11/2026):** a seção 4 do artigo menciona explicitamente **balanceamento por reamostragem antes do RandomForestClassifier**, além de 100 negativos com ≥10 transações. Portanto, o uso de reamostragem não é, por si só, uma divergência comprovada. Permanecem não especificados na mesma granularidade: sorteio exato dos 100 endereços, definição das 23 janelas positivas da nossa cópia, arredondamentos das entropias e decisões de pré-processamento.


| Ponto | Autores (PDF, seções 4–5) | Nossa reprodução verificada |
|---|---|---|
| Modelo | Random Forest, 100 árvores, profundidade 5, classes balanceadas, probabilidade >0,50 | Mesma configuração central |
| Treino | Tornado 10 ETH de março/2025 e 100 endereços aleatórios não mixer inspecionados no Etherscan | 23 janelas positivas de um único pool, 100 negativas selecionadas; **igualdade exata da amostra não demonstrada** |
| Teste | 29/10/2020, 1.114.702 transações, 230.658 endereços; 73+55+111=239 transações dos três pools | Mesmo dump/intervalo usado; 3 pools recuperados |
| Endereços sinalizados | **63** (3 Tornado, 60 restantes classificados pelos autores como outros serviços) | **9** no limiar 0,50 (3 Tornado, 6 demais **não verificados independentemente**) |

**Resultado cientificamente permitido:** metodologia geral e recuperação dos três contratos foram reproduzidas; **o total de alertas difere significativamente (9 vs 63)** e o protocolo completo ainda não foi demonstrado como equivalente. O F1 médio de CV de nosso treino (0,9778) não é uma métrica comparável publicada pelos autores. Não chamar os alertas adicionais de falsos positivos antes de verificação.


## Triagem documental dos nove alertas (17/11/2026)

- [x] Produzir [tabela auditável com 9 IDs, scores e fonte](experiments/EXP-01C-triagem-9-alertas.csv).
- [x] Produzir [relatório com limites dos rótulos](experiments/EXP-01C-triagem-9-alertas.md).
- [x] Confirmar 4 contratos Tornado conhecidos na referência expandida (3 no artigo + pool 100 ETH).
- [x] Encontrar fontes documentais para outros dois alertas: ForTube BANK e zkSync; **não tratá-los ainda como negativos verificados**.
- [x] Pesquisar os três endereços nas fontes públicas indexadas; **nenhum nome foi confirmado**, e acesso direto a exploradores não estava disponível nesta sessão. Manter o status *não identificado*, não inferir EOA/mixer.
- [x] Preparar etapa 9 no mesmo notebook 01: consulta aos endpoints públicos do Blockscout, preservando respostas e erros para auditoria, com salvamento opcional no Drive. Notebook validado sintaticamente, **a consulta NÃO foi executada no Colab ainda**.
- [x] **Executar etapa 9 no Colab**: seis requisições ao Blockscout retornaram HTTP 200, com três contratos identificados (AdminUpgradeabilityProxy, token ERC-20 SmartEther e DSProxy). [Relatório e evidências](experiments/EXP-01D-triagem-onchain-3.md)
- [x] Preparar etapa 10 no **mesmo notebook 01** para conferir, a partir de `data/interim/test_20201029.parquet`, transações de três endereços, contagens e quatro features versus dataset processado (gráfico e relatório; sintaxe validada, **execução Colab pendente**).
- [x] **Executar etapa 10 no Colab (17/11/2026)**, conferir 4 artefatos no Drive: 3 endereços, 12/12 features e n_tx em paridade numérica exata com dataset processado; 53/10/10 tx, 27/10/1 remetentes distintos. [Relatório EXP-01E](experiments/EXP-01E-auditoria-historica-features.md).
- [x] Preparar etapa 11 do notebook 01: coleta externa pelo Blockscout com paginação, eventos `Upgraded`, transações de 29/10/2020 e **indicador explícito de cobertura**. Código validado sintaticamente e versionado, mas ainda sem execução Colab.
- [x] Executar etapa 11 no Colab, conferir os quatro artefatos: [EXP-01F](experiments/EXP-01F-blockscout-2020-cobertura.md). API HTTP 200, SmartEther 10 tx e DSProxy 10 tx com cobertura integral da data; proxy `transactions` e `logs` ainda limitados (30 páginas; datas mais antigas 06/11 e 05/11/2020).
- [x] Encontrar dois eventos `Upgraded` posteriores a 29/10/2020: 12/11/2020 (impl. `0x7497…`) e 25/04/2022 (impl. atual `0xee2f…`). **Os tx_hash não foram extraídos no CSV e ainda precisam verificação.**
- [ ] Identificar a implementação **em 29/10/2020**; bloqueio de acesso a provedor de arquivo/histórico. Eventos e leitura de estado ainda não suficientes; não repetir consultas idênticas sem fonte com cobertura.
- [x] **Comparar hash a hash 20 transações da API Blockscout com o dump bruto Blockchair de 29/10/2020**: 20/20 hashes, remetentes, destinatários e blocos idênticos; SmartEther 10/10 e DSProxy 10/10. [Relatório EXP-01G](experiments/EXP-01G-auditoria-hashes-blockchair-blockscout.md); [script reproduzível](../scripts/auditar_hashes_2020.py).
- [ ] Validar as 53 transações do proxy em fonte independente com cobertura histórica completa (a chamada anterior não chegou a 29/10/2020; não interpretar zero API como zero tx).
- [x] **Preparar consulta direcionada do slot EIP-1967 no bloco final 11.154.799** e busca de logs no intervalo 11.148.274–11.154.799, preservando eventuais erros e limitações (etapa 12 do notebook 01, validada sintaticamente; execução no Colab pendente).
- [x] **Executar etapa 12 no Colab e conferir os três arquivos no Drive (17/11/2026)**: PublicNode HTTP 403; LlamaRPC HTTP 525; consulta de logs Blockscout HTTP 200/status 0 sem registros; **nenhum slot EIP-1967 histórico obtido**. Classificação: **inconclusivo_sem_archive**. [Relatório EXP-01H](experiments/EXP-01H-estado-proxy-historico-inconclusivo.md).
- [ ] Verificar histórico de upgrades ao longo de 29/10/2020 para não presumir que a implementação do final do dia valeu por todas as 53 transações.
- [ ] Conferir atividade do contrato em 29/10/2020 **também diretamente na blockchain**; a paridade interim→processed concluída é apenas verificação interna, não fonte independente.


### EXP-01I — Auditoria do protocolo e nova análise controlada (17/11/2026)
- [x] Confrontar **artigo original (seções 4–5)** com notebooks legados 03/03_v2 e módulos canônicos. [Relatório EXP-01I](experiments/EXP-01I-auditoria-protocolo-e-limites.md).
- [x] Identificar escolhas documentadas na reprodução, mas não detalhadas no artigo: **100 negativos escolhidos dos 147 aprovados** em 15/03/2025; discretização de entropias em **4/4/6 casas**; janela por destinatário-dia UTC; inclusão de Router **condicional à existência do arquivo**; transição legada de MIN_TX 5 para 10.
- [x] Registrar que o artigo **também descreve reamostragem**; isso por si só não explica 63 × 9. No treino atual, oversampling até 100/100 torna pesos `balanced` analiticamente redundantes, sujeito à verificação de scores no cenário controlado.
- [x] **Preparar e sincronizar etapa 13 no mesmo notebook 01**: cruzamento de balanceamento, sementes e filtros de elegibilidade, limiar fixo 0,50; registro de CSVs e manifesto. **Execução no Colab pendente.**
- [x] Redigir [seção provisória de limitações e contribuições](manuscrito/limitacoes-e-contribuicoes.md), sem alegar superioridade preditiva ou causalidade não demonstrada.
- [x] **Executar etapa 13 no Colab (17/11/2026) e auditar os 6 artefatos**: modelo-base reproduz 9; sem corte no teste (`min_tx>=1`) produz **49**; `min_tx>=5` → 14; `>=20` → 7; 3/3 pools recuperados. Políticas de balanceamento e sementes mantêm as nove identidades, exceto somente pesos com 10. [EXP-01J](experiments/EXP-01J-resultados-sensibilidade-63x9.md).
- [x] Redigir [EXP-02 — Protocolo temporal e por contrato](experiments/EXP-02-protocolo-temporal-contrato.md) com critérios de prontidão, baseline, métricas, guardas contra vazamento e limitações de rotulagem. **Protocolo planejado, sem execução de novos modelos.**
- [x] **Inventariar dados e resultado legado de 2026:** notebook 07b já avaliou **15/01/2026** com limiar congelado 0,85, 20.214 elegíveis, 9 alertas e 3/3 pools conhecidos. [EXP-02A](experiments/EXP-02A-inventario-e-triagem-2026.md).
- [x] **Triagem documental dos nove alertas 2026:** 3 pools Tornado do artigo e 6 contratos associados a OKX DEX, ApeCoin OFT Adapter/LayerZero, SwappableBridgeUniswapV3, Chainlink CCIP Router, MCT-XEN Batch Minter e Wormhole Relayer. [Matriz auditável](experiments/EXP-02A-matriz-triagem-2026.csv); [manifesto](experiments/EXP-02A-manifesto.json). **Ainda não são seis falsos positivos comprovados.**
- [x] **Formalizar protocolo histórico de revisão dos seis contratos**, com cobertura de transações, ABI, eventos, upgrades e dupla revisão documental. [EXP-02B](experiments/EXP-02B-protocolo-auditoria-2026.md); **nenhuma nova coleta executada ainda**.
- [ ] Auditar atividade exata dos seis candidatos em 15/01/2026, incluindo implementação histórica de proxies, e revisão independente de rótulos negativos.
- [ ] Obter positivos de **outros protocolos de mixers** e período verdadeiramente novo para holdout por protocolo, evitando reaproveitar 2026 como teste confirmatório novo.

## Evidências principais

- [Artigo original no Drive](https://drive.google.com/file/d/1FflHcOmD3lsO6HeGOp4D85RQbQz7c4EG/view)
- [Reprodução consolidada 01](https://drive.google.com/drive/folders/1Cykyn2M8BGj5mDxfnXHkyv7x0cBrBkWe)
- [Auditoria visual 04](https://drive.google.com/drive/folders/1_hnQANKXRyJ4kK6nvKdnYlS1JeFwGQ8t)
- [Resultados legados 2020](https://drive.google.com/drive/folders/1iZKAeZPEb6JOlH8KfqsR6-wqI1ygmojI)
- [Padrão dos notebooks](07_PADRAO_NOTEBOOKS.md)

**Próxima ação prioritária (pós-EXP-02A, 17/11/2026):** preservar a investigação **63 × 9** como limitação de reprodutibilidade (sensibilidade ao filtro demonstrada, causa exata não comprovada). No [EXP-02A](experiments/EXP-02A-inventario-e-triagem-2026.md) recuperamos e documentamos a **execução legada de 2026**, e identificamos documentalmente os seis candidatos adicionais. Não reexecutar 2026 como teste independente novo nem apresentar precisão de 33,3%/seis FPs como ground truth. Próxima etapa: **validar a atividade on-chain histórica de 15/01/2026, construir negativos revisados por avaliadores e reunir pools positivos de outro protocolo** para divisão por contrato/período. A situação do e-mail aos autores só deve constar como ausência de resposta se ainda persistir na data de fechamento do manuscrito.
