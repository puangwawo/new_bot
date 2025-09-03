from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

import store

app = FastAPI()

# Allow all CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount frontend static files
app.mount("/ui", StaticFiles(directory="frontend", html=True), name="ui")


class Signal(BaseModel):
    symbol: str
    side: str
    price: float
    ts: float


class TradeRequest(Signal):
    mode: str = "paper"


@app.get("/signals")
def get_signals():
    return store.list_signals()


@app.post("/signals")
def post_signal(signal: Signal):
    store.add_signal(signal.symbol, signal.side, signal.price, signal.ts)
    return {"status": "ok"}


@app.get("/trades")
def get_trades():
    return store.list_trades()


@app.post("/trade")
def trade(trade: TradeRequest, background_tasks: BackgroundTasks):
    data = trade.dict()
    mode = data.pop("mode", "paper")
    if mode == "paper":
        background_tasks.add_task(
            store.add_trade,
            data["symbol"],
            data["side"],
            data["price"],
            data["ts"],
        )
        return {"status": "paper trade", **data}
    else:
        # Placeholder for live trading via exchange
        # exchange.place_order(data)
        return {"status": "live trade executed", **data}


@app.get("/status")
def status():
    try:
        api_key_present = bool(os.environ["API_KEY"])
    except KeyError:
        api_key_present = False
    return {"api_key": api_key_present}
