import MySQLdb
import tweepy
from tweepy import *
from authenticator import authentication
from mysql_conn import db_connect


# Create table of user's tweets
cr_t_hash = """CREATE TABLE IF NOT EXISTS USER_HASHTAG_SEARCH(
                          UserId VARCHAR(255),
                          UserName VARCHAR(255),
                          ScreenName VARCHAR(255),
                          TweetText VARCHAR(255),
                          UserLocation VARCHAR(255),
                          PRIMARY KEY (UserId)
                          )"""


def search_hashtag(listOfTweets, keyword, numOfTweets):

    for keyword in tweepy.Cursor(api.search, q=keyword).items(numOfTweets):


        try:
            con = db_connect()
            con.set_character_set('utf8')
            cursr = con.cursor()
            cursr.execute(cr_t)

            if con:
                diction = {'UserId': keyword.user.id,
                           'UserName': keyword.user.name,
                           'ScreenName': keyword.user.screen_name,
                           'TweetText': keyword.text,
                           'UserLocation': keyword.user.location,
                           }

                userid = diction['UserId']
                username = diction['UserName']
                screen_name = diction['ScreenName']
                tweet_text = diction['TweetText']
                location = diction['UserLocation']

                query = "INSERT INTO USER_HASHTAG_SEARCH (UserId, UserName, ScreenName, TweetText, UserLocation) VALUES (%s, %s, %s, %s, %s)"

                cursr.execute(query, (userid, username, screen_name, tweet_text, location))
                listOfTweets.append(diction)
                print(listOfTweets)
                print(len(listOfTweets))
                con.commit()
                cursr.close()
                con.close()
                print("MySQL connection is closed")

            else:
                print('connection unsaccesful')








        except MySQLdb.Error as e:
            print(e)


if __name__ == "__main__":
    # Authentication

    cred = authentication()
    consumer_key = cred.getconsumer_key()
    consumer_secret = cred.getconsumer_secret()
    access_token = cred.getaccess_token()
    access_token_secret = cred.getaccess_token_secret()

    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    auth.secure = True

    # For user API: auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    preferred_hashtags = ["#Chania", "xania", "chania"]
    search_hashtag(listOfTweets=[], keyword=preferred_hashtags, numOfTweets=500)
