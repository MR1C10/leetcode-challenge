# Roman to Integer - Explicação da Solução

## Abordagem: Percorrendo a string de trás para frente e utilizando subtração condicional

A solução implementa a conversão de um número romano para um número inteiro com base nas regras clássicas dos algarismos romanos. A lógica se baseia em percorrer a string do final para o início e aplicar **subtração** quando um símbolo menor precede um maior.

## Lógica do Algoritmo:

1. Criamos um **dicionário** que mapeia cada símbolo romano ao seu valor inteiro correspondente:
   - Ex: `'I' → 1`, `'V' → 5`, `'X' → 10`, `'L' → 50`, `'C' → 100`, `'D' → 500`, `'M' → 1000`.

2. Inicializamos duas variáveis:
   - `resultadoFinal`: acumula a soma total (inicialmente `0`);
   - `valorAntes`: armazena o valor anterior durante o loop (inicialmente `0`).

3. Percorremos a string `s` **do final para o início**:
   - Para cada caractere `s[i]`, obtemos seu valor inteiro do dicionário.

4. Aplicamos a regra de subtração romana:
   - Se `valorAtual < valorAntes`, subtraímos `valorAtual` de `resultadoFinal`.
   - Caso contrário, somamos `valorAtual` a `resultadoFinal`.

5. Atualizamos `valorAntes` com o valor atual para a próxima iteração.

6. Ao final do loop, `resultadoFinal` conterá o número inteiro equivalente ao número romano original.

## Exemplo Passo a Passo:

Entrada: `s = "MCMXCIV"`

1. `V = 5` → como `5 >= 0`, soma → `resultado = 5`
2. `I = 1` → `1 < 5`, subtrai → `resultado = 4`
3. `C = 100` → `100 > 1`, soma → `resultado = 104`
4. `X = 10` → `10 < 100`, subtrai → `resultado = 94`
5. `M = 1000` → `1000 > 10`, soma → `resultado = 1094`
6. `C = 100` → `100 < 1000`, subtrai → `resultado = 994`
7. `M = 1000` → `1000 > 100`, soma → `resultado = 1994`

**Resultado final: `1994`**

## Complexidade:

- **Tempo:** O(n), onde n é o tamanho da string `s`.
- **Espaço:** O(1), já que o dicionário tem tamanho fixo e usamos apenas variáveis escalares.
