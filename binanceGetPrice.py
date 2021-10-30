from config import *
from binance.client import Client
import ccxt
'''
def ftx(token):
'''


def binance(token):
    client = Client(binance_api_key, binance_api_secret)
    depth = client.get_order_book(symbol=token)
    prices = client.get_all_tickers()
    for price in prices:
        if price['symbol'] == token:
            result = price
            break
    return depth, result['price']


def main():
    token1 = "BNB"
    token2 = "BTC"
    order_book = ccxt.binance().fetch_order_book(token1 + "/" + token2)
    tickers = ccxt.binance().fetch_tickers(token1 + "/" + token2)
    print(order_book)
    print(tickers[token1 + "/" + token2]['last'])
    print()
    print(binance(token1+token2)[0])
    print(binance(token1 + token2)[1])

if __name__ == "__main__":
    main()
