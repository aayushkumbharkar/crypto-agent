import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def call_ollama(prompt, model="llama3.2"):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=30,
        ).json()
        return response.get("response")
    except:
        return None


def critique(decision_text):
    prompt = f"""Evaluate this trading decision:

{decision_text}

Give:
- Strengths
- Weaknesses
- What should be done differently next time (IMPORTANT)"""

    output = call_ollama(prompt)

    if output is None:
        output = "Critic unavailable in cloud mode. Basic evaluation: Decision has been logged for analysis."

    return output
