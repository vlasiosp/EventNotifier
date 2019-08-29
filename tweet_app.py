import keys_urls
import tweepy

# ---Functions ---
def user_api():
    user = api.get_user('KostasVaxevanis')
    print(user.screen_name)
    print("The number of followers of user",user.screen_name, "are",user.followers_count)
    print("His friends are: ")
    for friend in user.friends():
        print(friend.screen_name)


def search_hashtag():
    for tweet in tweepy.Cursor(api.search, q="#Chania", count=100,
                               lang="en",
                               since="2017-04-03").items():
        print(tweet.created_at, tweet.text)

auth = tweepy.OAuthHandler(keys_urls.ck, keys_urls.cs)
auth.set_access_token(keys_urls.at, keys_urls.ats)

api = tweepy.API(auth)

# status = "Testing!"
# api.update_status(status=status)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user_api()