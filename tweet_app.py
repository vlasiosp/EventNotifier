import keys_urls
import tweepy

chania_loc="35.510457, 24.022692"

# ---Functions ---
def user_details():
    user = api.get_user('KostasVaxevanis')
    print(user.screen_name)
    print("The number of followers of user", user.screen_name, "are",user.followers_count)
    print("His friends are: ")
    for friend in user.friends():
        print(friend.screen_name)


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

def search_hashtag():
    for tweet in tweepy.Cursor(api.search, q="#Chania",count=100,
                               lang="en",
                               since="2017-04-03").items(1000):
        print(tweet.created_at, tweet.user.screen_name, tweet.text, tweet.place)


# --- User API Authentication ---

auth = tweepy.OAuthHandler(keys_urls.ck, keys_urls.cs)
auth.set_access_token(keys_urls.at, keys_urls.ats)
api = tweepy.API(auth)


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


#search_hashtag()
MyStreamListener()