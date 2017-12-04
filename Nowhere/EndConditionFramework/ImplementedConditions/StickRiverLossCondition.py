# Holds the StickRiverLossCondition class
# Author: William Kluge
# Date: 2017-11-10
from Nowhere.EndConditionFramework.IEndCondition import IEndCondition
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode


class StickRiverLossCondition(IEndCondition):
    """
    Condition for if the player uses the stick when they are by the river.
    """

    def __init__(self, engine):
        """
        :param engine: Engine controlling the game
        """
        super().__init__(engine)
        self.stick_used_at_river = False

    def check_condition(self):
        self.stick_used_at_river = self.engine.character.components[PositionNode.__name__].location == (0, -2, 0) \
                                   and self.engine.character.components[InventoryNode.__name__].search().find(
            "Stick") != -1

    def ending_message(self):
        return "You dropped your stick in the river. You Lose."

    def condition_met(self):
        return self.stick_used_at_river
