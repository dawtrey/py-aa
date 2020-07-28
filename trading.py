from alpha_vantage.foreignexchange import ForeignExchange 
import pandas as pd

akey = 'W0T38Z08CGRKF3MA'
cfrom = 'EUR' 
cto = 'USD'

global hold
global tsa

def get_price(akey, cfrom, cto):
    cc = ForeignExchange(key=akey)
    # There is no metadata in this call
    data, _ = cc.get_currency_exchange_rate(from_currency=cfrom,to_currency=cto)
    return data['8. Bid Price']

#def seriesify(akey, cfrom, cto):
#    jfile = get_price(akey, cfrom, cto)
#    bid = jfile['8. Bid Price']
#    ask = jfile['9. Ask Price']
#    time = jfile['6. Last Refreshed']
#    print('Bid price:', bid, '  Ask price:', ask, ' at time:', time[-8:])
#    return bid


def get_intraday(akey, cfrom, cto):
    ci = ForeignExchange(key=akey, output_format='pandas')  
    data, metadata = ci.get_currency_exchange_intraday(cfrom, cto, interval='1min', outputsize='full')
    return data['4. close']
    

#ts = get_intraday(akey, cfrom, cto)
#print(ts)
#establishing a variable sucht that we know whether to hold a position


def decision(akey, cfrom, cto, new):
    avg = sum(tsa) / len(tsa)
    if new > avg:
        return 1 
    else: 
        return 0

def minute(akey, cfrom, cto):
    global hold, tsa
    new = get_price(akey, cfrom, cto)
    if hold == 1:
        mult = mult * new / tsa[-1]
    hold = decision(akey, cfrom, cto, new)
    tsa.append(new)
    print('Relative wealth at this time: ', mult,'\n Current price: ', new, sep='')
    wait(60)

def trade(akey, cfrom, cto):
    global hold, tsa
    hold = 0
    tsa = [i for i in get_intraday(akey, cfrom, cto)]
    mult = 1
    print('Initialising trading!')
    print('Initial price: ', get_price(akey, cfrom, cto))
    for i in range(15):
        minute(akey, cfrom, cto)
    multif = mult * 1000
    print('Final relative wealth: {mult}. That means if you had $1000, you would now have {multif}')

trade(akey, cfrom, cto)
