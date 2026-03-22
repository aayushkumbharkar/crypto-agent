import requests


def get_price(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    return requests.get(url).json()[coin]["usd"]


def get_market_chart(coin="bitcoin", days=7):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days={days}"
    data = requests.get(url).json()
    return data["prices"]  # [timestamp, price]
