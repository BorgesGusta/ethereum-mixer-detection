# Projeto editável no Overleaf

**Versão:** 0.1 (17/11/2026) — **rascunho científico, não submetido**.

## Como usar

1. No Overleaf, clique em **New Project > Upload Project** e envie o ZIP de projeto, quando disponível. Alternativamente, crie um **Blank Project** e arraste todos os arquivos e pastas aqui listados.
2. Selecione **main.tex** como arquivo principal em **Menu > Main document**.
3. Configure o compilador **pdfLaTeX**; as referências usam BibTeX (`\bibliography{referencias}`).
4. Edite os parágrafos no `main.tex`, a bibliografia em `referencias.bib` e o gráfico em `figuras/sensibilidade.tex`.
5. Compile com **Recompile**. Se as referências aparecerem como [?], execute uma segunda compilação.

## Estrutura

- `main.tex`: artigo completo e editável em português.
- `referencias.bib`: entradas bibliográficas verificadas ou explicitamente provisórias.
- `figuras/sensibilidade.tex`: gráfico pgfplots editável em LaTeX (valores provenientes de EXP-01J).
- `README.md`: estas instruções.

## Cuidados antes de submeter

- **Não se trata ainda do template oficial do SBSeg**. Depois da escolha da chamada e trilha, adaptar a classe e formatação ao modelo oficial, preservando `\section`, tabelas e bibliografia.
- Preencher autores, afiliações, instituições e e-mails e verificar exigência de anonimato.
- Verificar todos os DOIs, nomes de autores, páginas e formato de citações.
- Não apresentar 6 alertas em 2026 como falsos positivos confirmados; não declarar precisão de 33,3% ou melhoria comprovada.
- O EXP-02C encerrou a paginação de **três transações MCT-XEN**, não das 315 transações diretas dos seis contratos.
- A divergência **63 × 9** segue sem causa identificada; e-mail aos autores só deve constar como não respondido se a situação persistir na data de fechamento.
- O experimento contextual e holdout por protocolo não foram concluídos; não inserir resultados fictícios.

Fonte canônica de resultados: [EXP-01J](https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-01J-resultados-sensibilidade-63x9.md), [EXP-02B](https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02B-resultados-auditoria-amostral-2026.md) e [EXP-02C](https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02C-resultados-logs-e-seletores.md).
