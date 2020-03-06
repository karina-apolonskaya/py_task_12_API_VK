import requests
import pprint

API_ID = 
URL = "https://api.vk.com/method/friends.getMutual"
URL_2 = "https://api.vk.com/method/users.get"
TOKEN = ""


class User:

    def __init__(self, id):
        self.id = id
        self.link = 'https://vk.com/id' + str(self.id)

    def __str__(self):
        return self.link

    def get_mutual_friends(self, user_id, target_id):
        self.user_id = user_id
        self.target_id = target_id

        response = requests.get(
            URL, 
            params = {
                "access_token": TOKEN, 
                "v": "5.52",
                "source_uid": user_id,
                "target_uid": target_id
            }
        )

        friends_list = list()

        for name in response.json()["response"]:
            params = {
                    "access_token": TOKEN, 
                    "v": "5.52",
                    "fields": ["first_name", "last_name"],
                    "user_id": name
                }
            response_2 = requests.get(
                URL_2, params = params             
            )
            friends_list.append(response_2.json())

        friends_list_2 = list()

        for friend in friends_list:
            info = friend["response"][0]
            first_name = info["first_name"]
            last_name = info["last_name"]
            ID = str(info["id"])
            link = 'https://vk.com/id' + ID
            friends_list_2.append(f"{first_name} {last_name}: {link}")
        return friends_list_2

    def __and__(self, other):
        return self.get_mutual_friends(user_id=self.id, target_id=other.id)


user_1 = User()
user_2 = User()

pprint.pprint(f"У пользователя {user_1} с пользователем {user_2} следующие общие друзья:")
pprint.pprint(user_1 & user_2)