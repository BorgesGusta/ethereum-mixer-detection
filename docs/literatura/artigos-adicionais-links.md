# Artigos adicionais verificados — PDFs para guardar no Drive

**Pesquisados em 17/11/2026.** Todos os endereços a seguir apontam para fontes acadêmicas e versões de leitura. As páginas PDF podem ser abertas e o arquivo baixado pelo pesquisador. O download automático para esta sessão não ficou disponível; **os PDFs complementares listados aqui ainda não foram copiados ao Drive**.

**Destino para os PDFs baixados:** `Biblioteca de Estudo e Pesquisa — NotebookLM / 04_ARTIGOS_ADICIONAIS`.

Pasta: https://drive.google.com/drive/folders/1aDqUFahABvsNuAeGbAeYh950nXFpmhan

## Prioridade 1 — Evidência funcional de contratos mixer

1. **Beyond a Fistful of Tumblers: Toward a Taxonomy of Ethereum-based Mixers** (Barbereau e colaboradores, ICIS 2023). PDF: https://orbilu.uni.lu/bitstream/10993/57137/1/_ICIS__Toward_a_Taxonomy_of_Ethereum_based_Mixers__final_version_%20%281%29.pdf . Página do repositório universitário: https://orbilu.uni.lu/handle/10993/57137 . Por quê: classificação das funcionalidades e arquitetura de mixer, ideal para a nossa rubrica de `deposit/withdraw/verifier` e contexto de contrato.

## Prioridade 2 — Análise de privacidade e dados on-chain

2. **Tutela: An Open-Source Tool for Assessing User-Privacy on Ethereum and Tornado Cash** (Wu et al., 2022). PDF: https://arxiv.org/pdf/2201.06811 . Por quê: heurísticas de vinculação e limitação da privacidade, útil para fundamentar riscos de inferência e cobertura.

3. **On How Zero-Knowledge Proof Blockchain Mixers Improve, and Worsen User Privacy** (2022). PDF: https://arxiv.org/pdf/2201.09035 . Por quê: estudo empírico de anonímato, DeFi, rede e comportamento dos usuários; aprofunda justificativas e ameaças à validade.

## Prioridade 3 — Generalização temporal e multi-chain

4. **Clustering Deposit and Withdrawal Activity in Tornado Cash: A Cross-Chain Analysis** (Cristodaro, Kramer e Tessone, 2025). PDF: https://arxiv.org/pdf/2510.09433 . Por quê: analisa relações temporais e diferenças entre redes; unidade de classificação diferente do nosso detector.

## Prioridade 4 — Leitura interdisciplinar

5. **Tornado Cash and Blockchain Privacy: A Primer for Economists and Policymakers** (Federal Reserve Bank of St. Louis, 2023). PDF: https://files.stlouisfed.org/files/htdocs/publications/review/2023/02/03/tornado-cash-and-blockchain-privacy-a-primer-for-economists-and-policymakers.pdf . Por quê: fundamenta discussão de privacidade e risco sem tratar todo usuário de mixer como criminoso.

## Os cinco PDFs que VOCÊ já enviou e que estão na biblioteca

- *Detecting Ethereum Mixers* — Amanda Akopova.
- *GNN-based Detection of Malicious Transactions in Ethereum Networks: Leveraging Tornado Cash Transaction Patterns* — Jeong e Yoon, BSCI 2025, DOI 10.1145/3709016.3737795.
- *Correlating Account on Ethereum Mixing Service via Domain-Invariant feature learning* — Che et al., arXiv:2505.09892, conhecido como StealthLink.
- *Tracing Money Laundering Across DeFi, Bridges, and Mixers on Ethereum* — Xing et al., arXiv:2610.32210, FPTracer.
- *MixGuard: Towards Detecting and Understanding Mixer Laundering on Ethereum* — Fu et al., arXiv:2609.27807.

Além disso, foi inserido o artigo-base SBSeg 2025 de Leale e Sendin na mesma pasta.

**Atenção:** o arquivo de PowerPoint `10.1039-c3lc51171e_figure.pptx` que veio no conjunto trata de **mistura microfluídica em laboratório** e não integra esta revisão de mixer de criptomoedas. Não colocá-lo no NotebookLM da pesquisa, pois o termo “mixer” é homônimo.

## Como usar no NotebookLM

Carregue primeiro o artigo SBSeg + Akopova + Taxonomia de Barbereau. Peça um quadro de **similaridade de problemas**, não um ranking de accuracy. Depois adicione FPTracer/MixGuard para ampliar a análise de observabilidade, fluxo de ativos e verificação independente de rótulos. Para bibliografia final, confirmar DOI e tipo de publicação das versões preprint.
