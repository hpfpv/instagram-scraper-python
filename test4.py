from InstagramAPI import InstagramAPI

user = "229eaglemotion"
password = "229motioneagle"

api = InstagramAPI(user, password)
api.login()

api.uploadPhoto('test.jpg', caption="")