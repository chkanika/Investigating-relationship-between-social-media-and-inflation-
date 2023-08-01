# 1. import libraries 
# 2. make class 
# 3. def function for variable 
# 4. def func to clean tweet 
# 5. def func to get tweet 
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
# generic twitter classes for sentiment analysis 

    def __init__(self):
        # class constructor and initalization method 
        # keys and tokens from twitter dev console 
        consumer_key = '5A07bgc0Dq2wtDMcrhdxsUfZG'
        consumer_secret = '94ula1KOe0rvjF9wc5bxKWsKsq4xXVqftgtzKNKVTy3aZjZJvq'
        access_token = '1595252769715195904-PDAw3uQqK7kpeeKangEM10Zxd8E00B'
        access_token_secret = '1595252769715195904-PDAw3uQqK7kpeeKangEM10Zxd8E00B'
        
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
        ''' 
        Utility function to classify sentiment of passed tweet using textblob's sentiment method
        '''
        # create textblob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        '''
        main function to fecth tweets and parse them
        ''' 
        # empty list to store parsed data 
        tweets = []
        try:
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q=query, count = count)
            # parsing tweets one by one 
            for tweets in fetched_tweets:
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {}
                # saving text of tweet 
                parsed_tweet['text'] = tweets.text
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweets.text)
                
                # appending parsed tweet to tweet list 
                if tweets.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                    else:
                        tweets.append(parsed_tweet)
             
            # return parsed tweets  
            return tweets 
        except tweepy.errors as e:
            # print error (if any)
            print("Error : " +str(e))
            
# 
# ... (The rest of your import and class definitions)

def main():
    # creating object of TwitterClient Class 
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query='lazy', count=10)
    
    # picking positive tweets from tweets 
    ptweets = [tweet_item for tweet_item in tweets if tweet_item['sentiment'] == 'Positive']
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    
    # picking negative tweets from tweets 
    ntweets = [tweet_item for tweet_item in tweets if tweet_item['sentiment'] == 'Negative']
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) - (len(ntweets)+len(ptweets)))/len(tweets)))
    
    # printing first 10 positive tweets 
    print('\n\nPositive tweets:')
    for tweet_item in ptweets[:10]:
        print(tweet_item['text'])
        
    # printing first 10 negative tweets 
    print('\n\nNegative tweets: ')
    for tweet_item in ntweets[:10]:
        print(tweet_item['text'])
        
if __name__ == "__main__":
    # calling main function 
    main()


