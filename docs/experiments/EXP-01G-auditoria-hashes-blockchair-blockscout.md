# EXP-01G — Paridade hash-a-hash entre Blockchair e Blockscout (29/10/2020)

**Data da análise:** 17/11/2026. **Estado:** executada fora do Colab, sobre os arquivos já guardados no Drive próprio. **Nenhum arquivo fonte foi alterado**.

## Fontes, reprodutibilidade e artefatos

- Dump original Blockchair: `data/raw/blockchair_ethereum_transactions_20201029.tsv.gz` (ID do Drive `1tSs5ds_rycsOy7brWZYRFo5fvXCHn9p2`), 1.114.702 linhas de transações, leitura streaming gzip TSV.
- Amostra independente Blockscout de 29/10/2020: [transacoes_20201029_api.csv](https://drive.google.com/file/d/1Eu0ExPPldUoLeAKv2xmFzEteJnv4wnP9/view), com 20 registros cobrindo integralmente o dia para SmartEther e DSProxy, conforme [EXP-01F](EXP-01F-blockscout-2020-cobertura.md).
- [Pasta de resultados própria no Google Drive](https://drive.google.com/drive/folders/1UJHW32QXPZrFMnLVWSTGrmhonizujqC0).
- [Auditoria linha a linha dos 20 hashes](https://drive.google.com/file/d/14iCpJf54Zguj2Lu0SZgVohxX49ve_UgC/view).
- [Resumo por endereço](https://drive.google.com/file/d/1rVqiifH7VTxkXqohRYo7a7Itq2r2dz7W/view).
- [Manifesto com SHA-256 de ambos os arquivos de entrada](https://drive.google.com/file/d/12qOkNRAn44z2fJXmPz74f3V6nIj6fpLK/view).
- [Script executado (`scripts/auditar_hashes_2020.py`)](../../scripts/auditar_hashes_2020.py) (também [no Drive](https://drive.google.com/file/d/1XJ1pQVaxIWc4sVkjpcm5Iua43fP6kybP/view)).

## Resultados

| Endereço | Nome documental | Quantidade no bruto | Quantidade na API com data coberta | Interseção dos hashes | Somente no bruto | Somente na API |
|---|---|---:|---:|---:|---:|---:|
| `0x98f1858c9740b9c5f2cd8abea67948873d38dc39` | SmartEther | 10 | 10 | **10** | **0** | **0** |
| `0xe113d58a4cb4dbac8a0da608ed7232785c1f2c18` | DSProxy | 10 | 10 | **10** | **0** | **0** |
| `0x5e60fcca904753a31f9df7d7f6b7856b6ec27aa9` | AdminUpgradeabilityProxy | 53 | **não coberto** | n/a | 53 (não consultadas) | 0 |

A amostra de 20 hashes distintos obtida do Blockscout teve **20/20 correspondências** no dump bruto Blockchair. Em cada um dos 20 registros verificamos **hash, remetente, destinatário e bloco idênticos** (após normalização de endereço/hash em minúsculas e prefixo 0x).

A igualdade dos conjuntos de hashes nas duas fontes para SmartEther e DSProxy exclui o risco de coincidência *somente das quantidades* nesses dois casos. **Não** há paridade externa verificada para as 53 transações do AdminUpgradeabilityProxy: a API parou em novembro/2020, após 30 páginas. Zero observações do proxy no arquivo da API **não é evidência de zero transações**.

## Interpretação

- É uma confirmação independente **de identidade e contagem das transações** em dois dos três contratos e do número de linhas do dump, não uma confirmação independente das quatro features internas por uma implementação diferente.
- O status econômico de SmartEther e DSProxy continua classificado como não confirmado para o propósito binário mixer/não mixer. A pesquisa não calcula falsos positivos a partir de nomes de contratos.
- Os dois eventos `Upgraded` conhecidos do proxy são de 12/11/2020 e 25/04/2022. **A implementação ativa em 29/10/2020 ainda não foi observada de maneira independente e não pode ser inferida de um log incompleto.**
- Este experimento não explica a diferença entre os **63 endereços** do artigo e os **9 da nossa reprodução**: aquela continua sendo uma questão de reprodutibilidade metodológica e seleção do conjunto de treino.

## Próximas verificações

1. Para o proxy, consultar o **slot de implementação EIP-1967** no estado histórico do bloco final de 29/10/2020 por `eth_getStorageAt` (exige endpoint Ethereum de arquivo). O método recebe endereço, slot e número de bloco e só permite conclusão caso tenha sucesso e traga o valor histórico, com proveniência do provedor registrada.
2. Alternativamente, investigar os eventos `Upgraded` em blocos até 29/10/2020 via consulta direta com filtros (não por 30 páginas do histórico mais recente).
3. Repriorizar a auditoria do treinamento e dos filtros do experimento, antes de iniciar novas comparações de modelos.
