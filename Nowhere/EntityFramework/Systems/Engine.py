# Holds the SystemManager class
# Author: William Kluge
# Date: 2017-9-18

import pygame
from pygame.locals import *

import Nowhere.PygameLibraries.eztext as eztext
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawLocationSystem import DrawLocationSystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.MoveSystem import MoveSystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.QuitSystem import QuitSystem


class Engine(object):
    """
    Manages the game loop and the processes that run within it
    TODO Get all entities into one array
    """

    continue_updating = True  # If the game should continue to be updated or if it should end
    locations = dict()  # Stores locations in the game
    character = None  # Character of the game
    game_font = None  # Font to use for any text put on the screen
    __system_queue = []  # The processes to be run the update loop
    __handled_systems = []  # Systems controlled by other systems and can be run without checking their end state

    def __init__(self):
        # Initialise screen
        pygame.init()
        pygame.display.set_caption('Nowhere')
        info_object = pygame.display.Info()
        self.screen = pygame.display.set_mode((int(info_object.current_w / 1280) * 1200,
                                               int(info_object.current_h / 800) * 600))
        # Initialize font
        self.game_font = pygame.font.SysFont("monospace", 15)
        # Create input box
        self.__input_box = eztext.Input(maxlength=45, color=(0, 0, 0), prompt='Enter Command: ')
        self.__input_box.set_font(self.game_font)
        # Initialize and Fill background
        self.__background = pygame.Surface(self.screen.get_size())
        self.__background = self.__background.convert()
        self.__background.fill((250, 250, 250))
        # Possible commands given characters location, surrounding items, etc.
        self.__possible_commands = dict()

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
        # Draw the background created in __init__ to the screen
        self.screen.blit(self.__background, (0, 0))

        # Events for self.__input_box
        events = pygame.event.get()

        # Process other events
        for event in events:
            # Close if window is closed
            if event.type == QUIT:
                return

        self.__input_box.update(events)
        self.__input_box.draw(self.screen)

        # Update processes in the main queue of the game
        for i in self.__system_queue:
            if i.update(time):
                self.remove_system(i)

        # Update processes that are completely controlled by other processes
        for i in self.__handled_systems:
            i.update(time)

        # Update user input (also draws possible commands to the screen)
        self.__update_commands()

        # Blit everything to the screen
        pygame.display.flip()

        user_input = self.__input_box.value

        # Checks if the user input is one of the possible commands
        if user_input in self.__possible_commands:
            self.add_system(self.__possible_commands[user_input])
            self.__input_box.value = ''

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

    def __update_commands(self):
        # Clear the commands from the last iteration
        self.__possible_commands.clear()

        # Update where the character can move to
        character_location = self.character.components[PositionNode.__name__].location

        if tuple([sum(i) for i in zip(character_location, (1, 0, 0))]) in self.locations:
            self.__possible_commands["north"] = MoveSystem(self.character, self, 0, (1, 0, 0))

        if tuple([sum(i) for i in zip(character_location, (0, 1, 0))]) in self.locations:
            self.__possible_commands["east"] = MoveSystem(self.character, self, 0, (0, 1, 0))

        if tuple([sum(i) for i in zip(character_location, (-1, 0, 0))]) in self.locations:
            self.__possible_commands["south"] = MoveSystem(self.character, self, 0, (-1, 0, 0))

        if tuple([sum(i) for i in zip(character_location, (0, -1, 0))]) in self.locations:
            self.__possible_commands["west"] = MoveSystem(self.character, self, 0, (0, -1, 0))

        if tuple([sum(i) for i in zip(character_location, (0, 0, 1))]) in self.locations:
            self.__possible_commands["up"] = MoveSystem(self.character, self, 0, (0, 0, 1))

        if tuple([sum(i) for i in zip(character_location, (0, 0, -1))]) in self.locations:
            self.__possible_commands["down"] = MoveSystem(self.character, self, 0, (0, 0, -1))

        # The default commands that can always be run
        self.__possible_commands["quit"] = QuitSystem(self)

        # Draw the command list to the screen
        text = [self.game_font.render("Possible Commands:", 1, (0, 0, 0))]

        for key in self.__possible_commands:
            text.append(self.game_font.render(key, 1, (0, 0, 0)))

        w, h = self.screen.get_size()
        start_location = (int(w * 0.02), int(h * 0.25))
        text_width, text_height = self.game_font.size("P")  # Just getting the height of the font
        for i in range(len(text)):
            self.screen.blit(text[i], tuple([sum(j) for j in zip(start_location, (0, text_height * i))]))
