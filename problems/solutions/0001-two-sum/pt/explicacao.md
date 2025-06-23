# 1. Two Sum - Explicação da Solução

## Abordagem: Utilizando Hash Table (Dicionário)

A solução utiliza uma estrutura de dados hash table para resolver o problema em uma única passagem pelos elementos do array.

## Lógica do Algoritmo:

1. Criamos um dicionário vazio `num_to_index` que irá mapear cada número do array para seu índice.
2. Percorremos o array `nums` com um loop.
3. Para cada número atual (`num`):
   - Calculamos o "complemento" (`target - num`) que, somado ao número atual, resultaria no valor alvo.
   - Verificamos se esse complemento já foi visto anteriormente (está no dicionário).
   - Se encontrarmos o complemento, retornamos os índices dos dois números.
   - Caso contrário, armazenamos o número atual e seu índice no dicionário para consultas futuras.

## Exemplo Passo a Passo:

Usando o exemplo: `nums = [2, 7, 11, 15]`, `target = 9`

1. Inicializamos `num_to_index = {}`
2. Iteração 1:
   - `num = 2`, `complemento = 9 - 2 = 7`
   - `7` não está em `num_to_index`
   - Adicionamos `num_to_index[2] = 0`
3. Iteração 2:
   - `num = 7`, `complemento = 9 - 7 = 2`
   - `2` está em `num_to_index` com valor `0`
   - Retornamos `[0, 1]` (índices dos números 2 e 7)
