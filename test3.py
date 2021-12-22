# import json

# dict = [
#             {
#                "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t50.12441-16/269365819_658950295120078_8490227802104295312_n.mp4?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=110&_nc_ohc=OvwbapQho2kAX8A9d_H&edm=AHlfZHwBAAAA&ccb=7-4&oe=61BC767D&oh=00_AT8u6j1lzd0RWo2gZ5UoE8kycM0eR25A5rGs-l2098NsIg&_nc_sid=21929d",
#                "config_width":480,
#                "config_height":480,
#                "mime_type":"video/mp4; codecs=\"avc1.42E01E, mp4a.40.2\"",
#                "profile":"BASELINE"
#             },
#             {
#                "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t50.12441-16/269365819_658950295120078_8490227802104295312_n.mp4?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=110&_nc_ohc=OvwbapQho2kAX8A9d_H&edm=AHlfZHwBAAAA&ccb=7-4&oe=61BC767D&oh=00_AT8u6j1lzd0RWo2gZ5UoE8kycM0eR25A5rGs-l2098NsIg&_nc_sid=21929d",
#                "config_width":480,
#                "config_height":480,
#                "mime_type":"video/mp4; codecs=\"avc1.42E01E, mp4a.40.2\"",
#                "profile":"BASELINE"
#             },
#             {
#                "src":"https://instagram.fcoo1-2.fna.fbcdn.net/v/t50.12441-16/269365819_658950295120078_8490227802104295312_n.mp4?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=110&_nc_ohc=OvwbapQho2kAX8A9d_H&edm=AHlfZHwBAAAA&ccb=7-4&oe=61BC767D&oh=00_AT8u6j1lzd0RWo2gZ5UoE8kycM0eR25A5rGs-l2098NsIg&_nc_sid=21929d",
#                "config_width":480,
#                "config_height":480,
#                "mime_type":"video/mp4; codecs=\"avc1.42E01E, mp4a.40.2\"",
#                "profile":"BASELINE"
#             }
            
#          ]
# best = dict[0]["src"]
# print (best)


# <div class="col-md-4 border border-info"  >
#                 <p style="font-size: 24px" id="story_owner"><strong>{{ story.story_owner }}</strong></p>
#                 <br>
#                 <div class="flex w-full h-screen">
#                     <div class="w-32 h-32 rounded-full conic-gradient relative">
#                         <img class="rounded-full w-full h-full bg-white" src="{{ story.path_to_profile_pic }}" id="story_owner_profile_pic" alt="">
#                     </div>
#                 </div>
#                 <br>
#                 <br>
#                 {% if story.is_video == True %}
#                     <div>
#                         <video controls width="300" autoplay>
#                             <source src="{{ story.path_to_media}}"
#                                     type="video/mp4" id="story_video"> 
#                         </video>
#                     </div>
#                 {% else %}
#                     <div>
#                         <img src="{{ story.path_to_media }}" id="story_image" align="center"/>
#                     </div>
#                 {% endif %} 
#             </div>

def story_time_str(story_time_taken):
    import time
    import datetime 

    response = ""
    story_time = story_time_taken
    ct = datetime.datetime.now()

    timeago = (ct - story_time).total_seconds()
    day = int(timeago / (24 * 3600))
    hour = int(((timeago / (24 * 3600) - day) * 24))
    minutes = int((((timeago / (24 * 3600) - day) * 24) - hour) * 60)
    if day > 0 :
        if day == 1:
            response += f"{day} day"
        else:
            response += f"{day} days"

        if hour > 0:
            if hour == 1:
                response += f", {hour} hour"
            else:
                response += f", {hour} hours"
        if minutes > 0:
            response += f", {minutes} min"
    else:
        if hour > 0:
            response += f"{hour} hours"
            if minutes > 0:
                response += f", {minutes} min"
        else:
            response += f"{minutes} min"

    return response

import requests
import os
from functools import lru_cache
from pymediainfo import MediaInfo
def story_media(video, display, is_video, filename):
    
    dir = ''
    video_file = f"{filename}.mp4"
    display_file = f"{filename}.jpg"
    print(video_file, display_file)
    if is_video:
        if os.path.exists(video_file) == False:
            with open(video_file, 'wb') as handle:
                response = requests.get(video, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break
                handle.write(block)
                
        # if os.path.exists(display_file) == False:
        #     with open(display_file, 'wb') as handle:
        #         response = requests.get(display, stream=True)

        #         if not response.ok:
        #             print(response)

        #         for block in response.iter_content(1024):
        #             if not block:
        #                 break
        #         handle.write(block)
        # get story duration

        story_duration = MediaInfo.parse(video).tracks[0].duration
    else:
        if os.path.exists(display_file) == False:
            with open(display_file, 'wb') as handle:
                response = requests.get(display, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break
                handle.write(block)
        story_duration = 5000
    
    return story_duration

test = story_media("https://instagram.fcoo1-2.fna.fbcdn.net/v/t50.12441-16/269674275_1051599902298481_5926364055401693769_n.mp4?_nc_ht=instagram.fcoo1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=WIQ3U-vXNa8AX9cleGV&tn=88XWGoZ_UZspQpVS&edm=AHlfZHwBAAAA&ccb=7-4&oe=61C2CAF8&oh=00_AT-GAGQnjFrRjMM9AYTWy4MPa-nDd1Xaxp23PJNiK2Fuvw&_nc_sid=21929d", "", True, "test_video")
print (test)