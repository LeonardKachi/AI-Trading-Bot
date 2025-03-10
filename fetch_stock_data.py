import yfinance as yf

# Download Apple stock data
df = yf.download("AAPL", start="2024-01-01", end="2025-01-01")

# Save to CSV
df.to_csv("data/AAPL_data.csv")
print("AAPL stock data saved successfully!")
