# EXP-04 — Triagem em duas camadas e qualidade da evidência

**Data de execução:** 18/11/2026. **Status:** EXECUTADO LOCALMENTE com arquivos preexistentes, sem chamadas externas, sem treinamento e sem novos rótulos.

## Motivação e conteúdo da disciplina

A proposta operacionaliza dois conteúdos documentados nos materiais fornecidos pelo pesquisador para a disciplina do Prof. Hugo P. Kuribayashi:
1. **Hash criptográfico SHA-256 / integridade** — Capítulo 2, parte 1, páginas 3 e 12–13: proteger a proveniência dos dados.
2. **Filtragem em camadas** — Capítulo 4, parte 2, páginas 10–16: analogia metodológica de triagem por características estatísticas seguida de inspeção funcional, **não um firewall real**.
A ementa prevê IDS, mas **este script não é IDS de pacotes** e não identifica intrusões, ilícitos ou mixers comprovados. A contribuição própria a testar é a *qualidade e rastreabilidade da evidência* de cada alerta.

## Método realizado

- **Camada 1 preservada:** seis contratos adicionais previamente sinalizados pelo Random Forest legado em 15/01/2026, limiar fixo 0,85; EXP-04 **não calcula scores**.
- **Camada 2 efetiva:** cruzar 18 transações de EXP-02B validadas por hash/remetente/destinatário/data com as três paginações EXP-02C. Consolidar completude de logs e funções reportadas em matriz por endereço, distinguindo evidência amostral de classificação funcional.
- **Controles:** integrar seis controles pré-selecionados EXP-03 com status de código histórico EXP-03B. Como nenhum `eth_getCode` histórico foi obtido, preservar `indeterminado`.
- **Travas:** SHA-256 dos cinco CSVs de entrada, 18 hashes únicos/6 alertas, três paginações completas e reconciliação de 586 logs; abortar se os requisitos divergirem.
- **Saídas:** três matrizes CSV, manifesto JSON, script de processamento Python e arquivo de evidência em pasta própria.

## Artefatos reais

[Pasta oficial Drive: EXP-04](https://drive.google.com/drive/folders/1drM-F9LfePDFSYrGYzlNmySfy0dWQK_K)

- [Script executado](https://drive.google.com/file/d/1Twxfz3N0rMA3R9xJEJX3Ycd5M3MqG7Ed/view) — [versão GitHub](../../scripts/exp04_triagem_evidencias.py), commit `176aa3ee`.
- [Manifesto EXP-04](https://drive.google.com/file/d/1QuaJOclfSqYk17ZAZGBf4EatqqaLszGP/view).
- [matriz_alertas.csv](https://drive.google.com/file/d/13MUk7BsmkSb7n6JdI3Ulu35e4n4WzDfS/view).
- [matriz_amostras.csv](https://drive.google.com/file/d/1V0vClIWF6HZXBfc9wo2NL2rd8crMRegm/view).
- [matriz_controles.csv](https://drive.google.com/file/d/1MsDCPiDiWNC0vAHw9PksDpcro5GAgwvr/view).

O manifesto inclui os SHA-256 das entradas e das três matrizes. A associação documental dos alertas é recuperada do manifesto EXP-02B se presente, mas esse arquivo de contexto **não faz parte das cinco travas de hash**; não interpretar a associação como identidade independente provada.

## Resultado reproduzido a partir dos artefatos anteriores

| Indicador | Observado |
|---|---:|
| Contratos alertados da amostra EXP-02B | **6** |
| Transações verificadas por hash, from, to e dia (EXP-02B) | **18** |
| Logs de eventos amostrados, após incorporar EXP-02C | **586** |
| Transações amostradas com paginação completa ao reunir EXP-02B e EXP-02C | **18/18** |
| Controles com estado histórico válido obtido em EXP-03B | **0/6** |
| Novos rótulos independentes produzidos | **0** |

**Importante:** essas contagens são **reconciliações das análises anteriores**, não nova descoberta de transações ou melhoria de desempenho. Os 586 eventos são somente dos 18 hashes selecionados, não dos 315 registros diretos do dia nem de toda a blockchain. A coluna `metodo_reportado` vem da API Blockscout; seletor não decodificado continua não identificado historicamente. **Não afirmar seis falsos positivos, precision/recall/F1, ou aumento da qualidade do detector.**

## Resultado de segurança aplicável

Conseguimos demonstrar uma **trilha de auditoria de integridade e cobertura de evidência**: nenhum endereço recebeu rótulo definitivo com base apenas em score, metadado atual ou transações isoladas. Essa separação é análoga à distinção entre alerta e confirmação em ferramentas de segurança; ainda não demonstra que uma segunda camada reduza falsos positivos, pois falta ground truth.

## Próximos passos

- [ ] Obter evidência histórica de tipo de contrato para os controles (piloto RPC archive EXP-03C) ou registrar limitação definitiva.
- [ ] Definir política de rotulagem independente por dois revisores, com separação por contrato/protocolo.
- [ ] Selecionar e auditar negativos contratuais adequados em protocolo **prospectivo**, sem alterar os seis pares congelados do EXP-03.
- [ ] Somente depois mensurar se uma política contextual altera falsos alarmes com controle de viés.
- [ ] Registrar no caderno científico; **não gerar PDF do artigo**.
