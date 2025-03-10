import sqlite3

from scripts.trade_execution import place_order

MAX_DRAWDOWN = 10  # Stop trading if we lose $10

def check_drawdown():
    conn = sqlite3.connect('trading_bot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(profit_loss) FROM trade_log WHERE date >= DATE('now', '-1 day')")
    total_loss = cursor.fetchone()[0] or 0
    conn.close()

    return total_loss <= -MAX_DRAWDOWN  # Stop trading if losses exceed max drawdown

if __name__ == "__main__":
    if check_drawdown():
        print("Max drawdown reached! Stopping trading for today.")
def fail_safe_check():
    if check_drawdown():  # Stop trading if max drawdown is hit
        print("🚨 Max drawdown reached! Stopping all trades.")
        return True
    return False
if not fail_safe_check():
    place_order("AAPL", 5, "buy")
