# Holds the MoveSystem class
# Author: William Kluge
# Date: 2017-9-18
from Nowhere.EntityFramework.Nodes.LocationsVisitedNode import LocationsVisitedNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Nodes.ScoreNode import ScoreNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem


class MoveSystem(ISystem):
    """Draws a scene"""

    def set_using(self, using):
        pass

    # TODO update to use new ISystem update due to command framework implimentation

    @property
    def priority(self):
        return self.__priority

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
        self.__priority = priority
        self.__amount = amount

    def set_target(self, entity):
        self.target_entity = entity

    @staticmethod
    def start(self):
        return True

    def update(self, time):  # TODO make work for any given entity
        character_position = self.engine.character.components[PositionNode.__name__]
        new_location = self.engine.vertical_add(character_position.location, self.__amount)
        character_position.location = new_location

        character_locations_visited = self.engine.character.components[LocationsVisitedNode.__name__]

        if not character_locations_visited.has_visited(new_location):
            self.engine.character.components[ScoreNode.__name__].change_score(5)
            character_locations_visited.visit_location(new_location)

        return True

    def end(self):
        return
