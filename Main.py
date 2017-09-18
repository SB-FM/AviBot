import datetime
import re

import discord

import CommandController
from db.Models import *

cc = CommandController.CommandController()


class Avibot(discord.Client):
    def __init__(self):
        super(Avibot, self).__init__()
        self.known_users = set()
        for user in Relation.select():
            self.known_users.add(user.userid)

    def check_user(self, message):
        if message.author.id not in self.known_users:
            test = Relation.get_or_create(
                userid=str(message.author.id),
                defaults={'relation_value': 0})
            self.known_users.add(message.author.id)

    # check for old triggers
    def check_old(self, message):
        olddefs = {"i'm too old", "im too old", "i am too old", "im way too old", "i'm way too old", "i am way too old",
                   "we're too old", "were too old", "we are too old", "we're way too old", "were too old",
                   "we are way too old"}
        Counter.get_or_create(
            name='oldpeople',
            defaults={'counter_value': 0, 'last_quote': "", 'author': ""})
        for _def in olddefs:
            if _def in message.content.lower():
                q = Counter.update(counter_value=Counter.counter_value + 1, last_quote=message.content,
                                   author=message.author.display_name).where(Counter.name == 'oldpeople')
                q.execute()
                break

    async def check_reaction_triggers(self, message):

        text = message.content.lower()
        if 'sunglasses' in text:
            await message.add_reaction(u"\U0001F60E")
        elif 'approve' in text:
            await message.add_reaction(self.fetch_emojis('MattApproves'))
        elif 'tired' in text or 'sleep' in text:
            await message.add_reaction(u"\U0001F4A4")
        elif 'lizard' in text:
            await message.add_reaction(u"\U0001F98E")
        elif re.search(r"\bavi\b", text):
            await message.add_reaction(u"\U0001F43A")

    def log_to_console(self, message):
        print("--------------")
        print(str(datetime.datetime.now().strftime("%H:%M:%S"))
              + "  |   "
              + message.author.display_name
              + ": "
              + " "
              + message.content)

    def fetch_emojis(self, needle):
        emoji_list = self.emojis
        for item in emoji_list:
            if item.name == needle:
                return item

    async def on_ready(self):
        print('logged in as')
        print(client.user.name)
        print('------')
        print(discord.__version__)

    async def on_member_update(self, before, after):
        if before.id == 155739141802295297 and after.id == 155739141802295297:
            if after.game is not None and after.game.type == 1 and after.guild.id == 164072311161356289:
                print("STREAM START TRIGGERED")
                # print(after.name + " " + after.game.name + str(after.game.type) + "" + str(after.guild.name))
                # await client.get_channel(337585332281409537).send(
                #  '*Avi is very excited that the commander just started streaming*')
                await client.get_channel(164072311161356289).send(
                    '*Avi is wagging her tail as the commander starts streaming*')

    async def on_message(self, message):
        if not message.author.bot:

            # parse commands starting with !
            if message.content.startswith('!'):
                if cc.validate(client, message):
                    self.log_to_console(message)
                    self.check_user(message)
                    await cc.call(client, message)
            else:
                # custom triggers
                self.check_old(message)
                await self.check_reaction_triggers(message)


client = Avibot()
client.run(token)
