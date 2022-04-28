import requests

from libs.vk_api.wall import Wall

vk_api = Wall(access_token="292ea767ac075b421d2defabb3ab866a8fb8f295d42feaa534979bdf9d384bafe03c9a102a9667ecbeb53")
vk_api.post(owner_id=212871717, message="Hello")
