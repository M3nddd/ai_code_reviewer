import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path("I:/Lab4/ai_code_reviewer/.env"))

API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_code(code: str, language: str) -> dict:
    prompt = f"""
You are an expert code reviewer. Analyze the following {language} code and provide:

1. **Bugs**: List any bugs or errors found
2. **Code Quality Issues**: Style, naming, complexity problems
3. **Security Issues**: Any security vulnerabilities
4. **Suggestions**: How to improve the code
5. **Overall Score**: Rate the code from 1-10

Format your response clearly with these exact sections.

Code to review:
```{language}
{code}
```
"""
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "nvidia/nemotron-3-super-120b-a12b:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
    )

    result = response.json()

    if "choices" not in result:
        error_msg = result.get("error", {}).get("message", str(result))
        raise Exception(f"API Error: {error_msg}")

    text = result["choices"][0]["message"]["content"]
    return parse_response(text)


def parse_response(text: str) -> dict:
    sections = {
        "bugs": "",
        "quality": "",
        "security": "",
        "suggestions": "",
        "score": "0",
        "raw": text
    }

    current = None
    lines = text.split("\n")

    for line in lines:
        lower = line.lower()
        if "bug" in lower:
            current = "bugs"
        elif "quality" in lower or "style" in lower:
            current = "quality"
        elif "security" in lower:
            current = "security"
        elif "suggestion" in lower or "improve" in lower:
            current = "suggestions"
        elif "score" in lower or "rating" in lower:
            current = "score"
            import re
            match = re.search(r'\b([0-9]|10)\b', line)
            if match:
                sections["score"] = match.group(1)
        elif current:
            sections[current] += line + "\n"

    return sections