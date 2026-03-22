def make_decision(market, risk):
    if risk == "high":
        decision = "HOLD"
    else:
        decision = "BUY"

    return {
        "decision": decision,
        "reason": f"24h change is {market['change_24h']}% indicating a {market['trend']} trend with {risk} risk.",
        "confidence": 70,
    }
