import requests
import json
import yfinance as yf
import ta
import pandas as pd
from config import config  # Import API keys

# Alpaca API Endpoints
HEADERS = {
    "APCA-API-KEY-ID": config.API_KEY,
    "APCA-API-SECRET-KEY": config.API_SECRET
}

# Function to place an order
def place_order(symbol, qty, side, stop_loss=None, take_profit=None):
    url = f"{config.BASE_URL}/v2/orders"
    
    order = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": "market",
        "time_in_force": "gtc"
    }
    
    if stop_loss or take_profit:
        order["order_class"] = "bracket"  # Bracket order with stop-loss & take-profit
        if stop_loss:
            order["stop_loss"] = {"stop_price": stop_loss}
        if take_profit:
            order["take_profit"] = {"limit_price": take_profit}
    
    response = requests.post(url, json=order, headers=HEADERS)
    return response.json()

# Function to calculate position size based on risk management
def calculate_position_size(account_balance, risk_percentage, entry_price, stop_loss_price):
    risk_amount = account_balance * (risk_percentage / 100)
    position_size = risk_amount / abs(entry_price - stop_loss_price)
    return round(position_size, 2)

# Function to calculate ATR-based stop loss
def calculate_atr_stop_loss(symbol, period="30d", interval="1d", multiplier=1.5):
    data = yf.download(symbol, period=period, interval=interval)
    data["ATR"] = ta.volatility.AverageTrueRange(high=data["High"], low=data["Low"], close=data["Close"]).average_true_range()
    return data["Close"].iloc[-1] - (data["ATR"].iloc[-1] * multiplier)

# Example Usage
if __name__ == "__main__":
    # Define trading parameters
    stock_symbol = "AAPL"
    account_balance = 5000  # $5000 Trading Account
    risk_percentage = 2  # Risk 2% per trade
    entry_price = 150  # Example stock price
    stop_loss_price = calculate_atr_stop_loss(stock_symbol)
    
    # Calculate position size
    position_size = calculate_position_size(account_balance, risk_percentage, entry_price, stop_loss_price)
    print(f"Position Size: {position_size} shares")
    
    # Place an order
    trade = place_order(stock_symbol, position_size, "buy", stop_loss=stop_loss_price, take_profit=150)
    print(trade)