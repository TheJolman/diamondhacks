import requests
import dotenv
import os
import json
DURATION = 86400
#Returns name of the cached data, if it exists and was created within the duration above. else, returns null.
def get_stock_data_cache(ticker, date):
    cache_name = f"Cache_{ticker}_{date}"
    if os.path.exists(cache_name):
        age = time.time()-os.path.getmtime(cache_name)
        if age>DURATION:
            return None
        with open(cache_name) as cache:
            out = json.load(cache)
        return out
    else:
        return None
def set_stock_data_cache(ticker, date, data):
    cache_name = f"Cache_{ticker}_{date}"
    with open(cache_name, "w") as cache:
        cache.write(data)
    return
    
def set_april_2nd_cache(ticker, data):
    cache_name = f"Cache_{ticker}_Tariff_Day"
    with open(cache_name, "w") as cache:
        cache.write(data)
def get_april_2nd_cache(ticker):
    cache_name = f"Cache_{ticker}_Tariff_Day"
    if os.path.exists(cache_name):
        with open(cache_name) as cache:
            out = json.load(cache)
        return out
        
    else:
        return None
        
