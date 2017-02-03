#run.py

from flask import Flask
from flask import request
import flask 
import tweepy
import os
import requests, json
import requests_oauthlib
import random

app = flask.Flask(__name__)

@app.route('/')  # Google "Python decorator" 
def index():
    ###### GETTY API image setup
    url = "https://api.gettyimages.com/v3/search/images?fields=id,title,comp,referral_destinations&sort_order=best&phrase=sushi"
    # my_headers = { "Api-Key": os.getenv("GETTY_KEY") }
    
    my_headers = { "Api-Key": "tt9qedn4c4p439qn4w7rkjy3" }
    
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    randNum = random.randint(0, 29)
    print "RANDOM NUMBER: " + str(randNum)
    pic = json_body["images"][randNum]["display_sizes"][0]["uri"]

    
    ###### TWITTER/TWEEPY API setup
    url = "https://api.twitter.com/1.1/search/tweets.json?l=en&q=sushi&src=typd&count=50" #returns 50 tweets. default 15. also in English. default all langs.
    # oauth = requests_oauthlib.OAuth1(
    #     os.getenv("CONSUMER_KEY"), 
    #     os.getenv("CONSUMER_SECRET_KEY"),
    #     os.getenv("ACCESS_TOKEN"),
    #     os.getenv("ACCESS_TOKEN_SECRET")
    # )
    
    oauth = requests_oauthlib.OAuth1(
        "7jLLLL9umXTzcehteOGYi64DB", 
        "X3Rnv5oi6nc1P5wLWsgDRiKbi0rYhrv8V2bfG20CKaml4MaYpt",
        "1518510956-T4xcbHXHnqokR75OJCtxqwhLHal4mSswfVfmstL",
        "EiZTFhSXUAFhhSrslbfH6nHygVIcGjFaKFClVU5arOUk4"
    )
    
    response = requests.get(url, auth=oauth)
    json_body =  response.json()
    randNum = random.randint(0, 49)
    text = json_body["statuses"][randNum]["text"] 
    name = json_body["statuses"][randNum]["user"]["name"]
    # print "LANGUAGE: " +  json_body["statuses"][randNum]["user"]["lang"]
    lang = json_body["statuses"][randNum]["user"]["lang"]
    while (lang != "en"):
        randNum = random.randint(0, 49)
        print "WHILING RANDOM: " + str(randNum)
        text = json_body["statuses"][randNum]["text"] 
        name = json_body["statuses"][randNum]["user"]["name"]
        lang = json_body["statuses"][randNum]["user"]["lang"]
    # print "LANGUAGE AGAIN: " +  json_body["statuses"][randNum]["user"]["lang"]
    print text
    print json_body["statuses"][randNum]["user"]["screen_name"]
    
    
    
      
    return flask.render_template('proj1.html', text=text, name=name, bg_image=pic)
    

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080))
)
