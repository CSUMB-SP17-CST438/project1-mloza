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
    ###### GETTY API image setup
    url = "https://api.gettyimages.com/v3/search/images?fields=id,title,comp,referral_destinations&sort_order=best&phrase=sushi"
    my_headers = { "Api-Key": os.getenv("GETTY_KEY") }
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    pic = json_body["images"][random.randrange(0, 30)]["display_sizes"][0]["uri"]
    # print pic
    
    
    ###### TWITTER/TWEEPY API setup
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET_KEY"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    results = api.search(q="sushi", lang="en")
    results = tweepy.Cursor(api.search, q="sushi", lang="en").items(1)
    
    
      
    return flask.render_template('twitterTest.html', public_tweets=results, bg_image=pic)
    # return "Hi"
    

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080))
)
