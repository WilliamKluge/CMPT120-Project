# Holds the DrawLocationSystem class
# Author: William Kluge
# Date: 2017-9-18

# Holds the DescriptionSystem class
# Author: William Kluge
# Date: 2017-9-18

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
        self.engine.screen.blit(self.target_entity.components[BackgroundNode.__name__].background_sprite, [0, 0])
        return False

    def end(self):
        return
