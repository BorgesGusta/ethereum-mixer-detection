# Notebooks: uso ativo versus arquivo histórico

**Arquivos já arquivados:** `legacy/` contém cópias de notebooks recuperados do Drive, incluindo variantes antigas. São evidência histórica, **não** interface oficial de execução nova.

**Quatro notebooks canônicos planejados:**
- `01_reproducao.ipynb`
- `02_avaliacao.ipynb`
- `03_temporal.ipynb`
- `04_auditoria.ipynb`

Eles serão criados progressivamente após a extração de funções para `src/ethmix/` e testes de paridade. Enquanto isso, usar `docs/02_EXPERIMENTOS.md` e `docs/06_ARQUITETURA_ENXUTA.md` para localização.

**Importante:** um experimento é identificado por config, dados, código e resultados; NÃO por um notebook separado.

## Primeira consolidação

O [01_reproducao.ipynb](01_reproducao.ipynb) está publicado como **versão inicial, ainda não executada/validada no Colab**. Ele trabalha com os Parquets já processados, carrega os módulos versionados de `src/ethmix` e grava relatórios novos por execução. Para repositório privado, configurar no Colab Secret `GITHUB_TOKEN` com acesso somente leitura aos conteúdos deste repositório ou usar `REPO_LOCAL`.

Os testes `tests/test_reproducao.py` estão escritos, mas ainda precisam ser executados em ambiente com dependências instaladas. A equivalência de hashes de datasets não substitui testes de paridade de previsão e resultados.

## Organização do Google Drive (17/11/2026)

- [00_ATIVOS — notebooks para execução](https://drive.google.com/drive/folders/1RbYa8atGZtaGyR_er8gpumiwRflDaeQv): contém [01_reproducao.ipynb (cópia operacional para Colab)](https://drive.google.com/file/d/1w6RsABh0o6w1DfbkGgF8M_DG3uCJjx1l/view).
- [99_LEGADO — notebooks históricos](https://drive.google.com/drive/folders/16NLfr-bvZwbgdJN6p-wCPMRrvIpJEmZ0): 14 notebooks originais movidos, preservando seus IDs, mais as cópias históricas 12.02A e 12.02B.
- A cópia operacional no Drive foi **recriada a partir da mesma lógica**, mas não é ainda um espelho byte a byte do notebook GitHub. A **versão canônica do código continua no GitHub**; até automatizarmos a sincronização, conferir diferenças antes de publicar conclusões científicas.
- Nenhuma pasta de datasets ou resultados foi movida.
