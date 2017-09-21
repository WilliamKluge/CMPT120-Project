# Holds the SystemManager class
# Author: William Kluge
# Date: 2017-9-18

import threading
import queue
import pygame
from pygame.locals import *

from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawLocationSystem import DrawLocationSystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.MoveSystem import MoveSystem


class Engine(object):
    """
    Manages the game loop and the processes that run within it
    TODO Get locations and character into one array
    """

    continue_updating = True  # If the game should continue to be updated or if it should end
    screen = None  # The screen that the game is blited on
    __system_queue = []  # The processes to be run the update loop
    __input_queue = queue.Queue  # Queue for user input
    __input_thread = threading.Thread  # Thread for getting user input
    __background = None  # Background of screen
    locations = dict()  # Stores locations in the game
    character = None

    def __init__(self):
        # Start input thread
        self.__input_queue = queue.Queue()
        self.__input_thread = threading.Thread(target=self.get_input, args=(self.__input_queue,), daemon=True)
        self.__input_thread.start()
        # Initialise screen
        pygame.init()
        info_object = pygame.display.Info()
        self.screen = pygame.display.set_mode((int(info_object.current_w / 1280) * 1200,
                                               int(info_object.current_h / 800) * 600))
        # self.__screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption('Nowhere')
        # Fill background
        self.__background = pygame.Surface(self.screen.get_size())
        self.__background = self.__background.convert()
        self.__background.fill((250, 250, 250))

    def add_system(self, process):
        """
        Adds a process to the queue
        :param process: Process to add
        :return: None
        """
        if process.start:
            self.__system_queue.append(process)
            return True
        return False

    def update(self, time):
        """
        Updates the running processes
        :param time: The delta time between the last loop and this one
        :return: None
        """
        self.screen.blit(self.__background, (0, 0))

        for i in self.__system_queue:
            if i.update(time):  # Update the system portion of the system/priority tuple
                self.remove_system(i)

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
        elif user_input == "north":
            self.add_system(MoveSystem(self.character, self, (1, 0, 0), 0))
        elif user_input == "south":
            self.add_system(MoveSystem(self.character, self, (-1, 0, 0), 0))
        elif user_input == "east":
            self.add_system(MoveSystem(self.character, self, (0, 1, 0), 0))
        elif user_input == "west":
            self.add_system(MoveSystem(self.character, self, (0, -1, 0), 0))
        elif user_input == "debug":
            print(self.character.components[PositionNode.__name__].location)
        elif user_input is not None:  # Not a known command, but there is still input
            print("Unknown command, try again")

    def remove_system(self, system):
        """
        Safely removes a process from the queue
        :param system: Process to remove
        :return: None
        """
        system.end()
        self.__system_queue.remove(system)

    def add_location(self, location, coordinate):
        """
        Adds a location to the game engine
        :param location: The entity of the location to add
        :param coordinate: Coordinate of the location (x, y, z)
        :return: None
        """
        self.locations[coordinate] = location

    def add_character(self, entity):
        """
        Adds the controllable character to the engine
        :param entity:
        :return:
        """
        self.character = entity
        self.add_system(DrawLocationSystem(self.character, self))

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
