import requests
import dotenv
import os
import time
import datetime
import asyncio

dotenv.load_dotenv()
POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY")

april_2nd_str = datetime.date(2025, 4, 2).strftime("%Y-%m-%d")
today_str = datetime.date.today().strftime("%Y-%m-%d")

async def get_stock_data(stocksTicker: str, date: str | None = None):

    if not date:
        date = today_str

    base_url = f"https://api.polygon.io/v1/open-close/{stocksTicker}/{date}"

    params = {
        "adjusted": True,
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

async def two_gets(stocksTicker: str):

    april_2nd_task = asyncio.create_task(
        get_stock_data(stocksTicker, april_2nd_str)
    )
    today_task = asyncio.create_task(
        get_stock_data(stocksTicker, today_str)
    )

    april_2nd_result = await april_2nd_task
    today_result = await today_task

    return {
        "april_2nd_data": april_2nd_result,
        "today_data": today_result,
        "comparison": {
            "ticker": stocksTicker,
            "date_comparison": [april_2nd_str, today_str]
        }
    }
