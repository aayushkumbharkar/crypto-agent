import requests
import os
import streamlit as st

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


def call_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY", "")

    if not api_key or api_key == "your-groq-key-here":
        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except:
            return None

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }
        response = requests.post(
            GROQ_API_URL, headers=headers, json=payload, timeout=60
        )
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return None
    except Exception as e:
        return None


def critique(decision_text):
    prompt = f"""Evaluate this trading decision:

{decision_text}

Give brief feedback:
- Strengths: (1-2 points)
- Weaknesses: (1-2 points)  
- Improvement: (1 sentence)"""

    output = call_groq(prompt)

    if output is None:
        return "Critic unavailable in cloud mode. The decision has been logged for analysis."

    return output
