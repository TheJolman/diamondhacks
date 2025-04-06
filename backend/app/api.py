from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import stocks as s

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["root"])
async def read_root(ticker: str = "IBM"):
    stock_data = s.get_stock_data(ticker=ticker)
    if stock_data:
        return stock_data
    else:
        return "Error getting stock data"

@app.get("/compare", tags=["comparison"])
async def compare_stocks(ticker: str = "IBM"):
    result = await s.two_gets(ticker=ticker)
    if result and result["apr_2nd_data"] and result["today_data"]:
        return result
    else:
        return {"error": "Error retrieving comparison data"}
