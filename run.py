#run.py
# dynamically retrieves sushi queries from Twitter and Getty sushi images

from flask import Flask
from flask import request
import flask
import os
import requests, json
import requests_oauthlib
import random

app = flask.Flask(__name__)

@app.route('/')  # Google "Python decorator" 
def index():
    ###### GETTY API image setup
    url = "https://api.gettyimages.com/v3/search/images?fields=id,title,comp,referral_destinations&sort_order=best&phrase=sushi"
    my_headers = { "Api-Key": os.getenv("GETTY_KEY") }
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    randNum = random.randint(0, 29) #only 30 pictures are returned
    pic = json_body["images"][randNum]["display_sizes"][0]["uri"] #size comp

    
    ###### TWITTER/TWEEPY API setup
    url = "https://api.twitter.com/1.1/search/tweets.json?l=en&q=sushi&src=typd&count=50" #returns 50 tweets. default 15. also in English. default all langs.
    oauth = requests_oauthlib.OAuth1(
        os.getenv("CONSUMER_KEY"), 
        os.getenv("CONSUMER_SECRET_KEY"),
        os.getenv("ACCESS_TOKEN"),
        os.getenv("ACCESS_TOKEN_SECRET")
    )
    response = requests.get(url, auth=oauth)
    json_body =  response.json()
    randNum = random.randint(0, 49)
    text = json_body["statuses"][randNum]["text"] 
    name = json_body["statuses"][randNum]["user"]["name"]
    screen_name = json_body["statuses"][randNum]["user"]["screen_name"]
    idNum = json_body["statuses"][randNum]["id"]
    lang = json_body["statuses"][randNum]["user"]["lang"]
    while (lang != "en"):
        randNum = random.randint(0, 49)
        text = json_body["statuses"][randNum]["text"] 
        name = json_body["statuses"][randNum]["user"]["name"]
        screen_name = json_body["statuses"][randNum]["user"]["screen_name"]
        idNum = json_body["statuses"][randNum]["id"]
        lang = json_body["statuses"][randNum]["user"]["lang"]
    
    
    
      
    return flask.render_template('proj1.html', text=text, name=name, bg_image=pic, screen=screen_name, idNum=idNum)
    

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080))
)
