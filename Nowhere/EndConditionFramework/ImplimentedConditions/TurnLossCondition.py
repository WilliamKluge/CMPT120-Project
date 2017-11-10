# Holds the TurnLossCondition class
# Author: William Kluge
# Date: 2017-11-10
from Nowhere.EndConditionFramework.IEndCondition import IEndCondition
from Nowhere.EntityFramework.Systems.ImplementedSystems.UpdateCommandSystem import UpdateCommandSystem


class TurnLossCondition(IEndCondition):
    """
    Condition for if the player takes too many moves.
    """

    def ending_message(self):
        return "You took too many moves. You Lose."

    def condition_met(self):
        command_system = next((x for x in self.engine.system_queue
                               if x.__class__.__name__ == UpdateCommandSystem.__name__), None)

        return command_system and command_system.moves_taken > 300
