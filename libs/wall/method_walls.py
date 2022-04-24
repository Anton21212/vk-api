import requests

# Получение токена
# resp = requests.post(
#     "https://oauth.vk.com/authorize?client_id=8146528&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall&response_type=token&v=5.131").json()

# КОНСТАНТЫ
V = 5.131
token = "token"


def wall_post(owner_id, message):
    """
    Cоздание записи на стене

    """

    response = requests.post('https://api.vk.com/method/wall.post?',
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': -owner_id,
                                 'friends_only': 0,
                                 'from_group': 1,
                                 'message': message,
                             })

    data = response.json()
    print(data)


# wall_post(owner_id=212871717,message="Anton")


def check_link(link):
    """
    Проверка ссылки для указания источника

    """

    response = requests.post("https://api.vk.com/method/wall.checkCopyrightLink?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'link': link,
                             })
    data = response.json()
    print(data)


# check_link(link="https://vk.com/great.food?w=wall-34451036_378271")


def off_comment(owner_id, post_id):
    """
    Выключает комментирование записи

    """

    response = requests.post("https://api.vk.com/method/wall.closeComments?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': -owner_id,
                                 'post_id': post_id,
                             })
    data = response.json()
    print(data)


# off_comment(owner_id=212871717, post_id=8)


def create_comment(owner_id, post_id, message, reply_to_comment, *sticker_id):
    """
    Создание коммента к записи

    """

    response = requests.post("https://api.vk.com/method/wall.createComment?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': -owner_id,
                                 'post_id': post_id,
                                 'message': message,
                                 "reply_to_comment": reply_to_comment,
                                 "sticker_id": sticker_id

                             })
    data = response.json()
    print(data)


# create_comment(owner_id=212871717, post_id=1, message="Не плохо", reply_to_comment=1)


def del_wall(owner_id, post_id):
    """
    Удалить запись со стены

    """

    response = requests.post("https://api.vk.com/method/wall.delete?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': -owner_id,
                                 'post_id': post_id,
                             }
                             )
    data = response.json()
    print(data)


# del_wall(owner_id=212871717, post_id=1)

def del_comment(owner_id, comment_id):
    """
    Удаляет комментарий к записи на стене.

    """

    response = requests.post("https://api.vk.com/method/wall.deleteComment?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': -owner_id,
                                 'comment_id': comment_id,
                             }
                             )
    data = response.json()
    print(data)


def edit_wall(owner_id, post_id, friends_only, message, close_comments):
    """
    Редактирование записи на стене

    """

    response = requests.post("https://api.vk.com/method/wall.edit?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': -owner_id,
                                 'post_id': post_id,
                                 'friends_only': friends_only,
                                 'message': message,
                                 'close_comments': close_comments,
                             }
                             )
    data = response.json()
    print(data)


def edit_comment_wall(owner_id, comment_id, message):
    """
    Редактирование коммента к записи

    """

    response = requests.post("https://api.vk.com/method/wall.editComment?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': -owner_id,
                                 'comment_id': comment_id,
                                 'message': message,
                             }
                             )
    data = response.json()
    print(data)


def get_wall(owner_id, count, filter, *offset, domain):
    """
    Возвращает список записей со стены пользователя или сообщества.

    """

    response = requests.post("https://api.vk.com/method/wall.get?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': -owner_id,
                                 'count': count,
                                 'filter': filter,
                                 'offset': offset,
                                 'domain': domain,
                             }
                             )
    data = response.json()
    print(data)


def get_ByID(posts):
    """
    Возвращает список записей со стен пользователей или сообществ по их идентификаторам.

    """

    response = requests.post("https://api.vk.com/method/wall.getById?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'posts': posts,
                             }
                             )
    data = response.json()
    print(data)


def get_Comment(owner_id, comment_id):
    """
    Получает информацию о комментарии на стене.

    """

    response = requests.post("https://api.vk.com/method/wall.getComment?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'comment_id': comment_id,

                             }
                             )
    data = response.json()
    print(data)


def get_Comments(owner_id, post_id, need_likes, offset, count, *sort, comment_id, start_comment_id):
    """
    Возвращает список комментариев к записи на стене.

    """

    response = requests.post("https://api.vk.com/method/wall.getComments?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'post_id': post_id,
                                 'need_likes': need_likes,
                                 'offset': offset,
                                 'count': count,
                                 'sort': sort,
                                 'comment_id': comment_id,
                                 'start_comment_id': start_comment_id,
                             }
                             )
    data = response.json()
    print(data)


def get_Reposts(owner_id, post_id, count, *offset):
    """
    Позволяет получать список репостов заданной записи.

    """

    response = requests.post("https://api.vk.com/method/wall.getReposts?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'post_id': post_id,
                                 'count': count,
                                 'offset': offset,
                             }
                             )
    data = response.json()
    print(data)


def open_Comments(owner_id, post_id):
    """
    Включает комментирование записи

    """

    response = requests.post("https://api.vk.com/method/wall.openComments?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'post_id': post_id,
                             }
                             )
    data = response.json()
    print(data)


def fix_wall(owner_id, post_id):
    """
    Закрепляет запись на стене (запись будет отображаться выше остальных).

    """

    response = requests.post("https://api.vk.com/method/wall.pin?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'post_id': post_id,
                             }
                             )
    data = response.json()
    print(data)


def report_Comment(owner_id, comment_id, reason):
    """

    Позволяет пожаловаться на комментарий к записи.

    """

    response = requests.post("https://api.vk.com/method/wall.reportComment?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'comment_id': comment_id,
                                 'reason': reason,
                             }
                             )
    data = response.json()
    print(data)


def report_Post(owner_id, comment_id, reason):
    """

    Позволяет пожаловаться на запись.

    """

    response = requests.post("https://api.vk.com/method/wall.reportPost?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'comment_id': comment_id,
                                 'reason': reason,
                             }
                             )
    data = response.json()
    print(data)


def repost(object, message, group_id, *mark_as_ads):
    """

    Копирует объект на стену пользователя или сообщества.

    """

    response = requests.post("https://api.vk.com/method/wall.repost?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'object': object,
                                 'message': message,
                                 'group_id': group_id,
                                 'mark_as_ads': mark_as_ads,
                             }
                             )
    data = response.json()
    print(data)


def restore(owner_id, post_id):
    """
    Восстанавливает удалённую запись на стене пользователя или сообщества.

    """

    response = requests.post("https://api.vk.com/method/wall.restore?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'post_id': post_id,
                             }
                             )
    data = response.json()
    print(data)


def restore_Comment(owner_id, comment_id):
    """
    Восстанавливает удаленный комментарий к записи на стене.

    """

    response = requests.post("https://api.vk.com/method/wall.restoreComment?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'comment_id': comment_id,
                             }
                             )
    data = response.json()
    print(data)


def search(owner_id, query, owners_only, count, offset, *domain):
    """
    Позволяет искать записи на стене в соответствии с заданными критериями.

    """

    response = requests.post("https://api.vk.com/method/wall.search?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'query': query,
                                 'owners_only': owners_only,
                                 'offset': offset,
                                 'count': count,
                                 'domain': domain,
                             }
                             )
    data = response.json()
    print(data)


def unfix_wall(owner_id,post_id):
    """
    Отменяет закрепление записи на стене.

    """

    response = requests.post("https://api.vk.com/method/wall.unpin?",
                             params={
                                 'access_token': token,
                                 'v': V,
                                 'owner_id': owner_id,
                                 'post_id': post_id,
                             }
                             )
    data = response.json()
    print(data)
