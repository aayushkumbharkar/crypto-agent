import streamlit as st
import pandas as pd
from core.orchestrator import run_agent
from core.memory import load_memory
from tools.coingecko_api import get_market_chart

st.set_page_config(page_title="CryptoPilot AI", page_icon="🚀", layout="wide")

st.title("🚀 CryptoPilot AI")
st.subheader("Autonomous Crypto Decision Intelligence Agent")

st.markdown("""
### Features:
- 📈 Real-time market analysis  
- 🤖 Multi-agent reasoning system  
- 🌐 Sentiment intelligence  
- 🧠 Self-improving memory  
- 🔍 Critic-based optimization  
""")

coin_options = ["bitcoin", "ethereum", "solana", "dogecoin", "cardano"]
coin = st.selectbox("Select Coin", coin_options, index=0)

days = st.slider("Select timeframe (days)", 1, 90, 7)

if st.button("Analyze Market"):
    with st.spinner("Analyzing market with AI agents..."):
        result = run_agent(coin)

    st.success("Analysis Complete")

    col1, col2, col3, col4 = st.columns(4)

    decision_text = result["decision"]
    signal = "HOLD"
    if "BUY" in decision_text:
        signal = "BUY"
    elif "SELL" in decision_text:
        signal = "SELL"

    sentiment_text = result["sentiment"]["sentiment"].upper()

    col1.metric("Signal", signal)
    col2.metric("Sentiment", sentiment_text)
    col3.metric("Score", f"{result['sentiment']['score']:.0%}")
    col4.metric("Timeframe", f"{days} days")

    if signal == "BUY":
        st.success("🟢 BUY Signal")
    elif signal == "SELL":
        st.error("🔴 SELL Signal")
    else:
        st.warning("🟡 HOLD Signal")

    st.markdown("## 🌐 Market Sentiment")
    sent = result["sentiment"]["sentiment"]
    if sent == "positive":
        st.success("🟢 Positive Sentiment")
    elif sent == "negative":
        st.error("🔴 Negative Sentiment")
    else:
        st.warning("🟡 Neutral Sentiment")
    st.caption(f"Sentiment Score: {result['sentiment']['score']}")

    st.markdown("## 🧠 AI Decision")
    st.code(decision_text, language="text")

    st.markdown("## 🔍 Critic Review")
    st.code(result["critique"], language="text")

    st.markdown("## 📈 Price Trend")
    with st.spinner("Loading chart..."):
        chart_data = get_market_chart(coin, days)

    if chart_data and len(chart_data) > 0:
        df = pd.DataFrame(chart_data, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        st.line_chart(df.set_index("timestamp"))
    else:
        st.warning("Could not load chart data. API rate limit may be active.")

st.sidebar.title("📊 Memory (Last Decisions)")
memory = load_memory()

if memory:
    for m in reversed(memory):
        st.sidebar.markdown(f"""
        **Time:** {m.get("timestamp", "N/A")}  
        **Decision:** {m.get("decision", "N/A")[:80]}...  
        ---
        """)
else:
    st.sidebar.info("No decisions yet. Run analysis to build memory.")
