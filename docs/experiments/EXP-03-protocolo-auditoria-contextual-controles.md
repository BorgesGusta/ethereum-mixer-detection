# EXP-03 — Protocolo de auditoria contextual com controles não alertados

**Redigido:** 18/11/2026. **STATUS: PROPOSTA DE PROTOCOLO — NÃO EXECUTADO.** É uma extensão de [EXP-02B](EXP-02B-protocolo-auditoria-2026.md) e [EXP-02C](EXP-02C-protocolo-paginacao-e-seletores.md), sem substituir seus relatórios. A escolha final da amostra deverá ser **congelada em manifesto com universo e SHA-256 antes de qualquer nova consulta externa por endereço**.

## Objetivo e pergunta

**RQ-EXP03:** como se comparam as evidências disponíveis e a cobertura de auditoria funcional entre endereços alertados pelo RF e endereços não alertados, quando definidos no mesmo dia e sujeitos a critérios transparentes de amostragem?

**Objetivo principal:** medir **cobertura da auditoria e ambiguidade funcional**, não estimar precisão/recall geral do classificador sem ground truth. **Não afirmar causalidade** de funcionalidades identificadas ou a ausência de atividade de mixer.

## Evitar retrabalho

**Já concluído e reaproveitável:** EXP-02A (nove alertas legados); EXP-02B (6 endereços adicionais, 315 tx diretas, 18 hashes selecionados e validados); EXP-02C (3 tx MCT-XEN com 466 logs completos, 586 logs no total das 18 amostras). **Não reconsultar as mesmas transações como se fossem novo experimento.** Os resultados de 2020/2026 já foram explorados e não formam holdout.

## População, estratificação e seleção antes de coleta

1. **Data e rede:** Ethereum mainnet, 15/01/2026, UTC; a análise será explicitamente **retrospectiva/exploratória**, sem novo teste cego.
2. **Universo:** carregar o [Parquet de features 2026 já utilizado](https://drive.google.com/file/d/12NHTZGd_-RPIt6c2gYlEjO0WZHcfyqQl/view), a lista [de alertas legados](https://drive.google.com/file/d/11kWohs3VvdDGVjwsN_t-S8EQVix6n9mf/view) e, se necessário, scores completos previamente salvos. **Antes da execução** confirmar: endereço, data, `n_tx`, score disponível, unicidade do contrato/endereço e hash SHA-256 das entradas.
3. **Grupo A (alertados):** reutilizar os **seis contratos adicionais** já auditados (fora dos três pools de referência) como casos intencionais; **não** denominá-los amostra aleatória nem negativos confirmados. Preservar os três pools de referência como controles positivos conhecidos **separados**, não misturá-los aos seis.
4. **Grupo B (não alertados):** formar a partir de endereços elegíveis `n_tx>=10` em 15/01/2026, excluídos os nove alertas e os pools de referência; confirmar score abaixo do limiar legado 0,85 com fonte previamente existente ou, caso scores não estejam preservados, registrar essa lacuna sem recalibrar/retreinar silenciosamente.
5. **Controle de atividade:** parear cada um dos seis alertados com **um não alertado** em mesma banda de `n_tx`, definida ANTES da inspeção externa: 10–19, 20–49, 50–99, >=100. Se não houver candidato na banda, registrar ausência e usar banda adjacente pré-definida pela menor distância ordinal, sem procurar por identidade/nome de contrato.
6. **Desempate determinístico:** ordenar candidatos por SHA-256 de `"EXP03-20261118|" + recipient_lowercase` e escolher o primeiro disponível sem reposição. Se não houver seis controles únicos válidos, registrar amostra menor e motivo em vez de forçar substituições.
7. **Saída pré-consulta obrigatória:** `plano_amostragem_exp03.json` com código/commit, ID e hashes das fontes, política de elegibilidade e bandas, critérios de exclusão, universo por banda, lista final de 6 + até 6 controles e SHA-256 do próprio arquivo. **Gate:** sem manifesto de seleção previamente fixado, não iniciar consultas externas e não alegar estudo controlado.

**Limite deliberado:** amostragem pareada por atividade não é aleatória da população total; seis pares são um piloto de auditoria, não estimativa populacional. Não reproduzir seus resultados como confirmação independente.

## Observações planejadas por endereço

- Identidade documental com evidência citada e **data histórica**; contrato/protocolo e endereço, status de verificação atual separado de código histórico.
- Número de transações diretas no recorte (e origem), amostra de hashes para verificações cruzadas de data/recipient/from/to/bloco.
- Chamada e assinatura de função: método decodificado, seletor, ABI atual e ABI/implementação histórica **se de fato obtidas**.
- Logs e eventos capturados, total de páginas, `next_page_params` final, divergências por hash, erros HTTP e restrições dos provedores.
- Campos `observacao_factual`, `inferencia_limitada`, `lacuna_historica`, `rotulo_cientifico` inicial `indeterminado`.
- Para casos de proxy atualizável: obter evidência histórica no bloco ou classificar `inconclusivo_proxy_historico`.
- **Dois revisores independentes** quando houver proposta de rótulo final; revisão sem score quando possível.

## Resultados permitidos e métricas

Permitidos: contagens e cobertura por grupo, diversidade de funções documentadas, fração de amostras com logs paginados por completo, proporção de endereços inconclusivos, concordância entre revisores **quando houver dois registros**.

**Proibidos sem base validada:** `6 falsos positivos`, `precision=33,3%`, novo F1/recall de toda a rede, superioridade de método contextual, generalização a protocolos não presentes no treinamento. O desenho é um **estudo piloto e exploratório**, não avaliação cega nem estimador não enviesado.

## Condições de GO/NO-GO e outputs

- **Gate 1 — preparação:** existência e hash de features/ranking/scores; confirmar universo e política de `n_tx`; congelar plano.
- **Gate 2 — auditoria:** consultas externas somente depois do Gate 1; controle de taxa e limite de páginas; zero mudanças em dados legados.
- **Gate 3 — revisão:** rótulo definitivo somente se evidência histórica suficiente e dois revisores; não inferir negativo a partir da ausência de função observada.
- **Outputs novos versionados:** `protocolo_exp03.json`, `amostra_congelada.csv`, `evidencias_endereco.csv`, `cobertura_api.csv`, `revisao_rotulos.csv`, `manifesto_exp03.json`, relatório Markdown com tabelas e limitações. Cada resultado recebe caminho novo e SHA-256, **sem sobrescrever EXP-02A/B/C**.
- **Se bloqueado:** salvar `NO_GO_exp03.md` com causas exatas de impossibilidade, e utilizar o tempo para construir o ground truth de outros protocolos previsto no EXP-02.

## Relação com artigo e próximo passo imediato

Registrar apenas **objetivo, desenho e motivação** no [caderno científico](../manuscrito/CADERNO_CIENTIFICO_VIVO.md) enquanto não houver execução. Depois do piloto, acrescentar tabela comparativa somente se o manifesto e as evidências puderem sustentá-la. **Nenhum PDF de artigo é requerido nesta etapa.**

**Próxima ação operacional:** conferir disponibilidade dos **scores individuais de 2026** e unicidade dos endereços no artefato já salvo, preparar script de seleção **sem executar coleta de transações**, congelar a amostra e gerar a matriz de controles.

## Verificação documental de prontidão — 18/11/2026

A inspeção do notebook histórico [07b](../../notebooks/legacy/07b_teste_2026_validacao_2020.ipynb) confirma que o código calculava `prob = modelo.predict_proba(...)` para todos os endereços elegíveis e exportava `sinalizados_teste_2026.csv` **somente para os sinalizados**. A listagem do diretório `results` no Drive oficial confirmou o CSV desses nove alertas, mas **não identificou arquivo de scores individuais de toda a população elegível** na listagem examinada. Portanto, **não tratar o score de cada não-alertado como disponível** nem marcar Gate 1 concluído.

**Próxima busca não redundante:** verificar se as pastas de execução do notebook 07b ou seus arquivos de intermediários preservam uma tabela completa de scores. Se não houver, documentar o bloqueio e decidir separadamente se é justificada uma **inferência somente para seleção de controles**, com artefato/versão/limiar congelados — sem apresentá-la como novo teste temporal independente. Reutilizar o CSV dos nove positivos e não recalcular EXP-02B/02C.
