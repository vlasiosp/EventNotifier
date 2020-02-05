"""
Program that cleans a tweet from spare elements nd leaves it with meaningful words that helps us classify each
tweet and make a user profile according to preferences
    """


from googletrans import Translator
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize.casual import TweetTokenizer
from mysql_conn import db_connect
import langdetect
import string
import re


translator =  Translator()

# We will use 2 languages , so we initialize 2 lists for Greek and English tweets to store the filtered tweets
t_clean_en = []


tTok = TweetTokenizer()

# Make a list of positive adjectives and adverbs to compare with the text
with open('positive_adj.py') as pos_adj_file:
    pos_adj = pos_adj_file.read().split(',')
    pos_adj_file.close()
    #print(pos_adj)

with open('positive_adv.py') as pos_adv_file:
    pos_adv = pos_adv_file.read().splitlines()
    pos_adv_file.close()
    #print(pos_adv)

positives = sorted(pos_adj + pos_adv)
#print(positives)



# This is the most important function for tweet processing
def tweet_process(tweet):

# clean text with regular expressions

    #remove links
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    #remove retweets
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    #remove mentions
    tweet = re.sub('@[^\s]+','',tweet)
    # remove punctuation
    tweet = re.sub('@[^\w\s]','', tweet)
    # remove # from hashtags and $ from
    tweet = re.sub(r'\#\w*', '', tweet)
    #remove numbers
    tweet = re.sub(r'\d', '', tweet)
    # remove dots
    tweet = re.sub(r'\.+', "", tweet)

    word_tok = tTok.tokenize(tweet)

    tags = pos_tag(word_tok)
    #print(tags)
    pos_all = [word for word,pos in tags if (pos.startswith('NN') or pos.startswith('RB') or pos.startswith('JJ'))]
    #print(pos_all)

    stop_words_en = set(stopwords.words("english"))




# We use language detection module to determine the language and store the tweets accordingly
    try:
        if langdetect.detect(tweet) == "en":
            # All selected pos tags (Nouns, adjectives and adverbs)
            for pos_w in pos_all:
                # Select all the twets where there are adj, adv with positive meaning
                if pos_w in positives:
                    # Select only nouns form the positive text
                    pos_noun = [pos_w for pos_w,pos in tags if (pos.startswith('NN'))]
                    for w in pos_noun:
                        if w not in stop_words_en and w not in string.punctuation:
                            t_clean_en.append(w)


            #print("English",t_clean_en)
            #print(tweet)
            return(t_clean_en)

        else:
            pass
    except:
        pass


def tweet_selector():
    con=db_connect()
    cursor=con.cursor()

# Select all users' screennames from db as tuple

    user_select_query = "SELECT ScreenName from USERS"
    cursor.execute(user_select_query)
    user_select = cursor.fetchall()
    #print(user_select)
    tw_list = []

# make a list and remove some special characters
    user_select = list(sum(user_select, ()))
    #print(user_select)

    for user in user_select:

        print(user)
        cursor.execute("""SELECT TweetText FROM `TWEETS` where ScreenName = %s""", (user,))

        # fetching user tweets and saving it to a list
        fetchall_usertweets = cursor.fetchall()
        fetchall_usertweets = list(sum(fetchall_usertweets, ()))

        # setting up a counter which counts the tweets of each user
        counter = 0

        #examine each user's tweet separately

        for tweet in fetchall_usertweets:
            print(tweet)
            counter += 1
            #Reset counter when we process all user's tweets
            if counter ==fetchall_usertweets[-1]:
                counter=0
    # bring tokenized tweets
            tw_pr = tweet_process(tweet)


    # If we reach the last tweet of the user, reset counter

            print(tw_pr, counter)





if __name__ == '__main__':

    tweet_selector()

