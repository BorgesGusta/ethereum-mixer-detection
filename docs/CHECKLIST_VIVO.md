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
- [ ] Identificar a implementação **em 29/10/2020**; a consulta de logs não chegou até essa data e não exclui upgrades anteriores.
- [x] **Comparar hash a hash 20 transações da API Blockscout com o dump bruto Blockchair de 29/10/2020**: 20/20 hashes, remetentes, destinatários e blocos idênticos; SmartEther 10/10 e DSProxy 10/10. [Relatório EXP-01G](experiments/EXP-01G-auditoria-hashes-blockchair-blockscout.md); [script reproduzível](../scripts/auditar_hashes_2020.py).
- [ ] Validar as 53 transações do proxy em fonte independente com cobertura histórica completa (a chamada anterior não chegou a 29/10/2020; não interpretar zero API como zero tx).
- [ ] Consultar **implementação do proxy no bloco histórico de 29/10/2020** via slot EIP-1967 com provedor de arquivo, ou logs de `Upgraded` filtrados por intervalo (registros anteriores a 12/11/2020 desconhecidos).
- [ ] Conferir atividade do contrato em 29/10/2020 **também diretamente na blockchain**; a paridade interim→processed concluída é apenas verificação interna, não fonte independente.

## Evidências principais

- [Artigo original no Drive](https://drive.google.com/file/d/1FflHcOmD3lsO6HeGOp4D85RQbQz7c4EG/view)
- [Reprodução consolidada 01](https://drive.google.com/drive/folders/1Cykyn2M8BGj5mDxfnXHkyv7x0cBrBkWe)
- [Auditoria visual 04](https://drive.google.com/drive/folders/1_hnQANKXRyJ4kK6nvKdnYlS1JeFwGQ8t)
- [Resultados legados 2020](https://drive.google.com/drive/folders/1iZKAeZPEb6JOlH8KfqsR6-wqI1ygmojI)
- [Padrão dos notebooks](07_PADRAO_NOTEBOOKS.md)

**Próxima ação prioritária (após execução da etapa 8 do notebook 01 em 17/11/2026):** investigar a divergência 63 vs 9, com rotulagem expandida (100 ETH), checagem de população, filtros, amostragem, processamento e decisões de treino. Evidências: [EXP-01B](experiments/EXP-01B-diagnostico-63-vs-9.md). Não ajustar limiar só para chegar a 63. A seguir,  investigar quantitativamente a diferença 63 vs 9 (população elegível, filtragem `n_tx`, agregação contrato-dia, reamostragem, negativos, discretização, score e regra de inferência). Já há uma hipótese empírica: o número 230.658 do artigo coincide exatamente com **destinatários distintos** do nosso dump de 2020; a união de sender+recipient é 377.296. Isto **não** resolve a divergência 63 vs 9. Enviar pedido de esclarecimento aos autores (realizado pelo pesquisador em 17/11/2026); aguardar eventual retorno, sem interromper a investigação. Só depois declarar a reprodução completa ou prosseguir a testes confirmatórios temporais.
