# Demonstração prática EXP-08 — triagem humana e integridade de evidências

**Estado:** implementação offline existente, testes locais previamente aprovados; repetir comandos abaixo no dia da apresentação. Não é integração com SIEM, rede ou bloqueio de carteiras.

## Objetivo didático (2 a 3 minutos)

Mostrar que um detector estatístico produz um **alerta a investigar**, e não uma prova de ilícito. Demonstrar separação entre evidência on-chain, decisão humana e garantia de integridade de um registro local de auditoria.

## Roteiro no terminal

No repositório, abra `scripts/security_triage/` e execute:

```bash
python3 -m unittest -v test_triage
python3 triage.py triage --input sample_cases.json --output saida_demo.jsonl
python3 triage.py verify --input saida_demo.jsonl
```

> O último comando confere o encadeamento SHA-256. O `triage.py triage` recusa sobrescrever um arquivo de auditoria existente; apague SOMENTE o arquivo `saida_demo.jsonl` criado pela própria demonstração antes de repetir.

Primeiro caso: Privacy Pools v1, evidências de documentação e log **fornecidas pelo operador**, sem `model_score` automático; resultado `indeterminado` e prioridade `revisar_evidencias`. Segundo caso: endereço **fictício de teste** com escore hipotético 0,82, mas nenhuma evidência; resultado `indeterminado`, prioridade `coletar_evidencias`. Ambos permanecem `REVIEW_ONLY` e `automated_blocking=false`.

Para demonstrar adulteração, **em uma cópia separada de `saida_demo.jsonl`**, substitua a string `REVIEW_ONLY` por `AUTO_BLOCK` e rode o verificador sobre a cópia. Deve ocorrer erro de integridade (a função SHA-256 não coincide). A suíte `test_triage.py` já possui teste automatizado dessa alteração; o comando `unittest` a executa.

## O que dizer ao professor

1. "O modelo identifica padrões de transações, mas pode confundir mixers com outros contratos financeiros."
2. "Nosso EXP-07 mostrou 0,9778 de F1 **interno**, mas todos os positivos são do mesmo contrato. Por isso não podemos tratar o escore como certeza."
3. "Construímos uma etapa posterior de segurança: um alerta vai para revisão, com evidências, justificativas e registros auditáveis."
4. "A sequência de hashes detecta uma modificação local no histórico, desde que o hash original tenha sido guardado fora do arquivo. Sem ancoragem externa não existe imutabilidade forte."
5. "O protótipo funciona offline; não fez conexão com a blockchain ou um SIEM, e nunca bloqueia operações."

## Riscos e limitações a não ocultar

- As flags `receipt_ok` e `pool_log_verified` são **informadas no JSON**, não verificadas por consulta on-chain pelo protótipo.
- O endereço do segundo caso é um endereço sintático de demonstração, não um contrato Ethereum cujo comportamento tenha sido verificado.
- Qualquer pessoa com escrita no arquivo pode alterar e reencadear todos os hashes; proteção real exige âncora externa, assinatura ou armazenamento WORM.
- A correlação documental não equivale a comprovação de crime, mixer equivalente ou risco financeiro.

**Fontes:** `scripts/security_triage/{triage.py,test_triage.py,sample_cases.json}` e `docs/experiments/EXP-08-plano-seguranca-e-conjuntos.md`, todos no ramo `docs/consolidacao-oficial-2026-11-17`.
