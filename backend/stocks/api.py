import requests
import dotenv
import os
import time
import datetime
import asyncio

dotenv.load_dotenv()
POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY")

async def get_stock_data(ticker: str | None = None,
                   ticker_type: str | None = None,
                   market: str = "stocks",
                   date: str | None = None,
                   exchange: str | None = None
                   ):

    base_url = "https://api.polygon.io/v3/reference/tickers"

    params = {
        "market": market,
        "active": "true",
        "order": "asc",
        "limit": 100,
        "sort": "ticker",
        "apiKey": POLYGON_API_KEY
    }

    if ticker:
        params["ticker"] = ticker
    if ticker_type:
        params["type"] = ticker_type
    if date:
        params["date"] = date
    if exchange:
        params["exchange"] = exchange

    try:
        r = requests.get(base_url, params=params)
        r.raise_for_status()
        data = r.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API Request failed {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response text: {e.response.text}")
        return None
    except requests.exceptions.JSONDecodeError as e:
        print(f"Response body does not contain valid JSON: {e}")
        print(f"Raw response text: {r.text}")
        return None


april_2nd_str = datetime.date(2024, 4, 2).strftime("%Y-%m-%d")
today_str = datetime.date.today().strftime("%Y-%m-%d")

async def two_gets(ticker: str | None = None,
                   ticker_type: str | None = None,
                   market: str = "stocks",
                   exchange: str | None = None):


    apr2_task = asyncio.create_task(
        get_stock_data(ticker, ticker_type, market, april_2nd_str, exchange)
    )
    today_task = asyncio.create_task(
        get_stock_data(ticker, ticker_type, market, today_str, exchange)
    )

    apr2_result = await get_stock_apr2
    today_result = await get_stock_now

    return {
        "april_2nd_data": apr2_result,
        "today_data": today_result,
        "comparison": {
            "ticker": ticker,
            "date_comparison": [april_2nd_str, today_str]
        }
    }
