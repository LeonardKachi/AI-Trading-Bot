import yfinance as yf
import ccxt
from forex_python.converter import CurrencyRates
import pandas as pd

def get_stock_data(symbol, start="2020-01-01", end="2024-01-01"):
    data = yf.download(symbol, start=start, end=end, interval="1d")
    data.to_csv(f"data/{symbol}_data.csv")  # Save to CSV
    return data

def get_forex_rate(base_currency, target_currency):
    c = CurrencyRates()
    rate = c.get_rate(base_currency, target_currency)
    return rate

def get_crypto_data(symbol="BTC/USDT"):
    binance = ccxt.binance()
    ohlcv = binance.fetch_ohlcv(symbol, timeframe='1d', limit=100)
    return ohlcv

# Example Usage
if __name__ == "__main__":
    print(get_stock_data("AAPL"))
    print(get_forex_rate("USD", "EUR"))
    print(get_crypto_data())
