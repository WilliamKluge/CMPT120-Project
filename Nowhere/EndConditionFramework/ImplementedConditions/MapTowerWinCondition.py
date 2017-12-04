# Holds the MapTowerWinCondition class
# Author: William Kluge
# Date: 2017-11-10
from Nowhere.EndConditionFramework.IEndCondition import IEndCondition
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode


class MapTowerWinCondition(IEndCondition):
    """
    Condition for if the player has the map when they are at the top of the tower
    """

    def ending_message(self):
        return "From the top of the tower you can use the map to navigate your way back to civilization. You Win!"

    def condition_met(self):

        return self.engine.character.components[PositionNode.__name__].location == (0, 1, 2) \
               and self.engine.character.components[InventoryNode.__name__].search().find("Map") != -1
