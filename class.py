from urllib.parse import urlencode

import requests

APP_ID = 6773521
AUTH_URL = 'https://oauth.vk.com/authorize?'

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'response_type': 'token',
    'scope': 'friends',
    'v': '5.92'
}

print(AUTH_URL + (urlencode(auth_data)))

token = 'bdcfe380c4d26faba46e109bbbc207fd9220e035eb0efea5206d193782c7ea1aa6c763d7275f05c9fae2a'


class User:
    def __init__(self, id_user):
        self.id_user = id_user

    def __str__(self):
        return 'https://vk.com/id' + str(self.id_user)

    def get_friends(self):
        params = {
            'user_id': self.id_user,
            'access_token': token,
            'v': '5.92'
        }

        response = requests.get('https://api.vk.com/method/friends.get',
                                params)
        return response.json()

    def mutual_friend(self, user_2):
        return list(
            set(User(self.id_user).get_friends()['response']['items']) & set(user_2.get_friends()['response']['items']))

    def __and__(self, other):
        mutual = list(
            set(User(self.id_user).get_friends()['response']['items']) & set(other.get_friends()['response']['items']))
        common_friends_class = []
        for i in mutual:
            common_friends_class.append(User(i))
        return common_friends_class

Kris = User(120597952)

Anna = User(176913353)
print(Kris.mutual_friend(Anna))
print(Kris&Anna)
print(Kris)
