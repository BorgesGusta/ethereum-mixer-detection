# EXP-05 — Guia de revisão independente A (Gustavo)

**Estado em 20/11/2026:** protocolo e fichas preparados; a ficha A nativa está **em branco em R001–R009**. O revisor B (Bruno) informa ter feito sua parte; suas respostas **não foram lidas** nesta conferência.

**Abrir somente:** [Sua planilha A](https://docs.google.com/spreadsheets/d/1zmaukMcbQSTemQL9eW8Oe9z68-9UF4Pedn4wR6jG2Jc/edit). [Protocolo de revisão](https://drive.google.com/file/d/1rN4LtgLXkzrybFTxL50mSRJeigcrMlQo/view).

## Pergunta da revisão

O endereço, **no período de 15/01/2026**, implementava um *mixer de pool com desvinculação de depósito e saque*, era uma função não mixer documentalmente demonstrada, ou permanece sem evidências suficientes?

## Como preencher cada um dos nove casos

1. Examine `case_id`, `endereco`, `data_alvo`. Não olhe planilha B, índice de coordenação, ranking de scores do RF ou tabelas de rótulo anteriores.
2. Procure **fontes primárias independentes do modelo**: código verificado, implantação, documentação histórica, transações, recibos, logs, ABI e, quando possível, evidência do bloco correspondente. Um nome atual em explorador não comprova o comportamento passado.
3. Complete `classe_proposta` apenas com: `positivo_confirmado`, `negativo_confirmado`, `indeterminado`, `fora_do_escopo` ou `nao_avaliado`. Na dúvida, prefira **`indeterminado` e explique a lacuna**.
4. Complete, com o que efetivamente verificou: `tipo_entidade_historico`, `funcao_economica_historica`, `evidencia_primaria_url`, `tx_ou_bloco_referencia`, `arquivo_sha256`, `cobertura_analisada`, `confianca_qualitativa`, `justificativa_curta`, `lacunas`, `data_revisao_utc`.
5. Se uma chamada RPC histórica falhar (ex. HTTP 403/525), registre **falha de acesso**, jamais ausência comprovada de código.
6. Não confunda mixer com ilegalidade. Não considere os seis alertas adicionais como negativos apenas porque parecem bridges, DEX, roteadores ou relayers.
7. Ao terminar R001–R009, registre a data em UTC, confira se as justificativas e links são específicos, preserve a ficha e avise **“EXP-05 A concluído”**. **Só depois** leremos a versão B final para reconciliação.

## O que fazemos depois

- Identificar e congelar as versões finais A e B, preservando os originais.
- Construir tabela de pareamento **R001–R009** com acordo, discordância e lacunas.
- Investigar divergências com evidência adicional; deixar `indeterminado` quando necessário.
- Reportar **concordância descritiva** do piloto; não publicar precisão/F1 do classificador a partir da amostra de alertas E05-P.
- Criar relatório `EXP-05__resultados_adjudicados__2026-11-20.md`, atualizar o caderno científico, o mapa do Drive e, se houver espaço e evidências, o artigo.

**Esta atividade é uma revisão independente de rótulos/casos, não uma revisão acadêmica por pareceristas externos do manuscrito.**
