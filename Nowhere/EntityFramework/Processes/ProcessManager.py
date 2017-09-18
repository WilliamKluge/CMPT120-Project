# Holds the ProcessManager class
# Author: William Kluge
# Date: 2017-9-18


class ProcessManager:
    """
    Manages the game loop and the processes that run within it
    """

    __process_queue = []  # The processes to be run the update loop

    def add_process(self, process, priority):
        """
        Adds a process to the queue
        :param process: Process to add
        :param priority: When this should be run compared to other processes
        :return: None
        """
        if process.start:
            self.__process_queue.append((process, priority))
            return True
        return False

    def update(self, time):
        """
        Updates the running processes
        :param time: The delta time between the last loop and this one
        :return: None
        """
        for i in self.__process_queue:
            if i.update(time):
                self.remove_process(i)

    def remove_process(self, process):
        """
        Safely removes a process from the queue
        :param process: Process to remove
        :return: None
        """
        process.end()
        self.__process_queue.remove(process)
