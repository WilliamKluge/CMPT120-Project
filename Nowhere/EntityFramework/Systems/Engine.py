# Holds the SystemManager class
# Author: William Kluge
# Date: 2017-9-18

import time

import pygame
from pygame.locals import *

import Nowhere.PygameLibraries.eztext as eztext
from Nowhere.EntityFramework.Systems.ImplementedSystems.EndScreenSystem import EndScreenSystem


class Engine(object):
    """
    Manages the game loop and the processes that run within it
    TODO Get all entities into one array
    """
    continue_updating = True  # If the game should continue to be updated or if it should end
    locations = dict()  # Stores locations in the game
    character = None  # Character of the game
    entities = []  # Entities of the game engine TODO move locations and character here
    game_font = None  # Font to use for any text put on the screen
    system_queue = []  # The processes to be run the update loop
    __ending_conditions = []
    __handled_systems = []  # Systems controlled by other systems and can be run without checking their end state

    def __init__(self):
        # Initialise screen
        pygame.init()
        pygame.display.set_caption('Nowhere')
        info_object = pygame.display.Info()
        self.screen = pygame.display.set_mode((int(info_object.current_w * 0.75),
                                               int(info_object.current_h * 0.75)))

        # Initialize font
        self.game_font = pygame.font.SysFont("monospace", 15)

        # Create input box
        self.input_box = eztext.Input(maxlength=45, color=(0, 0, 0), prompt='Enter your name: ')
        self.input_box.set_font(self.game_font)

        # Events that happen in the game
        self.events = None

        # Initialize and Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

    def add_system(self, system):
        """
        Adds a process to the queue
        :param system: Process to add
        :return: None
        """
        if system.start:
            self.system_queue.append(system)
            return True
        return False

    def update(self):
        """
        Runs the game
        :return: None
        """
        last_time = time.clock()

        while self.continue_updating:
            current_time = time.clock()

            # Draw the background created in __init__ to the screen
            self.screen.blit(self.background, (0, 0))

            # Events for self.__input_box
            self.events = pygame.event.get()
            # Process other events
            for event in self.events:
                # Close if window is closed
                if event.type == QUIT:
                    return

            sorted(self.system_queue, key=lambda system: system.priority)  # Sorts systems based on their priority

            # Update processes in the main queue of the game
            for i in self.system_queue:
                if i.update(current_time - last_time):
                    self.remove_system(i)

            # Update processes that are completely controlled by other processes
            for i in self.__handled_systems:
                i.update(current_time - last_time)

            self.input_box.update(self.events)
            self.input_box.draw(self.screen)

            for condition in self.__ending_conditions:
                # Iterate through the game ending conditions
                if condition.condition_met():
                    # If the condition to end the game has been met, print its message and return
                    end_system = EndScreenSystem(self)
                    end_system.set_using(condition.ending_message())
                    self.add_system(end_system)

            # Blit everything to the screen
            pygame.display.flip()

    def remove_system(self, system):
        """
        Safely removes a process from the queue
        :param system: Process to remove
        :return: None
        """
        try:
            system.end()
            self.system_queue.remove(system)
        except ValueError:
            # ValueError happens because the item no longer exists, and that's fine cause we were doing that anyways!
            return

    def add_location(self, location, coordinate):
        """
        Adds a location to the game engine
        :param location: The entity of the location to add
        :param coordinate: Coordinate of the location (x, y, z)
        :return: None
        """
        self.locations[coordinate] = location

    def add_entity(self, entity):
        """
        Adds an entity to the game engine
        :param entity: Entity to add to the game
        :return: None
        """
        self.entities.append(entity)

    def add_character(self, entity):
        """
        Adds the controllable character to the engine
        :param entity:
        :return: None
        """
        self.character = entity

    def add_end_condition(self, condition):
        """
        Adds an end condition to be checked
        :param condition: IEndCondition child
        :return: None
        """
        self.__ending_conditions.append(condition)

    def reset_data(self):
        """
        Resets all data in the engine to its default values
        :return:
        """
        self.locations = dict()  # Stores locations in the game
        self.character = None  # Character of the game
        self.entities = []  # Entities of the game engine TODO move locations and character here
        self.system_queue = []  # The processes to be run the update loop
        self.__ending_conditions = []
        self.__handled_systems = []  # Systems controlled by other systems can be run without checking their end state
        self.events = []

    @staticmethod
    def vertical_add(*iterables):
        """
        Adds iterables vertically.
        If tuples (1, 2, 3) and (1, 2, 3) are given tuple (2, 4, 6) will be returned
        :param iterables: Iterable objects to add
        :return: tuple_one and tuple_two added together
        """
        return tuple([sum(i) for i in zip(*iterables)])
