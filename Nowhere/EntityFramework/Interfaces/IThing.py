# Holds the Thing interface
# Author: William Kluge
# Date: 2017-9-18

import abc


class IThing(object):
    """
    Defines the interface for things in the game world.
    This includes any objects located in the user inventory or in the world.
    """

    @abc.abstractmethod
    def get_name(self):
        """Return the name of this object"""

    @abc.abstractmethod
    def can_pickup(self):
        """Return if the object can be picked up"""

    @abc.abstractmethod
    def throw(self):
        """Throw the item"""
