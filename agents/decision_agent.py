import requests
from core.memory import load_memory

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

Output:
Decision: BUY / SELL / HOLD
Reason: clear explanation
Confidence: percentage (0-100)"""

    output = call_ollama(prompt)

    if output is None:
        output = f"""
Decision: HOLD
Reason: Running in cloud mode without local LLM. Based on trend ({market["trend"]}) and sentiment ({sentiment["sentiment"]}), taking cautious stance.
Confidence: 60
"""

    return {"raw_output": output}
