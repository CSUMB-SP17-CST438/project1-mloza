#run.py

from flask import Flask
from flask import request
import flask 
import tweepy
import os
import requests, json
import random

app = flask.Flask(__name__)

@app.route('/')  # Google "Python decorator" 
def index():
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET_KEY"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    
    api = tweepy.API(auth)
    
    results = api.search(q="sushi", lang="en")
    
    results = tweepy.Cursor(api.search, q="sushi", lang="en").items(1)
      
    return flask.render_template('twitterTest.html', public_tweets=results)
    # return "Hi"
    

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080))
)
