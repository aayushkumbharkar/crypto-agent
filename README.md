# 🚀 CryptoPilot AI

**Multi-Agent Crypto Decision Intelligence System**

CryptoPilot AI is a multi-agent system that analyzes cryptocurrency markets using price trends, risk modeling, sentiment analysis, and LLM-based reasoning to generate trading decisions.

It doesn't just react to data — it thinks, critiques, and improves.

## 🧠 Core Idea

Traditional bots rely only on price signals.

CryptoPilot AI combines:

- 📈 Market data
- ⚠️ Risk assessment
- 🌐 Sentiment analysis
- 🤖 LLM reasoning
- 🔍 Self-critique

→ to produce higher-quality, explainable decisions

## ⚙️ Architecture

```
User Input (Coin)
        ↓
Market Agent → Fetch price + trend
        ↓
Sentiment Agent → Market sentiment score
        ↓
Risk Agent → Risk classification
        ↓
Decision Agent (LLM) → BUY / SELL / HOLD
        ↓
Critic Agent (LLM) → Evaluates reasoning
        ↓
Memory → Stores decisions for learning
```

## 🤖 Agents

| Agent | Description |
|-------|-------------|
| 📊 Market Agent | Fetches real-time crypto price data, identifies short-term trend |
| 🌐 Sentiment Agent | Analyzes market sentiment (positive/neutral/negative) |
| ⚠️ Risk Agent | Classifies market risk (low/medium/high) |
| 🧠 Decision Agent | Uses LLM to generate Decision, Reason, Confidence |
| 🔍 Critic Agent | Reviews decision quality, suggests improvements |
| 🖥️ Memory Module | Stores past decisions with timestamps for learning |

## 🖥️ UI (Streamlit)

Features:

- Real-time coin input
- BUY / SELL / HOLD signals
- AI reasoning (code-style output)
- Critic feedback
- Sentiment indicator
- Memory sidebar (recent decisions)
- Live price charts

## 🌐 Live Demo

👉 https://crypto-agent.streamlit.app

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama (Local LLM) / Groq API (Cloud LLM)
- Requests
- Modular Multi-Agent Architecture

## ⚡ Running Locally

```bash
# 1. Clone repo
git clone https://github.com/aayushkumbharkar/crypto-agent.git
cd crypto-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Ollama (for LLM)
ollama run llama3.2

# 4. Run app
streamlit run app.py
```

## 🔐 Environment Variables

Create a `.env` file for local development:

```
GROQ_API_KEY=your-groq-api-key  # Optional: for cloud LLM
OPENAI_API_KEY=your-openai-key  # Optional: alternative LLM
```

## 🧪 Example Output

```
Decision: SELL  
Reason: Downward trend + negative sentiment indicates potential further decline  
Confidence: 80%
```

**Critic Review:**
- Strengths: Clear reasoning based on data
- Weaknesses: Could quantify risk more
- Improvement: Add specific entry/exit points

## 🔥 What Makes This Different

- Multi-agent system (not single model)
- Combines structured + unstructured reasoning
- Built-in self-critique loop
- Explainable AI decisions
- Modular & extensible architecture
- Self-improving memory system

## 🧭 Future Improvements

- Real Twitter/Reddit sentiment integration
- Backtesting engine
- Portfolio optimization agent
- Autonomous trading execution
- On-chain data integration
- Multi-coin portfolio analysis

## 📄 License

MIT License
