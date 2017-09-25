# Holds the LocationsVisitedNode class
# Author: William Kluge
# Date: 2017-9-22


class LocationsVisitedNode(object):
    """
    Holds the data for the locations an entity has visited.
    This is structured like this so that if NPCs are added later their visited locations can be stored too. If a bool
    were to be used on the location one would need to be added for each PC and NPC. The reason that this is created
    to be stored on a character entity is so that if checking where a character has visited you call this on the
    character entity, not having to check every location.
    """

    def __init__(self):
        self.visited_locations = []

    def visit_location(self, location_coordinate):
        """
        Make sure that this node records that a location has been visited
        :param location_coordinate: Location that the user visited
        :return: None
        """
        if location_coordinate not in self.visited_locations:
            self.visited_locations.append(location_coordinate)

    def has_visited(self, location_coordinate):
        """
        Checks if the user has visited a location
        :param location_coordinate: Coordinate to check if the entity has visited
        :return: If the entity has visited the location
        """
        return location_coordinate in self.visited_locations
