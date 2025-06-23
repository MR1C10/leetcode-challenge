##### Este é o Readme do projeto _em inglês_, caso prefira acompanhar o Readme em Português-BR, [clique aqui](README-PT.md)

# LeetCode Challenge

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

## About LeetCode

[LeetCode](https://leetcode.com) is a premier platform for practicing coding problems and preparing for technical interviews. It offers a vast collection of problems that help developers enhance their algorithmic skills.

## Project Overview

This repository was created to document my journey through LeetCode challenges. Here, I share solutions, explanations, and lessons learned while solving problems on the platform.

With the goal of solving at least one challenge per day, I aim to promote continuous learning in algorithms and data structures.

## Getting Started

To contribute to or use this repository, you'll need to set up your environment first. The project uses Python to fetch and process LeetCode problems.

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/caio-andres/leetcode-challenge.git
   cd leetcode-challenge
   ```

2. Create a virtual environment (optional but recommended)

   ```bash
    python -m venv .venv

    # On Windows
    .venv\Scripts\activate

    # On macOS/Linux
    source .venv/bin/activate
   ```

3. Install the required dependencies

   ```bash
   pip install -r requirements.txt
   ```

### Using the Problem Generator Script

The repository includes a script to automatically fetch problems from LeetCode and create the directory structure:

1. Run the script

   ```bash
   python get_problem.py
   ```

2. Enter the LeetCode problem ID when prompted

   ```
   Digite o ID do problema: 1
   ```

3. The script will:
   - Fetch the problem details from LeetCode
   - Create the necessary directory structure
   - Generate description files in both English and Portuguese
   - Create a template solution file in Python


**Observation: Check if problem generate is the same what you wish to commit to this repo.
If not, check title problem in here <a href="https://leetcode.com/api/problems/all/">LINK</a> and catch it in "question id".**

**I made this program [LeetCode-Exporter](https://github.com/MR1C10/LeetCode-Exporter) that generates an .xlsx file with all the challenges separated by id, title, difficulty and tags**

### Directory Structure

After running the script, a new problem directory will be created following the repository structure pattern:

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

Now you're ready to solve LeetCode problems and contribute to the project!

## Summary

Here you will find a collection of all the problems I have solved. Each one is documented with its description, solution, and a clear explanation.

To view the full summary of all exercises, simply access the [`summary.md`](problems/summary.md).

If you wish to filter problems by difficulty, you can check the following files:

- **Easy Problems**: [`easy.md`](problems/easy.md)
- **Medium Problems**: [`medium.md`](problems/medium.md)
- **Hard Problems**: [`hard.md`](problems/hard.md)

## Repository Structure

Each problem is organized in its own directory, containing:

- **description.md**: The problem statement.
- **explanation.md**: A detailed explanation of the approach and logic used.
- **solution.py**: The implemented solution in Python.
- **solution.xx**: The implemented solution in any other language.

## Multilingual Support

To reach a wider audience, I’ve made the documentation available in both English and Portuguese. Each problem is organized as follows::

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

This format ensures consistency and makes it easier to navigate the problems I address in both languages.

## Our LeetCode Statistics

I used [LeetCode-Stats-Card](https://github.com/JacobLinCool/LeetCode-Stats-Card) to display my current statistics. You can see them below:

[@mr1c10](https://github.com/mr1c10)

![LeetCode Stats](https://leetcard.jacoblin.cool/mr1c10?theme=dark&font=Baloo%202)

## Current Progress



- **Total Problems Solved**: 1
- **Last Problem made**: [1. Two Sum](problems/solutions/0001-two-sum/solution.cs)


I am committed to maintaining this streak and continually expanding the repository with new challenges and solutions.

## Badges

LeetCode offers a variety of **badges** to recognize achievements and milestones throughout your problem-solving journey. These badges appear on user profiles and represent accomplishments like solving problems across different difficulties, maintaining daily streaks, and more.

To see the full list of available badges and learn how to earn each one, check out: [`badges.md`](badges/badges.md)

## Contributions

Contributions are welcome! If you'd like to add solutions in another langagues, improve existing ones, or provide explanations, feel free to fork the repository and submit a pull request.

<!-- ## Contributors -->

## Contact

For any questions or suggestions, contact me by accessing my Instagram:[Instagram](https://instagram.com/_mau_rodrigues).

Or feel free to connect with me on **LinkedIn**: [Mauricio Rodrigues](https://www.linkedin.com/in/mr1c10).

_To show your support, give this repo a ⭐ — it really means a lot. Thank you! :)_

##### Este é o Readme do projeto _em inglês_, caso prefira acompanhar o Readme em Português-BR, [clique aqui](README-PT.md)
