import alpaca_trade_api as tradeapi

# API Keys (Replace with your own)
API_KEY = "AKJVT03UL4EDGS0UP5D3"
API_SECRET = "EQ6j23fn1MR6T3APeTwyUfhlEf8owpllUDsCfSUk"
BASE_URL = "https://paper-api.alpaca.markets"  # Paper trading URL

# Connect to Alpaca
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version="v2")

def place_order(symbol, qty, side, order_type="market"):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=order_type,
            time_in_force="gtc"  # Good till canceled
        )
        print(f"Order Placed: {order}")
    except Exception as e:
        print(f"Error placing order: {e}")

# Example Usage
place_order("AAPL", 5, "buy")  # Buy 5 Apple stocks
def check_order_status(order_id):
    try:
        order = api.get_order(order_id)
        print(f"Order Status: {order.status}")
        return order.status
    except tradeapi.rest.APIError as e:
        print(f"API Error: {e}")
    except ConnectionError:
        print("Network Issue: Retrying...")
    except Exception as e:
        print(f"Error fetching order status: {e}")
        return None
