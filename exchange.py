from cachetools import cached, TTLCache
import cex
import DEX
import json

def get_orderbook_sum(orderbook, quantity):
    cur_q = quantity
    sum = .0
    for item in orderbook:
        if cur_q > float(item[1]):
            cur_q -= item[1]
            sum += item[1] * item[0]
        else:
            sum += cur_q * item[0]
            return sum
    return -1
    

def get_max_discount_sell(orderbook, price, quantity):
    orderbook_sum = get_orderbook_sum(orderbook["bids"], quantity)
    if orderbook_sum == -1:
        print('error1')
    nominal = price * quantity
    price = 1 - orderbook_sum/nominal
    delta = nominal - orderbook_sum
    return round(price*100, 5), round(delta, 5)

def get_max_discount_buy(orderbook, price, quantity):
    orderbook_sum = get_orderbook_sum(orderbook["asks"], quantity)
    if orderbook_sum == -1:
        print('error2')
    nominal = price * quantity
    price = 1 - nominal/orderbook_sum
    delta = orderbook_sum - nominal
    return round(price*100, 5), round(delta, 5)

@cached(cache=TTLCache(maxsize=780, ttl=3600))
def merge_orderbooks(token1, token2):
    funcs = [cex.binance, cex.ftx, cex.kucoin, cex.gateio, cex.kraken, cex.huobi, DEX.dyDx]
    merged_bids = []
    merged_asks = []
    merged_prices = []
    for f in funcs:
        try:
            a = f(token1, token2)
            merged_bids += a[0]['bids']
            merged_asks += a[0]['asks']
            merged_prices.append(a[1])
        except Exception as e:
            print(e)
    merged_bids.sort(reverse=True)
    merged_asks.sort(reverse=False)

    min_price = min(merged_prices)
    max_price = max(merged_prices)
    merged_orderbooks = {'bids': merged_bids, 'asks': merged_asks}
    return merged_orderbooks, min_price, max_price


def main(token1, token2, quantity, status):
    aaa = [['BTC', 'USDT'], ['SUSHI', 'USDT'], ['ETH', 'BTC'], ['UNI', 'USDT']]
    for i in aaa:
        merge_orderbooks(i[0], i[1])
    quantity = float(quantity)
    pairs = json.load(open("pairs_valid.json", "r"))
    if [token1, token2] in pairs:
        merged, min_p, max_p = merge_orderbooks(token1, token2)
        if(status == "buy"):
            return get_max_discount_buy(merged, min_p, quantity)
        elif(status == "sell"):
            return get_max_discount_sell(merged, max_p, quantity)
    else:
        return "This pair does not exists"
        


