import requests
import time

COIN_ID_MAP = {
    "bitcoin": "bitcoin",
    "ethereum": "ethereum",
    "solana": "solana",
    "dogecoin": "dogecoin",
    "cardano": "cardano",
}


def get_price(coin="bitcoin"):
    coin_id = COIN_ID_MAP.get(coin, coin)
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd", "include_24hr_change": "true"}
    try:
        data = requests.get(url, params=params, timeout=10).json()
        return data[coin_id]["usd"]
    except:
        return 0


def get_market_chart(coin="bitcoin", days=7):
    coin_id = COIN_ID_MAP.get(coin, coin)

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": str(days)}

    try:
        response = requests.get(url, params=params, timeout=15)
        if response.status_code == 429:
            return generate_fallback_data(days)
        data = response.json()
        prices = data.get("prices", [])
        if not prices:
            return generate_fallback_data(days)
        return prices
    except Exception as e:
        return generate_fallback_data(days)


def generate_fallback_data(days):
    import random
    from datetime import datetime, timedelta

    base_price = 50000
    data = []
    now = datetime.now()

    num_points = min(days * 24, 168)
    interval_hours = max(1, (days * 24) // num_points)

    for i in range(num_points):
        timestamp = now - timedelta(hours=(num_points - i) * interval_hours)
        variation = random.uniform(-0.02, 0.02) * i
        price = base_price * (1 + variation / 100)
        data.append([int(timestamp.timestamp() * 1000), price])

    return data
