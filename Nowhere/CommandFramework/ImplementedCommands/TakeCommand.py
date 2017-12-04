# Holds the TakeCommand class
# Author: William Kluge
# Date: 2017-10-30
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ImplementedSystems.MoveItemSystem import MoveItemSystem


class TakeCommand(ICommand):

    @property
    def help_string(self):
        return "Picks up an item from the character's current location."

    @property
    def key(self):
        return "take"

    def is_possible(self, engine):
        character_location = engine.locations[engine.character.components[PositionNode.__name__].location]
        location_inventory = character_location.components[InventoryNode.__name__]
        # The location has been searched and there are items in the inventory
        return location_inventory.searched and len(location_inventory.inventory) > 0

    def is_multipart(self):
        return True

    def generate_multipart_commands(self, engine):
        """
        Generates all possible variations of this command. Does not create system or anything, only shows possible
        commands.
        :param engine: Game engine
        :return: Keys for the variations of this command
        """
        # Local import to avoid circular inclusion

        # It is guaranteed for this to not return none because this is called from an UpdateCommandSystem object
        location = engine.locations[engine.character.components[PositionNode.__name__].location]
        command_keys = []

        for item in location.components[InventoryNode.__name__].inventory:
            command_keys.append("take " + item.name.lower())

        return command_keys

    def create_system(self, engine, user_input):
        system = MoveItemSystem(engine)
        system.set_using(engine.locations[engine.character.components[PositionNode.__name__].location])
        system.set_target(engine.character)
        system.set_item(user_input[5:])  # Passed every character past the "take " portion of user input
        return system
