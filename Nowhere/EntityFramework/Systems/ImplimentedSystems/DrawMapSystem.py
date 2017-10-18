# Holds the DrawMapSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
from Nowhere.EntityFramework.Nodes.LocationsVisitedNode import LocationsVisitedNode
from Nowhere.EntityFramework.Nodes.MapMarkerNode import MapMarkerNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem


class DrawMapSystem(ISystem):
    """Draws the world map based on what the player has discovered"""

    @property
    def priority(self):
        return 90  # Priority is less than DrawLocationSystem

    def __init__(self, engine):
        super().__init__(engine)

    def update(self, time):
        # Get screen size
        w, h = self.engine.screen.get_size()
        # Holds the locations the user has visited as a tuple of (coordinate, location entity)
        visited_locations = []

        # Get the map entity from the engines entity list
        map_entity = next((x for x in self.engine.entities
                           if len(x.components) == 2
                           and BackgroundNode.__name__ in x.components and MapMarkerNode.__name__ in x.components),
                          None)
        # Gets the background image of the map entity
        target_background = map_entity.components[BackgroundNode.__name__].background_screen

        for coordinate in self.engine.character.components[LocationsVisitedNode.__name__].visited_locations:
            # Iterates through the coordinates the user has visited
            # Location entity
            location = self.engine.locations[coordinate]
            visited_locations.append((coordinate, location))

        # Sets the background offset of the screen (this is the top-left pixel coordinate of the background)
        background_offset = [w * 0.185, h * 0.185]
        self.engine.screen.blit(target_background, background_offset)

        for i in visited_locations:
            # Iterates through locations the user has visited
            try:
                # Get the locations map marker
                map_marker_node = i[1].components[MapMarkerNode.__name__]
            except KeyError:
                # The location does not have a map marker, put in the error placeholder
                map_marker_node = map_entity.components[MapMarkerNode.__name__]

            # Set pixel position as it's pixel position combined with its offset and the backgrounds offset
            screen_location = self.engine.vertical_add(self.__coord_to_pixels(i[0], w, h),
                                                       map_marker_node.get_image_offset(),
                                                       background_offset)

            self.engine.screen.blit(map_marker_node.background_screen, screen_location)

        return self.engine.input_box.value

    def __coord_to_pixels(self, coordinate, w, h):
        """
        Translates a map coordinate into an amount of pixels to offset the map marker
        :param coordinate: Coordinate of the location to translate
        :param w: Width of the screen
        :param h: Height of the screen
        :return: Tuple of pixel location (x, y)
        """
        # Size of the map TODO get this from configuration
        map_size = (w * 0.65, h * 0.65)
        # Center of the map
        map_center = (int(map_size[0] / 2), int(map_size[1] / 2))
        # Pixel coordinates
        x_pixel = int(coordinate[0] * (map_size[0] * 0.06))
        y_pixel = int(coordinate[1] * (map_size[1] * 0.06))
        return self.engine.vertical_add(map_center, (x_pixel, y_pixel))
