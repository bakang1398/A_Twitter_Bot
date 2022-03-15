# import packages
import pip
import tweepy
import time

# Authenticate to twitter
consumer_key='Q0lv36a6kndbBY2yGdvJR4GMJ'
consumer_secret='d41e9LC1ssv8PM1GQOx8nG1nUQzZ9IRDDB32y6te3WmBSWr21z'
access_key='1503045545463627779-hgRSV7IoQg7lamzIFfnfy5sRoDJIDp'
access_secret='Pr7ZHW9CaACNWrB1noWiC6Kzkq70JaecXRUqcVfMDxzdL'


# Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user = api.me()
search= 'WomenInMining', 'WomenMiners' 
num_of_tweets = 700
for tweet in tweepy.Cursor(api.search,search).items(num_of_tweets):
    try:
        tweet.retweet()
        print("Retweet")
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
