from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

tweet = "@Noahpinion today's cold @ home https://twitter.com/Noahpinion"

tweet_words = []

for word in tweet.split(' '):
    if word.startswith('inflation') and len(word) > 1:
        word = '@user'
        
    elif word.startswith('http'):
        word = 'http'
    tweet_words.append(word)

tweet_proc = ' '.join(tweet_words)
    
roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)

tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative','Neutral', 'Positive']

# sentiment analysis 
encoded_tweet = tokenizer(tweet_proc, return_tensors ='pt')

output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
output = model(**encoded_tweet)

scorces = output[0][0].detach().numpy()
scorces = softmax(scorces)

for i in range(len(scorces)):
    l = labels[i]
    s = scorces[i]
    print(l,s)