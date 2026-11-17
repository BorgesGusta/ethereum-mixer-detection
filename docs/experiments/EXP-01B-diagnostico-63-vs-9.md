# EXP-01B — Diagnóstico da divergência 63 × 9 (17/11/2026)

## Estado
**Executado no Colab; cinco artefatos verificados no Drive.** Diagnóstico exploratório, não alteração do limiar ou reprodução exata do artigo.

- [Pasta oficial da execução](https://drive.google.com/drive/folders/1KGYsT5D5DeOVV-U-sEszb_3jKhigy6l9)
- [Contagens](https://drive.google.com/file/d/1BJWNSUOnvEKHmAVaj9K4L2JqOVgUa8ho/view)
- [Curva de limiares](https://drive.google.com/file/d/1uCUqy0bMla6Wr5aN0lQjil7nJBG_0zhY/view)
- [Scores por endereço](https://drive.google.com/file/d/1ZC-iBEmYvLxTN6IZR8aTOqfQ3cm5wJwG/view)
- [Gráficos](https://drive.google.com/file/d/1zsc6LmZa8XUDD5j9NNkWbf7r2mmNM9q1/view)
- [Manifesto](https://drive.google.com/file/d/1ubuTLhiRk2l-eSyMD70Pbo_McyipnQSG/view)

## Resultados dos arquivos executados

| Indicador | Valor |
|---|---:|
| Destinatários/janelas no dataset processado | 230.658 |
| Elegíveis com n_tx ≥ 10 | 4.038 |
| Destinatários únicos entre os elegíveis | 4.038 |
| Alertas no limiar do artigo (>0,50) | 9 |
| Pools de referência do artigo marcados no dataset | 3 de 3 |
| Alertas declarados pelos autores | 63 |

A contagem 230.658 coincide com o total de endereços do artigo, mas o relatório `sanidade_variantes_20201029.csv` mostra que é a contagem de **destinatários únicos**; a união sender ∪ recipient totaliza 377.296. O artigo não detalha essa definição na mesma granularidade; tratá-la como hipótese, não fato.

A curva exploratória produziu: >0,20 → 80 alertas; >0,25 → 66; >0,30 → 58; >0,45 → 10; >0,50 → 9. **Não ajustar o limiar para obter artificialmente 63**: o artigo especifica >0,50 e mudar o limiar não demonstra equivalência metodológica.

## Achado de rotulagem adicional

O `scores_elegiveis_2020.csv` registra **0xa160cdab225685da1d56aa342ad8841c3b53f291** entre os nove, com `prob_mixer=0,87`, `n_tx=29` e `tornado` vazio.

O relatório de auditoria anterior `paridade_router_features.csv` [Drive](https://drive.google.com/file/d/1Vuo98PnMKRoL1t4j9MHmkQz4s8bGfbfS/view) e `resumo_atribuicao.csv` [Drive](https://drive.google.com/file/d/1f98EfSSaGG-S1odChy0BkYSJyDDvDJ-p/view) registram esse mesmo endereço como **pool Tornado Cash de 100 ETH**, com 29 transações em 29/10/2020.

Assim, **a classificação referenciada ao artigo é 3 de 3**, mas ao cruzar com a lista histórica expandida dos quatro pools há **pelo menos 4 endereços Tornado conhecidos entre os 9 alertas**, e restam **5 não validados por esse conjunto de referência** (não declarar falsos positivos). **Não corrigir silenciosamente o arquivo parquet:** publicar relatório de correspondência e explicitar universos de rótulo distintos.

## Interpretação

- O modelo recebe apenas 4.038 janelas após o corte `n_tx ≥10`; 230.658 não são entradas diretas da RF.
- 63 (artigo) vs 9 (reprodução) segue **sem causa demonstrada**. Possibilidades a auditar: seleção e rótulos de treino, janela e filtros, configuração do balanceamento, distribuição das features, diferenças entre implementações e outras regras de inferência.
- Os scores são previsões do modelo refeito; não devem ser interpretados como probabilidades calibradas.
- Não há lista pública verificada dos 63 alertas para confrontar identidades. O pesquisador enviou e-mail aos autores em 17/11/2026.

## Próximas verificações

1. Produzir tabela explícita de rotulagem dos quatro pools e dos cinco outros alertas, com rótulos externos separados de predição.
2. Comparar a elegibilidade e a implementação com o artigo sem alterar hiperparâmetros para imitar 63.
3. Se autores responderem, conferir lista de 63 endereços, código e critério de amostragem.
4. Auditar recomputação de features desde os dados brutos; depois iniciar estudo temporal com protocolo harmonizado.
