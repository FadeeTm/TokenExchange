from config import *
from binance.client import Client
import ccxt
import cbpro
import gate_api

'''
def coinbase1(token1, token2):
    client = cbpro.PublicClient()
    auth_client = cbpro.AuthenticatedClient(coinbase_api_key, coinbase_api_secret, "1erryCV7peJtwPI2")

    ob = auth_client.get_product_order_book(product_id=token1+"-"+token2,level=2)

    return ob
'''

def gateio(token1, token2):
    configuration = gate_api.Configuration(
        host="https://api.gateio.ws/api/v4"
    )
    client = gate_api.ApiClient(configuration)
    instance = gate_api.SpotApi(client)
    order_book = instance.list_order_book(currency_pair=token1+"_"+token2)
    price = instance.list_tickers(currency_pair=token1+"_"+token2)[0].last
    return order_book, price


def ftx(token1, token2):
    ftx = ccxt.binance()
    order_book = ftx.fetch_order_book(token1 + "/" + token2)
    tickers = ftx.fetch_tickers(token1 + "/" + token2)
    return order_book, tickers[token1 + "/" + token2]['last']


def binance(token1, token2):
    client = Client(binance_api_key, binance_api_secret)
    order_book = client.get_order_book(symbol=(token1 + token2))
    prices = client.get_all_tickers()
    for price in prices:
        if price['symbol'] == (token1 + token2):
            result = price
            break
    return order_book, result['price']


def main():
    token1 = "BNB"
    token2 = "BTC"

    print(binance(token1, token2)[0])
    print(binance(token1, token2)[1])

    print(ftx(token1, token2)[0])
    print(ftx(token1, token2)[1])

    print(gateio(token1, token2)[0])
    print(gateio(token1, token2)[1])


if __name__ == "__main__":
    main()
