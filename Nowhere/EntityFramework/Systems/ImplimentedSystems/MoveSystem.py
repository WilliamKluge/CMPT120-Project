# Holds the MoveSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
import pygame


class MoveSystem(ISystem):
    """Draws a scene"""

    def __init__(self, entity, engine, amount, priority):
        self.target_entity = entity
        self.engine = engine
        self.__amount = amount
        self.priority = priority

    def set_target(self, entity):
        self.target_entity = entity

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        self.engine.character.components[PositionNode.__name__].location += self.__amount
        return True

    def end(self):
        return
