from libs.vk_api.session import VkApi

vk_api = VkApi(access_token=str(input("Enter the your token: ")))
vk_api.wall.post(owner_id=-212871717, message="Hello")
