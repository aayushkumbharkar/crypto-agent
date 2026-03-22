import requests
import os

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
OLLAMA_URL = "http://localhost:11434/api/generate"


def call_llm(prompt, model="llama3.2"):
    api_key = os.getenv("GROQ_API_KEY")

    if api_key:
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": "llama-3.2-3b-preview",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
            }
            response = requests.post(
                GROQ_API_URL, headers=headers, json=payload, timeout=30
            )
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            pass

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=30,
        )
        return response.json().get("response")
    except:
        return None


def critique(decision_text):
    prompt = f"""Evaluate this trading decision:

{decision_text}

Give brief feedback:
- Strengths: (1-2 points)
- Weaknesses: (1-2 points)  
- Improvement: (1 sentence)"""

    output = call_llm(prompt)

    if output is None:
        output = "Critic unavailable. Decision logged for analysis."

    return output
