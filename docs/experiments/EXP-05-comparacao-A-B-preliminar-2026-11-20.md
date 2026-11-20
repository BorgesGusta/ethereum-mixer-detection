# EXP-05 — Comparação das fichas A e B (E05-P)

**Data da comparação:** 20/11/2026 (UTC). **Estado:** confronto documental preliminar realizado; adjudicação independente e aprovação humana da ficha A pendentes. **Amostra:** 9 endereços sinalizados em 15/01/2026, selecionados pelo detector, não uma amostra aleatória. **Não permite estimar precisão, recall nem F1 do detector.**

## 1. Identificação e preservação dos artefatos

- **Ficha A:** [Google Sheets — Gustavo](https://docs.google.com/spreadsheets/d/1zmaukMcbQSTemQL9eW8Oe9z68-9UF4Pedn4wR6jG2Jc/edit), aba `revisao_independente_A_PREENCHER`, linhas 2–10. Conteúdo pré-preenchido com **apoio de IA**, classificação ainda **sem aprovação explícita caso a caso** e sem `data_revisao_utc`. Cópia A preservada em pasta restrita de coordenação.
- **Ficha B:** [Google Sheets — Bruno, versão preenchida](https://docs.google.com/spreadsheets/d/1g4mqfuxOewrfBgVIJY2q_lfkzctuG_sztGWEkTSETpw/edit), aba `revisao_independente_B_PREENCHER`, linhas 2–10, `data_revisao_utc` informado como 19/11/2026, 13:45Z ou 14:05Z. Cópia B preservada em pasta restrita de coordenação.
- **Outras fichas B no Drive:** planilhas IDs `1E-Dmy0qh0PeE4t8CEtZT-yUPYcXtSolPCtO_WNQ_AGs` e `11WKBS2R4rs1ZhnJQhhu8SXoIEjLOF9XALzXr27vCqSc` estão sem parecer; **não utilizadas**.
- **Protocolo predefinido:** [EXP05_protocolo_revisao_independente.md](https://drive.google.com/file/d/1rN4LtgLXkzrybFTxL50mSRJeigcrMlQo/view). Nenhuma ficha original foi modificada nesta comparação.

> **Ressalva de independência:** a ficha A foi redigida com auxílio de IA e não contém aprovação humana assinada; os números abaixo representam somente **concordância nominal entre fichas preliminares**, não concordância entre dois revisores humanos independentes. A abertura de B foi autorizada explicitamente pelo usuário em 20/11/2026.

## 2. Comparação resumida

| Caso | Classe A (rascunho IA) | Classe B (Bruno) | Comparação | Encaminhamento preliminar |
|---|---|---|---|---|
| R001 — ApeCoin OFT Adapter | `indeterminado` | `negativo_confirmado` | Divergente | Revisar conclusão negativa com evidência histórica suficiente |
| R002 — SwappableBridge | `indeterminado` | `negativo_confirmado` | Divergente | Revisar troca/ponte e histórico operacional |
| R003 — OKX DEX proxy | `indeterminado` | `indeterminado` | Igual | Manter indeterminado; código histórico da implementação não verificado |
| R004 — Wormhole Relayer | `indeterminado` | `negativo_confirmado` | Divergente | Forte candidato a negativo; verificar código/logs da implementação vigente |
| R005 — Chainlink CCIP Router | `indeterminado` | `negativo_confirmado` | Divergente | Forte candidato a negativo; conferir código e escopo da janela |
| R006 — Tornado Cash 1 ETH | `positivo_confirmado` | `positivo_confirmado` | Igual | Consenso documental provisório, pool já conhecido |
| R007 — MCT-XEN proxy | `indeterminado` | `indeterminado` | Igual | Manter indeterminado; implementação não verificada |
| R008 — Tornado Cash 10 ETH | `positivo_confirmado` | `positivo_confirmado` | Igual | Consenso documental provisório, pool já conhecido |
| R009 — Tornado Cash 0,1 ETH | `positivo_confirmado` | `positivo_confirmado` | Igual | Consenso documental provisório, pool já conhecido |

**Contagem bruta:** 5 classes iguais em 9 casos (55,6%); 4 divergentes (44,4%). A: 3 positivos e 6 indeterminados; B: 3 positivos, 4 negativos e 2 indeterminados. **Não calcular kappa entre revisores humanos**, pois A não foi aprovada por revisor humano independente. O 55,6% não é confiabilidade confirmada dos rótulos.

## 3. Onde as evidências do Bruno acrescentam informações

**R001 — OFT Adapter (A indeterminado, B negativo).** B relatou ABI de OFT Adapter com `send/quoteSend`, `OFTSent`, 15 chamadas `send(...)` de 15/01/2026 e uma transferência interna. A identificou a função geral, mas não verificou o período. B reconheceu que **não leu o código-fonte e não abriu os logs**, e assumiu que a ABI atual representa o período. **Decisão sugerida:** não tornar negativo consensual antes de conferir implementação e evidências históricas; a ausência de funções de mixer na ABI é indício, não prova isolada.

**R002 — SwappableBridge (A indeterminado, B negativo).** B relatou ABI `swapAndBridge/bridge`, 15 operações `swapAndBridge` no dia, uma transação com conversão de ETH para WETH, taxa e troco ao remetente. A registrou swap/ponte sem examinar transações específicas. B não examinou logs nem todo o código-fonte. **Decisão sugerida:** possível negativo, pendente de confirmação documental do comportamento no recorte definido.

**R003 — OKX DEX Proxy (ambos indeterminados).** B identificou uma implementação histórica sugerida como `0x85461e163c64f99a8709dff3bab0db808c358bd6` após examinar eventos `Upgraded`, e operações envolvendo WETH, mas informa que o código da implementação não está verificado. A também indicou falta de confirmação do proxy. **Encaminhamento:** manter `indeterminado`; consultar código/bytecode e evidência de implementação por bloco.

**R004 — Wormhole Relayer (A indeterminado, B negativo).** B informou ter resolvido o proxy para implementação `0x90995dbd1aae85872451b50a569de947d34ac4ee`, lido ABI com `deliver/send/forward`, quatro chamadas `deliver` do dia e eventos de atualização. Isso é evidência mais específica que a ficha A. B ainda **não leu o código-fonte nem logs das chamadas**. **Encaminhamento:** prioritário para adjudicação de possível negativo confirmado após confrontar provas e versão histórica.

**R005 — Chainlink CCIP Router (A indeterminado, B negativo).** B descreveu ABI `ccipSend/getFee/routeMessage`, quatro chamadas `ccipSend` no dia e uma falha. A indicou função de roteador sem prova da janela. B não abriu logs ou transações internas. **Encaminhamento:** possível negativo, mas decisão final requer avaliação de suficiência documental.

**R006 — Tornado Cash 1 ETH (ambos positivos).** B descreveu interface `deposit/withdraw`, prova, nullifier, denominação e exemplos de depósitos/retiradas via Router com logs do dia. A baseou-se principalmente na identificação documental. **Encaminhamento:** positivo de referência; a auditoria de B reforça a evidência, mas não cria protocolo positivo independente.

**R007 — MCT-XEN Proxy (ambos indeterminados).** B descreveu proxy, implementação `0xce2ae22de7d45558c5feaededd828dfd22c6d7a2`, chamadas com 100 IDs sequenciais e seletoras desconhecidas, sem código verificado, logs ou resolução completa da função. **Encaminhamento:** `indeterminado`.

**R008 — Tornado Cash 10 ETH (ambos positivos).** B identificou depósitos e retiradas e informou 43 transações via Router no dia segundo consulta Blockchair, com amostras de eventos no Etherscan. A conferiu a identidade do pool. **Encaminhamento:** positivo de referência, com escopo amostral explicitado.

**R009 — Tornado Cash 0,1 ETH (ambos positivos).** B descreveu `deposit/withdraw`, prova, nullifier e sinais de migração, além de registros amostrais de depósito e retirada no dia. A identificou o pool pela documentação. **Encaminhamento:** positivo de referência, com ressalva sobre migração/cobertura parcial.

### Limites comuns das duas fichas

1. Na coluna `arquivo_sha256`, B deixou as células vazias e A registrou `não calculado`. **Não há arquivos de evidência com hash anexado e verificado em ambas as revisões.** Os hashes de transações não substituem o SHA-256 de arquivos.
2. B relatou inspeção de ABI e partes de transações/logs, e explicitou lacunas de cobertura. A permanece assistida por IA e ainda não tem confirmação humana por caso.
3. O piloto contém somente **alertas selecionados pelo próprio RF**; classes desses casos **não estimam falsos negativos, sensibilidade populacional nem F1**.
4. As três concordâncias positivas referem-se ao **Tornado Cash**, cujo protocolo estava presente no treinamento; não demonstram generalização.
5. `negativo_confirmado` na ficha B representa **parecer de B**, não adjudicação final. Concordar com a função não implica verificação retrospectiva de toda a ausência possível de mixing.

## 4. Passos para encerramento

1. Gustavo revisar os nove rascunhos A, principalmente **R001, R002, R004, R005**, e registrar explicitamente se mantém ou altera cada classe. A ficha já está descegada neste momento; **qualquer mudança posterior será adjudicação/revisão pós-confronto**, não revisão A independente original. Registrar data e autor das mudanças.
2. Um adjudicador conferir a sustentação por código-fonte, implementações históricas e transações/logs pertinentes dos quatro casos de divergência. Não alterar fichas originais. Quando faltar evidência, usar `indeterminado`.
3. Salvar relatório final de adjudicação separado, com versões, fontes e regras aplicadas.
4. Relatar no artigo **análise qualitativa de nove alertas** e limitações, sem fabricar novas métricas de avaliação do detector. Especificar que houve comparação documental de fichas A assistida por IA e B humana, não estudo de confiabilidade interavaliadores humanos.

**Registro de procedência:** esta comparação foi preparada a partir das células A1:N10 das duas planilhas e do protocolo, sem acesso ao índice privado de rótulos do coordenador. As alegações técnicas de B são *registros do parecer B*, não uma revalidação independente de cada transação nesta etapa.
