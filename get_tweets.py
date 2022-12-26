import tweepy
import os
from dotenv import load_dotenv
load_dotenv()


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

# リファレンスの内容に沿って入力（https://docs.tweepy.org/en/stable/client.html）
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

QUERY = input("検索するキーワードを入力： ")
# Tweetを取得する上限
MAX_RESULTS = 30
tweets = client.search_recent_tweets(query=QUERY, max_results=MAX_RESULTS)

tweets_data = tweets.data

if tweets_data != None:
    for i, tweet in enumerate(tweets_data):
        print("No:" + str(i+1))
        print("tweet.text: " + tweet.text)
        print("\n")
else:
    print("該当がありませんでした")
