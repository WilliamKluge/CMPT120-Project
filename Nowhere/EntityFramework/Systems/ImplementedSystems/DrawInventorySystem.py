# Holds the DrawInventorySystem class
# Author: William Kluge
# Date: 2017-10-30

from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Systems.ImplementedSystems.DrawTextSystem import DrawTextSystem


class DrawInventorySystem(ISystem):
    """Draws a scene"""

    # TODO update to use new ISystem update due to command framework implimentation

    @property
    def priority(self):
        return 100

    def __init__(self, engine):
        super().__init__(engine)

    def update(self, time):
        # Get sizes
        w, h = self.engine.screen.get_size()

        # Get the values for the location and its data
        player_inventory = self.engine.character.components[InventoryNode.__name__].inventory

        inventory_string = "Backpack:" + " " * 111  # TODO create better way for multiline text than forcing wrap

        for item in player_inventory:
            inventory_string += item.name + " " * (120 + len(item.name))

        # Draw the background on the screen
        self.engine.add_system(DrawTextSystem(self.engine,
                                              inventory_string,
                                              [w * 0.85, h * 0.185]))

        return False  # Always draw the inventory
