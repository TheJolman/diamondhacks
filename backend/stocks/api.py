import requests
import dotenv
import os


def get_stock_data():

    dotenv.load_dotenv()
    POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY")
    url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={POLYGON_API_KEY}"

    r = requests.get(url)
    data = r.json()

    return data
