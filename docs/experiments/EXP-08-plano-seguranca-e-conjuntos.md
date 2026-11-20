# EXP-08 — Candidatos independentes, negativos difíceis e protótipo defensivo

**Data:** 19/11/2026. **Estado:** inventário/implementação demonstrativa concluídos; novos rótulos, treino em dataset ampliado e validação externa **não executados**. Entrega inicial do trabalho: 20/11/2026.

## 1. Problema científico e limites

O EXP-07 possui 123 linhas, mas **somente um contrato positivo** (23 dias) e 100 contratos negativos (uma observação por contrato). Em todos os cinco folds há identidade positiva compartilhada entre treino e teste. Portanto, alto F1 interno **não prova** detecção de novos contratos/protocolos.

**Nova hipótese, ainda não testada:** amostras negativas de funções on-chain plausivelmente confundíveis com mixers (*hard negatives*) e amostras positivas de protocolos independentes, após revisão externa, permitem construir uma avaliação mais difícil, com menor dependência de identidade.

## 2. Negativos difíceis: seleção sem circularidade

Inventário em `candidatos_classes.csv` inclui **seis famílias documentadas no EXP-02A** como entidades associadas a alertas (OKX DEX, ApeCoin OFT Adapter, SwappableBridge, Chainlink CCIP Router, MCT-XEN Batch Minter e Wormhole Relayer). **Todos continuam indeterminados; nenhum foi reclassificado como negativo.** Os seis são **candidatos** a negativo difícil pela função econômica potencialmente distinta, não exemplos de classe 0.

Portões obrigatórios: (i) determinar endereço exato, rede, proxy e data; (ii) verificar função econômica e logs/ABI no período; (iii) excluir evidência de mecanismo da classe positiva predefinida; (iv) revisão humana independente; (v) comparar controles por janela temporal/volume e origem das fontes; (vi) congelar lista, splits e critérios *antes* de avaliar modelo. Os seis foram selecionados a partir de alertas do RF: **esse conjunto é condicionado ao modelo e enviesado**; serve para análise de erros, não para teste externo sem viés. Construir em paralelo controles não selecionados por alertas.

## 3. Positivos de protocolo independente

- **Privacy Pools v1**, pool ETH mainnet `0xF241d57C6DebAe225c0F2e6eA1529373C9A9C9fB`, *Entrypoint* `0x6818809EefCe719E480a7526D76bD3e561526b46`. EXP-06A/06B/06C registraram interação de depósito, `CREATE` do contrato e quatro transações históricas `Withdrawn` verificadas em duas janelas. **Rótulo mixer binário NÃO atribuído**: falta validar equivalência à definição operacional, ABI/versão histórica e parecer independente.
- **RAILGUN**, arquitetura shield/unshield. Precisa de contrato e período histórico antes de qualquer teste; não assumir classe positiva idêntica.
- **Aztec Connect**, privacidade rollup/bridge: candidato a classe taxonômica distinta e possivelmente fora da janela de 2026.
- **Tornado Cash 100 ETH** seria controle de **mesma família**, não novo protocolo.

Um holdout válido requer **protocolos positivos independentes rotulados** e controles negativos definidos sem seleção pelos scores; reportar também métricas por contrato e por protocolo, não apenas por dia.

## 4. Implementação defensiva demonstrativa — triagem com evidências

`triage.py` é um protótipo didático *offline*, somente biblioteca padrão Python, com entrada JSON. Valida endereços Ethereum e hashes de transações; distingue confirmação de recibo/log de mera pontuação do ML; coloca casos em estado `indeterminado`; recomenda `revisar_evidencias` ou `coletar_evidencias`; registra os eventos em JSONL encadeado por SHA-256, com ferramenta de verificação contra adulteração acidental ou não autorizada. **Nunca classifica ilícito, nunca determina rotulagem científica e nunca bloqueia contratos.** Não envia dados à rede. Evidência com flags booleanas é **fornecida pelo operador**; o protótipo **não consulta recibos** nem valida criptograficamente a blockchain por si, portanto esses campos exigem ingestão confiável antes de produção.

### Execução (em diretório `scripts/security_triage`)

```bash
python3 -m unittest -v test_triage
python3 triage.py triage --input sample_cases.json --output saida_audit.jsonl
python3 triage.py verify --input saida_audit.jsonl
```

**Teste local concluído:** quatro casos unitários passaram; execução com dois casos de demonstração produziu dois registros encadeados e verificação bem-sucedida; mudança proposital de `REVIEW_ONLY` para `AUTO_BLOCK` provoca erro de integridade. Não é validação em SOC, SIEM ou ambiente real.

### Modelo de ameaça e controles

| Risco | Controle demonstrado | Lacuna para produção |
|---|---|---|
| Alerta de modelo confundido com prova | Nenhum score vira rótulo / bloqueio | calibrar probabilidade, validação independente |
| Evidência sem origem identificável | URL e hash sintaticamente validados | conferir origem, transação on-chain e assinaturas |
| Alteração de histórico de auditoria | Hash chain e verificador local | ancorar hash externo, assinatura e armazenagem WORM |
| Informações sensíveis registradas | Não solicita chaves privadas nem seed | controle de acesso, minimização e proteção de PII |
| Automação excessiva | `REVIEW_ONLY` fixo | políticas formais de resposta e aprovação humana |

**Importante:** SHA-256 encadeado sozinho não impede um atacante de reescrever a trilha inteira e recalcular hashes. Para garantia real, fixar o hash terminal em outro sistema de confiança (WORM, assinatura, timestamp externo). Não afirmar imutabilidade só por JSONL.

## 5. Proposta de integração com Segurança de Redes

Pipeline proposto (não implementado em rede): coletor de eventos on-chain → extrator de características → detector ML → correlacionador documental/on-chain → triagem humana (protótipo atual) → trilha de auditoria → painel/SIEM (futuro). Desenhar resposta em níveis: **observar → revisar → documentar → escalar**, jamais bloqueio automático a partir do classificador atual. A coleta e inferência automática, interface e SIEM **não foram implementados**.

## 6. Critérios de sucesso de uma etapa futura

- Novos contratos positivos realmente independentes, com etiquetas aprovadas por revisores.
- Controles difíceis e não selecionados por alertas, auditados em períodos correspondentes.
- Divisão agrupada por família/protocolo; sem reutilizar protocolo positivo no teste.
- Relatar precision, recall, F1 por contrato/protocolo, especificidade, taxas de falsa detecção por tipo de negativo, custo de triagem e intervalo de confiança quando dados permitirem.
- Comparar RF/árvores/boosting e, **se tamanho e natureza dos dados permitirem**, GNN (grafos) ou MLP (tabulares). CNN só se houver sequências adequadas; não usá-la como substituto de rótulos ausentes.

## 7. Status para artigo entregue 20/11/2026

**É legítimo afirmar:** protótipo didático local desenvolvido e testado; inventário de candidatos criado; proposta de protocolo EXP-08 escrita. **Não afirmar:** nova detecção validada, novos positivos/negativos confirmados, redução observada de falsos positivos, CNN/GNN treinada, melhoria real de F1, integração efetiva com SIEM ou resposta automática. Se espaço insuficiente, apresentar este trabalho como protótipo complementar e continuidade, preservando resultados empíricos anteriores como contribuição central.
