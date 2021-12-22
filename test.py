
import instaloader
from instaloader import exceptions as Exceptions
from instaloader import structures
import json
import os
import sys
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

os.chdir("tagged-stories")
# Instaloader Instance initiation
username = "229eaglemotion@gmail.com" # for scrapping, use dummy account
# username = "pif92@hotmail.com" # for scrapping, use dummy account
instance = instaloader.Instaloader()
instance.login(user=username, passwd="229motioneagle")
# instance.login(user=username, passwd="@Douke1987")
# instance.interactive_login(username=username)
account_to_mention = "229eaglemotion"
profile = instaloader.Profile.from_username(instance.context, username="229eaglemotion")
for story in instance.get_stories():
    for storyItem in story.get_items():
        storyItemJson = structures.get_json_structure(storyItem)
        logger.info(storyItemJson)
        for x in storyItemJson["node"]["tappable_objects"]:
            if x["__typename"] == "GraphTappableMention":
                if x["username"] == account_to_mention:
                    print ("ok")
                    owner = str(storyItemJson["node"]["owner"]["username"])
                    id = str(storyItemJson["node"]["id"])
                    file = owner + "-" + id + ".json"
                    if os.path.exists(file) == False:
                        f = open(file, "w")
                        f.write(json.dumps(storyItemJson))
                    else: 
                        print(f"Story Item {id} from username {owner} has already been processed")
                        logger.info(f"Story Item {id} from username {owner} has already been processed")
                else:
                    # print(f"No stories found mentionning {account_to_mention}")
                    logger.info(f"No stories found mentionning {account_to_mention}")





for story in stories:
            try:
                for storyItem in story.get_items():
                    storyItemJson  = structures.get_json_structure(storyItem)
                    for x in storyItemJson["node"]["tappable_objects"]:
                        if x["__typename"] == "GraphTappableMention":
                            if x["username"] == account_to_mention:
                                owner = str(storyItemJson["node"]["owner"]["username"])
                                id = str(storyItemJson["node"]["id"])
                                # temp = ".temp"
                                # file = temp + "/" + owner + "-" + id + ".json"
                                # if os.path.exists(file) == False:
                                for dir in [".temp", current_date_time, "latest"]:
                                    file = dir + "/" + owner + "-" + id + ".json"
                                    f = open(file, "w")
                                    f.write(json.dumps(storyItemJson))
                                    f.close()
            except (Exceptions.LoginRequiredException, Exceptions.PrivateProfileNotFollowedException) as err:
                logger.info(err)
                print (err)
                sys.exit(1)