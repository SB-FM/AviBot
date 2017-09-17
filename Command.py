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

    def call(self, client, message, params):
        pass


class StatusCommand(Command):
    def __init__(self, command, permission, _type):
        super(StatusCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    def call(self, client, message, params):
        user = Relation.get_or_create(
            userid=str(message.author.id),
            defaults={'relation_value': 0})

        return [client.send_message(message.channel,
                                    " PLACEHOLDER AVI_RELATION for USER: >" + message.author.display_name + "< : " + str(
                                        user[0].relation_value))]


class LoveCommand(Command):
    def __init__(self, command, permission, _type):
        super(LoveCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    def call(self, client, message, params):
        return [client.send_message(message.channel, "I love you too, " + message.author.display_name + " :heart:")]


class PetCommand(Command):
    def __init__(self, command, permission, _type):
        super(PetCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type
        self._relation_mod = 5

    def call(self, client, message, params):
        q = Relation.update(relation_value=Relation.relation_value + self._relation_mod).where(
            Relation.userid == message.author.id)
        q.execute()
        return [client.send_message(message.channel,
                                    "*Avi licks " + message.author.display_name + "'s hand and jumps around happily* :heart:")]


class OldPeopleCommand(Command):
    def __init__(self, command, permission, _type):
        super(OldPeopleCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    def call(self, client, message, params):
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

        return [client.Clientuser.send_message(message.channel, output)]


class ShooCommand(Command):
    def __init__(self, command, permission, _type):
        super(ShooCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type
        self._relation_mod = -5

    def call(self, client, message, params):
        q = Relation.update(relation_value=Relation.relation_value + self._relation_mod).where(
            Relation.userid == message.author.id)
        q.execute()
        return [client.send_message(message.channel, "*" +
                                    message.author.display_name + " shoos Avi away and she sadly toddles into a quiet corner.*")]


class PraiseCommand(Command):
    def __init__(self, command, permission, _type):
        super(PraiseCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    def call(self, client, message, params):
        return [client.send_message(message.channel, "You're the most beautiful being the world has ever seen, "
                                    + message.author.display_name + " <:vohiyo:335128884460781580>")]


class LogoutCommand(Command):
    def __init__(self, command, permission, _type):
        super(LogoutCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    def call(self, client, message, params):
        return [client.send_message(message.channel, "Gotta go! Byyyyee :vohiyo:"), client.logout()]


class UptimeCommand(Command):
    def __init__(self, command, permission, _type):
        super(UptimeCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

# takes a message id as argument

class FetchPostCommand(Command):
    def __init__(self, command, permission, _type):
        super(FetchPostCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    def call(self, client, message, params):
        for _channel in message.server.channels:
            channelid = _channel.id
                #client.get_message(channel.id, 358924330664722432).content
            return [client.get_message(_channel, '358924330664722432')]

        return [client.send_message(message.channel, "not found")]


class HelpCommand(Command):
    def __init__(self, command, permission, _type):
        super(HelpCommand, self).__init__(command, permission, _type)
        self._command = command
        self._permission = permission
        self._type = _type

    def call(self, client, message, params):
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
        return [client.send_message(message.channel, embed=em)]
