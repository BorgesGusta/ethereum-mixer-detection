# EXP-03B — Verificação histórica de tipo de endereço dos seis controles

**Preparado:** 18/11/2026 UTC. **Estado: NOTEBOOK PUBLICADO, NÃO EXECUTADO no Colab até este registro.** Parte do piloto exploratório EXP-03. Não cria rótulos negativos, não altera a amostra nem repete EXP-02B/02C.

## Onde executar

- [Notebook ativo no Drive](https://drive.google.com/file/d/1xxJUpr3rrTjGdBnLcJwB6te9-ivqqy-U/view?usp=drivesdk), em `Projeto_Mixers_Ethereum/notebooks/00_ATIVOS/16_EXP-03B_verificacao_historica_controles_2026.ipynb`.
- [Cópia do notebook versionada no GitHub](../../notebooks/16_EXP-03B_verificacao_historica_controles_2026.ipynb), commit `e725ef950d18725aae4f40228814680a0f7bfdf9`.
- Notebook original no Drive: 14.503 bytes, SHA-256 `9731290996b7d8c6288ea1eabf20fd5eafde7570c099df4b0af20c99fd34214b`. Cópia do Drive lida e salva no GitHub sem alteração do JSON.

**Ação para o pesquisador:** abrir notebook com Google Colaboratory, executar todas as células, autenticar a conta com acesso ao Drive. Compartilhar link da nova pasta `results/EXP-03B_controles_historicos_...`, caso a rotina finalize.

## Entradas existentes, sem novo processamento do RF

| Artefato | Drive | SHA-256 exigido |
|---|---|---|
| `controles_provisorios.csv` (EXP-03) | [arquivo](https://drive.google.com/file/d/1qgMy6Yy1UEGm6JgEQqkgrkoyjDHTCz-1/view) | `ea01869f2b776246578c1bd7c78253634704714b5d013853505657de34d890d5` |
| `amostras_tx_api.csv` (EXP-02B) | [arquivo](https://drive.google.com/file/d/17S6xCYOng7Fk21cYZGq5k1yKzNn3kqGq/view) | `83f42e349d25cbbcded99784ba9eb4c148b64c9d91eb3190aab00a76c5f3ea8d` |

**Seleção está congelada:** seis controles já selecionados, sem substituição silenciosa. Os seis alertas pareados são apenas âncoras para recuperar blocos históricos previamente verificados no EXP-02B; não são reauditorados.

## Pergunta e método

**RQ:** para cada controle não alertado, há código de contrato inteligente no **bloco da primeira transação verificada do alertado correspondente**, no dia 15/01/2026?

1. Reconciliar hashes de ambos arquivos de entrada e exigir seis pares únicos.
2. Recuperar **primeiro bloco** da amostra já validada EXP-02B para cada alertado, sempre no dia 15/01/2026.
3. Para o **controle** pareado, consultar `eth_getCode` no bloco histórico usando até dois endpoints públicos JSON-RPC. Registrar todos os provedores, HTTP, mensagens de erro, se código foi retornado, tamanho em bytes e SHA-256 do código quando houver.
4. Consultar `/api/v2/addresses/{address}` do Blockscout **somente como metadado atual** para os seis controles. Metadados atuais nunca substituem a prova histórica.
5. Registrar discordâncias entre provedores como `inconclusivo_conflito_entre_provedores`, indisponibilidade como `inconclusivo_sem_resposta_historica`, código presente como `codigo_presente_no_bloco_amostrado`, código vazio como `codigo_ausente_no_bloco_amostrado`.
6. **Não** converter ausência de código em um bloco em prova de EOA durante todo o dia, ausência de contratos históricos, ou negativa científica de mixer. Código presente tampouco comprova função econômica.
7. Outputs: `controles_estado_historico.csv`, `rpc_evidencias.csv`, `metadados_atuais.csv`, `manifesto_exp03b.json`, com SHA-256 de inputs e outputs.

**Limites:** blocos de referência são pontos específicos dentro do dia (primeira transação verificada do alertado), não prova de todo o intervalo de 24h. Endpoints públicos podem não fornecer estado de arquivo, e pode ser necessário provedor archive dedicado, sem mudar classificação de casos inconclusivos retroativamente.

## Gate para próxima pesquisa

- **Se código histórico presente para controles:** verificar função econômica e cobertura histórica; **sem rótulo binário automático**.
- **Se código ausente:** avaliar comparabilidade contratual e relatar controle não apto no bloco observado. **Não selecionar substituto silenciosamente.**
- **Se inconclusivo:** registrar limitação do provedor, buscar arquivo histórico confiável posteriormente ou descrever falha de cobertura.
- **Sem múltiplos contratos comparáveis:** não produzir inferência de superioridade, recall ou precision; documentar dificuldade do pareamento por n_tx.

## Estado e vínculo ao artigo

**Implementado e versionado, não executado nesta etapa.** Após execução real, auditar logs/manifestos no Drive e marcar o checklist. Anotar no [caderno científico vivo](../manuscrito/CADERNO_CIENTIFICO_VIVO.md), sem gerar PDF.

## Adendo de execução real — 18/11/2026 UTC

O pesquisador executou o notebook. Saídas em [pasta do Drive](https://drive.google.com/drive/folders/1WZ3tbWDY75Jmt_SBE8KX2EDbiUJzRKwu); [relatório auditado](EXP-03B-resultados-verificacao-historica-2026-11-18.md). As saídas coincidem com os SHA-256 registrados no manifesto. **12/12 consultas RPC geraram erros HTTP (403 ou 525); nenhuma prova de `eth_getCode` histórico foi obtida.** As seis tipagens e rótulos históricos continuam indeterminados. Blockscout respondeu 6/6 para metadados **atuais** (cinco `is_contract=false`, um `true` com `proxy_type=eip7702`). A marcação histórica 'NÃO EXECUTADO' no topo preserva o estado ao criar o protocolo; este adendo documenta a execução posterior. O EXP-03B **não validou** a comparabilidade dos controles e não autoriza novas métricas do classificador.
