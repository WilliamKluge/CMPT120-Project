# Holds the InventoryNode class
# Author: William Kluge
# Date: 2017-10-30


class InventoryNode(object):
    """Holds the data for items an entity holds"""

    def __init__(self, inventory):
        """
        :param inventory: Array of items to initialize the inventory with
        """
        self.inventory = inventory
        self.searched = False

    def search(self):
        """
        :return: A string containing the name of every item in the inventory
        """
        inventory_list = ""

        if len(self.inventory) > 0:
            for item in self.inventory:
                inventory_list += item.name + " "
        else:
            inventory_list = "No items found at this location."

        return inventory_list
