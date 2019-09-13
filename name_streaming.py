import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from authenticator import authentication
from mysql_conn import connect
from mysql_conn import Error
from dateutil import parser
import json


chania_loc = [23.42, 34.61, 24.38, 35.76]


class OutListener(StreamListener):

    def on_status(self, status):
        print(status.text)
        Name = status.user.screen_name
        print(Name)

    def on_data(self, data):

        try:
            raw_data = json.loads(data)

            if 'text' in raw_data:

                user_id = raw_data['user']['id']
                tweet = raw_data['text']
                username = raw_data['user']['screen_name']

                if raw_data['place'] is not None:
                    place = raw_data['place']['country']
                    print(place)
                else:
                    place = None

                location = raw_data['user']['location']

                # insert data just collected into MySQL database
                connect(user_id, username, tweet, place, location)
                #print("Tweet colleted at: {} ".format(str(created_at)))
        except Error as e:
            print(e)






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

connect('user_id', 'username', 'tweet', 'place', 'location')


