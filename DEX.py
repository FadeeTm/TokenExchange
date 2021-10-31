import requests

def dyDx(token1,token2):
    rOrdBook = requests.get(f'https://api.dydx.exchange/v3/orderbook/{token1}-{token2}')
    rMarket = requests.get(f'https://api.dydx.exchange/v3/markets?market={token1}-{token2}')
    jOrdBook = rOrdBook.json()
    jMarket = rMarket.json()
    ordB = {}
    ordB['bids'] = [[float(item['price']), float(item['size'])] for item in jOrdBook['bids']] 
    ordB['asks'] = [[float(item['price']), float(item['size'])] for item in jOrdBook['asks']]
    basePrice = jMarket['markets'][f'{token1}-{token2}']['indexPrice'] 
    return(ordB,basePrice)


def serumDex(token1,token2):
    rOrdBook = requests.get(f'https://serum-api.bonfida.com/orderbooks/{token1}{token2}')
    jOrdBook = rOrdBook.json()["data"]
    ordB = {}
    ordB['bids'] = [[float(item['price']), float(item['size'])] for item in jOrdBook['bids']] 
    ordB['asks'] = [[float(item['price']), float(item['size'])] for item in jOrdBook['asks']]
    basePrice = (ordB['bids'][0][0] + ordB['asks'][0][0]) / 2
    return(ordB,basePrice)


if __name__ == '__main__':
    print(serumDex('SUSHI','USDT'))