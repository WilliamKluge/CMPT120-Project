# Holds the InventoryNode class
# Author: William Kluge
# Date: 2017-10-30


class InventoryNode(object):
    """Holds the data for a game item"""

    def __init__(self, inventory):
        """
        :param inventory: Array of items to initialize the inventory with
        """
        self.inventory = inventory
