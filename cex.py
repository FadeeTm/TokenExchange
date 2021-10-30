from config import *
import ccxt


def binance1(token1, token2):
    binance = ccxt.binance({
        'apiKey': binance_key,
        'secret': binance_secret,
    })
    fetch_ord = binance.fetch_order_book(token1 + '/' + token2) 
    fetch_tick = binance.fetch_ticker(token1 + '/' + token2)['info']['lastPrice']
    return(fetch_ord, fetch_tick)


def coinb(token1, token2):
    coinbasepro = ccxt.coinbasepro({
        'apiKey': coinb_apiKey,
        'secret': coinb_secret,
        'password': coinb_password,
    })
    fetch_ord = coinbasepro.fetch_order_book(token1 + '/' + token2) 
    fetch_tick = coinbasepro.fetch_ticker(token1 + '/' + token2)['info']['price']
    return(fetch_ord, fetch_tick)


def ftx(token1, token2):
    ftx = ccxt.ftx({
        'apiKey': ftx_api_key,
        'secret': ftx_api_secret,
    })
    order_book = ftx.fetch_order_book(token1 + "/" + token2)['bids']
    tickers = ftx.fetch_tickers(token1 + "/" + token2)
    return order_book, tickers[token1 + "/" + token2]['last']


def kucoin1(token1, token2):
    kucoin_ = ccxt.kucoin({
        'apiKey': kucoin_apiKey,
        'secret': kucoin_secret,
        'password': kucoin_password,
    })
    fetch_ord = kucoin_.fetch_order_book(token1 + '/' + token2) 
    fetch_tick = kucoin_.fetch_ticker(token1 + '/' + token2)['info']['last']
    return(fetch_ord, fetch_tick)


def gateio1(token1, token2):
    gateio_ = ccxt.gateio({
        'apiKey': gateio_api_key,
        'secret': gate_io_secret,
        'password': gate_io_pass,
    })
    fetch_ord = gateio_.fetch_order_book(token1 + '/' + token2)['bids']
    fetch_tick = gateio_.fetch_ticker(token1 + '/' + token2)['last']
    return(fetch_ord, fetch_tick)



def kraken1(token1, token2):
    kraken = ccxt.kraken({
        'apiKey': kraken_apiKey,
        'secret': kraken_secret,
    })
    fetch_ord = kraken.fetch_order_book(token1 + '/' + token2) 
    fetch_tick = kraken.fetch_ticker(token1 + '/' + token2)['last']
    return(fetch_ord, fetch_tick)


def huobi_(token1, token2):
    huobi = ccxt.huobi({
        'apiKey': huobi_apiKey,
        'secret': huobi_secret,
    })
    fetch_ord = huobi.fetch_order_book(token1 + '/' + token2) 
    fetch_tick = huobi.fetch_ticker(token1 + '/' + token2)['last']
    return(fetch_ord, fetch_tick)


# if __name__ == "__main__":
#     print(binance1('BTC', 'USDT')[0])
#     print(binance1('BTC', 'USDT')[1])