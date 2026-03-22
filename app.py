import streamlit as st
from core.orchestrator import run_agent
from core.memory import load_memory

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

if st.button("Analyze Market"):
    with st.spinner("Analyzing market with AI agents..."):
        result = run_agent(coin)

    st.success("Analysis Complete")

    decision_text = result["decision"]

    if "BUY" in decision_text:
        st.success("🟢 BUY Signal")
    elif "SELL" in decision_text:
        st.error("🔴 SELL Signal")
    else:
        st.warning("🟡 HOLD Signal")

    st.markdown("## 🧠 AI Decision")
    st.code(decision_text, language="text")

    st.markdown("## 🔍 Critic Review")
    st.code(result["critique"], language="text")

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
