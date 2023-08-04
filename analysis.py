# # mount drive 
# # set toolkit 

# # Importing essential libraries and functions
# import pandas as pd
# import numpy as np
# import re
# import nltk
# from nltk.corpus import stopwords
# from numpy import array

# from tensorflow import keras
# from keras.preprocessing.text import one_hot, Tokenizer
# from keras.preprocessing.sequence import pad_sequences
# from keras.models import Sequential
# from keras.layers import LSTM
# from keras.layers import Activation, Dropout, Dense
# from keras.layers import Flatten, GlobalMaxPooling1D, Embedding, Conv1D, LSTM
# from sklearn.model_selection import train_test_split

# # importing the dataset 
# # tweets = 
# #  source? 

# # dataset exploration
# # tweets.shape  
# # tweets.head(5)

# import seaborn as sns
# # sns.countplot(x='sentiment', data=tweets)

# # data preprocessing 
# # tweets_[""][]

# # Tag-RE = re.compile()
# # remove html tag 

# import nltk
# nltk.download('stopwords')

# def preprocess_text(sen):
#     '''Cleans text data up, leaving only 2 or more char long non-stepwords composed of A-Z & a-z only
#     in lowercase'''
    
#     sentence = sen.lower()

#     # Remove html tags
#     # sentence = remove_tags(sentence)

#     # Remove punctuations and numbers
#     sentence = re.sub('[^a-zA-Z]', ' ', sentence)

#     # Single character removal
#     sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)  # When we remove apostrophe from the word "Mark's", the apostrophe is replaced by an empty space. Hence, we are left with single character "s" that we are removing here.

#     # Remove multiple spaces
#     sentence = re.sub(r'\s+', ' ', sentence)  # Next, we remove all the single characters and replace it by a space which creates multiple spaces in our text. Finally, we remove the multiple spaces from our text as well.

#     # Remove Stopwords
#     pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
#     sentence = pattern.sub('', sentence)

#     return sentence

# # calling preprocessing text func on tweets 
# X = []
# # sentences = list(tweets[""])
# # for sen in sentences:
#     # X.append(preprocess_text(sen))


# import tweepy
# from textblob import TextBlob

# # Set your Twitter API credentials
# consumer_key = "YOUR_CONSUMER_KEY"
# consumer_secret = "YOUR_CONSUMER_SECRET"
# access_token = "YOUR_ACCESS_TOKEN"
# access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# # Authenticate with Twitter API
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# # Define the word you want to search for
# search_word = "YOUR_SEARCH_WORD"

# try:
#     # Fetch tweets containing the search word
#     tweets = api.search_tweets(q=search_word, count=100, lang="en", tweet_mode="extended")

#     # Process the fetched tweets and store sentiment along with the tweet text
#     analyzed_tweets = []
#     for tweet in tweets:
#         # Access tweet text
#         tweet_text = tweet.full_text
#         # Perform sentiment analysis using TextBlob
#         analysis = TextBlob(tweet_text)
#         # Determine sentiment polarity (ranging from -1 to 1, where < 0 is negative, > 0 is positive)
#         sentiment_polarity = analysis.sentiment.polarity

#         # Store the tweet along with its sentiment polarity
#         analyzed_tweets.append((tweet_text, sentiment_polarity))

# except tweepy.TweepError as e:
#     # Handle Twitter API errors here
#     print("Error occurred:", e)

# # Filter positive tweets
# ptweets = [tweet for tweet, sentiment in analyzed_tweets if sentiment > 0]

# # Process or store the positive tweets (ptweets) as per your research requirements
# for tweet_text in ptweets:
#     print(tweet_text)
