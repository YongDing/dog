# -*- coding: utf-8 -*-
'''
Created on 2017年9月6日

@author: ding
'''

import requests
import time
import json

domain = "https://api.btcmarkets.net"
CURRENCY_RATE = 5.22
def marketLTCPrice():
    uri = "/market/LTC/AUD/tick"
    url = domain + uri
    r = requests.get(url, verify=True)
    ltcask = str(r.json()["bestAsk"])
    ltcbid = str(r.json()["bestBid"])
    last = str(r.json()["lastPrice"])
    result = [ltcask, ltcbid, last]
    return [float(price) * CURRENCY_RATE for price in result] 


def marketBTCPrice():
    uri = "/market/BTC/AUD/tick"
    url = domain + uri
    r = requests.get(url, verify=True)
    btcask = str(r.json()["bestAsk"])
    btcbid = str(r.json()["bestBid"])
    btclast = str(r.json()["lastPrice"])
    result = [btcask, btcbid, btclast]
    return [float(price) * CURRENCY_RATE for price in result]

def okcoinBTCPrice():
    url = "https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny"
    r = requests.get(url, verify=True)
    result = json.loads(r.text)
    ticker = result["ticker"]
    btcask = ticker["buy"]
    btcbid = ticker["sell"]
    btclast = ticker["last"]
    result = [btcask, btcbid, btclast]
    return [float(price) for price in result]

def okcoinLTCPrice():
    url = "https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny"
    r = requests.get(url, verify=True)
    result = json.loads(r.text)
    ticker = result["ticker"]
    ltcask = ticker["buy"]
    ltcbid = ticker["sell"]
    ltclast = ticker["last"]
    result = [ltcask, ltcbid, ltclast]
    return [float(price) for price in result]

def moveBrick():
    marketLTCResult = marketLTCPrice()
    okcoinLTCResult = okcoinLTCPrice()
    ltcProfit = (marketLTCResult[1] - okcoinLTCResult[0]) / okcoinLTCResult[0] * 100
    print "ltc market 买:%.2f, 卖:%2.f" % (marketLTCResult[0], marketLTCResult[1])
    print "ltc okcoin 买:%.2f, 卖:%2.f" % (okcoinLTCResult[0], okcoinLTCResult[1])
    print " 利润: %.2f"  % (ltcProfit,), "%"
    
    marketBTCResult = marketBTCPrice()
    okcoinBTCResult = okcoinBTCPrice()
    btcProfit = (marketBTCResult[1] - okcoinBTCResult[0]) / okcoinBTCResult[0] * 100
    print "btc market 买:%.2f, 卖:%2.f" % (marketBTCResult[0], marketBTCResult[1])
    print "btc okcoin 买:%.2f, 卖:%2.f" % (okcoinBTCResult[0], okcoinBTCResult[1])
    print " 利润: %.2f"  % (btcProfit,), "%"

    sumCash = 10000.00
    if ltcProfit > btcProfit:
        finalCash = sumCash / okcoinLTCResult[0] * marketLTCResult[1] / marketBTCResult[0] * okcoinBTCResult[1]
        print "搬砖莱特, 回流比特利润: %.2f" % ((finalCash - sumCash)/sumCash * 100,), "%"
    else:
        finalCash = sumCash / okcoinBTCResult[0] * marketBTCResult[1] / marketLTCResult[0] * okcoinLTCResult[1]
        print "搬砖比特, 回流莱特利润: %.2f" % ((finalCash - sumCash)/sumCash * 100,), "%"
        
def moveBrickInfo():
    marketLTCResult = marketLTCPrice()
    okcoinLTCResult = okcoinLTCPrice()
    ltcProfit = (marketLTCResult[1] - okcoinLTCResult[0]) / okcoinLTCResult[0] * 100
    content = u""
    content += u"ltc market 买:%.2f, 卖:%2.f" % (marketLTCResult[0], marketLTCResult[1]) + "\n"
    content += u"ltc okcoin 买:%.2f, 卖:%2.f" % (okcoinLTCResult[0], okcoinLTCResult[1]) + "\n"
    content += u" 利润: %.2f"  % (ltcProfit,) + "%\n"

    marketBTCResult = marketBTCPrice()
    okcoinBTCResult = okcoinBTCPrice()
    btcProfit = (marketBTCResult[1] - okcoinBTCResult[0]) / okcoinBTCResult[0] * 100
    content += u"btc market 买:%.2f, 卖:%2.f" % (marketBTCResult[0], marketBTCResult[1]) + "\n"
    content += u"btc okcoin 买:%.2f, 卖:%2.f" % (okcoinBTCResult[0], okcoinBTCResult[1]) + "\n"
    content += u" 利润: %.2f"  % (btcProfit,) + "%\n"

    sumCash = 10000.00
    if ltcProfit > btcProfit:
        finalCash = sumCash / okcoinLTCResult[0] * marketLTCResult[1] / marketBTCResult[0] * okcoinBTCResult[1]
        content += u"搬砖莱特, 回流比特利润: %.2f" % ((finalCash - sumCash)/sumCash * 100,) + "%"
    else:
        finalCash = sumCash / okcoinBTCResult[0] * marketBTCResult[1] / marketLTCResult[0] * okcoinLTCResult[1]
        content += u"搬砖比特, 回流莱特利润: %.2f" % ((finalCash - sumCash)/sumCash * 100,) + "%"
    return content

if __name__ == "__main__":
    print moveBrickInfo()
