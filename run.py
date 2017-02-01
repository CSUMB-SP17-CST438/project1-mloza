#run.py

import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/')  # Google "Python decorator" 
def index():
    print "This is a debug statement!"
    return "Hello, world! :)"
    

app.run(
    port=int(os.getenv('Port', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True #allows me to refresh the page for changes
)