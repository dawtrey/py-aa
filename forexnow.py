from alpha_vantage.foreignexchange import ForeignExchange 

akey = 'W0T38Z08CGRKF3MA'

print('Get current price. Enter the ticker for the from currency: ', end='')
cfrom = input()
print('And now the ticker for the to currency: ', end='')
cto = input()

def get_price(akey, cfrom, cto):
    print(f'Obtaining big and ask prices for transaction [{cfrom}:{cto}]:')
    cc = ForeignExchange(key=akey)
    # There is no metadata in this call
    data, _ = cc.get_currency_exchange_rate(from_currency=cfrom,to_currency=cto)
    return data


jfile = get_price(akey, cfrom, cto)
bid = jfile['8. Bid Price']
ask = jfile['9. Ask Price']
time = jfile['6. Last Refreshed']

print('Bid price:', bid, '  Ask price:', ask, ' at time:', time[-8:])
