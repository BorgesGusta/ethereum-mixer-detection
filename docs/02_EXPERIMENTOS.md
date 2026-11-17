# Catálogo de experimentos

| Experimento | Objetivo | Estado | Limitação-chave |
|---|---|---|---|
| 01–04 | Coleta, treino, reprodução e inferência | Executado; catalogação pendente | Comparabilidade com artigo original precisa de auditoria final |
| 05 | Ablação de features | Executado | F1 interno não demonstra generalização |
| 06–09 | Auditorias, teste externo 2026 e sensibilidade | Exploratório | Candidatos adicionais sem rótulos negativos garantidos |
| 10 | RF × Extra Trees × HGB × Regressão Logística | Executado | Positivos de um único contrato |
| 11 | Comparação externa RF/ET/voting | Executado | 2020/2026 já conhecidos e limiar não calibrado por modelo |
| 12.00 | Inventário de dados e hashes | Concluído | Verificação de existência/integridade, não cobertura temporal completa |
| 12.01 | Viabilidade do treino 2020 | Concluído | Quatro positivos apenas no dia 29/10/2020 |
| 12.02A | Paridade das quatro features | Concluído | Cobertura e atribuição diferem por data |
| 12.02B | Reconciliação por hash/Router | Concluído | 2020 sem CSV de chamadas equivalentes; 2025 com intervalo 15–21/03 |
| 12.03 | Montar treino 2020 com múltiplos dias | **Pendente** | Coleta, rótulos e confirmação da semântica histórica |

Referências:
- [Resultados RF/ET/voting no Drive](https://drive.google.com/drive/folders/1c1gTmnWY3LG6enj980nBHiOWXPXN-99B)
- [Auditoria 12.02B no Drive](https://drive.google.com/drive/folders/1pZijTh9D8h-2bw6IYStFONp318w330jQ)
- [Auditorias temporais no Drive](https://drive.google.com/drive/folders/1twHP6i1jwSemx59-Uc8C1N2nVlDabmCh)

**Não usar este catálogo como substituto das evidências originais**: números definitivos para artigo devem ter referência explícita ao CSV, hash e método.

Use [modelo de ficha](experiments/TEMPLATE.md) para adicionar experimentos.
