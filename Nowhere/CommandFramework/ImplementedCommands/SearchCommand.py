# Holds the SearchCommand class
# Author: William Kluge
# Date: 2017-11-10
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ImplementedSystems.DrawTextSystem import DrawTextSystem


class SearchCommand(ICommand):

    @property
    def help_string(self):
        return "Finds the items at the current location."

    @property
    def key(self):
        return "search"

    def is_possible(self, engine):
        return True

    def create_system(self, engine, user_input):
        # Get sizes
        w, h = engine.screen.get_size()
        # Get location
        location = engine.locations[engine.character.components[PositionNode.__name__].location]
        # Get location's inventory
        inventory = location.components[InventoryNode.__name__]

        inventory_list = inventory.search()

        inventory.searched = True

        return DrawTextSystem(engine,
                              inventory_list,
                              (w * 0.185, h * 0.185 + h * 0.65),  # (start position, start of background + image height)
                              no_wait=False)
