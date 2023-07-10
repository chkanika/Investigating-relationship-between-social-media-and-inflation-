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
    
    