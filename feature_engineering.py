import pandas as pd
import numpy as np

# Function to calculate moving averages
def moving_average(data, window=14):
    return data['Close'].rolling(window=window).mean()

# Function to calculate RSI (Relative Strength Index)
def rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Function to calculate MACD (Moving Average Convergence Divergence)
def macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()
    return macd_line, signal_line

# Function to extract all indicators
def extract_features(data):
    data['MA14'] = moving_average(data, 14)
    data['RSI'] = rsi(data, 14)
    data['MACD'], data['Signal_Line'] = macd(data)
    return data

# Example Usage
if __name__ == "__main__":
    df = pd.read_csv("data/AAPL_data.csv")
    df = extract_features(df)
    df.to_csv("data/AAPL_features.csv", index=False)
    print(df.head())
