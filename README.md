# AI Trading Bot

An AI-powered trading bot that combines news sentiment analysis with machine learning to make smart trading decisions in real time.

---

## Features

- **Real-Time News Analysis**: Fetches and analyzes current news articles to assess market sentiment.
- **Sentiment Evaluation**: Uses NLP techniques to determine positive or negative bias in financial headlines.
- **Machine Learning Predictions**: Predicts market trends based on historical data and sentiment.
- **Automated Trading**: Executes trades based on insights from trained models and strategy rules.
- **Risk Management**: Implements stop-loss and take-profit conditions to minimize risks.
- **Backtesting**: Allows users to simulate trading strategies on historical data.

---

## How It Works

1. **Collect**: Historical stock data + real-time news
2. **Analyze**: Sentiment scoring using NLP
3. **Predict**: Forecast future movements using ML models
4. **Trade**: Execute buy/sell orders based on insights
5. **Evaluate**: Monitor performance and manage risks

---

## 🛠️ Installation

```bash
git clone https://github.com/LeonardKachi/AI-Trading-Bot.git
cd AI-Trading-Bot
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Configuration

1. Open `config.py`
2. Add your **API keys**, model paths, and trading parameters
3. Save and start using the bot

---

## Usage

* **Backtesting**

```bash
python backtest.py
```

* **Live Trading**

```bash
python trade_ai.py
```

* **News Monitoring**

```bash
python news_monitor.py
```

---

## Project Structure

* `data_collection.py`: Pulls data from financial and news APIs
* `news_sentiment.py`: Classifies news headlines into sentiment scores
* `feature_engineering.py`: Cleans and transforms data for modeling
* `trade_ai.py`: Main trading logic with ML integration
* `backtest.py`: Strategy simulation on past data
* `config.py`: Project settings, API keys, and thresholds

---

## Requirements

* Python 3.7+
* `pandas`, `numpy`, `scikit-learn`, `nltk`, `requests`, `beautifulsoup4`, `matplotlib`, `yfinance`

---

## Disclaimer

> This bot is for **educational purposes** only.
> Use it at your own risk — the author is not responsible for any financial losses.

---

## License

This project is licensed under the **Unlicense** – free for personal or commercial use. No restrictions.

---

*Made by [LeonardKachi](https://github.com/LeonardKachi)*

```
