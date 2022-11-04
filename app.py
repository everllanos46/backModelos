from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import tweepy

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



api_key= "DaXWt24KzMBo9HS9xqdTLB463"
api_secret= "V4QyyCFBd9OIEXHgZXPuf2DPosxNwtLHnOWZFNsrQDNmJ5QkXt"
bearer_token="AAAAAAAAAAAAAAAAAAAAALOTiwEAAAAAyj%2Fv7offhCbcuOPrm8vHEgR%2B7iU%3DZhkSAkNkBh0H2hknpIMLsHw8o7Wlc8LIdXN40WXHkb5JvCpOhF"
access_token ="877685422935207936-iHSOIYf90ZmRQTdFwqMIqoGTp9K2WWK"
access_token_secret="a5BQVdhxkJbht55LLA2ahXQtcn83tgTgAgUbJPoQGh6Nl"
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api= tweepy.API(auth)

@app.get("/{tema}")
async def root(tema:str):
    search_term = f'{tema} -is:retweet'

    tweet_cursor = tweepy.Cursor(api.search_tweets, q= search_term, lang="es",
    tweet_mode="extended").items(10)

    tweets = [tweet.full_text for tweet in tweet_cursor]
    return {"message": tweets}

@app.post("/post_tweet")
async def root():
    

    tweet_cursor = client.search_recent_tweets(query="petro -is:retweet", max_results=10, user_fields = ['name','username'])
    return {"message": tweet_cursor}

@app.post("/probando")
async def root():
    tweet_cursor = client.get_users(usernames=['everllanos45'])
    return {"message": tweet_cursor}

@app.post("/getTweets/{tema}")
async def root(tema:str):
    tweets_json = []
    place = api.search_geo(query=tema, granularity="city")
    place_id = place[0].id
    searchs = api.search_tweets(q='place:%s' % place_id,geocode='10.46314,-73.253222,1000km', count='10')
    for tweet in searchs:
        tweetJson = tweet._json
        tweets_json.append(tweetJson)
    return {"message": tweets_json}