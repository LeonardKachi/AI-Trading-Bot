import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load historical data
df = pd.read_csv("data/AAPL_features.csv").dropna()

# Define Features (Technical Indicators) & Target (Buy/Sell)
features = ["RSI", "MACD", "SMA_20", "SMA_50", "Volume"]
df["Target"] = np.where(df["Close"].shift(-1) > df["Close"], 1, -1)  # Buy if price increases, else sell

# Split Data for Training & Testing
X = df[features]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Scale Features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# AI Predictions
df["Prediction"] = model.predict(scaler.transform(X[features]))

# Initialize Trading Simulation
initial_balance = 10000
balance = initial_balance
position = 0
trade_log = []
risk_per_trade = 0.02  # Risk 2% per trade

# Trading Simulation Loop
for i in range(len(df) - 1):
    signal = df["Prediction"].iloc[i]  # AI Prediction (1 = Buy, -1 = Sell)
    price = df["Close"].iloc[i]

    stop_loss = price * 0.98  # 2% Stop-Loss
    take_profit = price * 1.02  # 2% Take-Profit

    trade_size = (balance * risk_per_trade) / (price - stop_loss)

    if signal == 1 and balance >= trade_size * price:  # Buy
        position = trade_size
        balance -= trade_size * price
        trade_log.append({"Type": "BUY", "Price": price, "Balance": balance})

    elif signal == -1 and position > 0:  # Sell
        balance += position * price
        trade_log.append({"Type": "SELL", "Price": price, "Balance": balance})
        position = 0

# Final Balance & ROI Calculation
final_balance = balance + (position * df["Close"].iloc[-1])
roi = ((final_balance - initial_balance) / initial_balance) * 100

print(f"Final Balance: ${final_balance:.2f}")
print(f"ROI: {roi:.2f}%")

# Convert Trade Log to DataFrame
trade_df = pd.DataFrame(trade_log)

# Plot Balance Over Time
plt.plot(trade_df.index, trade_df["Balance"], label="Balance Over Time", color="blue")
plt.xlabel("Trade Number")
plt.ylabel("Balance ($)")
plt.title("AI-Powered Trading Simulation Performance")
plt.legend()
plt.show()

