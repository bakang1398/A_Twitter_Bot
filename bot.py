# import packages
import pip
import tweepy
import time

# Authenticate to twitter
consumer_key='4mkGugUhietXAVp3cia2HToPQ'
consumer_secret='SM0MQNXiUlg6vnVB04LnJne2wGtg2hwg6TxEFzWDJKxNru3Wlv'
access_key='1417823014989803522-LBUqaevW75pYSq7KKQv1b5uNOcSwT5'
access_secret='Kvtf6ymVqjVTQX26S2sD1XDdwi6F8pwSkJIS031bcLaX5'


# Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user = api.me()
search= 'Travelphotography' 
num_of_tweets = 700
for tweet in tweepy.Cursor(api.search,search).items(num_of_tweets):
    try:
        tweet.retweet()
        print("Retweet")
        time.sleep(0)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
