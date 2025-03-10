import requests
import time

# NewsAPI Key (Replace with your own)
NEWS_API_KEY = "e5ac0e90848c42408ec9b9541015e905"

# Function to get latest financial news
def get_latest_news(keyword="forex"):
    url = f"https://newsapi.org/v2/everything?q={keyword}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    return articles[:5]  # Return top 5 articles

# Function to continuously monitor news
def monitor_news():
    while True:
        news = get_latest_news()
        print("📰 Latest Financial News:")
        for article in news:
            print(f"- {article['title']} ({article['source']['name']})")
        print("-" * 40)

        time.sleep(1800)  # Refresh every 30 minutes

# Run the news monitoring function
if __name__ == "__main__":
    monitor_news()
