import socket
print(socket.gethostbyname('api.binance.com'))
import yfinance as yf
import ccxt
import requests
import time

# Alpha Vantage API Key (Replace with your own)
ALPHA_VANTAGE_API_KEY = "IIDBT6U8XL0T2MTP"

# Function to get real-time stock price
def get_real_time_stock_price(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    return data['Close'].iloc[-1]  # Get the latest closing price

# Function to get real-time forex price
def get_real_time_forex_rate(from_currency, to_currency):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url).json()
    return response.get("Realtime Currency Exchange Rate", {}).get("5. Exchange Rate", "N/A")

# Function to get real-time crypto price from Binance
def get_real_time_crypto_price(symbol="BTC/USDT"):
    binance = ccxt.binance()
    ticker = binance.fetch_ticker(symbol)
    return ticker['last']  # Get the latest price

# Function to continuously monitor prices
def monitor_prices():
    stock_symbol = "AAPL"  # Example stock
    forex_pair = ("USD", "EUR")  # Example forex pair
    crypto_symbol = "BTC/USDT"  # Example crypto pair
    
    while True:
        stock_price = get_real_time_stock_price(stock_symbol)
        forex_price = get_real_time_forex_rate(*forex_pair)
        crypto_price = get_real_time_crypto_price(crypto_symbol)

        print(f"📈 {stock_symbol} Stock Price: ${stock_price}")
        print(f"💱 {forex_pair[0]}/{forex_pair[1]} Forex Rate: {forex_price}")
        print(f"🪙 {crypto_symbol} Crypto Price: ${crypto_price}")
        print("-" * 40)

        time.sleep(60)  # Refresh every 60 seconds

# Run the monitoring function
if __name__ == "__main__":
    monitor_prices()

