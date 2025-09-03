"""Application configuration loaded from environment variables."""

from __future__ import annotations

import os
from dotenv import load_dotenv

load_dotenv()

USE_TESTNET: bool = os.getenv("USE_TESTNET", "true").lower() == "true"
BINANCE_KEY: str | None = os.getenv("BINANCE_KEY")
BINANCE_SECRET: str | None = os.getenv("BINANCE_SECRET")
