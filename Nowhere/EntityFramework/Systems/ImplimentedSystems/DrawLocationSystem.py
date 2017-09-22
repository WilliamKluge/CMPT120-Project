# Holds the DrawLocationSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawTextSystem import DrawTextSystem


class DrawLocationSystem(ISystem):  # TODO make this draw to a location not the character
    """Draws a scene"""             # (only need to render when location changes)

    def __init__(self, entity, engine):
        self.__target_entity = entity
        self.__engine = engine
        self.__text_process = None  # TODO have this start when the location changes

    def set_target(self, entity):
        self.__target_entity = entity

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        w, h = self.__engine.screen.get_size()
        target_location = self.__engine.locations[self.__target_entity.components[PositionNode.__name__].location]
        target_background = target_location.components[BackgroundNode.__name__].background_screen
        self.__engine.screen.blit(target_background, [w * 0.20, h * 0.20])
        self.__engine.add_system(DrawTextSystem(self.__engine,
                                                target_location.components[DescriptionNode.__name__].description,
                                                (w * 0.05, w * 0.05)))
        return False

    def end(self):
        return
