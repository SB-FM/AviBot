from config.config import *


class Relation(Model):
    userid = TextField(primary_key=True, unique=True)
    relation_value = IntegerField()

    class Meta:
        database = db


class Counter(Model):
    name = TextField(primary_key=True, unique=True)
    counter_value = IntegerField()
    last_quote = TextField()
    author = TextField()

    class Meta:
        database = db
