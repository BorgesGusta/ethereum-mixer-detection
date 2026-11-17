# EXP-01F — Verificação externa Blockscout em 29/10/2020

**Execução:** 17/11/2026, etapa 11 do notebook `01_reproducao.ipynb`. **Conferência dos quatro artefatos no Drive:** 17/11/2026.

**Pasta:** https://drive.google.com/drive/folders/1Xz6tBlOqQcMzzoX1uGycbZPwsyKv17iO

## Arquivos

- [cobertura_api.csv](https://drive.google.com/file/d/14zeKQuR5lScqwpgfQ4OolPuC9h0i5N7_/view)
- [transacoes_20201029_api.csv](https://drive.google.com/file/d/1Eu0ExPPldUoLeAKv2xmFzEteJnv4wnP9/view)
- [upgrades_proxy_api.csv](https://drive.google.com/file/d/1IV_5WA0NefIbknjhBhcn3zhJWr2At9uN/view)
- [manifesto.json](https://drive.google.com/file/d/16KZsAO_yJlNDyNZ1SIETUQcVPaonTsa_/view)

## Cobertura da API de transações e logs

| Endereço | Trilha | Páginas | HTTP final | Data mais antiga | Alcançou 29/10/2020? |
|---|---|---:|---:|---|---|
| `0x5e60fcca904753a31f9df7d7f6b7856b6ec27aa9` | transactions | 30 | 200 | 2020-11-06 | **Não** |
| `0x98f1858c9740b9c5f2cd8abea67948873d38dc39` | transactions | 16 | 200 | 2020-10-27 | **Sim** |
| `0xe113d58a4cb4dbac8a0da608ed7232785c1f2c18` | transactions | 3 | 200 | 2020-10-26 | **Sim** |
| `0x5e60fcca904753a31f9df7d7f6b7856b6ec27aa9` | logs | 30 | 200 | 2020-11-05 | **Não** |

**Contagens externas no dia 29/10/2020:** SmartEther 10 tx e DSProxy 10 tx (concordância de contagem com o dataset intermediário; **a igualdade dos hashes individuais ainda não foi conferida**). Para o proxy, zero transações no CSV desta execução significa **amostra inacessível por limite de paginação**, e **não zero transações no dia**; o dataset interno registra 53.

## Eventos `Upgraded` encontrados na parte consultada

- 2020-11-12T11:43:27Z; bloco 11242610; implementação `0x7497fd42b322d734c4877a35651971206eadced6`.
- 2022-04-25T15:12:03Z; bloco 14654508; implementação `0xee2fcecfb2075a85a31ee8676ce9ae5f3c3be6d7`.

**Ambos os registros carecem de `tx_hash` no CSV**, pois o parser não conseguiu extrair esse atributo no esquema recebido. Por isso, falta validar em consulta pontual ao bloco/log a transação originadora, seus tópicos e os valores. A busca paginada de logs não alcançou 29/10/2020; logo, **não podemos concluir se houve upgrades anteriores nem qual implementação estava ativa naquela data**. Os argumentos do construtor identificam a implementação inicial `0x68b37D89e1AEd3Dd348AD8B1cFC1E678539431D7`, mas ela não pode ser assumida como a histórica sem reconstituição da cadeia de upgrades.

## Interpretação

- A paridade das contagens 10/10 em **duas fontes** aumenta a confiança na completude *desses* casos. Recomenda-se comparar conjuntos de hashes (não apenas quantidade) antes de declarar paridade transacional.
- Para o proxy, a validação independente de suas 53 transações em 2020 **continua pendente**.
- Dois upgrades encontrados com timestamps posteriores ao experimento não dizem qual era a implementação em outubro de 2020, porque a cobertura foi parcial.
- Os achados não mudam labels, scores nem resolvem o desvio dos 63 alertas do artigo versus os 9 de nossa reprodução.

## Próxima etapa prioritária

1. Comparar hashes individuais das 20 transações recuperadas da fonte externa com hashes do dataset intermediário (com contagem de interseção e diferenças).
2. Realizar consulta direcionada ao histórico de implementação do proxy no bloco próximo a 29/10/2020 (eth_getStorageAt no slot EIP-1967 com bloco histórico, usando provedor de arquivo) **ou** paginar até atingir essa data e auditar `Upgraded`; evitar pedidos de API indiscriminados.
3. Prosseguir investigação da metodologia 63 versus 9 com os autores e os arquivos de treino/filtros.
