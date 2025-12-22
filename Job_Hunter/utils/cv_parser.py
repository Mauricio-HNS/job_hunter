# Job_Hunter/utils/cv_parser.py
import pdfplumber
from docx import Document
import re

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        raise ValueError("Formato de CV não suportado")

def parse_cv(file_path):
    """
    Retorna um dicionário com informações do CV:
    - skills
    - seniority
    - experience_years
    """
    text = extract_text(file_path)

    experience_match = re.search(r"(\d+)\s+anos?", text, re.IGNORECASE)
    experience_years = int(experience_match.group(1)) if experience_match else 0

    known_skills = ["C#", ".NET", "Flutter", "React", "Python", "JavaScript"]
    skills = [skill for skill in known_skills if skill.lower() in text.lower()]

    seniority = "Senior" if experience_years >= 10 else "Mid" if experience_years >= 5 else "Junior"

    return {
        "skills": skills,
        "seniority": seniority,
        "experience_years": experience_years
    }
