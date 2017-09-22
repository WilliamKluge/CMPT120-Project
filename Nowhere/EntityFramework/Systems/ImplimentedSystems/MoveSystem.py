# Holds the MoveSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem


class MoveSystem(ISystem):
    """Draws a scene"""

    def __init__(self, entity, engine, priority, amount):
        """
        Moves the character by the specified amount
        :param entity: Entity to move
        :param engine: Engine controlling the game
        :param priority: Priority of this process
        :param amount: Amount to move the character (given in a tripple tuple such as (x, y, z))
        """
        self.target_entity = entity
        self.engine = engine
        self.priority = priority
        self.__amount = amount

    def set_target(self, entity):
        self.target_entity = entity

    @staticmethod
    def start(self):
        return True

    def update(self, time):  # TODO make work for any given entity
        character_position = self.engine.character.components[PositionNode.__name__]
        new_location = tuple([sum(i) for i in zip(character_position.location, self.__amount)])
        character_position.location = new_location
        return True

    def end(self):
        return
