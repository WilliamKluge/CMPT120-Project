# Holds the MapCommand class
# Author: William Kluge
# Date: 2017-10-16
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Systems.ImplementedSystems.DrawMapSystem import DrawMapSystem


class MapCommand(ICommand):
    def __init__(self):
        self.__variations = dict()
        from Nowhere.EntityFramework.Systems.ImplementedSystems.UpdateCommandSystem import UpdateCommandSystem
        self.__command_system_name = UpdateCommandSystem.__name__

    @property
    def help_string(self):
        return "Draws the map of locations the player has discovered."

    @property
    def key(self):
        return "map"

    def is_possible(self, engine):
        inventory = engine.character.components[InventoryNode.__name__].inventory
        return next((x for x in inventory if x.name == "Map"), None) is not None

    def create_system(self, engine, user_input):
        return DrawMapSystem(engine)
