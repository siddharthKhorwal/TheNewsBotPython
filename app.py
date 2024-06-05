import yfinance as yf
import requests
import tweepy
import datetime
from datetime import datetime, timedelta
import time
import re
import newspaper
from newspaper import Article
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import schedule
import matplotlib.pyplot as plt
import threading
import instagrapi
from instagrapi import Client
import random
from textblob import TextBlob
import logging

#create a file which contains all the api key in this format 
    
    # api credentials of twitter
    #     api_key 
    #     api_secret 
    #     access_token 
    #     access_token_secret 
    #     bearer_token
    #   


    
#Run The command 'pip install -r requirements.txt' 
#make sure the requirements.txt file exists in the current directory as the terminal is opened at


# If You Want To See This Project In Action Vist My Twitter Bot 
# Link - https://x.com/TheNews_Bot

# Read API keys from file
all_keys = open('/path/to/your/api_keys_file', 'r').read().splitlines()

IMP_urls = [
    'https://www.bbc.com/news/topics/ckd09zdlvk2t',
    'https://www.aljazeera.com/where/asia/',
    'https://economictimes.indiatimes.com/news/defence',
    'https://economictimes.indiatimes.com/topic/global-financial-markets',
    'https://www.bbc.com/news/world',
    'https://www.livemint.com/market/stock-market-news',
]

top_100_stocks = [
    'APPLE INC', 'MICROSOFT CORPORATION', 'AMAZON.COM INC',
    'ALPHABET INC (GOOGLE)', 'BERKSHIRE HATHAWAY INC', 'META PLATFORMS INC (FACEBOOK)',
    'TESLA INC', 'NVIDIA CORPORATION', 'TAIWAN SEMICONDUCTOR MANUFACTURING COMPANY',
    'ALIBABA GROUP HOLDING LIMITED', 'SAMSUNG ELECTRONICS CO LTD', 'JOHNSON & JOHNSON',
    'VISA INC', 'WALMART INC', 'JPMORGAN CHASE & CO', 'PROCTER & GAMBLE CO',
    'UNITEDHEALTH GROUP INCORPORATED', 'MASTERCARD INCORPORATED', 'NESTLE S.A.',
    'HOME DEPOT INC', 'KWEICHOW MOUTAI CO LTD', 'LVMH MOËT HENNESSY LOUIS VUITTON SE',
    'ROCHE HOLDING AG', 'ASML HOLDING NV', 'WALT DISNEY COMPANY', 'TENCENT HOLDINGS LTD',
    'ADOBE INC', 'PAYPAL HOLDINGS INC', 'INTEL CORPORATION', 'CISCO SYSTEMS INC',
    'COCA-COLA COMPANY', 'PEPSICO INC', 'SALESFORCE.COM INC', 'ABBOTT LABORATORIES',
    'PFIZER INC', 'MERCK & CO INC', 'CHEVRON CORPORATION', 'RELIANCE INDUSTRIES LIMITED',
    'TOYOTA MOTOR CORPORATION', 'NIKE INC', 'NOVARTIS AG', 'EXXON MOBIL CORPORATION',
    'AT&T INC', 'COMCAST CORPORATION', 'ORACLE CORPORATION', 'QUALCOMM INCORPORATED',
    'UNILEVER PLC', 'SCHNEIDER ELECTRIC SE', 'SIEMENS AG', 'BRISTOL-MYERS SQUIBB COMPANY',
    'HONEYWELL INTERNATIONAL INC', 'ASTRAZENECA PLC', 'SCHLUMBERGER LIMITED', 'MEDTRONIC PLC',
    'SANOFI', 'AMERICAN TOWER CORPORATION', 'IBM (INTERNATIONAL BUSINESS MACHINES CORPORATION)',
    'BROADCOM INC', 'BHP GROUP LIMITED', 'GENERAL ELECTRIC COMPANY', 'ZOETIS INC',
    'SAP SE', 'BAYER AG', '3M COMPANY', 'COSTCO WHOLESALE CORPORATION', 'ACCENTURE PLC',
    'LORÉAL S.A.', 'AIRBUS SE', 'UNION PACIFIC CORPORATION', 'CVS HEALTH CORPORATION',
    'DANAHER CORPORATION', 'HSBC HOLDINGS PLC', 'BLACKROCK INC', 'BOSTON SCIENTIFIC CORPORATION',
    'CHARLES SCHWAB CORPORATION', 'AMGEN INC', 'PHILIP MORRIS INTERNATIONAL INC', 'INTUIT INC',
    'ALTRIA GROUP INC', 'STARBUCKS CORPORATION', 'NETFLIX INC', 'ANHEUSER-BUSCH INBEV SA/NV',
    'PROSUS N.V.', 'ABB LTD', 'DEERE & COMPANY', 'GLAXOSMITHKLINE PLC', 'HDFC BANK LIMITED',
    'HONDA MOTOR CO LTD', 'HITACHI LTD', 'AMERICAN EXPRESS COMPANY', 'GILEAD SCIENCES INC',
    'CITIGROUP INC', 'VINCI SA', 'IBERDROLA SA', 'CHINA CONSTRUCTION BANK CORPORATION',
    'AGRICULTURAL BANK OF CHINA LIMITED', 'BAIDU INC', 'INFOSYS LIMITED', 'TATA CONSULTANCY SERVICES LIMITED',
    'BAJAJ FINANCE LIMITED'
]

ticker_map = {
    'APPLE INC': 'AAPL', 'MICROSOFT CORPORATION': 'MSFT', 'AMAZON.COM INC': 'AMZN',
    'ALPHABET INC (GOOGLE)': 'GOOGL', 'BERKSHIRE HATHAWAY INC': 'BRK-B',
    'META PLATFORMS INC (FACEBOOK)': 'META', 'TESLA INC': 'TSLA', 'NVIDIA CORPORATION': 'NVDA',
    'TAIWAN SEMICONDUCTOR MANUFACTURING COMPANY': 'TSM', 'ALIBABA GROUP HOLDING LIMITED': 'BABA'
}

currency_symbols = {
    'USD': '$', 'EUR': '€', 'JPY': '¥', 'GBP': '£', 'AUD': 'A$', 'CAD': 'C$',
    'CHF': 'CHF', 'CNY': '¥', 'SEK': 'kr', 'NZD': 'NZ$', 'KRW': '₩', 'SGD': 'S$',
    'NOK': 'kr', 'MXN': 'Mex$', 'INR': '₹', 'RUB': '₽', 'ZAR': 'R', 'TRY': '₺',
    'BRL': 'R$', 'HKD': 'HK$', 'ISK': 'kr', 'THB': '฿', 'DKK': 'kr', 'IDR': 'Rp',
    'HUF': 'Ft', 'CZK': 'Kč', 'ILS': '₪', 'CLP': 'CLP$', 'PHP': '₱', 'AED': 'د.إ',
    'COP': 'COL$', 'SAR': '﷼', 'MYR': 'RM', 'RON': 'lei', 'VND': '₫', 'ARS': 'ARS$',
    'NGN': '₦', 'KES': 'Ksh', 'UAH': '₴', 'BDT': '৳', 'PEN': 'S/.', 'DZD': 'د.ج',
    'IQD': 'ع.د', 'MAD': 'د.م.', 'HRK': 'kn', 'CUP': 'CUP$', 'UZS': 'sm', 'GTQ': 'Q',
    'XAU': 'AU$', 'NPR': 'रू', 'ETB': 'Br', 'PYG': '₲', 'LKR': 'Rs', 'TZS': 'TSh',
    'GHS': 'GH₵', 'VEF': 'Bs', 'AFN': '؋', 'RSD': 'дин.', 'BYN': 'Br', 'TWD': 'NT$',
    'UGX': 'USh', 'BOB': 'Bs', 'SDG': 'ج.س.', 'KHR': '៛', 'SYP': '£S', 'JOD': "",
    'BHD': 'BD', 'LBP': 'ل.ل.', 'GTQ': 'Q', 'TTD': 'TT$', 'OMR': 'ر.ع.', 'TZS': 'TSh',
    'MZN': 'MT', 'BND': 'B$', 'XAF': 'FCFA', 'XPF': '₣', 'RWF': 'RF', 'NAD': 'N$',
    'ERN': 'Nfk', 'MWK': 'MK', 'XOF': 'CFA', 'HTG': 'G', 'GMD': 'D', 'KYD': 'CI$',
    'MUR': '₨', 'SBD': 'SI$', 'BWP': 'P', 'MVR': 'ރ.', 'GNF': 'FG', 'MOP': 'MOP$',
    'PGK': 'K', 'MNT': '₮', 'VUV': 'VT', 'LRD': 'L$', 'SZL': 'E', 'DJF': 'Fdj',
    'BTN': 'Nu.', 'GIP': '£G', 'SLL': 'Le', 'CVE': 'Esc', 'TOP': 'T$', 'FKP': '£F',
    'WST': 'WS$', 'SHP': '£', 'TMT': 'T', 'FKP': 'FK£', 'IMP': '£I', 'GGP': '£G',
    'JEP': '£J'
}

phrases_to_remove = [
    'here is why', 'major reasons', 'what is the cause', 'how can i remove these type of ending',
    'details', 'analysis', 'report', 'reasons', 'complete list', 'overview'
]

api_key_news = all_keys[6:7]

def get_exchange_rates(base_currency='USD'):
    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data['rates']
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def currency_conversion(amount, from_currency, to_currency):
    exchange_rates = get_exchange_rates(from_currency)
    if exchange_rates is None:
        return None
    # Convert from 'from_currency' to 'to_currency'
    to_currency_amount = amount * exchange_rates[to_currency]
    return to_currency_amount

def visualize_stock_performance(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['history']['Close'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Performance Over the Last Year')
    plt.legend()
    plt.savefig('stock_performance.png')

def create_api():
    try:
        # Read API keys from file
        api_key = all_keys[0]
        api_secret = all_keys[1]
        access_token = all_keys[2]
        access_token_secret = all_keys[3]
        bearer_token = all_keys[4]

        # Create client
        client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key,
                            consumer_secret=api_secret, access_token=access_token,
                            access_token_secret=access_token_secret)
        return client
    except Exception as e:
        logging.error(f"Some Error Occured {e}")
def tweet(client, message):
    try:
        client.create_tweet(text=message)
        print("Tweeted successfully!")
    except tweepy.TweepyException as e:
        print(f"Error while tweeting: {e}")

def get_website_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Function to clean headlines
def clean_headline(text):
    for phrase in phrases_to_remove:
        text = re.sub(r'\b' + re.escape(phrase) + r'\b', '', text, flags=re.IGNORECASE)
    return text.strip()

def get_top_headlines(url):
    final_tweets = []
    try:
        # Create an Article object
        my_article = Article(url, language="en")
        # Download the article
        my_article.download()
        # Parse the article
        my_article.parse()
        # Extract HTML using BeautifulSoup
        soup = BeautifulSoup(my_article.html, 'html.parser')
        # Extract and clean all h2 and h3 tags
        h2_tags = [clean_headline(tag.text) for tag in soup.find_all('h2')]
        h3_tags = [clean_headline(tag.text) for tag in soup.find_all('h3')]
        # Extract content paragraphs (p tags) and limit to the first 5 paragraphs
        paragraphs = [clean_headline(tag.text) for tag in soup.find_all('p')[:5]]
        # Combine h2 and h3 tags headlines
        headlines = h2_tags + h3_tags
        # List to hold the final tweets
        final_tweets = []
        # Limit to the first 5 headlines and content
        for i in range(min(5, len(headlines))):
            headline = headlines[i].rstrip('.') + "."
            content = paragraphs[i] if i < len(paragraphs) else ""
            # Combine headline and content into a tweet
            tweet = f"{headline} - {content}"
            # Ensure the tweet does not exceed 240 characters
            if len(tweet) > 240:
                # Find the last sentence boundary within the 240-character limit
                sentences = tweet.split('. ')
                short_tweet = ""
                for sentence in sentences:
                    if len(short_tweet) + len(sentence) + 2 <= 240:  # +2 for ". "
                        if short_tweet:
                            short_tweet += ". " + sentence
                        else:
                            short_tweet = sentence
                    else:
                        break
                tweet = short_tweet + "."
            # Append tweet to the final list
            final_tweets.append(tweet)
    except Exception as e:
        print(f"An error occurred: {e}")
    # Print each tweet for verification
    for tweet in final_tweets:
        print(tweet)
        print()
    # Return the list of tweets
    return final_tweets

def StockMarketNewsTweets(stock_name, exchange, currency, ticker):
    try:
        if exchange.upper() == 'NSE':  # Indian National Stock Exchange
            ticker_symbol = f"{ticker}.NS"
        elif exchange.upper() == 'BSE':  # Bombay Stock Exchange
            ticker_symbol = f"{ticker}.BO"
        else:  # Assume US stock exchange
            ticker_symbol = ticker
        data = yf.Ticker(ticker_symbol).history(period="1y", interval="1d")
        currency_symbol = currency_symbols.get(currency.upper())
        stockPrice_open = data.iloc[-1].Open
        client = create_api()
        date_today = datetime.datetime.now().strftime("%d-%m-%Y")
        message = (
            f"#StockMarket Updates\n,{date_today}, {stock_name} Opened At {currency_symbol}{stockPrice_open}"
        )
        tweet(client, message)
    except Exception as e:
        print(f'Some Error Occured {e}')

def Get_latest_news(params, country_name='in'):
    try:
        dateNow = datetime.datetime.now()
        current_datetime_iso = dateNow.strftime("%Y-%m-%dT%H:%M:%S")
        newsApilink = f'https://api.marketaux.com/v1/news/all?countries=in&filter_entities=true&limit=10&published_after={current_datetime_iso}&api_token=nvcRGZU8HGs2V7MovB5zCgHAwzuDcIrOg1Rix5C0'
        response = requests.get(newsApilink)
        if response.status_code == 200:
            news_data = response.json()
            if 'data' in news_data:
                news_articles = news_data['data']
                headlines = []
                for news_item in news_articles:
                    headlines.append(news_item['title'])
                return headlines
            else:
                print("No news data found.")
                return []
        else:
            print(f"Failed to fetch news. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f'Some Error Occured {e}')

def tweet_with_links(client, headlines):
    for i, headline in enumerate(headlines, start=1):
        tweet_message = f'#TopBusinessHeadlines \n {headline}'
        tweet(client, tweet_message)

def tweet_top_headlines():
    try:
        # Sample call to get_stock_data
        # get_stock_data('AAPL', 'US', 'USD')
        # API keys
        #
        # Create client
        # client = create_api()
        # message = "Twitter Bot First Tweet!"
        # tweet(client, message)
        # for stockname in top_100_stocks[:10]:
        #     return stockname
        exchange = 'US'
        currency = 'USD'
        for stockname in top_100_stocks[:10]:
            ticker = ticker_map.get(stockname, None)
            if ticker:
                # StockMarketNewsTweets(stockname,exchange,currency,ticker)
                pass
            else:
                print(f"No ticker symbol found for {stockname}")

        # Get the current date and time
        current_datetime = datetime.now()
        # Subtract one day from the current date
        one_day_before = current_datetime - timedelta(days=1)
        # Format the date and time in ISO 8601 format
        current_datetime_iso = one_day_before.strftime('%Y-%m-%dT%H:%M')
        params_ = {
            'limit': 10,  # Limit number of news articles to retrieve
            'published_after': current_datetime_iso,  # Retrieve news published after this datetime
            'api_token': api_key_news  # Your API token
        }
        news_headlines = Get_latest_news(params_, country_name="in")
        client = create_api()
        while True:
            if news_headlines:
                for i, headline in enumerate(news_headlines, start=1):
                    tweet_message = f'#Top Headlines \n . {headline}'
                    # Tweet each headline
                    tweet(client, tweet_message)
                    time.sleep(3600)  # Add a delay of 60 seconds (1 minute) between tweets
            else:
                print("No news to tweet.")

    except Exception as e:
        logging.error(f"Error in tweet_top_headlines: {e}")

def tweet_headline(client, message):
    tweet(client, message)

def Instabot(client):
    try:
        with open('instagramlogin', 'r') as f:
            username, password = f.read().splitlines()
        client.login(username, password)
        print("Instabot , Login successful!")
        print('slect operation :')
        x = input('Enter : ')
        if x.lower() == 'like':
            hashtag = 'bgmi'
            medias = client.hashtag_medias_recent(hashtag, 5)
            for i, media in enumerate(medias):
                if i % 3 == 0:
                    client.user_follow(media.user.pk)
                    print('Followed!')
    except Exception as e:
        logging.error(f"Error in Instabot: {e}")

def respond_to_mentions():
    try:
        # Create API client
        client = create_api()
        # Retrieve mentions from the user's timeline
        mentions = client.mentions_timeline()
        # Check if any mentions were found
        if mentions:
            print("Mention found!")

    except Exception as e:
        logging.error(f"Error in respond_to_mentions: {e}")

def get_news_with_sentiment(url):
    try:
        headlines = get_top_headlines(url)
        analyzed_headlines = []
        for headline in headlines:
            analysis = TextBlob(headline)
            sentiment = analysis.sentiment.polarity
            sentiment_type = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
            analyzed_headlines.append((headline, sentiment_type, sentiment))
        return analyzed_headlines
    except Exception as e:
        logging.error(f"Error  in get_news_with_sentiment for {url}: {e}")

def CallTopHeadlinesTweet(url):
    try:
        client = create_api()
        top_headlines = get_top_headlines(url)
        website_name = get_website_name(url)

        # Get the start time from the user
        start_time_str = input("Enter the start time for tweets (HH:MM): ")
        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        now = datetime.now()
        initial_time = datetime.combine(now.date(), start_time)
        
        if initial_time < now:
            initial_time += timedelta(days=1)  # Schedule for the next day if time has passed today

        for i, headline in enumerate(top_headlines, start=1):
            message = f"#TopNewsHeadlines\n{headline} Read Full Article At {url}\nCredit: {website_name}"
            # Schedule tweets at intervals starting from the specified time
            tweet_time = initial_time + timedelta(seconds=i * random.randint(40, 60))
            tweet_time_str = tweet_time.strftime("%H:%M")
            schedule.every().day.at(tweet_time_str).do(tweet_headline, client=client, message=message)
            logging.info(f"Scheduled tweet for {url} at {tweet_time_str}")

        while True:
            schedule.run_pending()
            time.sleep(1)  # Adjust as needed to avoid excessive CPU usage

    except Exception as e:
        logging.error(f"Error in CallTopHeadlinesTweet for {url}: {e}")

if __name__ == '__main__':
    logging.info("Starting Application:")
    threads = []
    # Create threads for each URL
    for i, url in enumerate(IMP_urls):
        thread = threading.Thread(target=CallTopHeadlinesTweet, args=(url,))
        threads.append(thread)
        # Start threads with delays
    for i, thread in enumerate(threads):
        thread.start()
        if i < len(threads) - 1:
            # No delay after the last thread
            time.sleep(2500)  # 30-minute delay
    # Join threads to ensure all threads complete before exiting
    for thread in threads:
        thread.join()

    logging.info("Finished Application:")

# x = get_news_with_sentiment(url = IMP_urls[0])
# print(x)