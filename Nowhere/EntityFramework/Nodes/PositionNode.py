# Holds the PositionNode class
# Author: William Kluge
# Date: 2017-9-18
from Nowhere.EntityFramework.Nodes.LocationsVisitedNode import LocationsVisitedNode


class PositionNode(object):
    """Holds the data for an entities coordinates"""

    def __init__(self, location, target_entity=None):
        """
        Initializes this node with a location, checks if the target entity is recording what locations are visited, and
        records the location if it is.
        :param location Location the entity is starting in
        :param target_entity Entity this is being added to
        """
        # Sets the location
        self.location = location
        # If the target is keeping track of positions, add this starting position to its visited locations
        if target_entity and LocationsVisitedNode.__name__ in target_entity.components:
            target_entity.components[LocationsVisitedNode.__name__].visit_location(location)
