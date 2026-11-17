# Plano de artigo com potencial de submissão — Hipóteses, experimentos e critérios de avanço

**Rascunho de decisão, 17/11/2026. Não equivale a submissão.** A meta é fortalecer uma contribuição original, com baseline verificável e avaliação honesta.

## 1. Títulos de trabalho (provisórios)

1. **Além da Entropia: Evidências Funcionais para Distinguir Mixers de Outros Serviços Ethereum em Detecção de Segurança**.
2. **Auditoria Reprodutível de Detecção de Mixers Ethereum: Limitações de Features Estatísticas e Contexto de Execução**.
3. **Mixers ou Routers? Uma Avaliação Explicável de Alertas de Contratos Ethereum sob Deriva Temporal**.

Usar o título 1 somente **se** executarmos e validarmos o modelo contextual; caso contrário preferir 2, que descreve contribuição já mais próxima dos resultados disponíveis.

## 2. Três questões de pesquisa candidatas

**RQ1 — Reprodutibilidade e elegibilidade:** em que medida escolhas de amostragem, filtro mínimo de transações e engenharia de features alteram a contagem e a composição dos alertas em um modelo de referência de quatro features?

**RQ2 — Diagnóstico de confusão de contratos:** que categorias e funções de serviços Ethereum aparecem entre os endereços sinalizados, e com qual confiança essas identidades podem ser confirmadas para a data específica da inferência?

**RQ3 — Valor incremental de contexto funcional:** a adição de evidência de execução (selectors, logs, diversidade de contrapartes, proxy/Router e cobertura) melhora desempenho em **novos contratos mixers versus negativos difíceis**, sem diminuir significativamente recall dos positivos?

RQ1 tem resultados internos reproduzidos; RQ2 tem **triagem documental, sem rótulos completos**; RQ3 é **hipótese ainda não testada**.

## 3. Desenho experimental progressivo

**Fase A — Fechar corpus de rótulos:** localizar contratos positivos de múltiplos protocolos mixers (não só Tornado), com identificação de código/eventos na data. Validar negativos difíceis de DEX, bridges, Router, token, relayers e batch minters por atividade e função real do dia. Marcar casos incompletos como indeterminados. Guardar votos de dois revisores.

**Fase B — Baselines congelados:** RF 4 features conforme protocolo do artigo; uma regra heurística baseada em evidências deposit/withdraw/proof; possível Logistic Regression com as mesmas features; **não escolher método após olhar o teste**.

**Fase C — Modelo contextual simples:** adicionar poucos atributos que possamos derivar de modo reprodutível (exemplo: diversidade de remetentes, evidência de deposit/withdraw executados, presença de eventos específicos e flag de cobertura de trace). Versionar regras de engenharia e faltantes. Para proxy, exigir implementação histórica validada ou marcar inconclusivo.

**Fase D — Holdout por grupo e tempo:** separar protocolos/contratos completos, preservar período futuro novo, registrar previamente splits e limiar. Validar generalização para arquitetura mixer distinta quando existir amostra.

**Fase E — Métricas e análise:** precision, recall, F1, PR-AUC e confusão **somente em conjunto rotulado independentemente**; matriz por categoria de negativo difícil; intervalo de incerteza quando houver amostra suficiente; contagem de alertas na população sem rótulo reportada apenas descritivamente. Medir custo de cobertura (quantos contratos exigem trace/ABI que não está disponível).

**Fase F — Ablation e ameaças:** retirar uma categoria de feature por vez, estudar sensibilidade a agregação por dia e ao Router, reportar casos em que dado histórico está indisponível, discutir rótulo incerto, data de coleta e escolha de limiar.

## 4. O que NÃO fazer

- Não mudar o limiar só para que 9 vire 63; o artigo não é um “alvo de otimização”.
- Não chamar seis serviços documentados de “seis falsos positivos” antes de revisão independente.
- Não declarar maior precisão, recall, F1, robustez ou “mais segurança” sem mesmo escopo, rótulos, testes e métricas.
- Não comparar o RF contratual diretamente com F1 de StealthLink (correlação de contas), MixGuard (lavagem por incidente) ou GNN de carteiras como se fossem classificadores da mesma tarefa.
- Não citar uma data de e-mail sem resposta como prova permanente; confirmar situação no fechamento do manuscrito.
- Não tornar os dados de 2026 (já explorados e utilizados em publicação interna) em “teste novo” depois de ajustes.

## 5. Estrutura recomendada para manuscrito

**Resumo:** motivação, pergunta, método, evidências e resultado quantitativo realmente medido, seguido de limitação.

**1. Introdução:** segurança de serviços em blockchain, risco de confundir contrato mixer com operações DeFi, falta de rótulos/observabilidade, questões de pesquisa e contribuições.

**2. Fundamentação:** Ethereum EVM, Router, proxy, traces/logs, mixers ZK, feature engineering, detecção e ameaça à validade.

**3. Trabalhos relacionados:** categorias de tarefa e revisão comparativa dos dez artigos. Destaque Akopova, Barbereau, FPTracer, MixGuard e estudo SBSeg 2025.

**4. Método:** datasets brutos, datas e autorizações, engenharia de features, coleta de contexto funcional, rótulos positivos/negativos, controles de integridade, hash e protocolo de validação.

**5. Avaliação:** reprodução 2020 e limitação 63×9; análise de sensibilidade 49/14/9/7; experimento de contexto com rótulos independentes; holdout de protocolos e tempo; custos e limitações.

**6. Discussão:** confusão com DEX/bridge/relayer, limites de observabilidade, validade de inferências e privacidade legítima.

**7. Conclusão:** contribuições demonstradas, limitações e dados abertos/replicabilidade.

## 6. Critério para decidir a submissão

Um trabalho experimental competitivo exige ao menos **uma contribuição clara e demonstrada**: método simples validado com novos dados; novo conjunto rotulado auditável; descoberta empírica com protocolo robusto; ou uma análise de reprodutibilidade rigorosa e aberta. Para reforçar as chances de aceite, reunir **revisor(es) acadêmico(s)**, alinhar o escopo à trilha de segurança e disponibilidade de código/dados, e seguir chamada oficial, formato e política de anonimização da conferência escolhida. **Aceite não pode ser garantido**.

**Possíveis eventos a acompanhar (verificar chamada vigente antes de decidir):** SBSeg, SBRC (trilhas adequadas), eventos de blockchain/security especializados, além de workshops em ACM/IEEE compatíveis. Não assumir calendários/CFPs de 2027 sem verificação oficial.

## 7. Cronograma por marcos (sem promessa de prazo)

- M1: revisão bibliográfica organizada e fichamento dos artigos; matriz de escopo das tarefas.
- M2: corpus de rótulos com pelo menos dois protocolos positivos e negativos difíceis com evidência histórica.
- M3: baselines, atributos funcionais e splits definidos **antes** da avaliação.
- M4: resultados com métricas válidas, ablações, cobertura e replicabilidade.
- M5: escrita, revisão acadêmica, ajustes de apresentação e submissão conforme edital vigente.

**Referências internas:** EXP-01J, EXP-02A, EXP-02B e checklist no GitHub.
