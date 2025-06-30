# 1. Two Sum - Explicação da Solução

## Abordagem: Utilizando Dicionário (Hash Table)

A solução utiliza um dicionário para armazenar os números já percorridos junto com seus respectivos índices. Essa abordagem permite resolver o problema em tempo linear **O(n)**, evitando a comparação de todos os pares possíveis (que teria complexidade O(n²)).

## Lógica do Algoritmo

1. Criamos um dicionário vazio chamado `mapa`, que irá mapear cada número do array para seu índice.
2. Percorremos o array `nums` com um laço `for`.
3. Para cada número atual `nums[i]`:
   - Calculamos o **complemento**: `complemento = target - nums[i]`.
   - Verificamos se esse complemento já existe no dicionário:
     - Se sim, significa que encontramos os dois números que somam o valor alvo (`target`), e retornamos os índices: o do complemento e o do número atual.
     - Caso contrário, adicionamos `nums[i]` ao dicionário, associando-o ao índice `i`.

## Exemplo Passo a Passo

**Entrada:** `nums = [2, 7, 11, 15]`, `target = 9`

1. Inicializamos o dicionário: `mapa = {}`
2. Iteração 0:
   - `nums[0] = 2`
   - `complemento = 9 - 2 = 7`
   - `7` **não** está no dicionário
   - Adiciona `2` ao dicionário: `mapa = { 2: 0 }`
3. Iteração 1:
   - `nums[1] = 7`
   - `complemento = 9 - 7 = 2`
   - `2` **está** no dicionário (índice `0`)
   - Retorna `[0, 1]`

## Complexidade

- **Tempo:** O(n), pois percorremos o array uma única vez.
- **Espaço:** O(n), por causa do dicionário usado para armazenar os números já vistos.

