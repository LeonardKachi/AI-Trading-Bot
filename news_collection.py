import requests
import json

API_KEY = "e5ac0e90848c42408ec9b9541015e905"

def get_financial_news(keyword="forex"):
    url = f"https://newsapi.org/v2/everything?q={keyword}&language=en&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if response status is not 200
        data = response.json()

        # Debugging: Print response structure
        print("API Response:", json.dumps(data, indent=2))

        if "articles" in data:
            return data["articles"]
        else:
            print("Warning: 'articles' key not found in response")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

# Example Usage
if __name__ == "__main__":
    news = get_financial_news()
    print(json.dumps(news[:5], indent=2))  # Print first 5 articles
