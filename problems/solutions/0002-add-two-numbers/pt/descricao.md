# 2. Somar Dois Números (Médio)

Você recebe duas listas ligadas **não vazias** representando dois inteiros não negativos. Os dígitos estão armazenados em **ordem reversa**, e cada um dos nós contém um único dígito. Some os dois números e retorne o resultado como uma lista ligada.

Você pode assumir que os dois números não contêm zeros à esquerda, exceto o próprio número 0.

## Exemplo 1:

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

    Entrada: l1 = [2,4,3], l2 = [5,6,4]
    Saída: [7,0,8]
    Explicação: 342 + 465 = 807.

## Exemplo 2:

    Entrada: l1 = [0], l2 = [0]
    Saída: [0]

## Exemplo 3:

    Entrada: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Saída: [8,9,9,9,0,0,0,1]

## Restrições

- O número de nós em cada lista ligada está no intervalo `[1, 100]`.
- `0 <= Node.val <= 9`
- É garantido que a lista representa um número que não possui zeros à esquerda.
