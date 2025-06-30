# Palindrome Number - Explicação da Solução

## Abordagem: Invertendo o número com operações matemáticas

A solução utiliza operações matemáticas simples (sem converter para string) para verificar se um número inteiro é um palíndromo, ou seja, se ele é igual a si mesmo quando lido de trás para frente.

## Lógica do Algoritmo:

1. Se o número for negativo (`x < 0`), já retornamos `false`, pois números negativos nunca são palíndromos (devido ao sinal `-`).
2. Armazenamos o número original em uma variável `original`, pois vamos modificar `x` durante o processo.
3. Criamos a variável `reservado` (reverso do número), inicialmente com valor `0`.
4. Enquanto `x` for maior que 0:
   - Extraímos o último dígito com `x % 10`.
   - Adicionamos esse dígito ao final do número invertido: `reservado = reservado * 10 + digito`.
   - Removemos o último dígito de `x` com `x /= 10`.
5. Ao final, comparamos se o número invertido (`reservado`) é igual ao original.
   - Se sim, o número é um palíndromo.
   - Caso contrário, não é.

## Exemplo Passo a Passo:

Usando o exemplo: `x = 121`

1. `original = 121`, `reservado = 0`
2. Iteração 1:
   - `digito = 121 % 10 = 1`
   - `reservado = 0 * 10 + 1 = 1`
   - `x = 121 / 10 = 12`
3. Iteração 2:
   - `digito = 12 % 10 = 2`
   - `reservado = 1 * 10 + 2 = 12`
   - `x = 12 / 10 = 1`
4. Iteração 3:
   - `digito = 1 % 10 = 1`
   - `reservado = 12 * 10 + 1 = 121`
   - `x = 1 / 10 = 0`
5. Comparação final:
   - `original (121)` == `reservado (121)` → **Retorna `true`**

## Complexidade:

- **Tempo:** O(log₁₀ n), pois percorremos os dígitos do número.
- **Espaço:** O(1), já que utilizamos apenas variáveis escalares.
