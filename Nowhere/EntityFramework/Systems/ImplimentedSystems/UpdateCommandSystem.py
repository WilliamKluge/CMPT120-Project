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


class UpdateCommandSystem(ISystem):
    """Updates the commands the user has available and draws the users score"""
    # TODO update to use new ISystem update due to command framework implimentation

    @property
    def priority(self):
        return 100

    def __init__(self, engine):
        """
        :param engine: Engine controlling the game
        """
        self.__engine = engine

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        # Update user input (also draws possible commands to the screen)
        user_input = self.__engine.input_box.value

        if self.__engine.input_box.value is not '':
            self.__engine.input_box.color = (0, 0, 0)

        if user_input in self.__engine.possible_commands:
            self.__engine.add_system(self.__engine.possible_commands[user_input])
            self.__engine.input_box.value = ''
        elif next((x for x in self.__engine.events if x.type == pygame.KEYDOWN and x.key == pygame.K_RETURN), None):
            self.__engine.input_box.color = (255, 0, 0)
            self.__engine.input_box.value = ''

        # Clear the commands from the last iteration
        self.__engine.possible_commands.clear()

        # Update where the character can move to
        character_location = self.__engine.character.components[PositionNode.__name__].location
        possible_commands = self.__engine.possible_commands

        if self.__engine.vertical_add(character_location, (1, 0, 0)) in self.__engine.locations:
            possible_commands["north"] = MoveSystem(self.__engine.character, self.__engine, 0, (1, 0, 0))

        if self.__engine.vertical_add(character_location, (0, 1, 0)) in self.__engine.locations:
            possible_commands["east"] = MoveSystem(self.__engine.character, self.__engine, 0, (0, 1, 0))

        if self.__engine.vertical_add(character_location, (-1, 0, 0)) in self.__engine.locations:
            possible_commands["south"] = MoveSystem(self.__engine.character, self.__engine, 0, (-1, 0, 0))

        if self.__engine.vertical_add(character_location, (0, -1, 0)) in self.__engine.locations:
            possible_commands["west"] = MoveSystem(self.__engine.character, self.__engine, 0, (0, -1, 0))

        if self.__engine.vertical_add(character_location, (0, 0, 1)) in self.__engine.locations:
            possible_commands["up"] = MoveSystem(self.__engine.character, self.__engine, 0, (0, 0, 1))

        if self.__engine.vertical_add(character_location, (0, 0, -1)) in self.__engine.locations:
            possible_commands["down"] = MoveSystem(self.__engine.character, self.__engine, 0, (0, 0, -1))

        # The default commands that can always be run
        possible_commands["quit"] = QuitSystem(self.__engine,
                                               "This game and its contents are all owned by "
                                               "William Kluge. Contact: klugewilliam@gmail.com")

        possible_commands["help"] = DrawTextSystem(self.__engine,
                                                   "Commands are located on the left of the screen.\n"
                                                   "Each direction command moves you in that direction."
                                                   "The quit command exits the game.", (50, 20),
                                                   no_wait=False)

        # Draw the command list to the screen
        text = [self.__engine.game_font.render("Possible Commands:", 1, (0, 0, 0))]

        for key in self.__engine.possible_commands:
            text.append(self.__engine.game_font.render(key, 1, (0, 0, 0)))

        w, h = self.__engine.screen.get_size()
        start_location = (int(w * 0.02), int(h * 0.25))
        text_width, text_height = self.__engine.game_font.size("P")  # Just getting the height of the font
        for i in range(len(text)):
            self.__engine.screen.blit(text[i], self.__engine.vertical_add(start_location, (0, text_height * i)))

        w, h = self.__engine.screen.get_size()  # Gets the size of the screen

        # Draws the user's score
        self.__engine.add_system(DrawTextSystem(self.__engine,
                                                "Score: "
                                                + str(self.__engine.character.components[ScoreNode.__name__].score),
                                                (w * 0.90, 0)))

        return False

    def end(self):
        return
