# Auto Trader Bot MVP

Kerangka awal bot auto-trader menggunakan FastAPI dan ccxt.

## Setup

1. Salin file `.env.example` menjadi `.env` dan isi `BINANCE_KEY` dan `BINANCE_SECRET` jika diperlukan.
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan API secara lokal pada port 8000:
   ```bash
   uvicorn api:app --reload --port 8000
   ```
4. Jalankan worker (mode paper):
   ```bash
   python worker.py
   ```

Secara default bot berjalan di testnet (`USE_TESTNET=true`).
