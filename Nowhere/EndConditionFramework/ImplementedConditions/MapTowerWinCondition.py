# Holds the MapTowerWinCondition class
# Author: William Kluge
# Date: 2017-11-10
from Nowhere.EndConditionFramework.IEndCondition import IEndCondition
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode


class MapTowerWinCondition(IEndCondition):
    """
    Condition for if the player uses the map while they are at the top of the tower
    """

    def __init__(self, engine):
        """
        :param engine: Engine controlling the game
        """
        super().__init__(engine)
        self.map_used_on_tower = None

    def check_condition(self):
        self.map_used_on_tower = self.engine.character.components[PositionNode.__name__].location == (0, 1, 2) \
               and self.engine.character.components[InventoryNode.__name__].search().find("Map") != -1

    def ending_message(self):
        return "From the top of the tower you can use the map to navigate your way back to civilization. You Win!"

    def condition_met(self):
        return self.map_used_on_tower
