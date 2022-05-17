import requests

from libs.vk_api.decorators_errors import error_checker


class Group:
    def __init__(self, access_token):
        self.access_token = access_token
        self.v = 5.131

    @error_checker
    def get_members(self, group_id: int, sort: str, count: int, offset: int = 0, filter: str = None) -> dict:
        """
        Возвращает список участников сообщества

        :param group_id: Идентификатор или короткое имя сообщества.
        :param sort: Сортировка, с которой необходимо вернуть список участников. Может принимать значения:
        • id_asc — в порядке возрастания ID;
        • id_desc — в порядке убывания ID;
        • time_asc — в хронологическом порядке по вступлению в сообщество;
        • time_desc — в антихронологическом порядке по вступлению в сообщество.
        Сортировка по time_asc и time_desc возможна только при вызове от модератора сообщества.
        :param count: Количество участников сообщества, информацию о которых необходимо получить.
        :param filter:
        • friends — будут возвращены только друзья в этом сообществе.
        • unsure — будут возвращены пользователи, которые выбрали «Возможно пойду» (если сообщество относится к
        мероприятиям).
        • managers — будут возвращены только руководители сообщества (доступно при запросе с передачей access_token
        от имени администратора сообщества).
        • donut — будут возвращены только доны (пользователи, у которых есть платная подписка VK Donut).
        offset - Смещение, необходимое для выборки определённого подмножества участников. По умолчанию 0.
        """

        response = requests.get(
            url='https://api.vk.com/method/groups.getMembers',
            params={
                'access_token': self.access_token,
                'v': self.v,
                'group_id': group_id,
                'sort': sort,
                'count': count,
                'filter': filter,
                'offset': offset,
            }
        )

        data = response.json()
        return data

    @error_checker
    def get(self, user_id: int, count: int, *, extended: int = 1, filter: str = None, offset: int = None,
            fields: str = None) -> dict:
        """
        Возвращает список сообществ указанного пользователя.

        :param user_id: Идентификатор пользователя, информацию о сообществах которого требуется получить.
        :param filter: Список фильтров сообществ, которые необходимо вернуть, перечисленные через запятую.
        Доступны значения:
        • admin;
        • editor;
        • moder;
        • advertiser;
        • groups;
        • publics;
        • events;
        • hasAddress.
        По умолчанию возвращаются все сообщества пользователя.
        При указании фильтра hasAddress вернутся сообщества, в которых указаны адреса в соответствующем блоке,
        admin будут возвращены сообщества, в которых пользователь является администратором,
        editor — администратором или редактором, moder — администратором, редактором или модератором,
        advertiser — рекламодателем. Если передано несколько фильтров, то их результат объединяется.
        :param fields:Список дополнительных полей, которые необходимо вернуть.
        Возможные значения:
        • activity;
        • can_create_topic;
        • can_post;
        • can_see_all_posts;
        • city;
        • contacts;
        • counters;
        • country;
        • description;
        • finish_date;
        • fixed_post;
        • links;
        • members_count;
        • place;
        • site;
        • start_date;
        • status;
        • verified;
        • wiki_page.
        Подробнее см. описание полей объекта group.
        Обратите внимание, этот параметр учитывается только при extended=1.
        :param offset: Смещение, необходимое для выборки определённого подмножества сообществ.
        :param count: Количество сообществ, информацию о которых нужно вернуть.
        :param extended:Если указать в качестве этого параметра 1, то будет возвращена полная информация о группах пользователя. По умолчанию 0.
        """

        response = requests.get(
            url='https://api.vk.com/method/groups.get',
            params={
                'access_token': self.access_token,
                'v': self.v,
                'user_id': user_id,
                'sort': fields,
                'count': offset,
                'filter': count,
                'offset': filter,
                'extended': extended,
            }
        )

        data = response.json()
        print(data)
        return data
