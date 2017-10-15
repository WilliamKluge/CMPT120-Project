# Holds the UpdateCommandSystem class
# Author: William Kluge
# Date: 2017-9-25
import pygame

from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Nodes.ScoreNode import ScoreNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawTextSystem import DrawTextSystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.MoveSystem import MoveSystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.QuitSystem import QuitSystem


class UpdateCommandSystem(ISystem):  # TODO make it so that commands use parts of the system like screen or character
    """Updates the commands the user has available and draws the users score"""

    def __init__(self, engine):
        """
        :param engine: Engine controlling the game
        """
        self.__engine = engine
        # Possible commands given characters location, surrounding items, etc.
        self.possible_commands = dict()

    def set_target(self, target):
        return

    def set_using(self, using):
        return

    @property
    def priority(self):
        return 100

    @staticmethod
    def start(self):
        return True

    def update(self, time):  # TODO only update the command dictionary when the user does something that would change it
        # Update user input (also draws possible commands to the screen)
        user_input = self.__engine.input_box.value
        # Get the size of the screen
        w, h = self.__engine.screen.get_size()
        # Sets the location to start drawing the text
        start_location = (int(w * 0.02), int(h * 0.25))
        # Getting the height and width of the font
        text_width, text_height = self.__engine.game_font.size("P")

        if self.__engine.input_box.value is not '':
            # If the input box is not empty, set the color to black
            self.__engine.input_box.color = (0, 0, 0)

        if user_input in self.possible_commands and next((x for x in self.__engine.events
                                                          if x.type == pygame.KEYDOWN and x.key == pygame.K_RETURN),
                                                         None):
            # Checks if the user press enter and has input that matches a command in possible commands
            self.__engine.add_system(self.possible_commands[user_input])
            self.__engine.input_box.value = ''

        # Clear the commands from the last iteration
        self.possible_commands.clear()

        # Update where the character can move to
        character_location = self.__engine.character.components[PositionNode.__name__].location

        if self.__engine.vertical_add(character_location, (1, 0, 0)) in self.__engine.locations:
            self.possible_commands["north"] = MoveSystem(self.__engine.character, self.__engine, 0, (1, 0, 0))

        if self.__engine.vertical_add(character_location, (0, 1, 0)) in self.__engine.locations:
            self.possible_commands["east"] = MoveSystem(self.__engine.character, self.__engine, 0, (0, 1, 0))

        if self.__engine.vertical_add(character_location, (-1, 0, 0)) in self.__engine.locations:
            self.possible_commands["south"] = MoveSystem(self.__engine.character, self.__engine, 0, (-1, 0, 0))

        if self.__engine.vertical_add(character_location, (0, -1, 0)) in self.__engine.locations:
            self.possible_commands["west"] = MoveSystem(self.__engine.character, self.__engine, 0, (0, -1, 0))

        if self.__engine.vertical_add(character_location, (0, 0, 1)) in self.__engine.locations:
            self.possible_commands["up"] = MoveSystem(self.__engine.character, self.__engine, 0, (0, 0, 1))

        if self.__engine.vertical_add(character_location, (0, 0, -1)) in self.__engine.locations:
            self.possible_commands["down"] = MoveSystem(self.__engine.character, self.__engine, 0, (0, 0, -1))

        # The default commands that can always be run
        self.possible_commands["quit"] = QuitSystem(self.__engine,
                                                    "This game and its contents are all owned by "
                                                    "William Kluge. Contact: klugewilliam@gmail.com")

        self.possible_commands["help"] = DrawTextSystem(self.__engine,
                                                        "Commands are located on the left of the screen.\n"
                                                        "Each direction command moves you in that direction."
                                                        "The quit command exits the game.", (50, 20),
                                                        no_wait=False)

        # Draw the command list to the screen

        text = [self.__engine.game_font.render("Possible Commands:", 1, (0, 0, 0))]  # The array of text to render

        for key in self.possible_commands:
            # Cycles through all possible commands
            if user_input in key:
                # Renders the text and adds it to the array if the user is already typing a command
                text.append(self.__engine.game_font.render(key, 1, (0, 0, 0)))

        if len(text) == 1:
            # If the only text is "Possible Commands:", set the color to red
            self.__engine.input_box.color = (255, 0, 0)

        for i in range(len(text)):
            # Blits the text to the screen
            self.__engine.screen.blit(text[i], self.__engine.vertical_add(start_location, (0, text_height * i)))

        # Draws the user's score
        self.__engine.add_system(DrawTextSystem(self.__engine,
                                                "Score: "
                                                + str(self.__engine.character.components[ScoreNode.__name__].score),
                                                (w * 0.90, 0)))

        return False

    def end(self):
        return
