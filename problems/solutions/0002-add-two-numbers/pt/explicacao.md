# 2. Add Two Numbers - Explicação da Solução

## Abordagem: Simulação de Adição com Listas Encadeadas

Esta solução simula o processo de adição de dois números representados como listas encadeadas, onde cada nó contém um dígito e estão ordenados do dígito menos significativo para o mais significativo (ordem inversa).

## Lógica do Algoritmo:

1. Criamos um nó "dummy" para iniciar nossa lista de resultados, facilitando o retorno do cabeçalho final.
2. Inicializamos variáveis para o total e para o carry (transporte).
3. Percorremos ambas as listas e continuamos enquanto houver nós em qualquer uma das listas ou um carry pendente.
4. Para cada posição:
   - Começamos com o valor do carry anterior
   - Adicionamos os valores dos nós atuais (se existirem)
   - Calculamos o novo dígito (resto da divisão por 10) e o novo carry (quociente da divisão por 10)
   - Criamos um novo nó com o dígito calculado e o adicionamos à lista de resultados

## Exemplo Passo a Passo:

Usando o exemplo: `l1 = [2,4,3]` e `l2 = [5,6,4]` que representam respectivamente 342 e 465.

1. Inicialização:

   - `dummy = ListNode(0)`, `res = dummy`
   - `total = 0`, `carry = 0`

2. Iteração 1:

   - `total = 0` (carry inicial)
   - `l1.val = 2`, `total = 2`, `l1` avança
   - `l2.val = 5`, `total = 7`, `l2` avança
   - `num = 7 % 10 = 7`, `carry = 7 // 10 = 0`
   - Adicionamos `ListNode(7)` à lista de resultados

3. Iteração 2:

   - `total = 0` (carry anterior)
   - `l1.val = 4`, `total = 4`, `l1` avança
   - `l2.val = 6`, `total = 10`, `l2` avança
   - `num = 10 % 10 = 0`, `carry = 10 // 10 = 1`
   - Adicionamos `ListNode(0)` à lista de resultados

4. Iteração 3:

   - `total = 1` (carry anterior)
   - `l1.val = 3`, `total = 4`, `l1` avança (agora é None)
   - `l2.val = 4`, `total = 8`, `l2` avança (agora é None)
   - `num = 8 % 10 = 8`, `carry = 8 // 10 = 0`
   - Adicionamos `ListNode(8)` à lista de resultados

5. O loop termina, pois ambas as listas foram percorridas e não há carry.

6. Retornamos `res.next` (o nó após o dummy), que é a cabeça da lista resultante: `[7,0,8]` representando 807.
