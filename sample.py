import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

# generic twitter classes for sentiment analysis 

def __init__(self):
    # class constructor and initalization method 
    # keys and tokens from twitter dev console 
    consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
    consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    
    # attempt authentication 
    try:
        # create OAuthHandler object 
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        # set access token and secret 
        self.auth.access_token(access_token, access_token_secret)
        # create tweepy API object to fetch tweets 
        self.api = tweepy.API(self.auth)
    except:
        print("Error: Authentication Falied")

def clean_tweet(self, tweet):
    # utility function to clean yweet by removing links, special characters using simple regex statements. 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(self, tweet):
    # utility function to classify sentiment of passed tweet using textblob's sentiment method 
    # create textblob object of passed tweet text 
    analysis = TextBlob(self.clean_tweet(tweet))
    # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'