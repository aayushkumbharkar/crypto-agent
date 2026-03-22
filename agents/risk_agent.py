def assess_risk(market_data):
    if market_data["trend"] == "volatile":
        return "high"
    return "medium"
