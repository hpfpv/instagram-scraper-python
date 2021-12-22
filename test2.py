# import json
# from datetime import datetime, date
import os
import instaloader
from instaloader import exceptions as Exceptions
from instaloader import structures
import json
import os
import sys
import logging
from timeit import repeat
from functools import lru_cache
import requests
# import shutil
dict = {
   "node":{
      "audience":"MediaAudience.BESTIES",
      "__typename":"GraphStoryImage",
      "id":"2728636018268262094",
      "dimensions":{
         "height":1334,
         "width":750
      },
      "display_resources":[
         {
            "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p640x640/267308619_2023823017795489_3528092255044060660_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=zFdC-OLn85sAX8Hd4oF&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT9WQ1rvK0PaivucPTQD9ZLAB5wU7BkZuqS0HpNxq32wDg&oe=61BB6DB8&_nc_sid=21929d",
            "config_width":640,
            "config_height":1138
         },
         {
            "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-15/e35/267308619_2023823017795489_3528092255044060660_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=zFdC-OLn85sAX8Hd4oF&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT-JcduvLJD78C_6UTAFVYk0w7EWizMXHRC5kEXXtezuhQ&oe=61BB08B0&_nc_sid=21929d",
            "config_width":750,
            "config_height":1334
         },
         {
            "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-15/e35/267308619_2023823017795489_3528092255044060660_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=zFdC-OLn85sAX8Hd4oF&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT-JcduvLJD78C_6UTAFVYk0w7EWizMXHRC5kEXXtezuhQ&oe=61BB08B0&_nc_sid=21929d",
            "config_width":1080,
            "config_height":1920
         }
      ],
      "display_url":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-15/e35/267308619_2023823017795489_3528092255044060660_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=zFdC-OLn85sAX8Hd4oF&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT-JcduvLJD78C_6UTAFVYk0w7EWizMXHRC5kEXXtezuhQ&oe=61BB08B0&_nc_sid=21929d",
      "media_preview":"ABgq5+iiipNhKKWigAopKdxjvn6f1z/SgBKKSigQlFJS0xBRSUUAf//Z",
      "gating_info":None,
      "fact_check_overall_rating":None,
      "fact_check_information":None,
      "sharing_friction_info":{
         "should_have_sharing_friction":False,
         "bloks_app_url":None
      },
      "media_overlay_info":None,
      "sensitivity_friction_info":None,
      "taken_at_timestamp":1639498780,
      "expiring_at_timestamp":1639585180,
      "story_cta_url":None,
      "story_view_count":0,
      "is_video":False,
      "owner":{
         "id":"6016351201",
         "profile_pic_url":"https://instagram.fcoo1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/23161181_2012477095700409_3013302832435560448_n.jpg?_nc_ht=instagram.fcoo1-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=D3n2y4X33S8AX-19tOj&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT_yWq4tmclGP33-zEfphF_b_Xg1dTedXHmXLUCMDxj3Eg&oe=61C01281&_nc_sid=21929d",
         "username":"229eaglemotion",
         "followed_by_viewer":False,
         "requested_by_viewer":False
      },
      "tracking_token":"eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMDkxNjZjZWEzYjk5NDNiMjg2MzYwODMzM2NhYzdiODgyNzI4NjM2MDE4MjY4MjYyMDk0Iiwic2VydmVyX3Rva2VuIjoiMTYzOTUwODkzMjUyMXwyNzI4NjM2MDE4MjY4MjYyMDk0fDYwMTYzNTEyMDF8YWY3YTdlZGY4YWJjYjAzNTU0MzE1OTYyNzAyZmVmZjQzNDUzNGQ1M2EyNTk5MTFhMzJhZGNjOTZkMmUxMzZjMiJ9LCJzaWduYXR1cmUiOiIifQ==",
      "tappable_objects":[
         {
            "__typename":"GraphTappableMention",
            "x":0.49341049127718706,
            "y":0.6786866379831471,
            "width":0.159481896005465,
            "height":0.032102154141250006,
            "rotation":0.0,
            "custom_title":None,
            "attribution":None,
            "username":"hpfpv",
            "full_name":"H. Pierre-Francois",
            "is_private":True
         }
      ],
      "story_app_attribution":None,
      "edge_media_to_sponsor_user":{
         "edges":[
            
         ]
      },
      "muting_info":None
   },
   "instaloader":{
      "version":"4.8.2",
      "node_type":"StoryItem"
   }
}

# # # node = dict["node"]
# # # tapable = node["tappable_objects"]
# # # print (type(dict))
# # # for x in dict["node"]["tappable_objects"]:
# # #    if x["username"] == "hpfpv":
# # #       owner = dict["node"]["owner"]["username"]
# # #       id = dict["node"]["id"]
# # #       f = open(f"{owner}-{id}.json", "w")
# # #       f.write(json.dumps(dict))

# # # nowt = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
# # # os.chdir("tagged-stories")
# # # file = ".temp/y3"
# # # if os.path.exists(file) == False:
# # #     if os.path.exists("latest"):
# # #         shutil.rmtree("latest")
# # #     os.mkdir("latest")
# # #     os.mkdir(nowt)
# # #     for dir in [".temp", nowt, "latest"]:
# # #         f = open(f"{dir}/y3", "w")
# # #         f.write("ok3")
# # #         f.close()


# # import instaloader
# # from instaloader import exceptions as Exceptions
# # from instaloader import structures
# # import json
# # import os
# # import shutil
# # import random
# # import sys
# # from datetime import datetime
# # import logging

# # logger = logging.getLogger()
# # logger.setLevel(logging.INFO)

# # # Information about account to be featured
# # account_to_mention = "229eaglemotion"

# # # Scraper accounts
# # scrapers = [
# #     {"username":"email1@email.com",
# #     "password":"password"
# #     },
# #     {"username":"email2@email.com",
# #     "password":"password"
# #     },
# #     {"username":"email3@email.com",
# #     "password":"password"
# #     },
# #     {"username":"email4@email.com",
# #     "password":"password"
# #     },
# #     {"username":"email5@email.com",
# #     "password":"password"
# #     }
# # ]
# # # Instaloader Instances initiation

# # random_scraper= random.choice(scrapers)

# # username = random_scraper["username"] 
# # password = random_scraper["password"]

# # print (random_scraper)
# # print (username, password)
# # # instance = instaloader.Instaloader()
# # # instance.login(user=username, passwd=password)



# import json
# import random
# # Search and return active scraper randomly
# def get_scraper():
#     with open(f"insta-scraper/assets/scrapers.json") as f:
#         data = f.read()
#     scrapers = json.loads(data)
#     active = False
#     while active == False:
#         random_scraper= random.choice(scrapers)
#         if random_scraper["status"] == "active":
#             active = True
#             username = random_scraper["username"] 
#             password = random_scraper["password"]

#     scraper = {
#         "username": username,
#         "password": password,
#     }
#     return scraper
    
# # Instaloader Instances initiation
# @lru_cache
# def get_instance():
#     """
#         Creates Instaloader instance with a random scraper from the scraper List
#         Returns instance
#     """
#     success = False
#     while success == False:
#         scraper = get_scraper()
#         username = str(scraper['username'])
#         password = str(scraper['password'])
#         try:
#             random_instance = instaloader.Instaloader()
#             random_instance.login(user=username, passwd=password)
#         except (Exceptions.ConnectionException, Exceptions.BadCredentialsException, Exceptions.InvalidArgumentException) as err:
#             message = {
#                 "function": "get_instance",
#                 "error": str(err),
#                 "details": f"scraper: {username}"
#             }
#             print (json.dumps(message))
#             # logger.info(json.dumps(message))
#         else:
#             success = True
#             message = {
#                 "function": "get_instance",
#                 "status": "instance is successfully created",
#                 "details": f"scraper: {username}"
#             }
#             print (json.dumps(message))
#             # logger.info(json.dumps(message))

#     return random_instance
# instance = get_instance()

# # print(get_instance.cache_info())
# @lru_cache
# def get_followers(instance, account_to_mention):
#     """
#         Returns a List of userIds of specified account followers
#         Uses its own Instaloader instance since account needs to be logged in to retrieve followers
#         Take an instance and the account as parameters
#     """

#     try:
#         profile = instaloader.Profile.from_username(instance.context, username=account_to_mention)
#         followers_iterator = profile.get_followers()
#     except (Exceptions.ProfileNotExistsException) as err:
#         message = {
#             "function": "get_followers",
#             "error": str(err)
#         }
#         # logger.info(json.dumps(message))
#         print (json.dumps(message))
#         sys.exit(1)

#     userIds = []
#     for account in followers_iterator:
#         userIds.append(account.userid)

#     return userIds
# get_followers(instance, "229eaglemotion")
# get_followers(instance, "229eaglemotion")
# print(get_followers.cache_info())

# # setup_code = "from __main__ import get_followers, get_instance"
# # stmt = "get_followers(get_instance(), '229eaglemotion')"
# # times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=3)
# # print(f"Minimum execution time: {min(times)}")

# # success = False
# #     while success == False:
# #         scraper = get_scraper()
# #         username = str(scraper['username'])
# #         password = str(scraper['password'])
# #         random_instance = instaloader.Instaloader()
# #         try:
# #             random_instance.login(user=username, passwd=password)
# #         except Exceptions.ConnectionException as err:
# #             message = {
# #                 "function": "get_instance",
# #                 "error": str(err),
# #                 "details": f"scraper: {username}"
# #             }
# #             logger.info(json.dumps(message))
# #             print (json.dumps(message))
# #         else:
# #             success = True
# #             message = {
# #                 "function": "get_instance",
# #                 "status": "instance is successfully created",
# #                 "details": f"scraper: {username}"
# #             }
# #             logger.info(json.dumps(message))
# #             print (json.dumps(message))

# #     return random_instance
import json
display = [
            {
               "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p640x640/268430240_648286416303865_1516137624972219047_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=pTOrC1zKXpsAX_N7qfJ&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT_XX1k24Ghjy5dQZg7ycTZr-BKh0w6MKctZuRXwoddhuQ&oe=61BD673A&_nc_sid=21929d",
               "config_width":640,
               "config_height":1138
            },
            {
               "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-15/e35/268430240_648286416303865_1516137624972219047_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=pTOrC1zKXpsAX_N7qfJ&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT_3KBHeoiLorAPd-prRBIDCuggp92dnq5mI_9qAmJCURQ&oe=61BDAA54&_nc_sid=21929d",
               "config_width":750,
               "config_height":1334
            },
            {
               "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-15/e35/268430240_648286416303865_1516137624972219047_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=pTOrC1zKXpsAX_N7qfJ&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT_3KBHeoiLorAPd-prRBIDCuggp92dnq5mI_9qAmJCURQ&oe=61BDAA54&_nc_sid=21929d",
               "config_width":1080,
               "config_height":1920
            }
         ]

# def profile_picture(url, filename):
#     os.chdir("templates/img/profile")
#     if os.path.exists("{filename}.jpg") == False:
#         with open(f"{filename}.jpg", 'wb') as handle:
#             response = requests.get(url, stream=True)

#             if not response.ok:
#                 print(response)

#             for block in response.iter_content(1024):
#                 if not block:
#                     break

#                 handle.write(block)
def profile_picture(url, filename):
    dir = 'templates/img/profile'
    name = f"{dir}/{filename}.jpg"
    if os.path.exists(name) == False:
        with open(name, 'wb') as handle:
            response = requests.get(url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
    return name

# def story_media(url, is_video, filename):
#     os.chdir("instaScraper/tagged-stories/media")
#     if is_video:
#         name = f"{filename}.mp4"
#     else:
#         name = f"{filename}.jpg"
#     if os.path.exists(name) == False:
#         with open(name, 'wb') as handle:
#             response = requests.get(url, stream=True)

#             if not response.ok:
#                 print(response)

#             for block in response.iter_content(1024):
#                 if not block:
#                     break
                
#                 handle.write(block)
    
def story_media(url, is_video, filename):
    dir = 'instaScraper/tagged-stories/media'
    if is_video:
        name = f"{dir}/{filename}.mp4"
    else:
        name = f"{dir}/{filename}.jpg"
    if os.path.exists(name) == False:
        with open(name, 'wb') as handle:
            response = requests.get(url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break
                
                handle.write(block)
    return name
    
s = story_media("https://instagram.fcoo1-2.fna.fbcdn.net/v/t50.12441-16/269365819_658950295120078_8490227802104295312_n.mp4?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=110&_nc_ohc=OvwbapQho2kAX8A9d_H&edm=AHlfZHwBAAAA&ccb=7-4&oe=61BC767D&oh=00_AT8u6j1lzd0RWo2gZ5UoE8kycM0eR25A5rGs-l2098NsIg&_nc_sid=21929d", True, "test7")      
p = profile_picture("https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-19/s150x150/69239464_2715622995147419_7869939009076592640_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=111&_nc_ohc=a9xERC0RLVoAX-x8v5H&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT8te9K7gpUf-7i1mgp3326Nu3CKwQvDfOYcShd_zswl8A&oe=61C251BA&_nc_sid=21929d", "hpfpv")

print (s)
print(p)


#     stories = [
        #    {
        #       "node":{
        #          "audience":"MediaAudience.DEFAULT",
        #          "__typename":"GraphStoryVideo",
        #          "id":"2729560035625431939",
        #          "dimensions":{
        #             "height":612,
        #             "width":612
        #          },
        #          "display_resources":[
        #             {
        #                "src":"https://static.cdninstagram.com/rsrc.php/null.jpg",
        #                "config_width":640,
        #                "config_height":640
        #             },
        #             {
        #                "src":"https://static.cdninstagram.com/rsrc.php/null.jpg",
        #                "config_width":750,
        #                "config_height":750
        #             },
        #             {
        #                "src":"https://static.cdninstagram.com/rsrc.php/null.jpg",
        #                "config_width":1080,
        #                "config_height":1080
        #             }
        #          ],
        #          "display_url":"https://static.cdninstagram.com/rsrc.php/null.jpg",
        #          "media_preview":"ABgq5miiloASiiigAooooAKKKKACiiigAooooA//2Q==",
        #          "gating_info":None,
        #          "fact_check_overall_rating":None,
        #          "fact_check_information":None,
        #          "sharing_friction_info":{
        #             "should_have_sharing_friction":False,
        #             "bloks_app_url":None
        #          },
        #          "media_overlay_info":None,
        #          "sensitivity_friction_info":None,
        #          "taken_at_timestamp":1639608932,
        #          "expiring_at_timestamp":1639695332,
        #          "story_cta_url":None,
        #          "story_view_count":None,
        #          "is_video":True,
        #          "owner":{
        #             "id":"255391219",
        #             "profile_pic_url":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t51.2885-19/s150x150/69239464_2715622995147419_7869939009076592640_n.jpg?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=111&_nc_ohc=VgYr056cZzYAX_4euMh&edm=AHlfZHwBAAAA&ccb=7-4&oh=00_AT8sRl42nIm72B95gthel8tuUe6BcPFrV7S-dqlq4R0wEw&oe=61C251BA&_nc_sid=21929d",
        #             "username":"hpfpv",
        #             "followed_by_viewer":False,
        #             "requested_by_viewer":False
        #          },
        #          "tracking_token":"eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTE2MjQzMDZjOTAyNGZmY2JiNTk3NzVlZmVkNThkN2EyNzI5NTYwMDM1NjI1NDMxOTM5Iiwic2VydmVyX3Rva2VuIjoiMTYzOTYwOTAzMTc0MXwyNzI5NTYwMDM1NjI1NDMxOTM5fDUwNzU0MjIyNzA3fDZhNTNhZjVjMDIyM2Q3ZTQ1MWViYzk0Y2QyZTVjNDE0M2UzNWVlOWY1ZWIzMTUzZWE2YzcwZjJmMjNmMDNmNzEifSwic2lnbmF0dXJlIjoiIn0=",
        #          "has_audio":True,
        #          "overlay_image_resources":None,
        #          "video_duration":1.301,
        #          "video_resources":[
        #             {
        #                "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t50.12441-16/269365819_658950295120078_8490227802104295312_n.mp4?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=110&_nc_ohc=OvwbapQho2kAX8A9d_H&edm=AHlfZHwBAAAA&ccb=7-4&oe=61BC767D&oh=00_AT8u6j1lzd0RWo2gZ5UoE8kycM0eR25A5rGs-l2098NsIg&_nc_sid=21929d",
        #                "config_width":480,
        #                "config_height":480,
        #                "mime_type":"video/mp4; codecs=\"avc1.42E01E, mp4a.40.2\"",
        #                "profile":"BASELINE"
        #             }
        #          ],
        #          "tappable_objects":[
        #             {
        #                "__typename":"GraphTappableMention",
        #                "x":0.5,
        #                "y":0.27811094452773605,
        #                "width":0.32007999999999903,
        #                "height":0.044977511244377,
        #                "rotation":0.0,
        #                "custom_title":None,
        #                "attribution":None,
        #                "username":"229eaglemotion",
        #                "full_name":"229eaglemotion",
        #                "is_private":False
        #             }
        #          ],
        #          "story_app_attribution":None,
        #          "edge_media_to_sponsor_user":{
        #             "edges":[
                    
        #             ]
        #          },
        #          "muting_info":None
        #       },
        #       "instaloader":{
        #          "version":"4.8.2",
        #          "node_type":"StoryItem"
        #       }
        #    }
        # ]