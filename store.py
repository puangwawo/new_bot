from collections import deque

_signals = deque(maxlen=500)
_trades = deque(maxlen=500)


def add_signal(symbol: str, side: str, price: float, ts: float) -> None:
    """Store a signal in memory."""
    _signals.append({
        "symbol": symbol,
        "side": side,
        "price": price,
        "ts": ts,
    })


def list_signals():
    """Return list of stored signals."""
    return list(_signals)


def add_trade(symbol: str, side: str, price: float, ts: float) -> None:
    """Store a trade in memory."""
    _trades.append({
        "symbol": symbol,
        "side": side,
        "price": price,
        "ts": ts,
    })


def list_trades():
    """Return list of stored trades."""
    return list(_trades)
