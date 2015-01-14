'''
Created on Aug 5, 2014

@author: jimhorng
'''
from grs import RealtimeTWSE, RealtimeOTC

quote = '19093'

print "===== TWSE ====="
realtime_stock = RealtimeTWSE(quote)
print realtime_stock.raw
print realtime_stock.data

print "===== OTC ====="
realtime_stock_otc = RealtimeOTC(quote)
print realtime_stock_otc.raw
print realtime_stock_otc.data