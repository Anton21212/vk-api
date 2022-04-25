import requests


# token = 'f8b57c4ef8b57c4ef8b57c4eb0f8c9322eff8b5f8b57c4e9ad17645c0a712eba0b16b28'
# fa75b8ce2cc45a2d28945f34a644c1149243ad458d079cb2c0bde19ea35c4160eead6e24101e51f09ed58

# https://oauth.vk.com/authorize?
# client_id=8146528
# &display=page
# &redirect_uri=https://oauth.vk.com/blank.html
# &scope=groups
# &response_type=token
# &v=5.131
#
# access_token=23afa5559213caaff735755293b3c82a4ca51eda24587b32b010b34168ade3f3581ecd87fdbe25880ea01
def user_ban(group_id, owner_id, reason, comment, comment_visible):
    response = requests.post('https://api.vk.com/method/groups.ban',
                             params={
                                 "access_token":
                                     "23afa5559213caaff735755293b3c82a4ca51eda24587b32b010b34168ade3f3581ecd87fdbe25880ea01",
                                 'v': 5.131,
                                 'group_id': group_id,
                                 'owner_id': owner_id,
                                 'reason': reason,
                                 'comment': comment,
                                 'comment_visible': comment_visible
                             })

    data = response.json()
    print(data)
# 212871717
# 352851907

# class App_adress():
#
#     def get_Countries(self):
#         response = requests.get('https://api.vk.com/method/database.getCountries',
#                                    params={
#                                        "access_token":
#                                            "23afa5559213caaff735755293b3c82a4ca51eda24587b32b010b34168ade3f3581ecd87fdbe25880ea01",
#                                        'v': 5.131,
#                                        'need_all': 1,
#                                        'code': "BY",
#                                    }
#                                 )
#
#         data = response.json()
#         z=(data['response']['items'])
#         for i in z:
#             self.x=(i['id'])


#     def get_City(self):
#
#         response = requests.get('https://api.vk.com/method/database.getCities',
#                                 params={
#                                     "access_token":
#                                         "23afa5559213caaff735755293b3c82a4ca51eda24587b32b010b34168ade3f3581ecd87fdbe25880ea01",
#                                     'v': 5.131,
#                                     'country_id' : self.x
#
#                                 }
#                                 )
#
#
#
#     def app_adress(self):
#         response = requests.post('https://api.vk.com/method/groups.addAddress',
#                                  params={
#                                      "access_token":
#                                          "23afa5559213caaff735755293b3c82a4ca51eda24587b32b010b34168ade3f3581ecd87fdbe25880ea01",
#                                      'v': 5.131,
#                                      'group_id': 212871717,
#                                      'title': 'Place of live',
#                                      'address': 'Mozyr, home 39',
#                                      'country_id' : self.x,
#
#                                      'is_main_address': 1,
#         }
#         )
#         data = response.json()
#         print(data)
#
#
# b = App_adress()
# b.get_Countries()
# b.app_adress()
