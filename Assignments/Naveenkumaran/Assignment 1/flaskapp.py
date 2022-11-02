from __future__ import print_function 
import sys
from datetime import datetime
from flask import Flask,redirect
import emoji
from urllib.request import urlopen
app = Flask(__name__)

@app.route("/")
def home():
    date = datetime.now().strftime("%H:%M:%S")
    return 'Time: %s' % str(date) 

@app.route("/emoji/")
def emojiPage():
    return emoji.emojize(":grinning_face_with_big_eyes:")

@app.route("/urllib/")
def pillowpkg():
    page = urlopen("http://geeksforgeeks.org/")
    return 'Url Package : %s '%str(page.headers)

@app.route('/print/')
def print_console():
    print('Assignment 1 id done', file=sys.stderr)
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)