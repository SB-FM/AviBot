from db.Models import *


class Bot:
    @staticmethod
    def connect():
        for user in Relation.select():
            print(user.userid)

    def __init__(self):
        self.known_users = set()
        for user in Relation.select():
            self.known_users.add(user.userid)

    def check_user(self, message):
        if message.author.id not in self.known_users:
            test = Relation.get_or_create(
                userid=str(message.author.id),
                defaults={'relation_value': 0})
