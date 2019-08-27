import keys_urls
import tweepy

auth = tweepy.OAuthHandler(keys_urls.ck, keys_urls.cs)
auth.set_access_token(keys_urls.ac, keys_urls.ats)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)