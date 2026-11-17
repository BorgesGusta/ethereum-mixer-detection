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

O [01_reproducao.ipynb](01_reproducao.ipynb) está publicado como **versão inicial, ainda não executada/validada no Colab**. Ele trabalha com os Parquets já processados, carrega os módulos versionados de `src/ethmix` e grava relatórios novos por execução. O notebook carrega os módulos diretamente da sua pasta própria no Drive (`src/ethmix/`) e verifica SHA-256. **Não é necessário token de GitHub para executar**.

Os testes `tests/test_reproducao.py` estão escritos, mas ainda precisam ser executados em ambiente com dependências instaladas. A equivalência de hashes de datasets não substitui testes de paridade de previsão e resultados.

## Organização do Google Drive (17/11/2026)

- [00_ATIVOS — notebooks para execução](https://drive.google.com/drive/folders/1RbYa8atGZtaGyR_er8gpumiwRflDaeQv): contém [01_reproducao.ipynb (cópia operacional para Colab)](https://drive.google.com/file/d/1w6RsABh0o6w1DfbkGgF8M_DG3uCJjx1l/view).
- [99_LEGADO — notebooks históricos](https://drive.google.com/drive/folders/16NLfr-bvZwbgdJN6p-wCPMRrvIpJEmZ0): 14 notebooks originais movidos, preservando seus IDs, mais as cópias históricas 12.02A e 12.02B.
- A cópia operacional no Drive foi **recriada a partir da mesma lógica**, mas não é ainda um espelho byte a byte do notebook GitHub. A **versão canônica do código continua no GitHub**; até automatizarmos a sincronização, conferir diferenças antes de publicar conclusões científicas.
- Nenhuma pasta de datasets ou resultados foi movida.


### Correção do Drive oficial (17/11/2026)

A pasta `mixers-ethereum` foi identificada como compartilhada por Bruno; não é o caminho canônico. A cópia de execução está em [Notebooks ativos no Drive próprio](https://drive.google.com/drive/folders/1VNdVfqmHt-csEcbh9M9SLaV_IgvpGwJ4), arquivo [01_reproducao.ipynb](https://drive.google.com/file/d/1ma1KHywnIF0lZ3LvsYEk7Ts-2h_J4W69/view). A versão GitHub e a cópia no Drive próprio foram sincronizadas em 17/11/2026; ambas usam `MyDrive/Segurança de Redes de Computadores/Projeto_Mixers_Ethereum` e os módulos `src/ethmix/`. A execução de paridade ainda é necessária para validar resultados.

### Inicialização simplificada (17/11/2026)

`01_reproducao.ipynb` agora monta o Drive antes de importar o código e confere SHA-256 dos três módulos em `src/ethmix/`, sincronizados com o GitHub. A autenticação no GitHub não é necessária no Colab. **A cópia do notebook e os módulos estão no Drive próprio; o GitHub continua sendo a fonte versionada.**


### Correção de localização (17/11/2026)

Se a pasta `Segurança de Redes de Computadores/Projeto_Mixers_Ethereum` não aparecer em `/content/drive/MyDrive`, **não criar atalhos adicionais nem mudar para o Drive de Bruno**. O `01_reproducao.ipynb` atualizado utiliza a API Google Drive com autenticação Google Colab e os IDs **das cópias do Drive próprio**, validando SHA-256 e salvando os relatórios no diretório `results/`. Não depende de caminho montado nem requer `GITHUB_TOKEN`.

A execução completa permanece **pendente de validação no Colab**. Cópia de trabalho no [Drive próprio](https://drive.google.com/file/d/1ma1KHywnIF0lZ3LvsYEk7Ts-2h_J4W69/view).

## Notebook 04 — Auditoria visual

[GitHub: 04_auditoria.ipynb](04_auditoria.ipynb) · [executar no Drive próprio](https://drive.google.com/file/d/1qsqTiOHSdJhSIiK1xGXAp83IpO-T0oq8/view).

Publicado em 17/11/2026: 11 células (4 de código), com 3 gráficos explicados e salvamento opcional de relatórios. Audita resultados já salvos, portanto **não substitui auditoria independente dos dumps**. Sua execução no Colab ainda não foi verificada.

Ver [padrão didático](../docs/07_PADRAO_NOTEBOOKS.md).
