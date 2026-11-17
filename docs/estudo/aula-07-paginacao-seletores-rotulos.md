# Aula 07 — Quando um evento está completo? Paginação, ABI e rótulos científicos

**Pesquisa:** Segurança de Redes de Computadores — Detecção de Mixers na Ethereum  
**Base experimental:** EXP-02B (executado) e EXP-02C (preparado, ainda não executado)

## Objetivos de aprendizagem

Ao terminar, você deverá conseguir distinguir: (a) a identidade de uma transação, (b) o conjunto de eventos de uma transação, (c) a função do contrato e (d) o rótulo científico do contrato.

### 1. Os números que já conhecemos

Em 15/01/2026, seis contratos sinalizados no teste legado receberam **315 transações diretas no conjunto intermediário**. Auditamos uma amostra determinística de **18 transações (3 por contrato)** no Blockscout, confirmando hash, remetente, destinatário e data em **18/18**. Para **15/18** consultas de logs, a API informou final da paginação. Para o **MCT-XEN**, cada uma das três amostras retornou **50 logs na primeira página**, com `next_page_params` indicando mais eventos. Portanto, os **150 logs** capturados desse contrato ainda não representavam o conjunto completo desses três hashes.

**Importante:** os 315 registros do conjunto local não são 315 hashes auditados externamente; os 18 hashes auditados não equivalem a uma rotulagem definitiva dos seis contratos.

### 2. O que significa `next_page_params`?

Uma API pode limitar o número de eventos por resposta. Quando existe continuação, ela devolve parâmetros para consultar a próxima página. O algoritmo correto é: consultar página 1; guardar o conteúdo; verificar `next_page_params`; quando não for nulo, passar os mesmos parâmetros na próxima chamada; parar quando for nulo ou quando ocorrer erro/limite; registrar a razão da parada.

Se uma página contiver 50 logs, isso **não significa que a transação produziu exatamente 50 eventos**. Em especial, não podemos usar eventos ausentes por paginação como evidência de ausência de interação com protocolos.

### 3. Funções e seletores de quatro bytes

Os primeiros quatro bytes do `input` de uma transação costumam identificar qual função foi chamada. O identificador é obtido pelos quatro primeiros bytes de **Keccak-256** da assinatura canônica da função, como `transfer(address,uint256)` → `0xa9059cbb`.

Um seletor sozinho não prova a função: assinaturas diferentes podem produzir o mesmo prefixo de quatro bytes. É preciso associá-lo à **ABI verificada do contrato/implementação correta**. Em contratos atualizáveis (*proxies*), a ABI publicada hoje pode não representar o código executado em janeiro de 2026.

No EXP-02B ficaram sem identificação as funções dos seletores `0xec5b999d` (OKX DEX proxy) e `0x98190f47` (MCT-XEN). O EXP-02C investigará essas assinaturas, separando correspondências na ABI atual de meras sugestões em bases públicas.

### 4. Quatro níveis diferentes de evidência

1. **Transação verificada:** hash, endereço, remetente e data conferidos em outra fonte.
2. **Eventos cobertos:** todas as páginas de logs daquela transação foram recuperadas, sem erros ou cursor repetido.
3. **Função identificada:** assinatura compatível com a ABI da implementação que era válida naquele bloco.
4. **Rótulo auditado:** evidências suficientes sobre a finalidade econômica e critérios de classe, com revisão independente e cobertura adequada.

Um nível não implica automaticamente o próximo. Especialmente em segurança, precisamos evitar que uma identificação superficial de serviço se transforme em falsa certeza de que um contrato é ou não mixer.

### 5. Exercícios de compreensão

**Q1.** Uma transação retorna 50 logs, e `next_page_params` não é nulo. Posso dizer que ela produziu 50 eventos? Justifique.

**Q2.** Se identificarmos `0xec5b999d` na ABI atual de um proxy, isso comprova que a função foi executada em janeiro de 2026?

**Q3.** O Blockscout confirmou 18/18 hashes. Podemos calcular a precisão geral do detector sobre as 20.214 janelas avaliadas?

**Q4.** Por que não devemos trocar o classificador ou o limiar depois de ver quais dos seis endereços parecem ter outra função?

**Q5 — atividade prática.** Escreva um pseudocódigo para a paginação que registre páginas, erros, número de logs, `next_page_params` e status de completude, com limite máximo de páginas.

### Gabarito

**Q1:** Não. São 50 na primeira página; pode haver mais, e apenas o fim da paginação permite fechar essa contagem.  
**Q2:** Não. Uma assinatura na ABI atual não comprova código/implementação histórica, especialmente em proxy atualizável; deve-se consultar estado e upgrades no bloco.  
**Q3:** Não. A amostra inclui apenas endereços já alertados e não tem rótulos independentes de toda a população; há viés de verificação.  
**Q4:** Seria ajuste retrospectivo sobre os mesmos dados, comprometendo uma avaliação independente e introduzindo risco de sobreajuste.  
**Q5:** Inicializar cursor vazio e conjunto de cursores vistos; consultar e registrar resposta; em erro, parar como incompleto; adicionar itens; se `next_page_params=null`, marcar completo; se repetido ou limite excedido, marcar incompleto e salvar motivo; avançar com os parâmetros exatos retornados.

## Referências da prática

- [Relatório EXP-02B](https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02B-resultados-auditoria-amostral-2026.md)
- [EXP-02C — Plano da auditoria de logs](https://github.com/BorgesGusta/ethereum-mixer-detection/blob/main/docs/experiments/EXP-02C-protocolo-paginacao-e-seletores.md)
- [Documentação Blockscout da API v2](https://github.com/blockscout/blockscout-api-v2-swagger)
