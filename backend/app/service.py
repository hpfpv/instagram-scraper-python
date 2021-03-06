import json
import os
from pymongo import MongoClient
import logging
import uuid
from datetime import datetime

from instaScraper import get_stories_tagged, download_stories
from instaScraper.modules.download import profile_picture, story_media
from instaScraper.modules.stories import get_followers_stories, check_for_new_stories, story_time_str

mongoUser = os.environ['MONGO_USER']
mongoPassword = os.environ['MONGO_PWD']
mongoURL = os.environ['MONGO_URL']
dbConnectString = "mongodb://" + mongoUser + ":" + mongoPassword + "@" + mongoURL + ":27017"

mongo = MongoClient(dbConnectString)
logging.basicConfig(filename="/app/logging/instastories-api-log", level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

instastoriesDb = mongo["instastories"]
eventsCollection = instastoriesDb["events"]

def getStoriesTagged(requestId, account_to_mention):
    try:
        storiesJson = check_for_new_stories(requestId, account_to_mention)
    except Exception as e:
        logger.info(e)
        response = eventsCollection.update_one(
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
        response = eventsCollection.update_one(
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

    log["status"] = "completed"
    log["record"] = record
    
    logger.info(json.dumps(log))
    print(json.dumps(log))

    eventsCollection.insert_one(record)  

    getStoriesTagged(requestId, account_to_mention)
    
    responseBody = {
        'requestId' : requestId
    }

    return  json.dumps(responseBody) 


def retrieveStories(requestId):
    log = {}
    log["function"] = "retrieve_stories"

    try:
        result = eventsCollection.find_one({"requestId" : requestId})
    except Exception as err:
        log["status"] = f"error: {str(err)}"
        response = {'requestId': requestId, 'time': "N/A", 'account': "N/A", 'request_state': "error"}
        logger.info(json.dumps(log))
        print(json.dumps(log))
        return json.dumps(response)
    else:
        if result:
            if result['request_state'] == 'completed':
                response = {'requestId': result['requestId'], 'time': result['time'], 'account': result['account'], 'request_state': result['request_state'], 'stories': result['stories']}
                log["status"] = "completed"
                log["response"] = response
                logger.info(json.dumps(log))
                print(json.dumps(log))
            else:
                response = {'requestId': result['requestId'], 'time': result['time'], 'account': result['account'], 'request_state': result['request_state']}
                log["status"] = "completed"
                log["response"] = response
                logger.info(json.dumps(log))
                print(json.dumps(log))
            return json.dumps(response)