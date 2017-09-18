import asyncio
from datetime import datetime

import discord

from db.Models import *

session_start = datetime.now()


class Command:
    def __init__(self, command, permission, command_type):
        self._command = command
        self._permission = permission
        self._command_type = command_type

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value

    @property
    def permission(self):
        return self._permission

    @permission.setter
    def permission(self, value):
        self._permission = value

    @property
    def command_type(self):
        return self.command_type

    @command_type.setter
    def command_type(self, value):
        self._command_type = value

    async def call(self, client, message, params):
        pass


class StatusCommand(Command):
    def __init__(self, command, permission, _type):
        super(StatusCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    async def call(self, client, message, params):
        user = Relation.get_or_create(
            userid=str(message.author.id),
            defaults={'relation_value': 0})

        await message.channel.send(
            " PLACEHOLDER AVI_RELATION for USER: >" + message.author.display_name + "< : " + str(
                user[0].relation_value))


class LoveCommand(Command):
    def __init__(self, command, permission, _type):
        super(LoveCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    async def call(self, client, message, params):
        await message.channel.send("I love you too, " + message.author.display_name + " :heart:")


class PetCommand(Command):
    def __init__(self, command, permission, _type):
        super(PetCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type
        self._relation_mod = 5

    async def call(self, client, message, params):
        q = Relation.update(relation_value=Relation.relation_value + self._relation_mod).where(
            Relation.userid == message.author.id)
        q.execute()
        await message.channel.send(
            "*Avi licks " + message.author.display_name + "'s hand and jumps around happily* :heart:")


class PlayCommand(Command):
    def __init__(self, command, permission, _type):
        super(PlayCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type
        self._relation_mod = 5

    async def call(self, client, message, params):
        q = Relation.update(relation_value=Relation.relation_value + self._relation_mod).where(
            Relation.userid == message.author.id)
        q.execute()
        await message.channel.send(
            "*Avi starts playing with " + message.author.display_name + ".*")
        # await client.change_presence(game=discord.Game(name='Nothing'))
        # await asyncio.sleep(60)
        # await client.change_presence(game=discord.Game(name='with ' + message.author.display_name,url='http://twitch.tv/avi',type=1))
        await client.change_presence(game=discord.Game(name='with ' + message.author.display_name))
        await asyncio.sleep(180)
        await client.change_presence(game=discord.Game(name=''))


class PuppeteerCommand(Command):
    def __init__(self, command, permission, _type):
        super(PuppeteerCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type
        self._relation_mod = 5

    async def call(self, client, message, params):
        if len(params) > 1:
            _channel_id = params[0]
            _message = params[1]
        else:
            _channel_id = 164072311161356289
            _message = params[0]
        await client.get_channel(int(_channel_id)).send(_message)


class OldPeopleCommand(Command):
    def __init__(self, command, permission, _type):
        super(OldPeopleCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    async def call(self, client, message, params):
        counter = Counter.get_or_create(
            name='oldpeople',
            defaults={'counter_value': 0})

        output = "Number of times people have complained about being too old: " \
                 + str(counter[0].counter_value)

        if counter[0].counter_value > 0:
            output += " \n Last old person: " \
                      + "**" + counter[0].author + "**" \
                      + "\n*" \
                      + "\"" + counter[0].last_quote + "\"*"

        await message.channel.send(output)


class ShooCommand(Command):
    def __init__(self, command, permission, _type):
        super(ShooCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type
        self._relation_mod = -5

    async def call(self, client, message, params):
        q = Relation.update(relation_value=Relation.relation_value + self._relation_mod).where(
            Relation.userid == message.author.id)
        q.execute()
        await message.channel.send("*"
                                   + message.author.display_name +
                                   " shoos Avi away and she sadly toddles into a quiet corner.*")


class PraiseCommand(Command):
    def __init__(self, command, permission, _type):
        super(PraiseCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    async def call(self, client, message, params):
        await message.channel.send("You're the most beautiful being the world has ever seen, "
                                   + message.author.display_name + " <:vohiyo:335128884460781580>")


class LogoutCommand(Command):
    def __init__(self, command, permission, _type):
        super(LogoutCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    async def call(self, client, message, params):
        await message.channel.send("Gotta go! Byyyyee :vohiyo:")
        await client.logout()


class UptimeCommand(Command):
    def __init__(self, command, permission, _type):
        super(UptimeCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    async def call(self, client, message, params):
        upt = datetime.now() - session_start
        mins, secs = divmod(upt.seconds, 60)
        hours, mins = divmod(mins, 60)
        res = "Running for: "'%02d:%02d:%02d' % (hours, mins, secs)
        await message.channel.send(res)


# takes a message id as argument

class FetchPostCommand(Command):
    def __init__(self, command, permission, _type):
        super(FetchPostCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    async def call(self, client, message, params):
        for channel in message.guild.text_channels:
            try:
                mess = await (channel.get_message(params[0]))
            except discord.NotFound:
                continue
            reaction_list = mess.reactions
            em = discord.Embed(title='',
                               description='                  ', colour=0xe91e63)
            em.add_field(name='Message', value=mess.clean_content, inline=False)

            for reac in reaction_list:
                userlist = ""
                users = await reac.users().flatten()
                for user in users:
                    userlist += user.display_name + " | "
                em.add_field(name=reac.emoji, value=userlist, inline=False)
            em.set_author(name=mess.author.display_name, icon_url=mess.author.avatar_url)
            await message.channel.send(embed=em)
            break


class HelpCommand(Command):
    def __init__(self, command, permission, _type):
        super(HelpCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    async def call(self, client, message, params):
        em = discord.Embed(title='',
                           description='                  ', colour=0xe91e63)
        em.add_field(name='!help', value="Show this message", inline=False)
        em.add_field(name='!pet', value="Pets Avi", inline=False)
        em.add_field(name='!shoo', value="Shoos Avi away", inline=False)
        em.add_field(name='!logout', value="Disconnects the bot (Mod only)", inline=False)
        em.add_field(name='!love', value="Love and be loved!", inline=False)
        em.add_field(name='!praise', value="Everyone needs a push from time to time!", inline=False)
        em.add_field(name='!status', value="Display your status with Avi", inline=False)
        em.add_field(name='!uptime', value="Display the bot running time", inline=False)
        em.set_author(name='Avi Command Help', icon_url=client.user.avatar_url)
        await message.channel.send(embed=em)
