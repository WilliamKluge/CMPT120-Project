# Holds the MapRiverLossCondition class
# Author: William Kluge
# Date: 2017-11-10
from Nowhere.EndConditionFramework.IEndCondition import IEndCondition
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode


class MapRiverLossCondition(IEndCondition):
    """
    Condition for if the player has the map when they are by the river.
    """

    def ending_message(self):
        return "The map got wet from the river and can no longer be used. You Lose."

    def condition_met(self):

        return self.engine.character.components[PositionNode.__name__].location == (0, -2, 0) \
               and self.engine.character.components[InventoryNode.__name__].search().find("Map") != -1
