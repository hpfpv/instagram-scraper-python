import requests
import urllib.request
import os
import json
import logging
from functools import lru_cache
from pymediainfo import MediaInfo

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# @lru_cache(maxsize=128)
def profile_picture(requestId, url, filename):
    log = {}
    log["function"] = "profile_picture"
    log["requestId"] = requestId

    dir = '/app/data/profile'
    if os.path.exists(dir) == False:
        os.mkdir(dir)

    name = f"{dir}/{filename}.jpg"
    if os.path.exists(name) == False:
        log["status"] = "Downloading profile picture"
        logger.info(json.dumps(log))
        try:
            p = requests.get(url, allow_redirects=True)
            open(name, 'wb').write(p.content)
        except Exception as err:
            log["status"] = f"error: {str(err)}"
            logger.info(json.dumps(log))
        else:
            log["status"] = "completed"
            logger.info(json.dumps(log))
        

# @lru_cache(maxsize=128)
def story_media(requestId, video, display, is_video, filename):
    
    log = {}
    log["function"] = "story_media"
    log["requestId"] = requestId

    dir = '/app/data/media'
    if os.path.exists(dir) == False:
        os.mkdir(dir)

    video_file = f"{dir}/{filename}.mp4"
    display_file = f"{dir}/{filename}.jpg"

    if is_video:
        if os.path.exists(video_file) == False:
            log["status"] = "Downloading story media"
            logger.info(json.dumps(log))
            try:
                r = requests.get(video, allow_redirects=True)
                open(video_file, 'wb').write(r.content)
            except Exception as err:
                log["status"] = f"error: {str(err)}"
                logger.info(json.dumps(log))
            else:
                log["status"] = "completed"
                logger.info(json.dumps(log))
        if os.path.exists(display_file) == False:
            try:
                r2 = requests.get(display, allow_redirects=True)
                open(display_file, 'wb').write(r2.content)
            except Exception as err:
                log["status"] = f"error: {str(err)}"
                logger.info(json.dumps(log))
            else:
                log["status"] = "completed"
                logger.info(json.dumps(log))

        # story_duration = MediaInfo.parse(video_file).tracks[0].duration
    else:
        if os.path.exists(display_file) == False:
            log["status"] = "Downloading story media"
            logger.info(json.dumps(log))
            try:
                r3 = requests.get(display, allow_redirects=True)
                open(display_file, 'wb').write(r3.content)
            except Exception as err:
                log["status"] = f"error: {str(err)}"
                logger.info(json.dumps(log))
            else:
                log["status"] = "completed"
                logger.info(json.dumps(log))
            
        # story_duration = 5000
    
    # return story_duration
