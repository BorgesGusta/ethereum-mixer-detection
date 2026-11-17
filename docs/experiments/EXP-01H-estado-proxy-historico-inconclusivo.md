# EXP-01H — Estado histórico do proxy, bloco 11.154.799 (29/10/2020)

**Data da execução:** 17/11/2026. **Estado:** executado, **inconclusivo por indisponibilidade dos provedores consultados**. Nenhuma alteração nos rótulos do dataset ou no modelo.

## Evidências geradas pela etapa 12 do notebook 01

[Pasta do Drive próprio](https://drive.google.com/drive/folders/1kY2LVeCpLdGpHt0f_ETwMZ3IxmGYGLHx)

- [leitura_slot_eip1967.csv](https://drive.google.com/file/d/1y-Cn2gc_bBj7HdCkd06LWdgjLzqmPVhE/view)
- [consulta_logs_dia.json](https://drive.google.com/file/d/1Huardhe39Ph-3RZnRuSqZTG1bUnyOMVa/view)
- [manifesto.json](https://drive.google.com/file/d/14NBTe_Rb0RxF6lwaq0LQXGsIB3Dnd9SP/view)

**Endereço consultado:** `0x5e60fcca904753a31f9df7d7f6b7856b6ec27aa9`.

**Bloco de referência do final de 29/10/2020:** `11154799`.

**Slot EIP-1967 da implementação:** `0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc`.

## Resultado real das respostas

| Provedor | Método | HTTP | Valor histórico recebido? | Interpretação |
|---|---|---:|---|---|
| `https://ethereum-rpc.publicnode.com` | `eth_getStorageAt` | 403 | Não | Acesso recusado |
| `https://eth.llamarpc.com` | `eth_getStorageAt` | 525 | Não | Erro do serviço/conexão |
| `https://eth.blockscout.com/api` | consulta de logs do dia | HTTP 200 / API `status=0` | Nenhum evento retornado | **Resposta não comprova ausência de upgrades**, especialmente sem comprovação de cobertura/semântica da API |

O manifesto registra exatamente `status: inconclusivo_sem_archive` e `implementacoes_respondidas: []`.

**Conclusão permitida:** o procedimento foi realizado e documentado, mas não houve leitura válida do slot no bloco histórico. **Não é permitido identificar a implementação vigente em 29/10/2020 nem afirmar ausência de eventos `Upgraded` naquele dia.** A diferença entre implementação inicial, duas implementações registradas após outubro de 2020 e a atual permanece um achado parcial.

## Próxima ação (não bloquear o projeto)

1. Marcar a investigação histórica do proxy como **dependência de provedor de arquivo Ethereum / fonte histórica independente**. Evitar repetir requisições aos mesmos endpoints sem uma justificativa ou credenciais adequadas.
2. **Repriorizar a divergência 63 vs 9 alertas**, atualmente a maior limitação de paridade do estudo.
3. Auditar comparabilidade do conjunto de treino (23 janelas positivas de um único pool, 100 amostras negativas), amostragem, regra `n_tx >= 10`, agregação por destinatário-dia, cálculo das quatro features, balanceamento e decisão de inferência. Não ajustar limiar a 0,25 para imitar 63.
4. Incorporar eventual resposta dos autores do SBSeg 2025 ao protocolo e a essa investigação com as devidas ressalvas.

## Relação com as evidências anteriores

- [EXP-01F](EXP-01F-blockscout-2020-cobertura.md): 2 eventos posteriores e cobertura de logs incompleta para 29/10/2020.
- [EXP-01G](EXP-01G-auditoria-hashes-blockchair-blockscout.md): paridade independente hash a hash em 20 transações dos outros dois contratos.
