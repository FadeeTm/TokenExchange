import requests

def binance(token1,token2):
    rOrdBook = requests.get(f'https://api.binance.com/api/v3/depth?symbol={token1}{token2}&limit=5000')
    rMarket = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={token1}{token2}')
    jOrdBook = rOrdBook.json()
    jMarket = rMarket.json()
    ordB = {}
    ordB['bids'] = [[float(item[0]), float(item[1])] for item in jOrdBook['bids']] 
    ordB['asks'] = [[float(item[0]), float(item[1])] for item in jOrdBook['asks']]
    basePrice = float(jMarket["price"])
    return(ordB,basePrice)

def ftx(token1,token2):
    rOrdBook = requests.get(f'https://ftx.com/api/markets/{token1}/{token2}/orderbook?depth=100')
    rMarket = requests.get(f'https://ftx.com/api/markets/{token1}/{token2}')
    jOrdBook = rOrdBook.json()["result"]
    jMarket = rMarket.json()["result"]
    ordB = {}
    ordB['bids'] = [[float(item[0]), float(item[1])] for item in jOrdBook['bids']] 
    ordB['asks'] = [[float(item[0]), float(item[1])] for item in jOrdBook['asks']]
    basePrice = float(jMarket["last"])
    return(ordB,basePrice)


def kucoin(token1,token2):
    rOrdBook = requests.get(f'https://api.kucoin.com/api/v1/market/orderbook/level2_100?symbol={token1}-{token2}')
    rMarket = requests.get(f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={token1}-{token2}')
    jOrdBook = rOrdBook.json()["data"]
    jMarket = rMarket.json()["data"]
    ordB = {}
    ordB['bids'] = [[float(item[0]), float(item[1])] for item in jOrdBook['bids']] 
    ordB['asks'] = [[float(item[0]), float(item[1])] for item in jOrdBook['asks']]
    basePrice = float(jMarket["price"])
    return(ordB,basePrice)


def gateio(token1,token2):
    rOrdBook = requests.get(f'https://api.gateio.ws/api/v4/spot/order_book?currency_pair={token1}_{token2}&limit=100')
    rMarket = requests.get(f'https://api.gateio.ws/api/v4/spot/tickers?currency_pair={token1}_{token2}')
    jOrdBook = rOrdBook.json()
    jMarket = rMarket.json()
    ordB = {}
    ordB['bids'] = [[float(item[0]), float(item[1])] for item in jOrdBook['bids']] 
    ordB['asks'] = [[float(item[0]), float(item[1])] for item in jOrdBook['asks']]
    basePrice = float(jMarket[0]["last"])
    return(ordB,basePrice)


def kraken(token1,token2):
    rOrdBook = requests.get(f'https://api.kraken.com/0/public/Depth?pair={token1}{token2}&count=100')
    rMarket = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={token1}{token2}')
    key = list(rOrdBook.json()["result"].keys())[0]
    jOrdBook = rOrdBook.json()["result"][key]
    jMarket = rMarket.json()["result"][key]
    ordB = {}
    ordB['bids'] = [[float(item[0]), float(item[1])] for item in jOrdBook['bids']] 
    ordB['asks'] = [[float(item[0]), float(item[1])] for item in jOrdBook['asks']]
    basePrice = float(jMarket["c"][0])
    return(ordB,basePrice)


def huobi(token1,token2):
    rOrdBook = requests.get(f"https://api.huobi.pro/market/depth?symbol={token1.lower()}{token2.lower()}&type=step0")
    rMarket = requests.get(f"https://api.huobi.pro/market/detail/merged?symbol={token1.lower()}{token2.lower()}")
    jOrdBook = rOrdBook.json()["tick"]
    jMarket = rMarket.json()["tick"]
    ordB = {}
    ordB['bids'] = [[float(item[0]), float(item[1])] for item in jOrdBook['bids']] 
    ordB['asks'] = [[float(item[0]), float(item[1])] for item in jOrdBook['asks']]
    basePrice = float(jMarket["close"])
    return(ordB,basePrice)


if __name__ == "__main__":
    funcs = [binance, ftx, kucoin, gateio, kraken, huobi]
    for f in funcs:
        print(f('BTC', 'USDT'))