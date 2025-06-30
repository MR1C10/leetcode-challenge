# 13. Roman to Integer (Fácil)

Os números romanos são representados por sete símbolos diferentes: `i`,` v`, `x`,` l`,
`C`,` d` e `m`.

    
    
    ** Símbolo ** ** Valor **
    I 1
    V 5
    X 10
    L 50
    C 100
    D 500
    M 1000

Por exemplo, `2` está escrito como` ii 'em numeral romano, apenas dois adicionados
junto. `12` está escrito como` xii`, que é simplesmente `x + ii`. O número `27`
está escrito como `xxvii`, que é` xx + v + ii`.

Os algarismos romanos geralmente são escritos maiores aos menores da esquerda para a direita.
No entanto, o numeral para quatro não é `iiii`. Em vez disso, o número quatro é
escrito como `iv`. Porque um está antes dos cinco que subtraímos que está fazendo
quatro. O mesmo princípio se aplica ao número nove, que é escrito como `ix`.
Existem seis casos em que a subtração é usada:

  * `I` posso ser colocado antes de` v` (5) e `x` (10) para fazer 4 e 9. 
  * `X` pode ser colocado antes de` l` (50) e `c` (100) para fazer 40 e 90. 
  * `C` pode ser colocado antes de` d` (500) e `m` (1000) para fazer 400 e 900.

Dado um número romano, converta -o em um número inteiro.

## Exemplo 1:

    
    
    Entrada: s = "iii"
    Saída: 3
    Explicação: III = 3.
    

## Exemplo 2:

    
    
    Entrada: s = "lviii"
    Saída: 58
    Explicação: L = 50, V = 5, iii = 3.
    

## Exemplo 3:

    
    
    Entrada: s = "mcmxciv"
    Saída: 1994
    Explicação: M = 1000, cm = 900, XC = 90 e IV = 4.
    

## restrições

  * `1 <= S.Length <= 15`
  * `s` contém apenas os caracteres` ('i', 'v', 'x', 'l', 'c', 'd', 'm') `.
  *É ** garantido ** que `s` é um número romano válido na faixa` [1, 3999] `.
