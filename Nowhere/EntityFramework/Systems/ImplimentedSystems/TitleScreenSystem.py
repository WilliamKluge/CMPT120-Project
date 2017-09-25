# Holds the DrawTextSystem class
# Author: William Kluge
# Date: 2017-9-21
import textwrap

import pygame

from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawLocationSystem import DrawLocationSystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.UpdateCommandSystem import UpdateCommandSystem


class TitleScreenSystem(ISystem):
    """Draws the title screen until the player presses a key"""

    @property
    def priority(self):
        return 0

    def __init__(self, engine, title, text):
        """
        Draws the title screen of the game
        :param engine: Engine controlling the game
        :param title: Title of the game
        :param text: Text to draw on the screen
        """
        self.__engine = engine
        self.__title = title
        self.__text = text
        self.background = pygame.Surface(engine.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((100, 100, 100))

    @staticmethod
    def start(self):
        return True

    def update(self, time):  # TODO clean this up
        line_length = 120
        wrapped_text = textwrap.wrap(self.__text, line_length)
        w, h = self.__engine.screen.get_size()
        text_width, text_height = self.__engine.game_font.size("P")  # Get the height of the font

        self.__engine.screen.blit(self.background, (0, 0))

        location = (w * 0.50 - (len(self.__title) * text_width) / 2, h * 0.50)
        self.__engine.screen.blit(self.__engine.game_font.render(self.__title, 1, (0, 0, 0)), location)

        for i in range(len(wrapped_text)):
            location = (w * 0.50 - (len(wrapped_text[i]) * text_width) / 2, h * 0.50 + text_height * (i + 1))
            self.__engine.screen.blit(self.__engine.game_font.render(wrapped_text[i], 1, (0, 0, 0)), location)

        self.__engine.screen.blit(self.__engine.game_font.render("Press any key to start", 1, (0, 0, 0)),
                                  (w * 0.50 - (22 * text_width) / 2, h * 0.90))

        return self.__engine.input_box.value  # Keep updating while the value in the box is empty

    def end(self):
        self.__engine.input_box.value = ''  # Clear anything entered in the input box
        self.__engine.add_system(DrawLocationSystem(self.__engine.character, self.__engine))
        self.__engine.add_system(UpdateCommandSystem(self.__engine))
        return
