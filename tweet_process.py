from googletrans import Translator
import nltk
from nltk import word_tokenize, wordpunct_tokenize, sent_tokenize
import itertools
from mysql_conn import db_connect
import langdetect
from langdetect import detect, detect_langs

translator =  Translator()

def tweet_process(tweet):
    tw_tknz= sent_tokenize(tweet)
    return tw_tknz

def tweet_translate(tweet):
    if tweet == translator.translate(tweet, src='el'):
        pass
    else:
        tweet = translator.translate(tweet, src='auto', dest='el')
    print("Translated Tweet:", tweet)


def tweet_selector():
    con=db_connect()
    cursor=con.cursor()

# Select all users' screennames from db as tuple

    user_select_query = "SELECT ScreenName from USERS"
    cursor.execute(user_select_query)
    user_select = cursor.fetchall()
    print(user_select)
    tw_list=[]
# make a list and remove some special characters
    user_select = list(sum(user_select, ()))

    print(user_select)
    counter=0
    for user in user_select:

        print(user)
        cursor.execute("""SELECT TweetText FROM `TWEETS` where ScreenName = %s""", (user,))
        q_f = cursor.fetchall()
        q_f = list(sum(q_f , ()))
        counter=0
        for tweet in q_f: # Για κάθε tweet ενός χρήστη
            tw_pr =  tweet_process(tweet)
            counter+=1
            if counter ==q_f[-1]:
                counter=0
            print(tw_pr, counter)
            # print ("/n",tw_pr)
            tw_list.append(tw_pr)
            # print(tw_list)


if __name__ == '__main__':

    tweet_selector()

