# import tweepy

# # Auth to Twitter
# auth = tweepy.OAuthHandler(
#     "H1u5orzGs13upRXpJohTbDEXN", "MyLLarwWMAUZuSnwd4LwR4zXKDNnZaVNYe3kyvySBTjiC0UwA7"
# )

# auth.set_access_token(
#     "1113084437657538561-FtCjJOSk1d4BJA4kf4UimkdfNEDJL7",
#     "3zkccwzdCGyiyGh0Y0rtcTvbwgIZOssiXprSZW8x1ucr4",
# )

# # Skapa en API object
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

###### Här börjar alt roligt #######

## Detta är en metod för att få tweets i sin home page
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said '{tweet.text}'")

## Detta är en metod för att posta en tweet
# api.update_status("Test tweet using tweepy :)")

# api.update_profile(
#     description="Future front-end dev. Currently learning react and python!"
# )

## Lite user details
# user = api.get_user("BillGates")

# print("User details")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 followers")
# for follower in user.followers():
#     print(follower.name)

## Printar ut tweets som följer ett specifikt critera
# for tweet in api.search(q="Python", lang="en", rpp=10):
#     print(f"{tweet.user.name}:{tweet.text}")