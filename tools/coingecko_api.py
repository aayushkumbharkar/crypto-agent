import requests


def get_price(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": "usd"}
    data = requests.get(url, params=params).json()
    return data[coin]["usd"]


def get_market_chart(coin="bitcoin", days=7):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {"vs_currency": "usd", "days": days}
    data = requests.get(url, params=params).json()
    return data.get("prices", [])
