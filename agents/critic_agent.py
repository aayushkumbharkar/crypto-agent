import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def critique(decision_text):
    prompt = f"""Evaluate this trading decision:

{decision_text}

Answer:
- Is the reasoning strong?
- What could be improved?
- Suggest a better version if possible."""

    response = requests.post(
        OLLAMA_URL, json={"model": "llama3.2", "prompt": prompt, "stream": False}
    )

    data = response.json()
    return data.get("response", "Error generating critique")
