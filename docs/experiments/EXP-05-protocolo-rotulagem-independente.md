# EXP-05 — Protocolo pré-registrado de rotulagem independente e validade externa

**Preparado em 18/11/2026. Estado: preparação de fichas EXECUTADA; revisão humana e novos rótulos NÃO EXECUTADOS.** Não altera resultados nem rótulos dos experimentos EXP-01J, EXP-02A/B/C, EXP-03/A/B/C ou EXP-04. Não executa acesso on-chain, treino ou avaliação de modelo.

## Pergunta

É possível obter rótulos independentes, transparentes e temporalmente delimitados para contratos sinalizados, preservando as classes `indeterminado` e `fora do escopo`, de modo que uma avaliação futura evite viés de seleção e vazamento por contrato/protocolo?

## Definição operacional **antes** de examinar casos

Classe **mixer de pool com desvinculação de depósito e saque**: protocolo/contrato cujo mecanismo operacional implementa agrupamento de fundos com retirada por uma conta potencialmente distinta, dificultando a associação pública direta entre depósitos e retiradas. Exige fonte independente do classificador e evidência de endereço, bytecode/funções, intervalo temporal e transações pertinentes. Não inferir ilicitude de usuários.

**Privacidade on-chain de outra arquitetura** (shielded pool, rollup privado, roteadores) fica **fora do universo de classificação binária até decisão metodológica separada**. Em especial, RAILGUN (shield/unshield, privado) e Aztec Connect (rollup/bridge histórico) são **famílias a examinar**, não positivos automaticamente equivalentes à classe estreita Tornado Cash. Um eventual experimento que amplie a classe deve receber novo nome, protocolo, definição de rótulos e conjunto de teste não usado para decisões.

**Negativo confirmado no recorte** não é prova da ausência eterna de mixers: exige evidência histórica de função não mixer, cobrindo o contrato correto, período/bloco e tipo/implementação, com uma regra predefinida de suficiência; casos ambíguos são `indeterminado`.

## População e cegamento

- **Conjunto piloto E05-P:** os **9 alertas legados de 15/01/2026**, três pools de referência Tornado Cash e seis endereços adicionais sem ground truth, preservados para **revisão de casos previamente selecionados**, NÃO uma amostra probabilística de toda a rede nem holdout cego.
- `indice_interno_nao_entregar_a_revisores.csv` registra quais três eram pools de referência e quais seis eram alertas adicionais. Guardar apenas com o coordenador, **não distribuir aos revisores**.
- `revisao_independente_A_PREENCHER.csv` e `revisao_independente_B_PREENCHER.csv` contêm **somente IDs, endereços, data e campos para registro**. Não expõem probabilidade, `rotulo` legado, `n_tx`, associação documental atual nem o score do RF. Endereços são visíveis para permitir auditoria on-chain: portanto é cegamento **a scores/modelo**, não à identidade econômica dos contratos.
- Dois revisores devem trabalhar separadamente, sem consultar a ficha um do outro, o ranking/modelo ou a matriz EXP-04 até entregar suas fichas. Revisão independente não significa que a identidade de contratos conhecidos seja desconhecida.

## Ficha e critérios de avaliação

Cada revisor preencherá para **todos os 9 casos**:

1. `classe_proposta`: exclusivamente `positivo_confirmado`, `negativo_confirmado`, `indeterminado`, `fora_do_escopo` ou `nao_avaliado`, com definição/justificativa textual. **Preencher somente com evidência suficiente**; caso contrário `indeterminado`.
2. `tipo_entidade_historico`: endereço de contrato/EOA/código delegado/proxy, respaldado **no bloco do período**; se não houver archive, `indeterminado`.
3. `funcao_economica_historica`: baseada em ABI/bytecode/trace do **período**; nomes de contratos atuais só fornecem indícios.
4. `evidencia_primaria_url`: documentação da implantação, contratos-fonte verificados, transaction hash, receipts/logs, EIP ou repositório original. Identificar **versão e data**.
5. `tx_ou_bloco_referencia`, `arquivo_sha256` e `cobertura_analisada`: bloco/data e evidência verificável, não resposta genérica de explorador.
6. `confianca_qualitativa`, `justificativa_curta`, `lacunas`, `data_revisao_utc`.

**Proibições:** declarar os seis adicionais negativos por constarem em DEX/bridge/relayer, concluir ausência de atividade com três transações, usar implementação atual para afirmar estado histórico, converter HTTP 403/525 em `eth_getCode=0x`, inferir mixer a partir do score, escolher o limiar depois de olhar os rótulos.

## Regras de adjudicação

1. Depois de receber A e B completos, comparar decisões **sem modificar as fichas originais**.
2. Se dois revisores concordarem e **ambos apresentarem evidência independente suficiente**, encaminhar para revisão documental final por adjudicador; a categoria não é automática.
3. Discordância, falta de evidência histórica, proxy não resolvido ou classe ampla conflitante → `indeterminado` e registrar motivo. Um terceiro revisor pode decidir com **evidência adicional documentada**, nunca pelo score.
4. Registrar taxas de concordância **apenas descritivamente** com o denominador claro; não reportar métricas do detector RF com E05-P, pois os casos foram selecionados a partir dos seus próprios alertas.
5. Manter os três positivos Tornado Cash como **referência do mesmo protocolo do treinamento**. Não tratá-los como novos protocolos positivos ou validação externa independente.

## Trilhas candidatas externas (pesquisa documental, NÃO rotulagem)

| Família | Fonte primária/documentação | Uso permitido nesta fase |
|---|---|---|
| Tornado Cash — pools fixos ETH | https://docs.tornadoeth.cash/generals/how-does-tornado-cash-work e https://github.com/tornadocash/tornado-core | Referência funcional de pool e verificação histórica de endereços; três já constam nos alertas 2026, **não novos holdouts** |
| RAILGUN | https://docs.railgun.org/developer-guide/wallet/transactions e https://github.com/Railgun-Community/deployments | **Candidato para investigar arquitetura shield/unshield**; não assumir equivalência à classe estreita nem endereço de implantação sem confronto com registro oficial e bloco |
| Aztec Connect histórico | https://docs.aztec.network/aztec_connect_sunset e https://github.com/AztecProtocol/aztec-connect-contracts | Arquitetura de privacidade/rollup/bridge **separada**; não rotular como mixer de pool automaticamente; confirmar vida útil e implantação por bloco |
| 6 alertas adicionais EXP-02B/C | [EXP-02B](EXP-02B-resultados-auditoria-amostral-2026.md), [EXP-02C](EXP-02C-resultados-logs-e-seletores.md) | Objetos de auditoria cujo status permanece **indeterminado**, não seis negativos conhecidos |

## Gates científicos

**Gate E05-0 PASSOU:** revisão em branco preparada; entradas originais auditadas; duas fichas separadas sem score; manifesto SHA-256; **0 rótulos novos**.

**Gate E05-1 PENDENTE:** revisores A e B designados, fichas completas com evidências independentes e datas e sem compartilhar respostas entre si.

**Gate E05-2 PENDENTE:** reconciliação do adjudicador e confirmação histórico-funcional com arquivos/hashes; recorte suficiente e proxy histórico se aplicável.

**Gate E05-3 BLOQUEADO para validação confirmatória:** exemplos positivos de mais de um protocolo comparável, negativos auditados fora da amostra selecionada pelos alertas, período futuro não explorado, split por contrato/protocolo e política congelada de Router/trace. Sem todos esses itens, **não calcular precision/recall/F1 ou alegar redução de falsos positivos**.

## Artefatos de preparação

Gerados por `scripts/exp05_preparar_revisao.py` a partir do [ranking original de nove alertas](https://drive.google.com/file/d/11kWohs3VvdDGVjwsN_t-S8EQVix6n9mf/view) e [matriz EXP-04](https://drive.google.com/file/d/13MUk7BsmkSb7n6JdI3Ulu35e4n4WzDfS/view); sem novos acessos externos. Os dois arquivos de revisão são **modelos em branco**, não resultados de rotulagem.

**Uso futuro no artigo:** método de criação de ground truth e risco de viés, distinguidos de execução e métricas. Não gerar PDF neste estágio.
