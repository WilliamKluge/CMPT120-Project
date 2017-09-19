# Holds the SystemManager class
# Author: William Kluge
# Date: 2017-9-18

import threading
import queue
import pygame
from pygame.locals import *
import tkinter


class Engine(object):
    """
    Manages the game loop and the processes that run within it
    """

    continue_updating = True
    __system_queue = []  # The processes to be run the update loop
    __input_queue = queue.Queue
    __input_thread = threading.Thread
    __background = None
    screen = None

    def __init__(self):
        self.__input_queue = queue.Queue()
        self.__input_thread = threading.Thread(target=self.get_input, args=(self.__input_queue,), daemon=True)
        self.__input_thread.start()
        # Initialise screen
        pygame.init()
        infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((int(infoObject.current_w / 1280) * 1200,
                                               int(infoObject.current_h / 800) * 600))
        # self.__screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption('Nowhere')
        # Fill background
        self.__background = pygame.Surface(self.screen.get_size())
        self.__background = self.__background.convert()
        self.__background.fill((250, 250, 250))

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

        # Blit everything to the screen
        pygame.display.flip()

        try:
            user_input = self.__input_queue.get(False)
        except queue.Empty:
            user_input = None

        with self.__input_queue.mutex:
            self.__input_queue.queue.clear()

        if user_input == "quit":
            self.continue_updating = False
        elif user_input == "dunkey":
            print("spaghetti and meatballs")
        elif user_input is not None:  # Not a known command, but there is still input
            print("Unknown command, try again")

    def remove_process(self, process):
        """
        Safely removes a process from the queue
        :param process: Process to remove
        :return: None
        """
        process[0].end()
        self.__system_queue.remove(process)

    @staticmethod
    def get_input(q):
        """
        Continuously gets input from the user and places it in the queue.
        Because this is used with a thread that has the daemon=True attribute, it will automatically be killed when the
        main process exits
        :return: None
        """
        while True:
            user_input = input("Enter a command")
            if user_input != "":
                q.put(user_input)
