# Holds the ISystem interface
# Author: William Kluge
# Date: 2017-9-18

from abc import ABC, abstractmethod


class ISystem(ABC):
    """
    Base class for a system
    """

    @abstractmethod
    def start(self):
        """
        Run the first time the system starts
        :return: A boolean indicating if the start was successful
        """

    @abstractmethod
    def update(self, time):
        """
        Run an update for the system and return true if it is done
        :param time: The difference in time between updates
        :return: If the system is done
        """

    @abstractmethod
    def end(self):
        """
        Clean up the system so that it can finish cleanly or start the next system
        :return: None
        """
