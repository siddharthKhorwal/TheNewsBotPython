News and Stock Market Twitter Bot
This project is a Twitter bot designed to tweet top news headlines and stock market updates at scheduled intervals. It fetches news articles from various sources and tweets them along with the relevant stock market information. Additionally, it can analyze the sentiment of news headlines and visualize the stock performance over time.

Getting Started,
To use this bot, follow these steps:

Prerequisites-

    Python 3.x
    Required Python packages (install via pip install -r requirements.txt):
    yfinance
    tweepy
    newspaper3k
    beautifulsoup4
    textblob
    instagrapi
    schedule
    matplotlib

Installation-

Clone this repository to your local machine:

    git clone https://github.com/your_username/news-twitter-bot.git

2.Navigate To The Project Directory

    cd news-twitter-bot

3.Install the required packages:

    pip install -r requirements.txt


Configuration-
    Create a file named api_keys.txt in the project directory.
    Add your API keys for Twitter and any other services required by the bot in the following format:


    # API credentials for Twitter
    YOUR_API_KEY
    YOUR_API_SECRET
    YOUR_ACCESS_TOKEN
    YOUR_ACCESS_TOKEN_SECRET
    YOUR_BEARER_TOKEN
    instagram username
    instagram pass
    your https://www.marketaux.com/ api key

Usage-
    To start the bot, run the following command:

    python main.py
Features-

    Tweets top news headlines from various sources.
    Fetches stock market updates and tweets them at scheduled intervals.
    Analyzes the sentiment of news headlines and tweets the sentiment along with the headline.
    Visualizes stock performance over time.

Example-
    Check out the Twitter bot in action: TheNews_Bot

Authors-
    Siddharth Khorwal
License-
    This project is licensed under the MIT License.

Acknowledgments-
    Thanks to Newspaper3k for providing a simple and fast way to extract articles from websites.
    Special thanks to yfinance for providing easy access to historical market data from Yahoo Finance.
