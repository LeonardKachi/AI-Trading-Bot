import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to get financial news sentiment
def get_news_sentiment(keyword="forex"):
    NEWS_API_KEY = "your_newsapi_key"
    url = f"https://newsapi.org/v2/everything?q={keyword}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    
    articles = response.get("articles", [])
    sentiments = []

    for article in articles[:5]:  # Analyze top 5 articles
        title = article["title"]
        sentiment = sia.polarity_scores(title)["compound"]  # Get sentiment score
        sentiments.append((title, sentiment))
    
    return sentiments

# Example Usage
if __name__ == "__main__":
    news_sentiments = get_news_sentiment()
    for title, sentiment in news_sentiments:
        print(f"{title} --> Sentiment Score: {sentiment}")
