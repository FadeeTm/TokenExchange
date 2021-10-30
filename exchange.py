def get_orderbook_sum(orderbook, quantity):
    cur_q = quantity
    sum = .0
    for item in orderbook:
        if cur_q > item[1]:
            cur_q -= item[1]
            sum += item[1] * item[0]
        else:
            sum += cur_q * item[0]
            return sum
    return -1
    

def get_max_discount_sell(orderbook, price, quantity):
    orderbook_sum = get_orderbook_sum(orderbook, quantity)
    if orderbook_sum == -1:
        print('error1')
    nominal = price * quantity
    return 1-orderbook_sum/nominal

def get_max_discount_buy(orderbook, price, quantity):
    orderbook_sum = get_orderbook_sum(orderbook, quantity)
    if orderbook_sum == -1:
        print('error2')
    nominal = price * quantity
    return 1 - nominal/orderbook_sum

def merge_orderbooks(token1, token2, ifSell = True):
    funcs = [cex.ftx, cex.ftx]
    merged_orderbooks = []
    merged_prices = []
    for f in funcs:
        try:
            a = f(token1, token2)
            if ifSell:
                merged_orderbooks += a[0]['bids']
            else:
                merged_orderbooks += a[0]['asks']
            merged_prices.append(a[1])
        except Exception as e:
            print(e)
    if ifSell:
        merged_orderbooks.sort(reverse=True)
    else:
        merged_orderbooks.sort(reverse=False)
    sum = 0
    for price in merged_prices:
        sum+=price
    price = sum/len(merged_prices)
    return merged_orderbooks, price



if __name__ == "__main__":
    import cex
    token1 = "BTC"
    token2 = "USDT"
    quantity = 100
    
    a = merge_orderbooks(token1, token2, ifSell = False)
    b = merge_orderbooks(token1, token2, ifSell = True)
    disc_s = get_max_discount_sell(a[0], a[1], quantity)
    disc_b = get_max_discount_buy(b[0], b[1], quantity)

    print(f'sell: {disc_s}')
    print(f'buy: {disc_b}')
    