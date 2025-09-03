"""Simple wrapper around ccxt's Binance USD-M futures exchange."""

from __future__ import annotations

import ccxt

from config import BINANCE_KEY, BINANCE_SECRET, USE_TESTNET

_exchange = ccxt.binanceusdm(
    {
        "apiKey": BINANCE_KEY,
        "secret": BINANCE_SECRET,
        "enableRateLimit": True,
    }
)

if USE_TESTNET:
    _exchange.set_sandbox_mode(True)


def fetch_ohlcv(symbol: str = "BTC/USDT:USDT", tf: str = "1m", limit: int = 200):
    """Fetch historical OHLCV data."""
    return _exchange.fetch_ohlcv(symbol, timeframe=tf, limit=limit)


def market_order(symbol: str, side: str, amount: float):
    """Place a market order (stub for now)."""
    print(f"[STUB] market_order: {side} {amount} {symbol}")
    return {"status": "paper"}
