
from summarizer import textrank
from flask import Flask, jsonify, request
import requests
from slacker import Slacker
import json
import os
from config import *

slack = Slacker(keys["slack"])
app = Flask(__name__)

@app.route("/slackGet", methods=['GET'])
def SlackGet():
	a =  "Get REquest"
	return a

@app.route("/slack", methods=['POST'])
def slackReq(): 
	req_data = request.form
	return req_data['token']

if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
