# Holds the DrawMapSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
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

        # Draw the background on the screen
        self.engine.screen.blit(target_background, [w * 0.185, h * 0.185])

        return self.engine.input_box.value
