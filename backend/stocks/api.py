import requests
import dotenv
import os
import time
from datetime import date, timedelta
import asyncio

dotenv.load_dotenv()
POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY")

async def get_stock_data(stocksTicker: str, date: str):

    base_url = f"https://api.polygon.io/v1/open-close/{stocksTicker}/{date}"

    params = {
        "adjusted": "true",
        "apiKey": POLYGON_API_KEY
    }

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

april_2nd_str = date(2025, 4, 2).strftime("%Y-%m-%d")
yesterday_str = (date.today() - timedelta(days=2)).strftime("%Y-%m-%d")

async def two_gets(stocksTicker: str):

    april_2nd_task = asyncio.create_task(
        get_stock_data(stocksTicker, april_2nd_str)
    )
    yesterday_task = asyncio.create_task(
        get_stock_data(stocksTicker, yesterday_str)
    )

    april_2nd_result = await april_2nd_task
    yesterday_result = await yesterday_task

    if april_2nd_result and yesterday_result:
        april_2nd_avg = (april_2nd_result["high"] + april_2nd_result["low"]) / 2
        yesterday_avg = (yesterday_result["high"] + yesterday_result["low"]) / 2
        return {
            "april_2nd_price": april_2nd_avg,
            "yesterday_price": yesterday_avg,
            "date_comparison": [april_2nd_str, yesterday_str]
        }
    else:
        return None
