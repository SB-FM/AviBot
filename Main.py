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


def fetch_emojis(client, needle):
    emoji_list = client.get_all_emojis()
    for item in emoji_list:
        if item.name == needle:
            return item


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print('------')
    print (discord.__version__)


@client.event
async def on_message(message):
    if not message.author.bot:
        print(message.content)
        _bot.check_old(message)
        if message.content.startswith('!fetch'):
           mess =await (message.channel.get_message(358957067668553729))
           await message.channel.send(mess.content)
        # parse commands starting with !
        elif message.content.startswith('!'):
            if cc.validate(client, message):
                log_to_console(message)
                _bot.check_user(message)
                for arg in cc.call(client, message):
                    await arg

        if 'sunglasses' in message.content:
            await client.add_reaction(message, u"\U0001F60E")
        elif 'approve' in message.content:
            await client.add_reaction(message, fetch_emojis(client, 'MattApproves'))
        elif 'tired' in message.content or 'sleep' in message.content:
            await client.add_reaction(message, u"\U0001F4A4")
        elif 'lizard' in message.content:
            await client.add_reaction(message, u"\U0001F98E")
        elif 'Avi' in message.content:
            await client.add_reaction(message, u"\U0001F43A")


client.run('MzU2ODMwMDk4Nzc2Nzg0OTA3.DJhDeQ.hcADojSfXKjZy2PNIUnq8P1tNgw')
