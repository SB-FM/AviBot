import datetime

import discord

import Bot
import CommandController

cc = CommandController.CommandController()
bot = Bot.Bot()


class Avibot(discord.Client):
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

    async def on_message(self, message):
        if not message.author.bot:
            bot.check_old(message)
            # parse commands starting with !
            if message.content.startswith('!'):
                if cc.validate(client, message):
                    self.log_to_console(message)
                    bot.check_user(message)
                    await cc.call(client, message)

            if 'sunglasses' in message.content.lower():
                await message.add_reaction(u"\U0001F60E")
            elif 'approve' in message.content.lower():
                await message.add_reaction(self.fetch_emojis('MattApproves'))
            elif 'tired' in message.content.lower() or 'sleep' in message.content.lower():
                await message.add_reaction(u"\U0001F4A4")
            elif 'lizard' in message.content.lower():
                await message.add_reaction(u"\U0001F98E")
            elif 'avi' in message.content.lower():
                await message.add_reaction(u"\U0001F43A")


client = Avibot()
client.run('MzU2ODMwMDk4Nzc2Nzg0OTA3.DJhDeQ.hcADojSfXKjZy2PNIUnq8P1tNgw')
