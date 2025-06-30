import requests
import re
from html2text import html2text
import os
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='pt')

def save_full_structure(problem_data):
    if not problem_data:
        return False

    title = problem_data.get("title", "Unknown Problem")
    difficulty = problem_data.get("difficulty", "Unknown")
    question_id = problem_data.get("questionId", "000")
    slug = problem_data.get("titleSlug")
    content_md = process_html_content(problem_data.get("content", ""))

    # Traduzir o conteúdo para PT
    content_md_pt = translate_text(content_md)

    # Formata o ID com 4 dígitos (ex: 0001, 0293)
    folder_name = f"{str(question_id).zfill(4)}-{slug}"
    base_path = os.path.join("problems", "solutions", folder_name)

    try:
        # Criar dirs
        os.makedirs(os.path.join(base_path, "en"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "pt"), exist_ok=True)

        # en
        with open(os.path.join(base_path, "en", "description.md"), "w", encoding="utf-8") as f:
            f.write(f"# {question_id}. {title} ({difficulty})\n\n")
            f.write(content_md + "\n")

        with open(os.path.join(base_path, "en", "explanation.md"), "w", encoding="utf-8") as f:
            f.write("")

        # pt
        with open(os.path.join(base_path, "pt", "descricao.md"), "w", encoding="utf-8") as f:
            f.write(f"# {question_id}. {title} ({translate_difficulty(difficulty)})\n\n")
            f.write(content_md_pt + "\n")

        with open(os.path.join(base_path, "pt", "explicacao.md"), "w", encoding="utf-8") as f:
            f.write("")

        # Solução em Python
        snippets = problem_data.get("codeSnippets", [])
        python_snippet = next((s for s in snippets if s["langSlug"] == "python3"), None)
        solution_code = python_snippet["code"] if python_snippet else "# Escreva sua solução aqui\n"
        
        # Comentar o código da solução
        commented_solution_code = "\n".join([f"## {line}" for line in solution_code.splitlines()])

        with open(os.path.join(base_path, "solution.cs"), "w", encoding="utf-8") as f:
            f.write(commented_solution_code + "\n")

        return True

    except Exception as e:
        print(f"Erro ao salvar estrutura de diretórios: {e}")
        return False

def translate_text(text):
    try:
        translated = GoogleTranslator(source='en', target='pt').translate(text)
        return translated
    except Exception as e:
        print(f"Erro ao traduzir texto: {e}")
        return text

def translate_difficulty(difficulty):
    mapping = {
        "Easy": "Fácil",
        "Medium": "Médio",
        "Hard": "Difícil"
    }
    return mapping.get(difficulty, difficulty)

def get_slug_by_id(problem_id):
    url = "https://leetcode.com/api/problems/all/"
    try:
        res = requests.get(url)
        res.raise_for_status()
        problems = res.json().get("stat_status_pairs", [])
        
        for item in problems:
            stat = item.get("stat", {})
            if str(stat.get("question_id")) == str(problem_id):
                return stat.get("question__title_slug")
        return None
    except Exception as e:
        print(f"Erro ao buscar o slug: {e}")
        return None

def get_problem_data(slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/"
    }
    payload = {
        "operationName": "questionData",
        "variables": { "titleSlug": slug },
        "query": """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            title
            titleSlug
            content
            difficulty
            codeSnippets {
              lang
              langSlug
              code
            }
          }
        }
        """
    }

    try:
        res = requests.post(url, json=payload, headers=headers)
        res.raise_for_status()
        return res.json().get("data", {}).get("question", {})
    except Exception as e:
        print(f"Erro ao buscar dados do problema: {e}")
        return None

def process_html_content(html_content):
    if not html_content:
        return ""
    
    markdown = html2text(html_content)
    markdown = re.sub(r'\n{3,}', '\n\n', markdown).strip()
    markdown = re.sub(r'\*\*Example (\d+):\*\*', r'## Example \1:', markdown)
    markdown = re.sub(r'\*\*Constraints:\*\*', r'## Constraints', markdown)
    markdown = re.sub(r'\*\*(Input|Output|Explanation):\*\*', r'\1:', markdown)
    markdown = re.sub(r'^(Input:.*|Output:.*|Explanation:.*)', r'    \1', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'\*\*Follow-up:\s*\*\*', r'**Follow-up:** ', markdown)
    return markdown

def main():
    problem_id = input("Digite o ID do problema: ")
    
    slug = get_slug_by_id(problem_id)
    if not slug:
        print("Não foi possível encontrar o slug correspondente ao ID informado.")
        return

    print(f"Slug encontrado: {slug}")

    problem_data = get_problem_data(slug)
    if not problem_data:
        print("Não foi possível obter os dados.")
        return
    
    if save_full_structure(problem_data):
        print("Estrutura criada com sucesso!")
    else:
        print("Erro ao gerar estrutura do problema.")

if __name__ == "__main__":
    main()
