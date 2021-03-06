# Holds the ISystem interface
# Author: William Kluge
# Date: 2017-9-18

from abc import ABC, abstractmethod


class ISystem(ABC):
    """
    Base class for a system
    """

    @abstractmethod
    def __init__(self, engine):
        self.engine = engine
        self.using = None
        self.target = None

    @property
    @abstractmethod
    def priority(self):
        """
        :return: The priority of this system. Lower = higher priority
        """
        pass

    def set_target(self, target):
        """
        Sets the entity for this system to target
        :param target: Entity to target
        :return: None
        """
        self.target = target

    def set_using(self, using):
        """
        Sets the entity for this system to use
        :param using: Entity to use
        :return: None
        """
        self.using = using

    def start(self):
        """
        Run the first time the system starts
        :return: A boolean indicating if the start was successful
        """
        return True

    @abstractmethod
    def update(self, time):
        """
        Run an update for the system and return true if it is done
        :param time: The difference in time between updates
        :return: If the system is done
        """

    def end(self):
        """
        Clean up the system so that it can finish cleanly or start the next system
        :return: None
        """
        return
