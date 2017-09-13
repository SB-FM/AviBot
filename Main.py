import datetime

import discord
from Bot import Bot
from CommandController import CommandController

client = discord.Client()
cc = CommandController()

_bot = Bot()


def log_to_console(message):
    print("--------------")
    print(str(datetime.datetime.now().strftime("%H:%M:%S"))
          + "  |   "
          + message.author.display_name
          + ": "
          + " "
          + message.content)


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!'):
        if cc.validate(client, message):
            log_to_console(message)
            _bot.check_user(message)
            for arg in cc.call(client, message):
                await arg


client.run('MzU2ODMwMDk4Nzc2Nzg0OTA3.DJhDeQ.hcADojSfXKjZy2PNIUnq8P1tNgw')
