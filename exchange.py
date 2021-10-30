def get_orderbook_sum(orderbook, quantity):
    cur_q = quantity
    sum = .0
    for item in orderbook:
        if cur_q > float(item[1]):
            cur_q -= float(item[1])
            sum += float(item[1]) * float(item[0])
        else:
            sum += cur_q * float(item[0])
            break
    return sum

def get_max_discount_sell(token1, token2, quantity):
    orderbook, price = cex.binance(token1, token2)
    orderbook_sum = get_orderbook_sum(orderbook['bids'], quantity)
    nominal = float(price) * quantity
    return 1-orderbook_sum/nominal

def get_max_discount_buy(token1, token2, quantity):
    orderbook, price = cex.binance(token1, token2)
    orderbook_sum = get_orderbook_sum(orderbook['asks'], quantity)
    nominal = float(price) * quantity
    return orderbook_sum/nominal

if __name__ == "__main__":
    import cex
    token1 = "BTC"
    token2 = "USDT"
    quantity = 100
    disc = get_max_discount_buy(token1, token2, quantity)
    print(disc)