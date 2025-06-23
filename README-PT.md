##### Este é o Readme do projeto _em português_, caso prefira acompanhar o Readme em inglês, [clique aqui](README.md)

# Desafio LeetCode

<p align="center">
  <img src="Media/Image/leetcode-challenge.png" alt="LeetCode Logo" width="400">
</p>

<p align="center">
  <a href="https://github.com/mr1c10/leetcode-challenge/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/mr1c10/leetcode-challenge?color=ffa116&logo=github&style=flat-square" alt="GitHub Contributors">
  </a>
  <a href="https://github.com/mr1c10/leetcode-challenge/stargazers">
    <img src="https://img.shields.io/github/stars/mr1c10/leetcode-challenge?color=ffa116&logo=github&style=flat-square" alt="GitHub Stars">
  </a>
  <a href="https://github.com/mr1c10/leetcode-challenge/forks">
    <img src="https://img.shields.io/github/forks/mr1c10/leetcode-challenge?color=ffa116&logo=github&style=flat-square" alt="GitHub Forks">
  </a>
</p>

## Sobre o LeetCode

[LeetCode](https://leetcode.com) é uma plataforma de referência para praticar problemas de programação e se preparar para entrevistas técnicas. Ela oferece uma vasta coleção de problemas que ajudam desenvolvedores a aprimorar suas habilidades em algoritmos.

## Visão Geral do Projeto

Este repositório foi criado para documentar minha jornada pelos desafios do LeetCode. Aqui, compartilho soluções, explicações e lições aprendidas ao resolver problemas na plataforma.

Com o objetivo de resolver pelo menos um desafio por dia, busco promover o aprendizado contínuo em algoritmos e estruturas de dados.

## Como Começar

Para contribuir ou utilizar este repositório, você precisará configurar seu ambiente. O projeto utiliza Python para buscar e processar problemas do LeetCode.

### Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório

   ```bash
   git clone https://github.com/caio-andres/leetcode-challenge.git
   cd leetcode-challenge
   ```

2. Crie um ambiente virtual (opcional, mas recomendado)

   ```bash
   python -m venv .venv

   # No Windows
   .venv\Scripts\activate

   # No macOS/Linux
   source .venv/bin/activate
   ```

3. Instale as dependências necessárias

   ```bash
   pip install -r requirements.txt
   ```

### Usando o Script Gerador de Problemas

O repositório inclui um script para buscar automaticamente problemas do LeetCode e criar a estrutura de diretórios:

1. Execute o script

   ```bash
   python get_problem.py
   ```

2. Digite o ID do problema do LeetCode quando solicitado

   ```
   Digite o ID do problema: 1
   ```

3. O script irá:
   - Buscar os detalhes do problema no LeetCode
   - Criar a estrutura de diretórios necessária
   - Gerar arquivos de descrição em inglês e português
   - Criar um arquivo de solução modelo em Python

**Observação: Verifique se o problema gerado é o mesmo que você deseja adicionar ao repositório.
Se não for, confira o título do problema neste <a href="https://leetcode.com/api/problems/all/">LINK</a> e pegue o "question id".**

### Estrutura de Diretórios

Após rodar o script, um novo diretório de problema será criado seguindo o padrão do repositório:

```
problems/
└── solutions/
    └── 0001-two-sum/
        ├── en/
        │   ├── description.md
        │   └── explanation.md
        ├── pt/
        │   ├── descricao.md
        │   └── explicacao.md
        └── solution.cs
```

Agora você está pronto para resolver problemas do LeetCode e contribuir com o projeto!

## Sumário

Aqui você encontrará uma coleção de todos os problemas que resolvi. Cada um está documentado com sua descrição, solução e uma explicação clara.

Para ver o sumário completo de todos os exercícios, acesse [`summary.md`](problems/summary.md).

Se quiser filtrar os problemas por dificuldade, confira os arquivos:

- **Problemas Fáceis**: [`easy.md`](problems/easy.md)
- **Problemas Médios**: [`medium.md`](problems/medium.md)
- **Problemas Difíceis**: [`hard.md`](problems/hard.md)

## Estrutura do Repositório

Cada problema é organizado em seu próprio diretório, contendo:

- **description.md**: O enunciado do problema.
- **explanation.md**: Uma explicação detalhada da abordagem e lógica utilizada.
- **solution.py**: A solução implementada em C#.
- **solution.xx**: A solução implementada em qualquer outra linguagem.

## Suporte Multilíngue

Para alcançar um público maior, disponibilizei a documentação em inglês e português. Cada problema é organizado assim:

```
├── problems
│   └── solutions
│       ├── 001-two-sum
│       │   ├── en/
│       │   │   ├── description.md
│       │   │   └── explanation.md
│       │   ├── pt/
│       │   │   ├── descricao.md
│       │   │   └── explicacao.md
│       │   ├── solution.cs
│       │   └── solution.xx
```

Esse formato garante consistência e facilita a navegação pelos problemas em ambos os idiomas.

## Nossas Estatísticas no LeetCode

Usei o [LeetCode-Stats-Card](https://github.com/JacobLinCool/LeetCode-Stats-Card) para exibir minhas estatísticas atuais. Você pode vê-las abaixo:

[@mr1c10](https://github.com/mr1c10)

![LeetCode Stats](https://leetcard.jacoblin.cool/mr1c10?theme=dark&font=Baloo%202)

## Progresso Atual

- **Total de Problemas Resolvidos**: 1
- **Ultimo problema resolvido**: [1. Two Sum](problems/solutions/0001-two-sum/solution.cs)

Estou comprometido em manter essa sequência e expandir continuamente o repositório com novos desafios e soluções.

## Insígnias

O LeetCode oferece várias **insígnias** para reconhecer conquistas e marcos ao longo da sua jornada de resolução de problemas. Essas insígnias aparecem no perfil do usuário e representam feitos como resolver problemas de diferentes dificuldades, manter sequências diárias, entre outros.

Para ver a lista completa de insígnias disponíveis e saber como conquistar cada uma, confira: [`badges.md`](badges/badges.md)

## Contribuições

Contribuições são bem-vindas! Se quiser adicionar soluções em outra linguagem, melhorar as existentes ou fornecer explicações, fique à vontade para fazer um fork do repositório e enviar um pull request.

<!-- ## Contribuidores -->

## Contato

Para dúvidas ou sugestões, entre em contato pelo meu Instagram: [Instagram](https://instagram.com/_mau_rodrigues).

Ou, se preferir, conecte-se comigo no **LinkedIn**: [Mauricio Rodrigues](https://www.linkedin.com/in/mr1c10).

_Se quiser apoiar, deixe uma estrela ⭐ no repositório — isso significa muito. Obrigado! :)_

##### Este é o Readme do projeto _em português_, caso prefira acompanhar o Readme
