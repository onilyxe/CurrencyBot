import http.client
import cachetools.func
import requests
import json
from concurrent.futures import ThreadPoolExecutor

USD = "USDT"
URL = "https://api.binance.com"
API_TYPES = {"price": "/api/v3/ticker/price", "time": "/api/v3/time"}

# Все монеты
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cached(currs=["BTC", "ETH", "ATOM", "ADA", "FTM", "SOL", "XRP", "XTZ", "OMG", "LUNA", "MANA", "LINK", "KSM", "DOGE"]):
    return get_rates_concurrent(currs)

# BTC
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedBTC(currs=["BTC"]):
    return get_rates_concurrent(currs)
    
# ETH
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedETH(currs=["ETH"]):
    return get_rates_concurrent(currs)
    
# ATOM
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedATOM(currs=["ATOM"]):
    return get_rates_concurrent(currs)
    
# ADA
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedADA(currs=["ADA"]):
    return get_rates_concurrent(currs)
    
# FTM
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedFTM(currs=["FTM"]):
    return get_rates_concurrent(currs)
    
# SOL
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedSOL(currs=["SOL"]):
    return get_rates_concurrent(currs)
    
# XRP
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedXRP(currs=["XRP"]):
    return get_rates_concurrent(currs)
    
# XTZ
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedXTZ(currs=["XTZ"]):
    return get_rates_concurrent(currs)
    
# OMG
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedOMG(currs=["OMG"]):
    return get_rates_concurrent(currs)
    
# LUNA
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedLUNA(currs=["LUNA"]):
    return get_rates_concurrent(currs)
    
# MANA
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedMANA(currs=["MANA"]):
    return get_rates_concurrent(currs)
    
# LINK
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedLINK(currs=["LINK"]):
    return get_rates_concurrent(currs)
    
# KSM
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedKSM(currs=["KSM"]):
    return get_rates_concurrent(currs)
    
# DOGE
@cachetools.func.ttl_cache(maxsize=20, ttl=5)
def get_rates_cachedDOGE(currs=["DOGE"]):
    return get_rates_concurrent(currs)
    

def get_rates_concurrent(currs=["BTC", "ETH", "ATOM", "ADA", "FTM", "SOL", "XRP", "XTZ", "OMG", "LUNA", "MANA", "LINK", "KSM", "DOGE"]):
    executor = ThreadPoolExecutor(max_workers=4)
    if isinstance(currs, str):
        currency_pairs = currs + USD
    else:
        currency_pairs = [currency + USD for currency in currs]
    result = zip(currency_pairs, executor.map(make_request, currency_pairs))
    return dict(result)


def get_rates(currs=["BTC", "ETH", "ATOM", "ADA", "FTM", "SOL", "XRP", "XTZ", "OMG", "LUNA", "MANA", "LINK", "KSM", "DOGE"]):
    currency_pairs = [currency + USD for currency in currs]
    results = [{symbol: make_request(symbol)} for symbol in currency_pairs]
    return results


def make_request(symbol):
    try:
        params = {"symbol": symbol}
        r = requests.get(url=URL+API_TYPES["price"], params=params)
        return json.loads(r.content)["price"]
    except:
        return None
