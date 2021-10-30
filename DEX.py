from config import *
import requests

def dyDx(token1,token2):
    rOrdBook = requests.get(f'https://api.dydx.exchange/v3/orderbook/{token1}-{token2}')
    rMarket = requests.get(f'https://api.dydx.exchange/v3/markets?market={token1}-{token2}')
    jOrdBook = rOrdBook.json()
    jMarket = rMarket.json()
    ordB = {}
    ordB['bids'] = [[item['price'], item['size']] for item in jOrdBook['bids']] 
    ordB['asks'] = [[item['price'], item['size']] for item in jOrdBook['asks']]
    basePrice = jMarket['markets'][f'{token1}-{token2}']['indexPrice'] 
    return(ordB,basePrice)

if __name__ == '__main__':
    dyDx('UNI','USD')