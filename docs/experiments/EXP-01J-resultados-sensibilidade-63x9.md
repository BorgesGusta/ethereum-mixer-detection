# EXP-01J — Resultados controlados da sensibilidade 63 × 9

**Execução confirmada:** 17/11/2026 às 14:29:36 UTC. **Notebook:** etapa 13 de `notebooks/01_reproducao.ipynb`. **Status:** concluído, com seis artefatos produzidos e conferidos no Google Drive.

## Fontes verificadas

- [Pasta oficial desta execução no Drive](https://drive.google.com/drive/folders/1AFO6k3ShxdsZABU1OoFBXez7Dd8FngOx)
- [Manifesto da execução](https://drive.google.com/file/d/1hZkvRQtJoxJ0TNlE0ATMefPdrjJEl01e/view)
- [Composição do treino](https://drive.google.com/file/d/1lUUV98NICvJSN035TYUMAuF0-fHGSADC/view)
- [Comparação de elegibilidade](https://drive.google.com/file/d/1fGYC9pNVHlGILcEbJnlqBqulEWZTM0-o/view)
- [Comparação de balanceamento e sementes](https://drive.google.com/file/d/1G41RFk-LqJ4Li6RYJ3iwhawB_BdrnXZx/view)
- [Lista dos alertas de todos os cenários com `n_tx>=10`](https://drive.google.com/file/d/1fBRZbG6Auy8xM56vgpQrpSFtnF10c346/view)
- [Gráfico de sensibilidade](https://drive.google.com/file/d/1KIBJKeFUiHZQWU6p8kcSPGj1vvDnOXpn/view)

O manifesto confirma o limiar fixo `p>0.50`, referência `min_tx=10`, Random Forest com 100 árvores e `max_depth=5`, e `base_igual_modelo_carregado=true`. Hashes SHA-256 de treino e teste:
- treino `0a8baa11cee97d338d7a8d92b984f38192ba1a10ec915cc4a06d67ec94ad5c32`;
- teste `6f8fd4e83e816c785d449116699065ad77425c9da6e7b19d9bcda36f42bddb51`.

## Resultado A — Efeito do filtro de elegibilidade, sem retreinar

| min_tx | Janelas elegíveis | Janelas efetivamente classificadas | Features inválidas | Alertas >0,5 | Referências Tornado recuperadas |
|---:|---:|---:|---:|---:|---:|
| 1 | 230658 | 230658 | 0 | 49 | 3 |
| 5 | 7865 | 7865 | 0 | 14 | 3 |
| 10 | 4038 | 4038 | 0 | 9 | 3 |
| 20 | 2464 | 2464 | 0 | 7 | 3 |

Para o modelo treinado do projeto, **40/49 alertas sob `min_tx=1` são excluídos ao exigir `min_tx>=10`**, mantendo o mesmo limiar. Exatamente **35** alertas têm `1<=n_tx<5`, **5** têm `5<=n_tx<10`, **2** têm `10<=n_tx<20` e **7** têm `n_tx>=20`; esses valores derivam das contagens cumulativas da tabela, não da lista completa de 49 hashes (não exportada neste ensaio). 

Essa evidência demonstra o efeito do **filtro da nossa própria implementação**. Como não sabemos qual filtro e universo exatos os autores aplicaram ao testar, **não prova que esse foi o motivo da divergência com os 63 alertas**. Mesmo sem cutoff além de `>=1`, nossa versão produz 49, **14 a menos que 63**. Não se deve ajustar o filtro para forçar a coincidência.

## Resultado B — Balanceamento e semente, mantendo n_tx>=10

| Cenário | Treino após reamostragem | Alertas | Pools referência | Interseção com 9 originais | Scores idênticos à base? |
|---|---|---:|---:|---:|---|
| Oversampling + class_weight=balanced, seed42 | 100 positivos + 100 negativos | 9 | 3/3 | 9 | sim |
| Somente class_weight=balanced, seed42 | 23 positivos + 100 negativos | 10 | 3/3 | 9 | não |
| Somente oversampling, seed42 | 100 positivos + 100 negativos | 9 | 3/3 | 9 | **sim** |
| Nenhum dos dois, seed42 | 23 positivos + 100 negativos | 9 | 3/3 | 9 | não |
| Oversampling+balanced, seed7 | 100 positivos + 100 negativos | 9 | 3/3 | 9 | não |
| Oversampling+balanced, seed123 | 100 positivos + 100 negativos | 9 | 3/3 | 9 | não |

A partir do arquivo de alertas, **o mesmo conjunto de 9 contratos aparece em todos os cenários**. A política `somente pesos` acrescenta um décimo alerta: `0xd1917932a7db6af687b523d5db5d7f5c2734763f`, com score **0,51**, sem remover nenhum dos nove.

Os scores da base e do cenário `somente oversampling` são **exatamente iguais**, consistente com o fato de que o `class_weight='balanced'` se torna neutro quando o conjunto de treino foi reamostrado para 100 positivos e 100 negativos. As sementes 7 e 123 mudaram os scores, mas **não** as identidades sinalizadas nessa população elegível.

Portanto, **nenhum desses cenários explica o salto de 9 para 63** mantendo `min_tx>=10` e o dataset atual.

## Resultado C — Composição do treino

| Classe | Janelas | Endereços distintos | Dias distintos | Mediana n_tx |
|---|---:|---:|---:|---:|
| Negativo (0) | 100 | 100 | 1 | 23,5 |
| Positivo (1) | 23 | 1 | 23 | 23 |

Isso **limita a interpretação da CV estratificada por linha**: janelas do mesmo contrato positivo podem aparecer em treino e validação. O estudo não demonstra reconhecimento de mixers **não vistos** apenas por recuperar os 3 pools Tornado Cash em 2020. Os 100 negativos foram rotulados por inspeção do projeto e não há identidade comprovada com os 100 negativos usados pelos autores.

## Conclusões sustentadas e limitações

1. O parâmetro de elegibilidade **modifica substancialmente a população de inferência e o número de alertas** dentro da reprodução, e o artigo menciona `>=10` especificamente na seleção de 100 negativos, não descrevendo com mesma precisão o universo de teste.
2. O desvio **63 vs 9 permanece não resolvido**. Relevantes variáveis ainda não identificadas em condições equivalentes incluem amostra exata de treino, discretização da entropia, regras de Router, engenharia de features e unidade de agregação. **Não temos lista de 63 hashes nem código original para fazer atribuição causal.**
3. Não é rigoroso tratar as 60 detecções adicionais do artigo como falsos positivos verificados no nosso universo; as referências e procedimentos de rotulagem não são equivalentes.
4. A falta de resposta ao pedido enviado aos autores em 17/11/2026 **não é fato conclusivo neste momento**. Se persistir até a redação final, relatar como limitação de disponibilidade de informações, **sem atribuir incorreção aos autores**.
5. Os procedimentos de checksum, auditoria de features, fontes cruzadas e controle de cobertura reforçam **reprodutibilidade e auditabilidade**, não provam aumento de precisão/recall ou de segurança adversarial.

## Decisão metodológica para o próximo ciclo

**Encerrar a busca retroativa de um filtro/limiar que produza exatamente 63.** Manter a divergência como limitação de reprodutibilidade, podendo reabri-la apenas diante de nova evidência documental (resposta dos autores, código/CSV originais). Avançar com [EXP-02](EXP-02-protocolo-temporal-contrato.md): inventário de rótulos positivos/negativos e avaliação por contrato e período, evitando vazamento entre janelas do mesmo endereço e informando cobertura dos dados. Novas métricas externas exigem ground truth auditado.
