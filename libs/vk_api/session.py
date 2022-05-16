from libs.vk_api.methods.group import Group
from libs.vk_api.methods.wall import Wall


class VkApi:
    def __init__(self, access_token):
        self.access_token = access_token
        self.wall = Wall(access_token=self.access_token)
        self.group = Group(access_token=self.access_token)
