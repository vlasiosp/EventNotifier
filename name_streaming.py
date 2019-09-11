import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from authenticator import authentication
import json


chania_loc = [23.42, 34.61, 24.38, 35.76]


class OutListener(StreamListener):

    def on_status(self, status):
        print(status.text)
        Name = status.user.screen_name
        print(Name)




# Connect to DB

if __name__ == "__main__":
    # Get access and key from another class


# Authentication
    cred = authentication()

    consumer_key = cred.getconsumer_key()
    consumer_secret = cred.getconsumer_secret()

    access_token = cred.getaccess_token()
    access_token_secret = cred.getaccess_token_secret()

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Start streaming

    myListener = OutListener()
    stream = Stream(auth=api.auth, listener=myListener)

    stream.filter(locations=[23.42, 34.61, 24.38, 35.76], is_async=True)

# Find relevant hashtag users


