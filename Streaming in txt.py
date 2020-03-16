import tweepy



class TweetsListener(tweepy.StreamListener):

    def on_connect(self):
        print("Estoy conectado!")

    def on_status(self, status):
        path = open('./data.txt', 'a')
        print(status.text, file=path)
        path.close()  

    def on_error(self, status_code):
        print("Error", status_code)



consumer_key = "Mbl6PRyuF9NzCyZJqKokWWS9Y"
consumer_secret = "d2u6ah734HhLYqtb1CuV5dDyReTnJDBktahyMNfvFu0UL8FCbM"
access_token = "1238150300000595970-ylMfnUNjdNWVZKjQgftuoEmedLDOlI"
access_token_secret = "UmZPGzy6AODk8dhUP3gZqsK0tfDGt7JgfM1MuetyUPpyd"

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