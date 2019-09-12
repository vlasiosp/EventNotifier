import time
import tweepy
from authenticator import authentication
import json



def search_hashtag(listOfTweets, keywords, numOfTweets):
    # Iterate through all tweets containing the given word, api search mode
    for key in keywords:
        for tweet in tweepy.Cursor(api.search, q=key).items(numOfTweets):
            # Add tweets in this format
            dict_ = {'Screen Name': tweet.user.screen_name,
                     'User Name': tweet.user.name,

                     }
            '''Tweet Created At': tweet.created_at,
                    'Tweet Text': tweet.text,
                    'User Location': tweet.user.location,
                    'Tweet Coordinates': tweet.coordinates,
                    'Retweet Count': tweet.retweet_count,
                    'Retweeted': tweet.retweeted,
                    'Phone Type': tweet.source,
                    'Favorite Count': tweet.favorite_count,
                    'Favorited': tweet.favorited,
                    'Replied': tweet.in_reply_to_status_id_str
                     # Να μην ξεχάσω αν έχει λάθη μήπως σχετίζεται με το unicode'''

            listOfTweets.append(dict_)
    print(listOfTweets)
    print(len(listOfTweets))
    titiv = listOfTweets



if __name__ == "__main__":

    hashtags = ['#Chania', '#ChaniaPost']
    # Authentication
    cred = authentication()

    consumer_key = cred.getconsumer_key()
    consumer_secret = cred.getconsumer_secret()

    access_token = cred.getaccess_token()
    access_token_secret = cred.getaccess_token_secret()

    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    #auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # search_hashtag(listOfTweets=[], keywords=hashtags, numOfTweets=1000)
    names = ["#ChaniaPost", "#Chania"]
    for name in names:
        followers = tweepy.Cursor(api.followers_ids, screen_name=name).items()

        while True:
            with open('tweets.json', 'w', encoding='utf8') as file:
                try:
                    follower = next(followers)
                except tweepy.TweepError:
                    time.sleep(60 * 15)
                    follower = next(followers)
                except StopIteration:
                    break

                print(follower)

                file.write(str(follower))

