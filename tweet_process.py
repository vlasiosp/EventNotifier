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
    print(user_select)


    # make a list and remove some special characters
    user_select = list(sum(user_select, ()))

    print(user_select)

    for user in user_select:

        print(user)
        query = cursor.execute("""SELECT TweetText FROM `TWEETS` where ScreenName = %s""", (user,))
        q_f = cursor.fetchall()
        print(q_f)











    '''for tweet in tweet_select:
            tokened[i] = word_tokenize(tweet)
            print(tokened[i])
        i+=1'''






if __name__ == '__main__':

    word_split()

