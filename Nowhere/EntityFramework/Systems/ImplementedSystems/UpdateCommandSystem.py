# Holds the UpdateCommandSystem class
# Author: William Kluge
# Date: 2017-9-25
import pygame

from Nowhere.CommandFramework.ImplimentedCommands.DownCommand import DownCommand
from Nowhere.CommandFramework.ImplimentedCommands.EastCommand import EastCommand
from Nowhere.CommandFramework.ImplimentedCommands.HelpCommand import HelpCommand
from Nowhere.CommandFramework.ImplimentedCommands.MapCommand import MapCommand
from Nowhere.CommandFramework.ImplimentedCommands.NorthCommand import NorthCommand
from Nowhere.CommandFramework.ImplimentedCommands.PointsCommand import PointsCommand
from Nowhere.CommandFramework.ImplimentedCommands.QuitCommand import QuitCommand
from Nowhere.CommandFramework.ImplimentedCommands.SouthCommand import SouthCommand
from Nowhere.CommandFramework.ImplimentedCommands.TakeCommand import TakeCommand
from Nowhere.CommandFramework.ImplimentedCommands.UpCommand import UpCommand
from Nowhere.CommandFramework.ImplimentedCommands.WestCommand import WestCommand
from Nowhere.EntityFramework.Systems.ISystem import ISystem


class UpdateCommandSystem(ISystem):  # TODO make it so that commands use parts of the system like screen or character
    """Updates the commands the user has available and checks if they are being activated"""

    def __init__(self, engine):
        """
        :param engine: Engine controlling the game
        """
        super().__init__(engine)
        # Commands that can be run (any command that is any part of the game)
        self.commands = [NorthCommand(), SouthCommand(), EastCommand(), WestCommand(), UpCommand(), DownCommand(),
                         TakeCommand(), MapCommand(), PointsCommand(), QuitCommand(), HelpCommand()]
        # Commands that the user can enter in the current iteration
        self.possible_commands = dict()

        self.moves_taken = 0

    @property
    def priority(self):
        return 100

    def update(self, time):  # TODO only update the command dictionary when the user does something that would change it
        # Gets user input as lower case characters
        user_input = self.engine.input_box.value.lower()

        # Clear the commands from the last iteration
        self.possible_commands.clear()

        for command in self.commands:
            if command.is_possible(self.engine):
                if command.is_multipart() and user_input[:len(command.key)] == command.key:
                    # The command is multipart and the first part of the user's input is the command's key
                    for i in command.generate_multipart_commands(self.engine):
                        self.possible_commands[i] = command
                else:
                    self.possible_commands[command.key] = command

        if user_input in self.possible_commands \
                and next((x for x in self.engine.events if x.type == pygame.KEYDOWN and x.key == pygame.K_RETURN),
                         None):
            # Checks if the user press enter and has input that matches a command in possible commands
            command = self.possible_commands[user_input]  # Command the user triggered
            self.engine.add_system(command.create_system(self.engine, user_input))
            self.engine.input_box.value = ''

            if command.key == "north" or command.key == "south" or command.key == "east" or command.key == "west":
                self.moves_taken += 1

        self.__draw_commands(user_input)

        return False

    def __draw_commands(self, user_input):
        # Get the size of the screen
        w, h = self.engine.screen.get_size()
        # Sets the location to start drawing the text
        start_location = (int(w * 0.02), int(h * 0.25))
        # Getting the height and width of the font
        text_width, text_height = self.engine.game_font.size("P")

        text = [self.engine.game_font.render("Possible Commands:", 1, (0, 0, 0))]  # The array of text to render

        for key in self.possible_commands:
            # Cycles through all possible commands
            if user_input == key[0:len(user_input)]:
                # Renders the text and adds it to the array if the user is already typing a command
                text.append(self.engine.game_font.render(key, 1, (0, 0, 0)))

        if len(text) == 1:
            # If the only text is "Possible Commands:", set the color to red
            self.engine.input_box.color = (255, 0, 0)
        else:
            self.engine.input_box.color = (0, 0, 0)

        for i in range(len(text)):
            # Blits the text to the screen
            self.engine.screen.blit(text[i], self.engine.vertical_add(start_location, (0, text_height * i)))
