import requests
from core.memory import load_memory

OLLAMA_URL = "http://localhost:11434/api/generate"


def make_decision(market, risk):
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

    prompt = f"""You are a self-improving crypto trading AI.

Past decisions and critiques:
{memory_context}

Current Market:
- Price: ${market["price"]}
- Change: {market["change_24h"]}%
- Trend: {market["trend"]}
- Risk: {risk}

Learn from past mistakes and improve.

Output:
Decision: BUY / SELL / HOLD
Reason: clear explanation
Confidence: percentage (0-100)"""

    response = requests.post(
        OLLAMA_URL, json={"model": "llama3.2", "prompt": prompt, "stream": False}
    ).json()

    return {"raw_output": response.get("response", "Error generating response")}
