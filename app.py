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
- 🧠 Self-improving memory  
- 🔍 Critic-based optimization  
""")

coin = st.text_input("Enter Coin (bitcoin, ethereum, solana)", "bitcoin")
days = st.selectbox("Select timeframe (days)", [1, 7, 30], index=1)

if st.button("Analyze Market"):
    with st.spinner("Analyzing market with AI agents..."):
        result = run_agent(coin)

    st.success("Analysis Complete")

    # Metrics
    col1, col2, col3 = st.columns(3)

    # Parse decision for metrics
    decision_text = result["decision"]
    signal = "HOLD"
    if "BUY" in decision_text:
        signal = "BUY"
    elif "SELL" in decision_text:
        signal = "SELL"

    trend = "Analyzing..."
    if "Trend:" in decision_text:
        trend = decision_text.split("Trend:")[-1].split()[0]

    col1.metric(
        "Signal", signal, "📊" if signal == "BUY" else "📉" if signal == "SELL" else "⏸️"
    )
    col2.metric("Trend", trend)
    col3.metric("Timeframe", f"{days} days")

    # Signal Badge
    if signal == "BUY":
        st.success("🟢 BUY Signal")
    elif signal == "SELL":
        st.error("🔴 SELL Signal")
    else:
        st.warning("🟡 HOLD Signal")

    st.markdown("## 🧠 AI Decision")
    st.code(decision_text, language="text")

    st.markdown("## 🔍 Critic Review")
    st.code(result["critique"], language="text")

    # Price Chart
    st.markdown("## 📈 Price Trend")
    with st.spinner("Loading chart..."):
        chart_data = get_market_chart(coin, days)

    if chart_data:
        df = pd.DataFrame(chart_data, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        st.line_chart(df.set_index("timestamp"))
    else:
        st.warning("Could not load chart data")

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
