# Holds the UseCommand class
# Author: William Kluge
# Date: 2017-12-4
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Systems.ImplementedSystems.UseItemSystem import UseItemSystem


class UseCommand(ICommand):
    """
    Command to use an item in the character's inventory
    """

    def __init__(self):
        """
        Sets up the dictionary to be used
        """
        self.key_item_dict = dict()

    @property
    def help_string(self):
        return "Uses an item at the character's current location."

    @property
    def key(self):
        return "use"

    def is_possible(self, engine):
        # The location has been searched and there are items in the inventory
        return next((x for x in engine.character.components[InventoryNode.__name__].inventory if x.use_command is not
                    None), None)

    def is_multipart(self):
        return True

    def generate_multipart_commands(self, engine):
        """
        Generates all possible variations of this command. Does not create system or anything, only shows possible
        commands.
        :param engine: Game engine
        :return: Keys for the variations of this command
        """
        # It is guaranteed for this to not return none because this is called from an UpdateCommandSystem object
        command_keys = []

        for item in engine.character.components[InventoryNode.__name__].inventory:
            if item.use_command is not None:
                command = "use " + item.name.lower()
                command_keys.append(command)
                self.key_item_dict[command] = item

        return command_keys

    def create_system(self, engine, user_input):
        system = UseItemSystem(engine)
        system.set_using(self.key_item_dict[user_input])
        return system

