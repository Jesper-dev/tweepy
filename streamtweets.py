import json
import tweepy

# Denna class används för att lyssna på nya tweets
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"TWEET FROM:{tweet.user.name}:{tweet.text} TWEET ENDED")

    def on_error(self, status):
        print("Error detected")


# Auth to Twitter
auth = tweepy.OAuthHandler(
    "H1u5orzGs13upRXpJohTbDEXN", "MyLLarwWMAUZuSnwd4LwR4zXKDNnZaVNYe3kyvySBTjiC0UwA7"
)

auth.set_access_token(
    "1113084437657538561-FtCjJOSk1d4BJA4kf4UimkdfNEDJL7",
    "3zkccwzdCGyiyGh0Y0rtcTvbwgIZOssiXprSZW8x1ucr4",
)

# Skapa en API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "React", "Javascript"], languages=["en"])