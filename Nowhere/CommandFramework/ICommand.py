# Holds the Command class
# Author: William Kluge
# Date: 2017-10-13
from abc import abstractmethod


class ICommand:
    """
    Defines what a command will do, what the user needs to enter to activate it, and the help string to describe it
    """

    @property
    @abstractmethod
    def key(self):
        """
        :return: Key the user needs to enter to run the command
        """
        return self.key

    @property
    @abstractmethod
    def help_string(self):
        """
        :return: String describing this method
        """
        return self.help_string

    @abstractmethod
    def is_possible(self, engine):
        """
        Determines if the current command can be run or not
        :param engine: Game engine
        :return: Whether or not this command can be run
        """

    @abstractmethod
    def create_system(self, engine, using=None, target=None):
        """
        Returns the created system to add to the system queue of the engine
        :param engine: Game engine
        :param using: Entity the system is using
        :param target: Entity the system is targeting
        :return: Created system
        """
