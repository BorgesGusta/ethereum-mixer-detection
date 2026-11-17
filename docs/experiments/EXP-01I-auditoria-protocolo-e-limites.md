# EXP-01I — Auditoria de protocolo e hipóteses para a divergência 63 × 9

**Data:** 17/11/2026. **Status:** auditoria documental concluída e **etapa 13 executada em 17/11/2026 às 14:29 UTC**. Resultados quantitativos e fontes: [EXP-01J](EXP-01J-resultados-sensibilidade-63x9.md). Os dados, pesos, limiar do protocolo original e rótulos não foram alterados.

## Materiais efetivamente comparados

- Artigo: Pedro Leale e Ivan da Silva Sendin, *Uma Proposta de Algoritmo para a Detecção de Mixers na Ethereum*, SBSeg 2025, seções 4–5. [PDF original](https://drive.google.com/file/d/1FflHcOmD3lsO6HeGOp4D85RQbQz7c4EG/view).
- Notebook legado `03_negativos_features_treino.ipynb` e versão posterior `03_negativos_features_treino_v2.ipynb`, disponíveis no acervo do projeto.
- Módulos versionados [`src/ethmix/features.py`](../../src/ethmix/features.py) e [`src/ethmix/models.py`](../../src/ethmix/models.py).
- [Notebook canônico `01_reproducao.ipynb`](../../notebooks/01_reproducao.ipynb).
- Resultados da reprodução e curva de scores [EXP-01B](EXP-01B-diagnostico-63-vs-9.md) e evidências seguintes [EXP-01C](EXP-01C-triagem-9-alertas.md), [EXP-01D](EXP-01D-triagem-onchain-3.md), [EXP-01E](EXP-01E-auditoria-historica-features.md), [EXP-01F](EXP-01F-blockscout-2020-cobertura.md), [EXP-01G](EXP-01G-auditoria-hashes-blockchair-blockscout.md) e [EXP-01H](EXP-01H-estado-proxy-historico-inconclusivo.md).

## Pontos verificados contra o artigo

| Aspecto | Artigo, seções 4–5 | Reprodução documentada | Diagnóstico |
|---|---|---|---|
| Classificador | RF 100 árvores; max_depth=5; pesos automáticos; decisão p>0,5 | Mesma configuração central; seed=42 | **Equivalência de parâmetros centrais, não de modelo treinado** |
| Balanceamento | Reamostragem dos dados rotulados ANTES do treino | Oversampling da classe minoritária até igualar 100 negativos, inclusive dentro dos folds | Reamostragem consta do artigo; diferença exata de sorteio/execução ainda indeterminada |
| Negativos | 100 endereços aleatórios não mixers, >=10 tx, inspecionados no Etherscan | Em 03_v2: 150 candidatos avaliados (147 aceitos/3 descartados) e 100 primeiros aceitos, transações recebidas em 15/03/2025 | **Não se conhece a amostra exata dos autores.** Inspeção em 2026 não equivale à mesma lista ou ao mesmo critério histórico |
| Positivos | Transações do pool Tornado 10 ETH em março/2025 | 23 janelas positivas (contrato-destinatário/dia) de **um único contrato** | Unidade e seleção exatas dos registros originais não publicadas |
| Router | Artigo fala em transações do endereço conhecido; não explicita mecanismo Router | Notebook 03_v2 registra `INCLUIR_ROUTER=True`, mas só anexa transações via Router **se o CSV existir** | **Potencial divergência condicional**, não confirmar inclusão real na execução sem verificar artefato/proveniência |
| Agregação | Quatro características transacionais por endereço, período não inteiramente descrito | Janela `(recipient, dia UTC)`; 4 features | Método plausível, **paridade algorítmica não demonstrada** |
| Discretização | Artigo não especifica casas decimais das entropias | Shannon base 2 após `round(value_eth,4)`, `round(internal_value_eth,4)`, `round(fee_eth,6)` | Parâmetro não documentado no artigo; afeta as features |
| Filtro de elegibilidade | Pelo menos dez transações **explicitamente para amostras negativas**; filtro do teste não detalhado na mesma granularidade | `n_tx>=10` na inferência; 4.038 dentre 230.658 destinatários | Não confundir exigência explícita de negativos com regra publicada para todo o conjunto de teste |
| Legados locais | — | Notebook 03 antigo define `MIN_TX=5`; 03_v2 define `MIN_TX=10` | **Mudança histórica documentada**, não é prova de causa da divergência com autores |
| Validação | Resultado qualitativo de três pools Tornado recuperados | CV de cinco folds estratificada por linha do treino com 23 positivas de um só pool | CV tem dependência entre janelas do mesmo contrato; não confirma generalização para mixers novos |
| Teste | 29/10/2020: 1.114.702 tx, 230.658 endereços, 239 tx nos três pools, 63 alertas | Mesma data, totais reconciliados; 4.038 elegíveis, 9 alertas, mesmos 3 pools | Diferença de **54 alertas**, causa não identificada |

### Interpretação do balanceamento

Com 100 negativos e 23 positivos, o nosso oversampling leva a **100/100 exemplos por classe**. Se `class_weight='balanced'` for calculado sobre esse conjunto já balanceado, o peso por classe é 1 e o efeito adicional do parâmetro é nulo. Essa observação é analítica; a igualdade das probabilidades será conferida na execução controlada da etapa 13. Isso **não** determina os pesos efetivamente aprendidos pelos autores sem acesso à implementação deles.

## Novo experimento planejado e isolação causal

Etapa 13 anexada ao **mesmo notebook canônico 01**:

1. Fixar 4.038 candidatos (`n_tx>=10`) e limiar **0,50**. Comparar 4 políticas de balanceamento com seed 42: (a) oversampling + pesos balanceados (base), (b) somente pesos, (c) somente oversampling, (d) nenhum. Guardar número de alertas, pools conhecidos, sobreposição dos alertas e coincidência exata dos scores.
2. Fixar política base e variar somente `random_state` (42, 7, 123), mantendo todas as demais escolhas.
3. Fixar **o mesmo modelo-base** e variar só `n_tx` no conjunto de teste (1, 5, 10, 20), mostrando mudança do universo elegível e quantos pools são recuperados. Também contabilizar separadamente as janelas com features não finitas, evitando excluí-las silenciosamente. A variante com `n_tx=1` testa a hipótese de classificação de todos os destinatários, enquanto o artigo explicita `>=10` apenas para seleção dos negativos.
4. Registrar diversidade dos contratos/dias do treino. A análise usa o conjunto **existente**, sem alterar seleção dos 100 negativos nem Router. Não atribuir causa da diferença 63 × 9 a um fator sem evidência empírica.

**Saídas produzidas e verificadas no Drive ([pasta de execução](https://drive.google.com/drive/folders/1AFO6k3ShxdsZABU1OoFBXez7Dd8FngOx)):** `composicao_treino.csv`, `comparacao_cenarios.csv`, `comparacao_elegibilidade.csv`, `alertas_cenarios.csv`, `grafico_sensibilidade.png` e `manifesto.json` em pasta exclusiva no Drive.

## Como escrever a limitação no artigo, se permanecer sem explicação

O principal resultado é **reprodução parcial** do método e recuperação dos três contratos de referência, com divergência no número de alertas. Não atribuir à falta de resposta dos autores a causa da diferença: a solicitação enviada em 17/11/2026 busca esclarecer detalhes, mas a diferença foi observada no experimento independentemente do e-mail. Caso não haja resposta **até o fechamento do manuscrito**, indicar isso apenas como restrição de acesso a código, amostras, rótulos e decisões de pré-processamento, e não como evidência de erro dos autores.

### Contribuições que podem ser demonstradas sem alegar superioridade preditiva

- **Transparência e rastreabilidade**: módulos versionados, SHA-256 de dados, parâmetros, logs, manifestos, scripts e artefatos.
- **Verificação cruzada de dados**: 20/20 hashes, remetentes, destinatários e blocos coincidentes entre dump Blockchair e API Blockscout para dois contratos; **não generalizar para os demais endereços**.
- **Qualidade de rótulos**: distinção entre três pools considerados pelo artigo, pool adicional 100 ETH e outros contratos documentalmente identificados; cinco alertas não devem ser declarados falsos positivos automaticamente.
- **Validade temporal**: apontar limitações de Router, contratos atualizáveis, história de implementação e variações de cobertura; o caso do proxy ficou inconclusivo devido a indisponibilidade de estado histórico.
- **Segurança metodológica**: integridade, proveniência e prevenção de sobreinterpretação. Isso não equivale a segurança criptográfica/operacional superior ou maior acurácia do detector.

## Pendências para resultado científico final

- Equivalência dos 100 negativos e do universo de inferência dos autores; acesso aos códigos ou resposta dos autores se possível.
- Executar etapa 13 e interpretar efeitos, sem otimizar retrospectivamente para 63.
- Depois definir e executar experimentos temporais com divisões por contrato e período, negativos independentes e medidas de precisão/recall sob ground truth auditado.

## Adendo de resultados da etapa 13 (executada)

- No filtro original `n_tx>=10`: **9 alertas**; no cenário sem corte adicional (`n_tx>=1`): **49 alertas**. Outros cortes: `>=5` → 14 e `>=20` → 7. São 40 alertas no universo `1<=n_tx<10` do nosso próprio modelo; a distância para os **63 do artigo persiste**, inclusive com `min_tx=1`.
- Balanceamento e semente (7, 42, 123) conservaram os mesmos 9 endereços no universo `n_tx>=10`, exceto a variante somente pesos, que adicionou `0xd191...76f` (score 0,51); nenhuma explica os 63.
- A composição do treino foi confirmada: 23 positivas, **um contrato em 23 dias**, e 100 negativas de **100 endereços em um só dia**. CV por linha não representa generalização para contratos novos.
- **Conclusão editorial:** tratar 63 × 9 como divergência de reprodução não resolvida, com um fator de sensibilidade mensurado (elegibilidade); não atribuir causa específica sem código/amostras originais dos autores. [Relatório EXP-01J](EXP-01J-resultados-sensibilidade-63x9.md).
