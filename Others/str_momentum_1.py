#!/usr/bin/python

## str_momentum_1.py

from datetime import datetime,timedelta
from heapq import nlargest

#ticker转换为id
tk2id=lambda x: x+'.XSHG' if x[0]=='6'else x+'.XSHE' 

#获取3月25日活跃主题对应的所有股票
themeList = DataAPI.ActiveThemesGet('20150325').themeID.tolist()
sa = []
for t in themeList:
    sa += DataAPI.TickersByThemesGet(themeID=str(t)).ticker.tolist()
sa = list(set(sa))

#以下为回测参数
start = '2014-12-24'
end = '2015-04-24'
benchmark = 'HS300'
universe = map(tk2id, sa)
capital_base = 10000000
refresh_rate = 20
longest_history = 20

def initialize(account):
    pass

def handle_data(account):
    # 获取调仓日活跃主题相关股票tickers
    themeList = DataAPI.ActiveThemesGet(account.current_date.strftime('%Y%m%d')).themeID.tolist()        
    ta = {}
    for t in themeList:
        ta[t] = DataAPI.TickersByThemesGet(themeID=str(t)).ticker.tolist() 
    
    # 获取过去20个交易日的收盘价
    p = account.get_attribute_history('closePrice', 20)
    
    #找调仓日内按照等权return加和最大的20个主题
    sa = {}
    for stock in account.universe:
        sa[stock] = p[stock][-1] / p[stock][0] -1 #从调仓日之前20天的return

    tb = {}
    for t in ta:
        tb[t] = sum(sa.get(s,0) for s in ta[t])
    tb = nlargest(20,tb,tb.get)
    
    # 找这最好的20个主题中最好的5只股票
    sc = []
    for t in tb:
        sc += nlargest(5,[s for s in map(tk2id,ta[t]) if s in sa],sa.get)
    sc = list(set(sc))
    
    for stock in account.valid_secpos: # 卖出目前所有持有的股票
        order_to(stock, 0)

    for stock in sc: # 买进新选出的100只股票
        order(stock, account.referencePortfolioValue / len(sc) / p[stock][-1])