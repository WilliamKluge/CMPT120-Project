# Holds the DrawLocationSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Nodes.LocationsVisitedNode import LocationsVisitedNode
from Nowhere.EntityFramework.Nodes.NameNode import NameNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Systems.ImplementedSystems.DrawTextSystem import DrawTextSystem


class DrawLocationSystem(ISystem):  # TODO make this draw to a location not the character
    """Draws a scene"""             # (only need to render when location changes)

    @property
    def priority(self):
        return 100

    def __init__(self, engine):
        super().__init__(engine)
        self.__text_process = None  # TODO have this start when the location changes

    def update(self, time):
        # Get sizes
        w, h = self.engine.screen.get_size()

        # Get the coordinate of current location of the entity the system is using
        using_location = self.using.components[PositionNode.__name__].location
        # Get the location entity associated with the using's coordinate
        target_location = self.engine.locations[using_location]
        # Get the background image of the current location
        target_background = target_location.components[BackgroundNode.__name__].background_screen
        # Get the path of where the user has traveled
        using_location_path = self.using.components[LocationsVisitedNode.__name__].visited_locations

        # Always blit the background for a location
        self.engine.screen.blit(target_background, [w * 0.185, h * 0.185])

        # Always blit the location name
        self.engine.add_system(DrawTextSystem(self.engine,
                                              target_location.components[NameNode.__name__].name,
                                              (w * 0.05, w * 0.04)))

        if using_location_path.index(using_location) == len(using_location_path) - 1:
            # If the coordinate exists in the location path at the end of the array, draw long description
            self.engine.add_system(DrawTextSystem(self.engine,
                                                  target_location.components[DescriptionNode.__name__].description,
                                                  (w * 0.05, w * 0.05),
                                                  self.engine.character.components[NameNode.__name__].name))

        return False
