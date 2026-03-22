import requests


def analyze_market(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": "usd", "include_24hr_change": "true"}
    data = requests.get(url, params=params).json()

    coin_data = data.get(coin, {})
    price = coin_data.get("usd", 0)
    change = coin_data.get("usd_24h_change", 0)

    trend = "up" if change > 0 else "down"

    return {"price": price, "trend": trend, "change_24h": change}
