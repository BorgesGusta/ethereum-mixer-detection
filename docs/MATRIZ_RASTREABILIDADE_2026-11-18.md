# D1.2 — Matriz de rastreabilidade experimental (primeira revisão)

**Revisão documental:** 18/11/2026. **Finalidade:** reaproveitar evidências existentes antes de decidir por qualquer reexecução. **Não executa nem valida modelos de novo.**

| ID | Execução histórica / status | Código/notebook existente no GitHub | Dados/manifesto de execução | Evidências de saída | Vinculação exata de commit executado? | Limitações |
|---|---|---|---|---|---|---|
| EXP-01J | 17/11/2026 14:29:36 UTC; executado | [notebooks/01_reproducao.ipynb](../notebooks/01_reproducao.ipynb), etapa 13; blob consultado `5230f2cbbeeb56c6d1f4ab4b1c29f46ee7d46560` | [manifesto no Drive](https://drive.google.com/file/d/1hZkvRQtJoxJ0TNlE0ATMefPdrjJEl01e/view); SHA-256 treino `0a8baa11cee97d338d7a8d92b984f38192ba1a10ec915cc4a06d67ec94ad5c32`; teste `6f8fd4e83e816c785d449116699065ad77425c9da6e7b19d9bcda36f42bddb51` | [seis artefatos](https://drive.google.com/drive/folders/1AFO6k3ShxdsZABU1OoFBXez7Dd8FngOx); [relatório](experiments/EXP-01J-resultados-sensibilidade-63x9.md) | **Não estabelecida**: blob atual verificado, mas não identificado como o executado | Sensibilidade 49/14/9/7; não explica 63×9 |
| EXP-02A | Inventário 17/11 de teste legado 15/01/2026; não houve nova inferência | [notebook legado 07b no Drive](https://drive.google.com/file/d/1w0rdPBevY4Pc9IrLxz8IGT7lBgCOVVK3/view); [manifesto documental](experiments/EXP-02A-manifesto.json) | [triagem e manifesto](https://drive.google.com/drive/folders/15Do7dwtJgd4T7pkmXDptDfMKWn2NHkIE) | [CSV de nove alertas](https://drive.google.com/file/d/11kWohs3VvdDGVjwsN_t-S8EQVix6n9mf/view); [relatório](experiments/EXP-02A-inventario-e-triagem-2026.md) | **Não estabelecida** | Conjunto 2026 já explorado; seis rótulos não confirmados |
| EXP-02B | 17/11/2026 16:10:57 UTC; executado | [notebook 13](../notebooks/13_EXP-02B_auditoria_funcional_2026.ipynb), blob `27d84221cea08605e13c2fed273c0c72a5cb5d92`; [script](../scripts/exp02b_auditoria_2026.py), blob `764d9eba10dcd3be01b64c91a19223c0593a3412` | [manifesto e inputs](https://drive.google.com/drive/folders/1rV5mJ0rkINLML5aFUFnl0s7g1ybwrwOb); SHA-256 intermediário `9537f05d29044991f9a4750de1ea1b2dc5a466c4155826d53d14c4957cbbd143`; ranking `5e989df3b50b2e5f84cab01af7fef4861dcb5eb63ecd0a2f5ae9f62ed9e8a260` | [relatório](experiments/EXP-02B-resultados-auditoria-amostral-2026.md); 18 hashes amostrados e 6 contagens conciliadas | **Não estabelecida**; blob atual não prova correspondência com código executado | 18/18 é amostra; 315 é contagem de tx diretas, não verificação externa integral |
| EXP-02C | 17/11/2026 17:25:57 UTC; executado | [protocolo](experiments/EXP-02C-protocolo-paginacao-e-seletores.md); [notebook no Drive](https://drive.google.com/file/d/1ZP68tB80XqhYIkyhWP6GOwpe3BDrquPU/view); [script versionado](../scripts/exp02c_logs_abi.py), blob `a3d89ec7663a216241c7e8eac1fd4cd28a14cd16`; [notebook 14 versionado](../notebooks/14_EXP-02C_logs_MCT_XEN_e_abi.ipynb); **correspondência exata à execução ainda a conferir** | [manifesto EXP-02C](https://drive.google.com/file/d/1AM7PnVWFb5lFSBhuOYwkofBoEZ3xVXsW/view); SHA-256 das entradas do EXP-02B `83f42e349d25cbbcded99784ba9eb4c148b64c9d91eb3190aab00a76c5f3ea8d` e `b4442151e64a86722aed72caf15a785f6da800fc139d8befa8e50a41bd143571` | [pasta 6 artefatos](https://drive.google.com/drive/folders/13348CzioFtdQWc6snAEPQLroVBiAO_6T); [relatório](experiments/EXP-02C-resultados-logs-e-seletores.md) | **Não estabelecida** | 466 logs completos de três hashes; proxies históricos inconclusivos |

**Observação sobre hashes:** blobs SHA do GitHub identificam o conteúdo lido nesta revisão, **não** demonstram por si só a revisão exata usada no Colab. Hashes SHA-256 de insumos acima são os registrados nos relatórios e manifestos, **não recalculados agora**. O teste legado 2026 não deve ser executado de novo apenas para confirmar o resumo já conhecido.

## Verificações pendentes sem retrabalho

- [ ] Comparar versões e metadados de execução dos notebooks Colab com commits históricos por arquivo e horário.
- [x] Localizar o caminho do script EXP-02C: [`scripts/exp02c_logs_abi.py`](../scripts/exp02c_logs_abi.py) e [`notebooks/14_EXP-02C_logs_MCT_XEN_e_abi.ipynb`](../notebooks/14_EXP-02C_logs_MCT_XEN_e_abi.ipynb). **Ainda pendente** associar o commit exato executado ao manifesto; identificação de arquivo não é prova da versão executada.
- [ ] Verificar hashes de outputs prioritários nos bytes reais armazenados no Drive; não apenas aceitar o manifesto como auditoria completa.
- [ ] Distinguir inventário documental (EXP-02A) de execução real do notebook legado 07b.
- [ ] Acrescentar ambiente, versões de dependências, seeds e convenções de Router quando realmente disponíveis.
- [ ] Não repetir EXP-01J, EXP-02B ou EXP-02C sem identificar falha material documentada.

**Conclusão permitida:** existem referências rastreáveis para os quatro marcos. A rastreabilidade **até a revisão exata executada** ainda está incompleta. O arquivo serve de mapa para completar essa lacuna com inspeção de evidências, não reexecução indiscriminada.

## Checagem adicional: commits históricos e identidade do arquivo

Consulta ao histórico do GitHub em 18/11/2026. Foram comparados os blobs dos arquivos **na revisão do commit histórico** e na `main` atual, com correspondência exata. Os commits são anteriores aos horários relatados das execuções; isso indica versões candidatas, **mas não substitui provar a cópia exata do Colab**.

| Experimento | Arquivo | Commit candidato anterior à execução (UTC) | Blob no commit = blob atual? |
|---|---|---|---|
| EXP-01J | `notebooks/01_reproducao.ipynb` | [`9fd895a`](https://github.com/BorgesGusta/ethereum-mixer-detection/commit/9fd895a04b011838298d09917f6d339d3f9cd036), 17/11 14:25:53 | **Sim**, `5230f2cbbeeb56c6d1f4ab4b1c29f46ee7d46560`; relatório executado 14:29:36 |
| EXP-02B | `notebooks/13_EXP-02B_auditoria_funcional_2026.ipynb` | [`05f9cc2`](https://github.com/BorgesGusta/ethereum-mixer-detection/commit/05f9cc21d20562b171b9dfe595a931c9acbba547), 17/11 15:38:14 | **Sim**, `27d84221cea08605e13c2fed273c0c72a5cb5d92`; execução 16:10:57 |
| EXP-02B | `scripts/exp02b_auditoria_2026.py` | [`0414fc5`](https://github.com/BorgesGusta/ethereum-mixer-detection/commit/0414fc59fb485f65ca88d00694fb46d62c5ead1f), 17/11 15:38:19 | **Sim**, `764d9eba10dcd3be01b64c91a19223c0593a3412` |
| EXP-02C | `notebooks/14_EXP-02C_logs_MCT_XEN_e_abi.ipynb` | [`4ca6583`](https://github.com/BorgesGusta/ethereum-mixer-detection/commit/4ca658323cd6a2ba17ba7864594eded62d681da1), 17/11 16:43:46 | **Sim**, `2affccf111c036692c7126351ee4dfc65cb01d72`; execução 17:25:57 |
| EXP-02C | `scripts/exp02c_logs_abi.py` | [`53bf9d2`](https://github.com/BorgesGusta/ethereum-mixer-detection/commit/53bf9d2a8f74ef17b8517a1b0c7d89295c011fdb), 17/11 16:43:51 | **Sim**, `a3d89ec7663a216241c7e8eac1fd4cd28a14cd16` |

**Estado atualizado:** arquivo e commit candidato comprovados por versão Git; cópia e execução do Colab continuam com vínculo **provável, não demonstrado de forma conclusiva**, porque o manifesto não registra os hashes Git dos notebooks. EXP-02A é inventário documental e seu notebook legado 07b requer verificação própria. Reexecução não necessária para fechar essa lacuna: preferir checagem dos metadados do notebook efetivamente executado no Drive.
