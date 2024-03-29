"""
Program that cleans a tweet from spare elements and leaves it with meaningful words that helps us classify each
tweet and make a user profile according to preferences
    """

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize.casual import TweetTokenizer
from mysql_conn import db_connect
import langdetect
import string
import re
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
category_dict = {}

# Code for tweets in engish
#t_clean_en = []

pos_lem = WordNetLemmatizer()
tTok = TweetTokenizer()

# Make a list of positive adjectives and adverbs to compare with the text
with open('positive_adj.py') as pos_adj_file:
    pos_adj = pos_adj_file.read().split(',')
    pos_adj_file.close()
    #print(pos_adj)

with open('positive_adv.py') as pos_adv_file:
    pos_adv = pos_adv_file.read().splitlines()
    pos_adv_file.close()
    # print(pos_adv)

positives = sorted(pos_adj + pos_adv)
#print(positives)


# This is the most important function for tweet processing
def tweet_process(tweet, t_clean_en):

    # clean text with regular expressions
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # remove retweets
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove mentions
    tweet = re.sub('@[^\s]+', '', tweet)
    # remove punctuation
    tweet = re.sub('@[^\w\s]', '', tweet)
    # remove # from hashtags and $
    tweet = re.sub(r'\#\w*', '', tweet)
    # remove numbers
    tweet = re.sub(r'\d', '', tweet)
    # remove dots
    tweet = re.sub(r'\.+', "", tweet)

    word_tok = tTok.tokenize(tweet)

    tags = pos_tag(word_tok)
    # print(tags)
    pos_all = [word for word, pos in tags if (pos.startswith('NN') or pos.startswith('RB') or pos.startswith('JJ'))]
    # print(pos_all)

    stop_words_en = set(stopwords.words("english"))


# We use language detection module to determine the language and store the tweets accordingly
    try:
        if langdetect.detect(tweet) == "en":
            # All selected pos tags (Nouns, adjectives and adverbs)
            for pos_w in pos_all:
                stemmer = SnowballStemmer("english")
                wnl = WordNetLemmatizer()
                # Select all the tweets where there are adj, adv with positive meaning
                if pos_w in positives:
                    # Select only nouns form the positive text
                    pos_noun = [pos_w for pos_w,pos in tags if (pos.startswith('NN'))]
                    for w in pos_noun:
                        if w not in stop_words_en and w not in string.punctuation:
                            #t_clean_en.append(stemmer.stem(w))
                            t_clean_en.append(wnl.lemmatize(w))

            # print("English",t_clean_en)
            #print(tweet)
            return(t_clean_en)

        else:
            return None
            pass
    except:
        return None
        pass


def tweet_selector():
    con = db_connect()
    cursor = con.cursor()

# Select all users' screen names from db as tuple

    user_select_query = "SELECT ScreenName from USERS"
    cursor.execute(user_select_query)
    user_select = cursor.fetchall()
    # print(user_select)
    tw_list = []

# make a list and remove some special characters
    user_select = list(sum(user_select, ()))
    #print(user_select)

    for user in user_select:
        t_clean_en = []
        print("Processing user: " + user)
        cursor.execute("""SELECT TweetText FROM `TWEETS` where ScreenName = %s""", (user,))

        # fetching user tweets and saving it to a list
        fetchall_usertweets = cursor.fetchall()
        fetchall_usertweets = list(sum(fetchall_usertweets, ()))

        # setting up a counter which counts the tweets of each user
        counter = 0

        # examine each user's tweet separately

        for tweet in fetchall_usertweets:
            counter += 1
            #print("\tprocessing tweet {}: {}".format(counter,tweet))
            # Reset counter when we process all user's tweets
            #if counter ==fetchall_usertweets[-1]:
            #    counter=0
    # bring tokenized tweets
            tw_pr = None
            tw_pr = tweet_process(tweet,t_clean_en)
            #if(tw_pr != None)
            #print("\t{}\tresult: {}".format(counter,tw_pr) )
        print(t_clean_en)
        usercats = {}
        for k in category_dict.keys():
            usercats[k] = 0
        for word in t_clean_en:
            for k in category_dict.keys():
                for v in category_dict[k]:
                    if v == word:
                        usercats[k] = 1 + usercats[k]
        print(usercats)


if __name__ == '__main__':
    category_dict["theater"] = ["actor", "play", "theater"]
    category_dict["night_life"] = ["bar", "pub", "club", "coffee", "restaurant"]
    category_dict["site_seeing"] = ["museum", "ancient", "church"]
    category_dict["astronomy"] = ["Nebula", "Star", "Galaxy", "Eclipse", "Laser", "NASA"]
    category_dict["science"] = ["Pascal", "Laser", "Magnetic", "Force"]
    tweet_selector()

