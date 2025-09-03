"""Trading strategy calculations."""

from __future__ import annotations

import pandas as pd
import ta


def analyze(ohlcv):
    """Analyze OHLCV data and generate trading signals."""
    df = pd.DataFrame(
        ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )
    df["ma20"] = df["close"].rolling(window=20).mean()
    df["ma50"] = df["close"].rolling(window=50).mean()
    df["rsi"] = ta.momentum.rsi(df["close"], window=14)

    latest = df.iloc[-1]
    signal = "HOLD"
    score = 0
    if latest["ma20"] > latest["ma50"] and latest["rsi"] < 70:
        signal = "BUY"
        score = 1
    elif latest["ma20"] < latest["ma50"] and latest["rsi"] > 30:
        signal = "SELL"
        score = -1

    return {
        "signal": signal,
        "ma20": float(latest["ma20"]),
        "ma50": float(latest["ma50"]),
        "rsi": float(latest["rsi"]),
        "score": score,
    }
