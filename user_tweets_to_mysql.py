
import datetime
import tweepy
from authenticator import authentication
from mysql_conn import db_connect
import MySQLdb


def user_select():

    try:

        con = db_connect()
        curs = con.cursor()
        curs.execute("SELECT UserId FROM USERS")
        row = curs.fetchone()

        while row is not None:
            print(row)
            row = curs.fetchone()
            return row
        curs.close()
        con.close()


    except MySQLdb.Error as e:
        print(e)



def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    cred = authentication()
    consumer_key = cred.getconsumer_key()
    consumer_secret = cred.getconsumer_secret()

                            #for UserAuthHandler
                            #access_token = cred.getaccess_token()
                            #access_token_secret = cred.getaccess_token_secret()

    # Authentication
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
                            #auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)



    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name,  tweet_mode="extended", count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200,  tweet_mode="extended", max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("Timestamp:%s...  %s tweets downloaded so far" % (datetime.datetime.now(), len(alltweets)))

        try:
            con = db_connect()

            for tweet in alltweets:
                curs = con.cursor()
                curs.execute('SET NAMES utf8mb4;')
                curs.execute('SET CHARACTER SET utf8mb4;')
                curs.execute('SET character_set_connection=utf8mb4')
                query = 'INSERT IGNORE INTO TWEETS (ScreenName, TweetId, Created_at, TweetText) Values (%s, %s, %s, %s)'
                curs.execute(query, (screen_name, tweet.id_str, tweet.created_at, tweet.full_text))
                con.commit()

        except MySQLdb.Error as e:
            print(e)
            pass







if __name__ == '__main__':
    count = 0
    con = db_connect()

    curs = con.cursor()
    curs.execute('SET NAMES utf8;')
    curs.execute('SET CHARACTER SET utf8;')
    curs.execute('SET character_set_connection=utf8;')
    user_row = "SELECT ScreenName FROM USERS"
    curs.execute(user_row)
    screen_names=curs.fetchall()
    screen_names = [i[0] for i in screen_names]
    print(screen_names, len(screen_names))
    try:
        for screen_name in screen_names:
            get_all_tweets(screen_name)
            #print(get_all_tweets(screen_name))
            count+=1
            print(count," user's tweets processed")
            print(screen_name)
    except tweepy.TweepError as er:
        if er:
            print(er)
            pass


    curs.close()
    con.close()
