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

    def check_old(self, message):
        olddefs = {"i'm too old", "im too old", "i am too old", "im way too old", "i'm way too old", "i am way too old",
                   "we're too old", "were too old", "we are too old", "we're way too old", "were too old",
                   "we are way too old"}
        counter = counter = Counter.get_or_create(
            name='oldpeople',
            defaults={'counter_value': 0, 'last_quote': "", 'author': ""})
        for _def in olddefs:
            if _def in message.content.lower():
                q = Counter.update(counter_value=Counter.counter_value + 1, last_quote=message.content,
                                   author=message.author.display_name).where(Counter.name == 'oldpeople')
                q.execute()
                break
