from agents.market_agent import analyze_market
from agents.risk_agent import assess_risk
from agents.decision_agent import make_decision
from core.memory import save_memory


def run_agent(coin="bitcoin"):
    market = analyze_market()
    risk = assess_risk(market)
    decision = make_decision(market, risk)

    save_memory({"coin": coin, "decision": decision})

    return decision
