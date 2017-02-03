#run.py

from flask import Flask
from flask import request
import flask 
import tweepy
import os
import requests, json
import random

app = flask.Flask(__name__)

CONSUMER_KEY = '7jLLLL9umXTzcehteOGYi64DB'
CONSUMER_SECRET_KEY = 'X3Rnv5oi6nc1P5wLWsgDRiKbi0rYhrv8V2bfG20CKaml4MaYpt'

ACCESS_TOKEN = '1518510956-T4xcbHXHnqokR75OJCtxqwhLHal4mSswfVfmstL'
ACCESS_TOKEN_SECRET = 'EiZTFhSXUAFhhSrslbfH6nHygVIcGjFaKFClVU5arOUk4'


@app.route('/')  # Google "Python decorator" 
def index():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth)
    
    results = api.search(q="sushi", lang="en")
    
    results = tweepy.Cursor(api.search, q="sushi", lang="en").items(1)
      
    return flask.render_template('twitterTest.html', public_tweets=results)
    

app.run(
    port=int(os.getenv('Port', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    #=True #allows me to refresh the page for changes
)
