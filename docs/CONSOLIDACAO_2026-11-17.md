# Consolidação documental oficial — 17/11/2026

**Natureza:** reconciliação de documentação em branch separada, sem reexecutar modelos, alterar notebooks, substituir dados brutos ou modificar resultados legados. **Base:** relatórios e manifestos já versionados; o checklist permanece como controle operacional.

## Arquivos corrigidos

| Arquivo | Desvio observado | Ação documental |
|---|---|---|
| `README.md` | Estado de 16/11 e artigo descrito como futuro | Atualizados marco, links, limites científicos e fontes vigentes |
| `docs/00_PAINEL.md` | Resumo anterior às auditorias de 17/11 | Seção explícita de atualização, sem apagar painel histórico |
| `docs/01_CRONOLOGIA.md` | Sem marcos 17/11 | Acréscimo de EXP-01G/01J/02A/02B/02C e manuscrito |
| `docs/02_EXPERIMENTOS.md` | Catálogo parava em 12.03 | Acréscimo de novos protocolos, auditorias e limites |
| `docs/03_DECISOES.md` | Decisões antigas sem distinção vigente | Matriz de regras vigentes; ADRs históricos seguem pendentes |
| `docs/04_DADOS.md` | Instruções provisórias de migração conviviam com decisão final | Histórico preservado, prioridade da decisão final explicada |
| `docs/05_PLANO.md` | Ações já realizadas descritas como futuras | Próximas prioridades e estados corrigidos |
| `manuscript/README.md` | Não apontava a fontes LaTeX existentes | Redirecionamento para `artigo/overleaf/` v0.1 |

## Afirmações sustentadas pelas evidências, sem extrapolação

1. **Reprodução 2020:** 3/3 pools Tornado de referência recuperados; há 9 alertas próprios versus 63 no artigo. A explicação exata da diferença é **desconhecida**.
2. **EXP-01J:** RF/limiar inalterados; `min_tx` 1, 5, 10 e 20 resultou em 49, 14, 9 e 7 alertas, respectivamente. Isso demonstra sensibilidade ao universo de elegibilidade **no nosso pipeline**, não equivalência ao protocolo original.
3. **EXP-02A:** conjunto 15/01/2026 já foi inspecionado com limiar 0,85, 20.214 elegíveis, 9 alertas e 3/3 pools de referência; **não** é novo teste cego.
4. **EXP-02B:** 6/6 contagens diretas conferidas (315 no total); 18/18 transações **amostradas** conciliadas com Blockscout. Não há inspeção externa exaustiva de 315 transações nem rótulos binários independentes.
5. **EXP-02C:** logs de 3 amostras MCT-XEN completos (83/83/300 = 466). Com 120 logs das outras 15 amostras do EXP-02B são 586 logs nas 18 amostras, **não** em todas as 315 transações. Dois seletores e implementações históricas dos proxies continuam indeterminados.
6. **Manuscrito:** fontes editáveis LaTeX v0.1 existem em `artigo/overleaf/`; não há evidência nesta revisão de compilação bem-sucedida, aprovação, submissão ou melhora de desempenho.

## Pendências que NÃO foram resolvidas nesta consolidação

- Auditoria recursiva de SHA-256 da migração da pasta compartilhada para o Drive oficial e equivalência dos documentos nativos.
- Vincular cada execução legada a commit/notebook específico, ambiente, versões de dependências, manifestos e outputs.
- Reconciliar os registros históricos conflitantes de `MIN_TX`, Router, critérios de negativos e limiares via ADR, com datas reais, sem retroatividade.
- Esclarecer 63×9 somente diante de evidência original nova (lista/código/resposta dos autores).
- Validar implementações dos proxies e rótulos históricos e ampliar auditagem para população não alertada.
- Obter exemplos positivos de diferentes protocolos e teste futuro independente com divisão por protocolo/período.
- Compilar, revisar e adaptar manuscrito à chamada oficial; verificar bibliografia.

## Protocolo para novas conversas e sessões

1. Ler `README.md`, `docs/CHECKLIST_VIVO.md`, `docs/00_PAINEL.md`, `docs/01_CRONOLOGIA.md`, `docs/03_DECISOES.md` e este registro.
2. Confirmar últimos commits da `main` e status de pull requests ainda não integrados.
3. Consultar a ficha do experimento e os artefatos originais no Drive antes de usar números no manuscrito.
4. Diferenciar **planejado / código preparado / executado / auditado / confirmado externamente**.
5. Ao concluir, adicionar evidência, o que não foi demonstrado e próximo passo. Não reescrever resultados para produzir conclusões desejadas.
6. Manter originais e históricos preservados; nunca assumir que a revisão de documentação equivale a reexecução de dados ou aprovação científica.

## Fontes principais

- [Checklist vivo](CHECKLIST_VIVO.md)
- [EXP-01J](experiments/EXP-01J-resultados-sensibilidade-63x9.md)
- [EXP-02 — protocolo temporal por contrato](experiments/EXP-02-protocolo-temporal-contrato.md)
- [EXP-02A](experiments/EXP-02A-inventario-e-triagem-2026.md)
- [EXP-02B](experiments/EXP-02B-resultados-auditoria-amostral-2026.md)
- [EXP-02C](experiments/EXP-02C-resultados-logs-e-seletores.md)
- [Manuscrito v0.1](../artigo/overleaf/README.md)
- [Drive oficial](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj)

**Integridade editorial:** todas as correções desta consolidação são documentais; nenhum resultado experimental foi recalculado ou independente e exaustivamente revalidado.
