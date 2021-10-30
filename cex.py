from config import *
from binance.client import Client
import ccxt
import cbpro
import gate_api


def binance(token1, token2):
    client = Client(binance_api_key, binance_api_secret)
    order_book = client.get_order_book(symbol=(token1 + token2))
    prices = client.get_all_tickers()
    for price in prices:
        if price['symbol'] == (token1 + token2):
            result = price
            break
    return order_book, result['price']


def coinbase1(token1, token2):
    client = cbpro.PublicClient()
    auth_client = cbpro.AuthenticatedClient(coinbase_api_key, coinbase_api_secret, "1erryCV7peJtwPI2")

    ob = auth_client.get_product_order_book(product_id=token1+"-"+token2,level=2)

    return ob


def ftx(token1, token2):
    ftx = ccxt.binance()
    order_book = ftx.fetch_order_book(token1 + "/" + token2)
    tickers = ftx.fetch_tickers(token1 + "/" + token2)
    return order_book, tickers[token1 + "/" + token2]['last']


def kucoin1(token1, token2):
    kucoin_ = ccxt.kucoin(coinb_apiKey, coin_secret, coinb_password)
    fetch_ord = kucoin_.fetch_order_book(token1 + '/' + token2) 
    fetch_tick = kucoin_.fetch_ticker(token1 + '/' + token2)['info']['last']
    return(fetch_ord, fetch_tick)


def gateio(token1, token2):
    configuration = gate_api.Configuration(
        host="https://api.gateio.ws/api/v4"
    )
    client = gate_api.ApiClient(configuration)
    instance = gate_api.SpotApi(client)
    order_book = instance.list_order_book(currency_pair=token1+"_"+token2)
    price = instance.list_tickers(currency_pair=token1+"_"+token2)[0].last
    return order_book, price


def kraken1(token1, token2):
    kraken = ccxt.kraken(kraken_apiKey, kraken_secret)
    fetch_ord = kraken.fetch_order_book(token1 + '/' + token2) 
    fetch_tick = kraken.fetch_ticker(token1 + '/' + token2)['last']
    return(fetch_ord, fetch_tick)


def huobi_(token1, token2):
    huobi = ccxt.huobi(huobi_apiKey, huobi_secret)
    fetch_ord = huobi.fetch_order_book(token1 + '/' + token2) 
    fetch_tick = huobi.fetch_ticker(token1 + '/' + token2)['last']
    return(fetch_ord, fetch_tick)


def main():
    token1 = "BTC"
    token2 = "USDT"

    # print(kucoin1(token1, token2)[0])
    # print(kucoin1(token1, token2)[1])

    # print(binance(token1, token2)[0])
    # print(binance(token1, token2)[1])

    # print(ftx(token1, token2)[0])
    # print(ftx(token1, token2)[1])

    # print(gateio(token1, token2)[0])
    # print(gateio(token1, token2)[1])


if __name__ == "__main__":
    main()