# Roteiro de apresentação científica — versão inicial

**Documento de planejamento, não slides finais.** Adaptar duração e ordem à chamada do congresso.

| Slide | Título | Evidência visual / fala |
|---|---|---|
| 1 | Auditoria da detecção de mixers na Ethereum | Problema, motivação e pergunta científica, sem equiparar mixer a crime |
| 2 | Por que o problema é difícil? | Mixers, DEXs, bridges e roteadores podem ter movimentos complexos parecidos |
| 3 | Base metodológica | Artigo SBSeg 2025, quatro features, RF 100 árvores, profundidade 5 |
| 4 | Dados e protocolo | 23 janelas positivas de um contrato, 100 negativas, dados 2020/2025/2026 |
| 5 | Reprodução parcial | 1.114.702 transações, 239 para os pools, 3/3 recuperados, 63 do artigo vs 9 nossos |
| 6 | Descoberta controlada | Gráfico: filtro >=1, >=5, >=10 e >=20 transações → 49/14/9/7 alertas |
| 7 | Evidência externa | 20/20 hashes 2020 e 18/18 hashes amostrados 2026; limites de escopo |
| 8 | O que fazem os contratos sinalizados? | Exemplos: send, swapAndBridge, ccipSend, batchClaimRank, deliver |
| 9 | Completude não é ground truth | 150 logs iniciais MCT-XEN → 466 após completar as 3 amostras; proxies sem histórico |
| 10 | Conclusão e próximo passo | Qualidade de auditoria demonstrada; rótulos independentes e holdout para melhoria contextual ainda pendentes |

**Perguntas difíceis para ensaiar:** por que 63 vs 9 não comprova erro dos autores? Por que 9 alertas não equivalem a 9 mixers? Por que 18 hashes conferidos não validam todas as 315 transações? Por que o treino com um pool não prova generalização? Por que não chamar os seis serviços de falsos positivos? Que controles dão ao estudo rigor em segurança?

**Critério de versão final:** números consolidados e congelados, templates/tempo definidos, figuras legíveis, revisão de orientador e coautores.
