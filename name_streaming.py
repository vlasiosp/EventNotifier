import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from authenticator import authentication
from mysql_conn import db_connect
import MySQLdb
import json
from urllib3.exceptions import ProtocolError
from dateutil import parser


chania_loc = [21.236572,34.703235,25.317993,36.361587]

cr_t_activity = """CREATE TABLE IF NOT EXISTS USER_ACTIVITY(
                            Created_at VARCHAR (255),
                            UserId VARCHAR(255),
                            ScreenName VARCHAR(255),
                            TweetText VARCHAR(255),
                            Place VARCHAR(255),
                            Location VARCHAR(255) ,
                            PRIMARY KEY (UserId) 
                                )"""

def store_db(created_at,user_id, screen_name, tweet, place, location):
    """
    connect to MySQL database and insert twitter data
    """

    try:
        con = db_connect()
        con.set_character_set('utf8')


        cursor = con.cursor()

        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')

        if con:
            print("Connection successful")


            #Insert twitter data


            cursor.execute(cr_t_activity)
            query = "INSERT INTO USER_ACTIVITY (Created_at, UserId, ScreenName, TweetText, Place, Location) VALUES (%s, %s, %s, %s, %s, %s)"

            cursor.execute(query, (created_at, user_id, screen_name, tweet, place, location))
        else:
            print('connection unsaccesful')

        con.commit()
        cursor.close()
        con.close()
        print("MySQL connection is closed")
        return

    except MySQLdb.Error as e:
        print(e)




class OutListener(StreamListener):

    def on_status(self, status):
        print(status.text)
        Name = status.user.screen_name
        print(Name)


    def on_data(self, data):

        try:
            rawdata = json.loads(data)

            # grab the wanted data from the Tweet

            user_id = rawdata['user']['id']
            screen_name = rawdata['user']['screen_name']
            text = rawdata['text']
            #text_id = rawdata['id']
            created_at = parser.parse(rawdata['created_at'])
            location = rawdata['user']['location']

            if rawdata['place'] is not None:

                place = rawdata['place']['country']

            else:
                place = None

            # print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))
            print(created_at, user_id, screen_name, text, place, location)

            # insert the data into the MySQL database
            store_db(created_at, user_id, screen_name, text,  place, location)


        except MySQLdb.Error as e:
            print(e)

    def on_exception(self, exception):
        print(exception)
        return


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
    stream = Stream(auth=api.auth, listener=myListener )


    while True:
        try:
            stream.filter(locations=chania_loc, is_async=True)

        except:
            # Bypass some errors related to urllib3 requests
            (ProtocolError)
            continue
