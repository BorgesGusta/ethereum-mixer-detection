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
- [ ] Executar o diagnóstico no Colab e comparar as evidências produzidas
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

## Evidências principais

- [Artigo original no Drive](https://drive.google.com/file/d/1FflHcOmD3lsO6HeGOp4D85RQbQz7c4EG/view)
- [Reprodução consolidada 01](https://drive.google.com/drive/folders/1Cykyn2M8BGj5mDxfnXHkyv7x0cBrBkWe)
- [Auditoria visual 04](https://drive.google.com/drive/folders/1_hnQANKXRyJ4kK6nvKdnYlS1JeFwGQ8t)
- [Resultados legados 2020](https://drive.google.com/drive/folders/1iZKAeZPEb6JOlH8KfqsR6-wqI1ygmojI)
- [Padrão dos notebooks](07_PADRAO_NOTEBOOKS.md)

**Próxima ação prioritária (notebook 01 atualizado no Drive próprio em 17/11/2026):** executar as células da etapa 8 (dependem das variáveis de execução anteriores), salvar CSVs de scores, curvas e gráficos no Drive e interpretar sem ajustar limiar só para chegar a 63. A seguir,  investigar quantitativamente a diferença 63 vs 9 (população elegível, filtragem `n_tx`, agregação contrato-dia, reamostragem, negativos, discretização, score e regra de inferência). Já há uma hipótese empírica: o número 230.658 do artigo coincide exatamente com **destinatários distintos** do nosso dump de 2020; a união de sender+recipient é 377.296. Isto **não** resolve a divergência 63 vs 9. Enviar pedido de esclarecimento aos autores (realizado pelo pesquisador em 17/11/2026); aguardar eventual retorno, sem interromper a investigação. Só depois declarar a reprodução completa ou prosseguir a testes confirmatórios temporais.
