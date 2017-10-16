# Holds the NorthCommand class
# Author: William Kluge
# Date: 2017-10-15
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawTextSystem import DrawTextSystem


class HelpCommand(ICommand):
    def __init__(self):
        self.__variations = dict()

    @property
    def help_string(self):
        return "Prints help to the user...you just ran this command."

    @property
    def key(self):
        return "help"

    def is_possible(self, engine):
        return True

    def is_multipart(self):
        return True

    def generate_multipart_commands(self, engine):
        """
        Generates all possible variations of this command.
        :param engine: Game engine
        :return: Keys for the variations of this command
        """
        # Local import to avoid circular inclusion
        from Nowhere.EntityFramework.Systems.ImplimentedSystems.UpdateCommandSystem import UpdateCommandSystem
        # It is guaranteed for this to not return none because this is called from an UpdateCommandSystem object
        command_list = next((x for x in engine.system_queue if x.__class__.__name__ == UpdateCommandSystem.__name__),
                            None).commands
        command_keys = []

        for command in command_list:
            if command.is_possible(engine):
                key = "help " + command.key
                self.__variations[key] = command.help_string
                command_keys.append("help " + command.key)

        return command_keys

    def create_system(self, engine, user_input):
        return DrawTextSystem(engine, self.__variations[user_input], (50, 20), no_wait=False)
