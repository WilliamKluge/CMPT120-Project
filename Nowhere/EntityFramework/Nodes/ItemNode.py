# Holds the ItemNode class
# Author: William Kluge
# Date: 2017-10-30


class ItemNode(object):
    """Holds the data for a game item"""

    def __init__(self, name, description):
        """
        :param name: Name of the item
        :param description: Description of the item
        """
        self.name = name
        self.description = description
