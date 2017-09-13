from peewee import *

mysql = {'host': 'localhost',
         'user': 'root',
         'passwd': '',
         'db': 'write-math'}

server_id = '164072311161356289'
#server_id = '337585332281409537'

db = SqliteDatabase(r'c:/Users/n_lan/PycharmProjects/Avi/db/AviDB.db')
db.connect()