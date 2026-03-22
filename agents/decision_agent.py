import requests
import os
import streamlit as st
from core.memory import load_memory

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
            "model": "llama-3.1-8b-instant",
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


def make_decision(market, risk, sentiment):
    past = load_memory()

    memory_context = (
        "\n".join(
            [
                f"- Decision: {m.get('decision', '')} | Outcome: {m.get('critique', '')[:100]}"
                for m in past
            ]
        )
        or "No past decisions yet."
    )

    prompt = f"""You are an expert crypto trading AI.

Market Data:
- Price: ${market["price"]}
- 24h Change: {market["change_24h"]}%
- Trend: {market["trend"]}

Risk Level: {risk}

Sentiment Analysis:
- Sentiment: {sentiment["sentiment"]}
- Score: {sentiment["score"]}

Past decisions:
{memory_context}

Make a decision considering BOTH market data and sentiment.

Output ONLY this format:
Decision: BUY / SELL / HOLD
Reason: one sentence explanation
Confidence: percentage (0-100)"""

    output = call_groq(prompt)

    if output is None:
        output = f"""
Decision: HOLD
Reason: Based on trend ({market["trend"]}) and sentiment ({sentiment["sentiment"]}), taking cautious stance.
Confidence: 60
"""

    return {"raw_output": output}
