from agents.market_agent import analyze_market
from agents.risk_agent import assess_risk
from agents.decision_agent import make_decision
from agents.critic_agent import critique
from core.memory import save_memory


def run_agent(coin="bitcoin"):
    market = analyze_market()
    risk = assess_risk(market)
    decision = make_decision(market, risk)
    review = critique(decision["raw_output"])

    save_memory({"market": market, "decision": decision, "critique": review})

    return {"decision": decision["raw_output"], "critique": review}
