# Holds the SystemManager class
# Author: William Kluge
# Date: 2017-9-18


class Engine(object):
    """
    Manages the game loop and the processes that run within it
    """

    continue_updating = True
    __system_queue = []  # The processes to be run the update loop

    def add_system(self, process, priority):
        """
        Adds a process to the queue
        :param process: Process to add
        :param priority: When this should be run compared to other processes
        :return: None
        """
        if process.start:
            self.__system_queue.append((process, priority))
            return True
        return False

    def update(self, time):
        """
        Updates the running processes
        :param time: The delta time between the last loop and this one
        :return: None
        """
        for i in self.__system_queue:
            if i[0].update(time):  # Update the system portion of the system/priority tuple
                self.remove_process(i)

    def remove_process(self, process):
        """
        Safely removes a process from the queue
        :param process: Process to remove
        :return: None
        """
        process[0].end()
        self.__system_queue.remove(process)
