import requests
import json
import time
from config import config  # Import API keys

# Alpaca API Headers
HEADERS = {
    "APCA-API-KEY-ID": config.API_KEY,
    "APCA-API-SECRET-KEY": config.API_SECRET
}

# Function to fetch open positions with optional symbol filtering and retry logic
def get_open_positions(symbol=None, retries=3, delay=3):
    url = f"{config.BASE_URL}/v2/positions"

    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

            positions = response.json()

            if not positions:
                print("✅ No open positions found.")
                return []

            # Filter by symbol if specified
            if symbol:
                positions = [pos for pos in positions if pos["symbol"].upper() == symbol.upper()]

                if not positions:
                    print(f"⚠️ No open positions for {symbol}.")
                    return []

            return positions

        except requests.exceptions.RequestException as e:
            print(f"❌ Attempt {attempt+1} failed: {e}")

            if attempt < retries - 1:
                print(f"🔄 Retrying in {delay} seconds...")
                time.sleep(delay)

    print("⛔ Failed to fetch open positions after multiple attempts.")
    return []

# Example Usage
if __name__ == "__main__":
    positions = get_open_positions()  # Get all open positions

    if positions:
        print(json.dumps(positions, indent=4))  # Pretty-print positions

    # Example: Get open positions for a specific stock (e.g., "AAPL")
    apple_positions = get_open_positions(symbol="AAPL")

    if apple_positions:
        print("\n📊 Open Positions for AAPL:")
        print(json.dumps(apple_positions, indent=4))

