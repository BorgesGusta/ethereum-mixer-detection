# EXP-03B — Resultado auditado da verificação histórica dos seis controles

**Estado:** executado no Colab e **outputs auditados** em 18/11/2026. **Resultado de verificação histórica: inconclusivo (0/6)** por bloqueios HTTP dos provedores, não por ausência demonstrada de código. Nenhum rótulo científico foi atribuído, não houve retreino nem alteração da amostra.

## Referências canônicas e execução

- [Pasta Drive EXP-03B](https://drive.google.com/drive/folders/1WZ3tbWDY75Jmt_SBE8KX2EDbiUJzRKwu).
- [Manifesto](https://drive.google.com/file/d/1RJLHzW3GGGewmikEGbNVSp3mesuRxkgd/view), execução declarada `2026-11-18T02:53:11.487212+00:00`.
- [controles_estado_historico.csv](https://drive.google.com/file/d/19ih1w5zQgZta2qZ0LI2aH-K0PnvASX98/view)
- [rpc_evidencias.csv](https://drive.google.com/file/d/1V5fh2fsZfImEuu7e_s_JASuDcYdnXP0T/view)
- [metadados_atuais.csv](https://drive.google.com/file/d/1bI0_5FH7j-i2DW-3P14cYNVvn3nJ3ZnO/view)
- [Notebook versionado](../../notebooks/16_EXP-03B_verificacao_historica_controles_2026.ipynb), [protocolo](EXP-03B-protocolo-verificacao-tipo-historico.md).

## Integridade e escopo

Todos os hashes SHA-256 das três saídas foram **recalculados sobre os arquivos reais baixados do Drive** e coincidiram com `sha256_saidas` do manifesto:

| Arquivo | Linhas | SHA-256 |
|---|---:|---|
| `rpc_evidencias.csv` | 12 | `b03c28cb267182d3ca9edc50f2666f08df8118617c208d2e7a64c331a523e144` |
| `controles_estado_historico.csv` | 6 | `0db4e36948edc8a261d6031355657b2fe7814a4dfba30bb4e97a50850caf72eb` |
| `metadados_atuais.csv` | 6 | `ed08ed4d47b827b880d5e0b81c45799b5373f99df9e2a4894562d14c524cca34` |

Manifesto declara hashes dos insumos congelados **sem recálculo independente nesta revisão**: `controles_provisorios.csv` = `ea01869f2b776246578c1bd7c78253634704714b5d013853505657de34d890d5`; `amostras_tx_api.csv` = `83f42e349d25cbbcded99784ba9eb4c148b64c9d91eb3190aab00a76c5f3ea8d`. Esses hashes já haviam sido verificados nas etapas EXP-03 e EXP-02B.

Seis controles congelados, seis blocos-âncora extraídos do EXP-02B, todos em 15/01/2026, e doze consultas RPC tentadas. Nenhuma mudança nos seis pares nem nas classes.

## Resultados das consultas

| Provedor | Total | Resposta HTTP | Código histórico obtido |
|---|---:|---|---|
| `https://ethereum.publicnode.com` | 6 | 403 em 6/6 | 0 |
| `https://eth.llamarpc.com` | 6 | 525 em 6/6 | 0 |
| Blockscout API /addresses, **estado atual** | 6 | 200 em 6/6 | Não consulta estado histórico |

**Todos os seis controles receberam `status_codigo_historico=inconclusivo_sem_resposta_historica`, `tipagem_funcional=indeterminada` e `rotulo_cientifico=indeterminado`.** Uma resposta HTTP 403 ou 525 **não** é `0x` retornado por `eth_getCode`; não demonstra EOA nem ausência de bytecode em 2026.

### Metadados atuais, nunca retroativos

| Controle | Blockscout `is_contract` atual | `proxy_type` atual | Situação histórica |
|---|---|---|---|
| `0xbd70bb67c90ea7d01abcf5b0c973a3830c7cff88` | False | vazio | Indeterminada |
| `0x18d1b124044e028511875cfdb380c240f6f87035` | True | **eip7702** | Indeterminada |
| `0xf7de94d35d6a28563b66506ec4e7a9826b583ac1` | False | vazio | Indeterminada |
| `0xac345edaa698ba22f0db05a73209e4373c2d3120` | False | vazio | Indeterminada |
| `0x99dcb46e59971c30f860f451e8e05c3084be03dd` | False | vazio | Indeterminada |
| `0xff00000000000000000000000000000000000010` | False | vazio | Indeterminada |

**Atenção EIP-7702:** status `is_contract=True` atual com `proxy_type=eip7702` merece tratamento distinto de contrato implantado tradicionalmente. Pode envolver delegação de código para conta. Sem evidência do bloco histórico, não inferir implantação em 15/01/2026, função ou adequação como controle.

## Avaliação da utilidade científica

- **Execução e integridade:** satisfatórias para documentar cobertura de consultas e respostas.
- **Gate 1-B — tipagem histórica:** **NÃO SATISFEITO**: 0/6 respostas históricas válidas.
- **Gate 2 — auditoria funcional comparativa:** **NÃO INICIADO**. Não temos seis contratos controles comparáveis, nem provas de EOA ou rótulos negativos.
- **Gate 3 — revisão independente:** pendente.
- Os controles anteriores tinham score RF = 0,0 e foram pareados por bandas de `n_tx`, não por função econômica. Não utilizar a divisão como evidência de melhora do detector.
- **Sem retrabalho:** não repetir as 12 consultas bloqueadas aos mesmos serviços sem mudar justificadamente a fonte/infraestrutura de prova. Não reexecutar EXP-02B/C nem retreinar RF.

## Próximo passo sugerido (ainda não executado)

1. Fazer **inventário documental de provedores que realmente ofereçam estado histórico de Ethereum no bloco 24.236.xxx**, ou encontrar recibos/artefatos históricos previamente armazenados.
2. Realizar no máximo **teste diagnóstico mínimo com um endereço e um bloco**, confirmar capacidade da nova fonte e depois os demais seis, com limites de taxa e manifesto.
3. Em paralelo, desenhar **amostra de controles da mesma categoria econômica** (contratos auditados), preservando a amostra congelada como piloto diagnóstico e registrando novo protocolo antes da seleção. **Nunca substituir retrospectivamente os seis pares**.
4. Se não existir fonte histórica acessível, relatar limitação e direcionar a sprint para positivos independentes de outros protocolos e revisão do ground truth.

**Estado do artigo:** registrar somente como achado de limitação de cobertura de auditoria histórica, sem PDF e sem afirmar robustez/superioridade.
