#run.py

from flask import Flask
from flask import request
import flask 
import tweepy
import os
import random

app = flask.Flask(__name__)

CONSUMER_KEY = '7jLLLL9umXTzcehteOGYi64DB'
CONSUMER_SECRET_KEY = 'X3Rnv5oi6nc1P5wLWsgDRiKbi0rYhrv8V2bfG20CKaml4MaYpt'

ACCESS_TOKEN = '1518510956-T4xcbHXHnqokR75OJCtxqwhLHal4mSswfVfmstL'
ACCESS_TOKEN_SECRET = 'EiZTFhSXUAFhhSrslbfH6nHygVIcGjFaKFClVU5arOUk4'


#urllib3.disable_warnings()


@app.route('/')  # Google "Python decorator" 
def index():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth)
    
    
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print tweet.text
    #tweets = tweepy.api.public_timeline();
    
    results = api.search(q="sushi", lang="en")
    # if (not tweet.retweeted) and ('RT @' not in tweet.text):
    
    results = tweepy.Cursor(api.search, q="sushi", lang="en").items(1)
    # tweet = api.get_status(results)
    # user_id = tweet.user.id
      
    print "This is a debug statement!"
   # return "Hello, world! :)"
    return flask.render_template('twitterTest.html', public_tweets=results)
    

app.run(
    port=int(os.getenv('Port', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True #allows me to refresh the page for changes
)


#import boto
#from boto.s3.connection import S3Connection
#s3 = S3Connection(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET_KEY'])



#client = Client(CONSUMER_KEY, CONSUMER_SECRET)
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)


# app.config.setdefault('TWEEPY_CONSUMER_KEY', CONSUMER_KEY)
# app.config.setdefault('TWEEPY_CONSUMER_SECRET', CONSUMER_SECRET_KEY)
# app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', ACCESS_TOKEN)
# app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', ACCESS_TOKEN_SECRET)

#tweepy = Tweepy(app)

# get search term from querystring 'q'
    # query = request.args.get('q','#redburns')
    

   # user = api.get_user("twitter")
    
    
    
    
    
    # tweet = client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')
    # print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':'))
    
    # # Show rate limit status for this application
    # status = client.rate_limit_status()
    # print status['resources']['search']