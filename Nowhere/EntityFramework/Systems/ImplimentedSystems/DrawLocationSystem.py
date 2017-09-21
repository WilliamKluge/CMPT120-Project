# Holds the DrawLocationSystem class
# Author: William Kluge
# Date: 2017-9-18
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
import pygame


class DrawLocationSystem(ISystem):
    """Draws a scene"""

    target_entity = None
    engine = None

    def __init__(self, entity, engine):
        self.target_entity = entity
        self.engine = engine

    def set_target(self, entity):
        self.target_entity = entity

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        # try:  # TODO improve this crap code (here for testing)
        #     target_background = self.target_entity.components[BackgroundNode.__name__].background_screen
        # except KeyError:
        target_location = self.engine.locations[self.target_entity.components[PositionNode.__name__].location]
        target_background = target_location.components[BackgroundNode.__name__].background_screen

        w, h = self.engine.screen.get_size()
        self.engine.screen.blit(target_background, [w * 0.20, h * 0.20])
        return False

    def end(self):
        return
