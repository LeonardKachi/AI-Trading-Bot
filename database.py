import sqlite3
import pandas as pd
import os
import requests

# Database and file paths
DB_NAME = "data/trading_bot.db"
CSV_FILE = "data/AAPL_data.csv"

# Function to save data to SQLite
def save_to_db(data, table_name):
    with sqlite3.connect(DB_NAME) as conn:
        data.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Data saved to {table_name} in {DB_NAME}")

# Function to fetch forex rates
def get_forex_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")  # Debugging line
    print(f"Response Text: {response.text}")  # Debugging line
    
    if response.status_code == 200:
        try:
            decoded_data = response.json()
            return decoded_data['rates'].get(target_currency, "Currency not found")
        except requests.exceptions.JSONDecodeError:
            print("Error: Unable to decode JSON response")
            return None
    else:
        print("Error: API request failed")
        return None

# Main execution
if __name__ == "__main__":
    # Load CSV data if available
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        print("CSV loaded successfully")
        save_to_db(df, "apple_stock")
    else:
        print(f"Error: File '{CSV_FILE}' not found. Please check the path or generate the data.")
    
    # Fetch and display forex rate
    forex_rate = get_forex_rate("USD", "EUR")
    print(f"Forex Rate (USD to EUR): {forex_rate}")


# Function to save real-time data to database
def save_real_time_data(data, table_name):
    conn = sqlite3.connect(DB_NAME)
    data.to_sql(table_name, conn, if_exists="append", index=False)
    conn.close()

# Example Usage
if __name__ == "__main__":
    df = pd.DataFrame({"symbol": ["AAPL"], "price": [170.50], "timestamp": [pd.Timestamp.now()]})
    save_real_time_data(df, "real_time_prices")
