# Holds the MoveSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
import pygame


class MoveSystem(ISystem):
    """Draws a scene"""

    target_entity = None
    engine = None
    __amount = None

    def __init__(self, entity, engine, amount):
        self.target_entity = entity
        self.engine = engine
        self.__amount = amount

    def set_target(self, entity):
        self.target_entity = entity

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        z = self.engine.character.components[PositionNode.__name__].location
        new_location = (z[0] + self.__amount[0], z[1] + self.__amount[1], z[2] + self.__amount[2])
        self.engine.character.components[PositionNode.__name__].location = new_location
        print(self.engine.character.components[PositionNode.__name__].location)
        # self.engine.remove_system()
        return True

    def end(self):
        return
