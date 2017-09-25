# Holds the LocationNode class
# Author: William Kluge
# Date: 2017-9-18
from Nowhere.EntityFramework.Nodes.LocationsVisitedNode import LocationsVisitedNode


class PositionNode(object):
    """Holds the data for describing an entity"""

    def __init__(self, location):
        """
        Initializes this node with a location.
        :param location List with 3 ints (x, y, z).
        """
        self.location = location

    def __init__(self, target_entity, location):
        """
        Initializes this node with a location, checks if the target entity is recording what locations are visited, and
        records the location if it is.
        :param target_entity Entity this is being added to
        :param location Location the entity is starting in
        """
        if LocationsVisitedNode.__name__ in target_entity.components:
            target_entity.components[LocationsVisitedNode.__name__].visit_location(location)
        self.location = location
