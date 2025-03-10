import csv
import pandas as pd
from datetime import datetime

LOG_FILE = "logs/trades_log.csv"

# Function to log trade data
def log_trade(trade_data):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            trade_data.get("symbol"),
            trade_data.get("qty"),
            trade_data.get("side"),
            trade_data.get("filled_avg_price"),
            trade_data.get("status"),
        ])

# Example Usage
if __name__ == "__main__":
    trade_example = {
        "symbol": "AAPL",
        "qty": 1,
        "side": "buy",
        "filled_avg_price": 145.5,
        "status": "filled"
    }
    log_trade(trade_example)
def analyze_performance():
    df = pd.read_csv(LOG_FILE)
    win_rate = len(df[df["profit_loss"] > 0]) / len(df) * 100
    avg_profit = df["profit_loss"].mean()
    max_loss = df["profit_loss"].min()
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Average Profit Per Trade: {avg_profit:.2f}")
    print(f"Max Loss: {max_loss:.2f}")

if __name__ == "__main__":
    analyze_performance()

def log_trade(symbol, qty, side, price, status):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), symbol, qty, side, price, status])
    print(f"Trade logged: {symbol} - {side} {qty} @ {price}")

# Example Usage
log_trade("AAPL", 5, "buy", 150.50, "executed")
