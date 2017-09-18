# Holds the Thing interface
# Author: William Kluge
# Date: 2017-9-18


from zope.interface import Interface
from zope.interface import Attribute


class IThing(Interface):
    """
    Defines the interface for things in the game world.
    This includes any objects located in the user inventory or in the world.
    """

    name = Attribute(""""Name of thing""""")
    pickupable = Attribute("""If the item can be picked up""")

    def throw(self):
        """Throw the item"""
