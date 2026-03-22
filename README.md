# 🚀 CryptoPilot AI

Multi-Agent Crypto Decision Intelligence System

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

### 📊 Market Agent
Fetches real-time crypto price data
Identifies short-term trend

### 🌐 Sentiment Agent
Analyzes market sentiment (positive / neutral / negative)
Influences final decision

### ⚠️ Risk Agent
Classifies market risk (low / medium / high)

### 🧠 Decision Agent (LLM)
Uses structured prompts to generate:
- Decision
- Reason
- Confidence

### 🔍 Critic Agent
Reviews decision quality
Suggests improvements
Adds explainability layer

### 🖥️ Memory Module
Stores past decisions with timestamps
Enables future learning & tracking

## 🖥️ UI (Streamlit)

Features:

- Real-time coin input
- BUY / SELL / HOLD signals
- AI reasoning (code-style output)
- Critic feedback
- Sentiment indicator
- Memory sidebar (recent decisions)

## 🚀 Live Demo

👉 https://crypto-agent.streamlit.app

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama (Local LLM) / Groq (Cloud LLM)
- Requests
- Modular Multi-Agent Architecture

## ⚡ Running Locally

1. Clone repo
```bash
git clone https://github.com/aayushkumbharkar/crypto-agent.git
cd crypto-agent
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Start Ollama (for LLM)
```bash
ollama run llama3.2
```

4. Run app
```bash
streamlit run app.py
```

## 🌐 Deployment Notes

- Streamlit Cloud used for frontend hosting
- Local LLM (Ollama) replaced with Groq API for cloud
- Full LLM capability available in local environment

## 🧪 Example Output

```
Decision: SELL  
Reason: Downward trend + negative sentiment indicates potential further decline  
Confidence: 80%

Critic Review:

Strong reasoning
Suggests adding risk quantification
Recommends identifying triggers
```

## 🔥 What Makes This Different

- Multi-agent system (not single model)
- Combines structured + unstructured reasoning
- Built-in self-critique loop
- Explainable AI decisions
- Modular & extensible architecture

## 🧭 Future Improvements

- Real Twitter/Reddit sentiment integration
- Backtesting engine
- Portfolio optimization agent
- Autonomous trading execution
- On-chain data integration
