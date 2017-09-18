# Holds the Process interface
# Author: William Kluge
# Date: 2017-9-18

import abc


class IProcess(object):
    """
    Base class for a process
    """

    @abc.abstractmethod
    def start(self):
        """Starts the process"""

    @abc.abstractmethod
    def update(self, time):
        """Run an update for the process and return if it is done"""

    @abc.abstractmethod
    def end(self):
        """Clean up the process so that it can finish cleanly or start the next process"""
