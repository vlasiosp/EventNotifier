import nltk
from nltk import word_tokenize, wordpunct_tokenize, sent_tokenize
import MySQLdb
from mysql_conn import db_connect








def word_split():
    con=db_connect()
    cursor=con.cursor()

    #Select all users' screennames from db as tuple

    user_select_query = "SELECT ScreenName from USERS"
    cursor.execute(user_select_query)
    user_select = cursor.fetchall()

    # make a list and remove some special characters
    user_select = list(sum(user_select, ()))
    user_select = str(user_select)

    # split words by comma

    allusers = user_select.split(",")




    print (user_select)

    for user in user_select:

        print(user)
        tweet_select_query = """SELECT TweetText FROM `TWEETS` where ScreenName = '&s'"""
        cursor.execute(tweet_select_query, user)
        tweet_select = cursor.fetchall()
        print(tweet_select)










        '''for tweet in tweet_select:
            tokened[i] = word_tokenize(tweet)
            print(tokened[i])
            i+=1'''






if __name__ == '__main__':

    word_split()

