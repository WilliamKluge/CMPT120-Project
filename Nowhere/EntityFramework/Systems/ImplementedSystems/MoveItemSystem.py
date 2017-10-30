# Holds the MoveItemSystem class
# Author: William Kluge
# Date: 2017-10-30
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem


class MoveItemSystem(ISystem):
    """Draws text to the screen"""

    @property
    def priority(self):
        return 10  # High priority system

    def __init__(self, engine):
        super().__init__(engine)
        self.item_name = None

    def set_item(self, item_name):
        self.item_name = item_name

    def update(self, time):
        """
        set_using, set_target, and set_item must all be called before this point
        :param time:
        :return:
        """
        if self.using is None or self.target is None or self.item_name is None:
            raise ValueError("using, target, and/or item_name was not set before update was called")

        target_inventory = self.target.components[InventoryNode.__name__].inventory
        using_inventory = self.using.components[InventoryNode.__name__].inventory

        item_entity = next((x for x in self.using if x.name == self.item_name), None)

        if item_entity is None:
            pass
        else:
            using_inventory.append(item_entity)
            target_inventory.remove(item_entity)

