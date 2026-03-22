import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def make_decision(market, risk):
    prompt = f"""You are an expert crypto trading analyst AI.

Analyze the following:

Market Data:
- Price: ${market["price"]}
- 24h Change: {market["change_24h"]}%
- Trend: {market["trend"]}

Risk Level: {risk}

Give output in this format:
Decision: BUY / SELL / HOLD
Reason: clear explanation
Confidence: percentage (0-100)"""

    response = requests.post(
        OLLAMA_URL, json={"model": "llama3.2", "prompt": prompt, "stream": False}
    )

    data = response.json()
    return {"raw_output": data.get("response", "Error generating response")}
