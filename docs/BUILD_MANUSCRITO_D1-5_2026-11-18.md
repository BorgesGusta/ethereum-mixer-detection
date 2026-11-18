# D1.5–D1.7 — Compilação e revisão inicial do manuscrito LaTeX

**Data de verificação:** 18/11/2026. **Estado:** PDF compilado localmente; manuscrito ainda **não importado no Overleaf**, não submetido, não adaptado ao template de conferência e não revisado integralmente por autores/orientador.

## Fontes compiladas e integridade

Fontes foram recuperadas pelo conector do GitHub e reconstruídas em uma pasta local; o conteúdo final das três fontes foi conferido pelo **Git blob SHA-1** local contra os hashes GitHub na branch `docs/consolidacao-oficial-2026-11-17`:

| Arquivo | SHA do blob Git (igual ao local) |
|---|---|
| `artigo/overleaf/main.tex` | `719be165d49761e2d34d5b7f07111961440c4b08` |
| `artigo/overleaf/referencias.bib` | `58f35dc476a1ce02694b568338dc17d7daebc5ba` |
| `artigo/overleaf/figuras/sensibilidade.tex` | `a92f2665b2e0889bce441885de0a9f984c71f4af` |

Não houve reexecução de experimentos ou modificação de resultados.

## Procedimento de build

- Compilador local: `pdflatex` com `bibtex8` (o comando `bibtex` não existia neste ambiente, mas `bibtex8` sim).
- Primeira tentativa: referências indefinidas porque não havia BibTeX; ao gerar o `.bbl`, a bibliografia com caracteres UTF-8 não escapados falhou no `bibtex8`.
- Correção **mínima versionada**: normalização de caracteres acentuados de `referencias.bib` para comandos TeX; preserva o conteúdo bibliográfico. Uma quebra possível adicionada a `internal_value_entropy` em `main.tex` eliminou um `Overfull \\hbox` de 25,7 pt.
- Sequência final: `bibtex8 main` (produz `.bbl`, porém retorna status 1 por **três avisos de metadados**); `pdflatex -interaction=nonstopmode -halt-on-error main.tex` **duas vezes**, ambas com código de saída **0**.
- PDF final: **7 páginas A4**, `222260` bytes; SHA-256 `17d3b3dc28cf7dfe16a95d63bb3a1513be0a447871a6f1d855c2e1e0dbaa08fd`.
- Log da última passagem LaTeX: **sem erros, citações indefinidas ou avisos `Overfull/Underfull`**.
- Inspeção visual amostral de páginas do PDF: capa/resumos, tabelas, gráfico de elegibilidade, ameaças e referências. Não é revisão editorial final de cada parágrafo.

## Pendências editoriais observadas

1. `barbereau2023taxonomy` **sem autores**: `bibtex8` informa que não pode ordenar por autor/chave. Confirmar metadados da publicação.
2. `blockchair` e `blockscout` **sem ano**: `bibtex8` emite aviso; não inventar ano de publicação, decidir formato e data de acesso ao revisar a bibliografia.
3. Fonte `leale2025mixers` contém nota expressa para conferir DOI e dados editoriais antes de submeter.
4. Autores e afiliações ainda são placeholders; verificar regras de anonimização e template quando o evento for escolhido.
5. Literatura adicional (MixGuard, FPTracer, StealthLink, GNN) ainda sem referências bibliográficas validadas.
6. O arquivo ainda identifica rascunho `v0.1`. **Compilar não equivale a publicar/aceitar ou verificar métricas científicas.**

## Conclusão permitida

**Compilação técnica validada localmente** para fontes identificadas por blobs Git; **bibliografia compila com avisos de metadados pendentes**. Não houve build dentro do serviço Overleaf. PDF foi produzido no ambiente de execução do assistente, **não enviado ao Drive** nesta etapa. A passagem de `v0.1` para `v0.2` depende de revisão científica e verificação editorial.

## Próximas tarefas

- [ ] Conferir metadados da bibliografia com PDFs originais e fontes primárias.
- [ ] Revisar integralmente o texto e as tabelas com matriz de rastreabilidade, inclusive a distinção entre 63×9 e 49/14/9/7.
- [ ] Formalizar versão v0.2 do artigo **somente quando** essas correções científicas forem concluídas.
- [ ] Confirmar compilação no Overleaf e adaptação de template oficial, quando necessário.
