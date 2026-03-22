import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def critique(decision_text):
    prompt = f"""Evaluate this trading decision:

{decision_text}

Give:
- Strengths
- Weaknesses
- What should be done differently next time (IMPORTANT)"""

    response = requests.post(
        OLLAMA_URL, json={"model": "llama3.2", "prompt": prompt, "stream": False}
    ).json()

    return response.get("response", "Error generating critique")
