# D1.4 — Auditoria de integridade dirigida no Google Drive (18/11/2026)

## Escopo, origem e confirmação de acesso

- **Pasta oficial:** [Projeto_Mixers_Ethereum](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj). Metadados Google Drive consultados em 18/11/2026 mostram proprietário da pasta e permissão de escrita da conta conectada. Esta informação resolve a dúvida histórica de titularidade, **mas não comprova integridade da migração inteira**.
- **Estrutura existente:** `data/raw` (30 itens no primeiro nível), `data/interim` (14), `data/processed` (4), `notebooks/00_ATIVOS` (6), `results` com diretórios de EXP-01J/02A/02B/02C.
- **Procedimento:** leitura de metadados das pastas e download **somente dos arquivos pequenos de maior utilidade**, cálculo local de SHA-256 de quatro saídas reais e comparação com manifestos originais do mesmo Drive. Nenhuma execução da blockchain foi refeita, nenhum arquivo do Drive foi alterado.

## Conferência de artefatos reais

| Experimento | Arquivo | Drive | SHA-256 calculado dos bytes | SHA-256 no manifesto | Paridade |
|---|---|---|---|---|---|
| EXP-02B | `amostras_tx_api.csv` (9752 bytes) | [arquivo](https://drive.google.com/file/d/17S6xCYOng7Fk21cYZGq5k1yKzNn3kqGq/view) | `83f42e349d25cbbcded99784ba9eb4c148b64c9d91eb3190aab00a76c5f3ea8d` | mesmo | **SIM** |
| EXP-02B | `eventos_amostras.csv` (228174 bytes) | [arquivo](https://drive.google.com/file/d/1NwJFLTrrMtpLndn2vMV7fLzy9oQJMlH6/view) | `b4442151e64a86722aed72caf15a785f6da800fc139d8befa8e50a41bd143571` | mesmo | **SIM** |
| EXP-02C | `status_paginacao.csv` (457 bytes) | [arquivo](https://drive.google.com/file/d/1uyeomb9MIBuXWlvswDii1boP_70O2hkE/view) | `42db4ef99505297d916f8aa9906f80f97a225ef2ca919eaf566cddc2dd9e5bc3` | mesmo | **SIM** |
| EXP-02C | `seletor_vs_abi_atual.csv` (802 bytes) | [arquivo](https://drive.google.com/file/d/1F2SD_Wu6CtbZg_sxrUPtKsvlOTq6E-5N/view) | `a722f447214a578fc7901eed100be0161ebac9362f128b1dab05b0645840e4ad` | mesmo | **SIM** |

**Manifestos de referência:** [EXP-02B](https://drive.google.com/file/d/1uM3FQlaJQXXMKuTuACO6BI2oLU1_qVE7/view), [EXP-02C](https://drive.google.com/file/d/1AM7PnVWFb5lFSBhuOYwkofBoEZ3xVXsW/view). Os scripts em Drive `EXP-02B_script_auditoria_2026.py` (12571 bytes) e `EXP-02C_script_paginacao_e_abi.py` (10034 bytes) também foram baixados e tiveram seus blobs `git hash-object` comparados com os blobs do GitHub. **Correspondências:** `764d9eba10dcd3be01b64c91a19223c0593a3412` (EXP-02B) e `a3d89ec7663a216241c7e8eac1fd4cd28a14cd16` (EXP-02C). **Isso comprova igualdade de scripts armazenados, não histórico exato de execução do Colab**.

## Próximas verificações sem retrabalho

- [x] Confirmar pasta oficial e suas subpastas principais no Drive
- [x] Localizar scripts/manifestos dos EXP-02B e EXP-02C
- [x] Conferir SHA-256 de quatro outputs selecionados **contra seus próprios manifestos**
- [x] Comparar scripts versionados no Drive e GitHub por blob Git
- [ ] Verificar os SHA-256 de amostras prioritárias contra **arquivos originais da pasta compartilhada**, pois paridade com manifesto não prova equivalência da migração
- [ ] Inventário recursivo completo de origem × destino e diferenças de documentos nativos
- [ ] Identificar/reconciliar cópia exata do notebook executado no Colab com commit de GitHub
- [ ] Atestar todos os arquivos binários grandes; não executar download integral sem necessidade

## Estado de D1.4

**PARCIALMENTE EXECUTADA** — amostra prioritária verificada, mas **migração integral ainda não certificada**. Não confundir a conferência interna das saídas com a comparação de arquivos origem × cópia. A próxima tarefa deve priorizar um inventário recursivo e comparação de fontes, antes de baixar grandes dumps.

**Princípio:** não reexecutar EXP-01J, 02B e 02C; não modificar datasets históricos; registrar limites de cobertura.
