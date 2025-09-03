"""Background worker that periodically analyzes the market."""

from __future__ import annotations

import time

from exchange import fetch_ohlcv
from strategy import analyze


def run():
    while True:
        data = fetch_ohlcv()
        result = analyze(data)
        print(result)
        time.sleep(5)


if __name__ == "__main__":
    run()
