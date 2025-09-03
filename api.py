"""FastAPI endpoints for the trading bot."""

from __future__ import annotations

from fastapi import FastAPI

from config import USE_TESTNET
from exchange import fetch_ohlcv, market_order
from strategy import analyze

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Auto trader bot"}


@app.get("/status")
def status():
    return {"status": "ok", "testnet": USE_TESTNET}


@app.get("/prices")
def prices(symbol: str = "BTC/USDT:USDT", tf: str = "1m", limit: int = 200):
    data = fetch_ohlcv(symbol, tf, limit)
    return {"symbol": symbol, "prices": data}


@app.get("/analysis")
def analysis(symbol: str = "BTC/USDT:USDT", tf: str = "1m", limit: int = 200):
    data = fetch_ohlcv(symbol, tf, limit)
    return analyze(data)


@app.post("/trade")
def trade(
    symbol: str = "BTC/USDT:USDT",
    side: str = "buy",
    amount: float = 0.001,
    mode: str = "paper",
):
    if mode == "live":
        return market_order(symbol, side, amount)
    return {
        "status": "paper",
        "symbol": symbol,
        "side": side,
        "amount": amount,
    }
