from .wall.method_walls import *


class VkApi():
    def __init__(self, access_token):
        self.access_token = access_token
        self.wall = Wall(access_token=self.access_token)