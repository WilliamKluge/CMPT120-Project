# Holds the LocationNode class
# Author: William Kluge
# Date: 2017-9-18


class PositionNode(object):
    """Holds the data for describing an entity"""

    location = ()

    def __init__(self, location):
        """Initializes this node with a location. Should be in a list with 3 ints (x, y, z)."""
        self.location = location
