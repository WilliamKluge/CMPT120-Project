# Holds the DrawLocationSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Nodes.NameNode import NameNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawTextSystem import DrawTextSystem


class DrawLocationSystem(ISystem):  # TODO make this draw to a location not the character
    """Draws a scene"""             # (only need to render when location changes)

    # TODO update to use new ISystem update due to command framework implimentation

    @property
    def priority(self):
        return 100

    def __init__(self, engine):
        super().__init__(engine)
        self.__text_process = None  # TODO have this start when the location changes

    def update(self, time):
        # Get sizes
        w, h = self.engine.screen.get_size()

        # Get the values for the location and its data
        target_location = self.engine.locations[self.using.components[PositionNode.__name__].location]
        target_background = target_location.components[BackgroundNode.__name__].background_screen

        # Draw the background on the screen
        self.engine.screen.blit(target_background, [w * 0.185, h * 0.185])
        self.engine.add_system(DrawTextSystem(self.engine,
                                              target_location.components[DescriptionNode.__name__].description,
                                              (w * 0.05, w * 0.05),
                                              self.engine.character.components[NameNode.__name__].name))
        return False
