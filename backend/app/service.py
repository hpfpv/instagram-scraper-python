import json
import os
from pymongo import MongoClient
import logging
import uuid
from datetime import datetime

from instaScraper import get_stories_tagged, download_stories
from instaScraper.modules.download import profile_picture, story_media
from instaScraper.modules.stories import get_followers_stories, check_for_new_stories, story_time_str

mongoUser = os.environ.get('MONGO_USER')
mongoPassword = os.environ.get('MONGO_PWD')
mongoURL = os.environ.get('MONGO_URL')

mongo = MongoClient(f"mongodb://{mongoUser}:{mongoPassword}@{mongoURL}:27017")

logger = logging.getLogger()
logger.setLevel(logging.INFO)
eventsTable = mongo.instastories.events

def getStoriesTagged(requestId, account_to_mention):
    try:
        storiesJson = check_for_new_stories(account_to_mention)
    except Exception as e:
        logger.info(e)
        response = eventsTable.update_one(
            {
                'requestId': requestId,
            },
            {"$set": {
                "request_state": "error"
                }
            }
        )
        response = {}
        response["Update"] = "Success"
    else:
        response = eventsTable.update_one(
            {
                'requestId': requestId,
            },
            {"$set": {
                "request_state": "completed", 
                "stories": json.dumps(storiesJson)
                }
            }
        )
        
        response = {}
        response["Update"] = "Success"

        return response

def recordEvents(account_to_mention):
    log = {}
    log["function"] = "record_events"
    
    requestId = str(uuid.uuid4())
    record = {
        "requestId" : requestId ,
        "time" : str(datetime.now()) ,
        "account" :  account_to_mention ,
        "request_state": "in-progress" ,
    }

    log["message"] = json.dumps(record)
    logger.info(json.dumps(log))

    eventsTable.insert_one(record)  

    getStoriesTagged(requestId, account_to_mention)
    
    responseBody = {
        'requestId' : requestId
    }

    return  json.dumps(responseBody) 


def retrieveStories(requestId):
    response = mongo.find_one({"requestId" : requestId})

    return json.dumps(response)