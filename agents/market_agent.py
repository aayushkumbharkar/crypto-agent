import requests


def analyze_market():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    data = requests.get(url).json()

    price = data["market_data"]["current_price"]["usd"]
    change = data["market_data"]["price_change_percentage_24h"]

    trend = "up" if change > 0 else "down"

    return {"price": price, "trend": trend, "change_24h": change}
