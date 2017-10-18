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
        return 90

    def __init__(self, engine):
        super().__init__(engine)

    def update(self, time):
        # Get sizes
        w, h = self.engine.screen.get_size()

        # Get the values for the location and its data
        map_entity = next((x for x in self.engine.entities
                           if len(x.components) == 2
                           and BackgroundNode.__name__ in x.components and MapMarkerNode.__name__ in x.components),
                          None)
        target_background = map_entity.components[BackgroundNode.__name__].background_screen

        visited_locations = []

        for coordinate in self.engine.character.components[LocationsVisitedNode.__name__].visited_locations:
            location = self.engine.locations[coordinate]
            visited_locations.append((coordinate, location))

        # Draw the background on the screen
        background_offset = [w * 0.185, h * 0.185]
        self.engine.screen.blit(target_background, background_offset)

        for i in visited_locations:
            map_marker_node = i[1].components[MapMarkerNode.__name__]
            screen_location = self.engine.vertical_add(self.__coord_to_pixels(i[0], w, h),
                                                       map_marker_node.get_image_offset(),
                                                       background_offset)
            self.engine.screen.blit(map_marker_node.background_screen, screen_location)

        return self.engine.input_box.value

    def __coord_to_pixels(self, coordinate, w, h):
        map_size = (w * 0.65, h * 0.65)
        x_pixel = int(coordinate[0] * (map_size[0] * 0.05))
        y_pixel = int(coordinate[1] * (map_size[1] * 0.05))
        map_center = (int(map_size[0] / 2), int(map_size[1] / 2))
        return self.engine.vertical_add(map_center, (x_pixel, y_pixel))
