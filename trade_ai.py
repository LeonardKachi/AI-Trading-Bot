import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("data/AAPL_features.csv")

# Define the target variable (1 = Buy, 0 = Hold, -1 = Sell)
df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, -1)

# Select features
features = ['MA14', 'RSI', 'MACD', 'Signal_Line']
X = df[features].dropna()
y = df['Target'].loc[X.index]  # Align target with features

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model
import joblib
joblib.dump(model, "models/trade_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
