from flask import Flask, jsonify, request, Response, send_file
import json
from flask_cors import CORS
import logging

import service

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# app = Flask(__name__, 
#             static_url_path='', 
#             static_folder='web/static',
#             template_folder='web/templates')
app = Flask(__name__)
CORS(app)

@app.route("/")
def healthCheckResponse():
    return jsonify({"message" : "Nothing here, used for health check."})
        
@app.route("/<account_to_mention>/stories", methods=['GET', 'POST'])
def recordEvents(account_to_mention):
    log = {}
    log["function"] = "recordEvents"

    serviceResponse = service.recordEvents(account_to_mention)
    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse

@app.route("/<requestId>", methods=['GET', 'POST'])
def retrieveStories(requestId):
    log = {}
    log["function"] = "retrieveStories"

    serviceResponse = service.retrieveStories(requestId)
    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse

@app.route("/profile/<file>")
def getProfile(file):
    profile = f'data/profile/{file}'
    return send_file(profile)

@app.route("/media/<file>")
def getMedia(file):
    profile = f'data/media/{file}'
    return send_file(profile)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)