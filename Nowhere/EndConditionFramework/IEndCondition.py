# General definition of what a game ending condition should look like
# Author: William Kluge
# Date: 2017-11-10
from abc import abstractmethod


class IEndCondition:
    """
    General class for how any game ending condition behaves.
    """

    def __init__(self, engine):
        """
        Constructor needed for all game ending conditions
        :param engine: Engine running the game
        """
        self.engine = engine

    @property
    @abstractmethod
    def ending_message(self):
        """
        :return: Message to show the user if the game is ended with this condition
        """

    @abstractmethod
    def condition_met(self):
        """
        :return: Returns if the condition for the game to end is met
        """