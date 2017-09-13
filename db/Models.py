from config.config import *


class Relation(Model):
    userid = TextField(primary_key=True, unique=True)
    relation_value = IntegerField()

    class Meta:
        database = db
