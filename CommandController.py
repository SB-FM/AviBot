from Command import *


class CommandController:
    commands = []

    def __init__(self):

        self.commandlist = {'!status': [0, 'message', StatusCommand],
                            '!love': [0, 'message', LoveCommand],
                            '!logout': [1, 'message', LogoutCommand],
                            '!praise': [0, 'message', PraiseCommand],
                            '!uptime': [0, 'message', UptimeCommand],
                            '!help': [0, 'message', HelpCommand],
                            '!pet': [0, 'message', PetCommand],
                            '!shoo': [0, 'message', ShooCommand],
                            '!oldpeople': [0, 'message', OldPeopleCommand],
                            '!fetchPost': [1, 'message', FetchPostCommand],
                            '!play': [0, 'message', PlayCommand],
                            '!pupp': [2, 'message', PuppeteerCommand],
                            }

        self.rolelist = {'Owner': 1,
                         'Stream Owner': 1,
                         'Orange': 1,
                         'The Fairy': 1,
                         '#C1EDB2': 1,
                         'She who Draws': 1,
                         "#BF1717": 1,
                         'Moderator': 1,
                         'Moderator+': 1,
                         '#5CFF01': 1,
                         '#AB1616': 1,
                         '32A00E': 1,
                         'F207E3': 1,
                         'FF0000': 1,
                         'E88ED3': 1,
                         'Blue': 1,
                         }
        self.session_start = datetime.now()
        self.gen()

    def get_session_start(self):
        return self.session_start

    def gen(self):
        for cmd in self.commandlist:
            item = self.commandlist.get(cmd)
            func = item[2]
            # print(item)
            obj = func(cmd, item[0], item[1])
            self.commands.append(obj)

    def call(self, client, message):
        for _cmd in self.commands:
            params = message.content.split(" ")
            if _cmd.command == params[0]:
                params.pop(0)
                print (params)
                return _cmd.call(client, message, params)

    def validate(self, client, message):
        for _cmd in self.commands:
            #  print(str(_cmd.command) + " " + str(_cmd.permission) + " / " + str(
            # self.rolelist.get(str(message.author.top_role), 0)) + str(message.content) + " :: " + str(
            # message.content == _cmd.command)
            params = message.content.split(" ")
            if _cmd.command == params[0] and (_cmd.permission <= self.rolelist.get(str(message.author.top_role),
                                                                                        0) or message.author.id ==318602871912398859):
                # print("True")
                return True

        # print("false")

        return False
