# Arquitetura enxuta da pesquisa — proposta adotada em 16/11/2026

## Princípio
**Quatro notebooks ativos, código compartilhado em módulos Python, experimentos identificados por configuração e execução, e documentação curta em Markdown.**

O número de experimentos NÃO determina o número de notebooks. Um experimento é uma execução rastreável de um protocolo, não necessariamente um novo arquivo `.ipynb`.

## Interface de trabalho

| Notebook canônico | Objetivo | Abrange o acervo anterior |
|---|---|---|
| `notebooks/01_reproducao.ipynb` | Coleta/preparo, quatro features, treino RF e reprodução do artigo | 01, 02, 03, 04 |
| `notebooks/02_avaliacao.ipynb` | Comparação de modelos, ablação, sensibilidade, validação e investigação de candidatos | 05, 07b, 08, 10, 11 |
| `notebooks/03_temporal.ipynb` | Análise 2020–2026, treino histórico e avaliação cronológica | Proposta de estudo 12.03+ |
| `notebooks/04_auditoria.ipynb` | Inventário, hashes, integridade, reconciliação direta/via Router e paridade das features | 12.00, 12.01, 12.02A, 12.02B |

**Estado:** os quatro nomes acima são o projeto de consolidação; não afirmar que os notebooks finais já foram implementados ou reproduzem outputs. Primeiro inventariar, depois extrair funções e testar, só então consolidar.

## Organização de código

```text
notebooks/
  01_reproducao.ipynb
  02_avaliacao.ipynb
  03_temporal.ipynb
  04_auditoria.ipynb
  legacy/                          # arquivos históricos imutáveis
src/ethmix/
  io.py                           # leitura, validação, persistência, SHA-256
  features.py                     # cálculo das 4 features, sem lógica de notebook
  attribution.py                  # recipient direto / chamadas internas por hash
  datasets.py                     # amostras, rótulos e políticas temporais
  models.py                       # treino, avaliação, calibração
  reporting.py                    # tabelas e gráficos
configs/
  experimentos/                   # parâmetros por experimento
tests/                             # testes de paridade e regressão
docs/
  00_PAINEL.md
  01_CRONOLOGIA.md
  02_EXPERIMENTOS.md
  03_DECISOES.md
  04_DADOS.md
  05_PLANO.md
  06_ARQUITETURA_ENXUTA.md
  aulas/                           # notas de estudo, conceitos e explicações
  experiments/                     # registro por experimento, não novo notebook
manuscript/                         # artigo posteriormente
```

## Fluxo de execução
1. **Selecionar configuração:** ID do experimento (ex.: EXP-010), data UTC, datasets e hashes.
2. **Executar notebook canônico:** módulos de `src/ethmix` fazem o processamento e geram resultados.
3. **Salvar execução única:** `results/EXP-010/<UTC>_<commit>/`, sem sobrescrever anteriores.
4. **Registrar interpretação:** observação vs. hipótese, limitações e implicações científicas.
5. **Atualizar painel/cronologia:** apontar para resultados e evidências, não duplicar tabelas manualmente.
6. **Publicar no artigo:** referenciar apenas resultados que atendam aos critérios de validade.

## Padrão didático de cada notebook
1. O que queremos descobrir?
2. Conceito teórico em linguagem natural (incluindo glossário).
3. O que entra e de onde veio?
4. Código curto com função importada (evitar dezenas de células de implementação).
5. Como ler tabela/gráfico?
6. O que resultado permite e NÃO permite afirmar?
7. Como reproduzir esta execução? (config, hashes e commit)

## Regras de consolidação
- Guardar notebooks legados em `notebooks/legacy`, incluindo versões originais e refatoradas; não deletar nem renomear o original do Drive.
- Não mesclar dois experimentos com split, amostragem ou rótulos incompatíveis sem identificadores separados.
- Não reaproveitar limiar selecionado com resultados de teste para fazer afirmações confirmatórias.
- Diferenciar **reprodução**, **exploração**, **teste confirmatório** e **auditoria**.
- Não portar dependências pesadas ou dados binários ao GitHub.
- Criar notebook final somente quando as funções tiverem teste de paridade com o legado.
