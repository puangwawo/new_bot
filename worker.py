import time
from typing import Any, Dict, List

import requests

BASE_URL = "http://localhost:8000"
SYMBOLS: List[str] = [
    "BTC/USDT:USDT",
    "XRP/USDT:USDT",
    "DOGE/USDT:USDT",
    "TRUMP/USDT:USDT",
]


def fetch_analysis(symbol: str) -> Dict[str, Any] | None:
    """Fetch market analysis for a symbol.

    Returns None if the request fails.
    """
    try:
        resp = requests.get(f"{BASE_URL}/analysis", params={"symbol": symbol}, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:  # pragma: no cover - network errors
        print(f"analysis error for {symbol}: {exc}")
        return None


def post(path: str, data: Dict[str, Any]) -> None:
    """Send a JSON POST request and ignore failures."""
    try:
        requests.post(f"{BASE_URL}{path}", json=data, timeout=10)
    except Exception as exc:  # pragma: no cover - network errors
        print(f"post {path} failed: {exc}")


def process_symbol(symbol: str) -> None:
    analysis = fetch_analysis(symbol)
    if not analysis:
        return

    signal = (
        analysis.get("signal")
        or analysis.get("summary", {}).get("RECOMMENDATION")
        or analysis.get("recommendation")
    )
    price = analysis.get("price") or analysis.get("last_price") or analysis.get("close")

    if signal in {"BUY", "SELL"} and price is not None:
        post("/signals", {"symbol": symbol, "signal": signal, "price": price})
        post(
            "/trade",
            {"symbol": symbol, "side": signal, "price": price, "mode": "paper"},
        )


def main() -> None:
    while True:
        for symbol in SYMBOLS:
            process_symbol(symbol)
        time.sleep(5)


if __name__ == "__main__":
    main()
