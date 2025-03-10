import joblib
import pandas as pd
from news_sentiment import get_news_sentiment

# Load AI model and scaler
model = joblib.load("models/trade_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Load new market data
df = pd.read_csv("data/AAPL_features.csv").dropna()
X_live = scaler.transform(df[['MA14', 'RSI', 'MACD', 'Signal_Line']].iloc[-1:].values)

# Predict trading signal (1=Buy, -1=Sell)
signal = model.predict(X_live)[0]

# Get latest sentiment score
news_sentiments = get_news_sentiment()
average_sentiment = sum(score for _, score in news_sentiments) / len(news_sentiments)

# Define trading action
if signal == 1 and average_sentiment > 0.1:
    action = "BUY"
elif signal == -1 and average_sentiment < -0.1:
    action = "SELL"
else:
    action = "HOLD"

print(f"Trading Decision: {action}")
