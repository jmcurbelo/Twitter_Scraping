import tweepy

class TweetsListener(tweepy.StreamListener):

    def on_connect(self):
        print("Estoy conectado!")

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print("Error", status_code)



consumer_key = "XXX"
consumer_secret = "XXX"
access_token = "XXX-XXX"
access_token_secret = "XXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
streamingApi.filter(
    # follow=["151179935"],
    track=["Cuba"]
    #locations=[-99.36492421,19.04823668,-98.94030286,19.59275713] # Ciudad de Mexico
)