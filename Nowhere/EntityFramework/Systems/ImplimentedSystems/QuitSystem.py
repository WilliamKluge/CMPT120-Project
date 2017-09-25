# Holds the QuitSystem class
# Author: William Kluge
# Date: 2017-9-22
import textwrap

import pygame

from Nowhere.EntityFramework.Systems.ISystem import ISystem


class QuitSystem(ISystem):
    """Draws text"""

    @property
    def priority(self):
        return 0

    def __init__(self, engine, text):
        """
        Draws end screen of the game
        :param engine: Engine controlling the game
        :param text: Text to draw on the screen
        """
        self.__engine = engine
        self.__text = text
        self.background = pygame.Surface(engine.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((100, 100, 100))
        self.start()

    def start(self):
        return True

    def update(self, time):  # TODO clean this up
        self.__engine.system_queue.clear()
        self.__engine.system_queue.append(self)
        line_length = 120
        wrapped_text = textwrap.wrap(self.__text, line_length)
        w, h = self.__engine.screen.get_size()
        text_width, text_height = self.__engine.game_font.size("P")  # Get the height of the font

        self.__engine.screen.blit(self.background, (0, 0))

        for i in range(len(wrapped_text)):
            location = (w * 0.50 - (len(wrapped_text[i]) * text_width) / 2, h * 0.50 + text_height * i)
            self.__engine.screen.blit(self.__engine.game_font.render(wrapped_text[i], 1, (0, 0, 0)), location)

        self.__engine.screen.blit(self.__engine.game_font.render("Press any key to quit", 1, (0, 0, 0)),
                                  (w * 0.50 - (21 * text_width) / 2, h * 0.90))

        return self.__engine.input_box.value  # Keep updating while the value in the box is empty

    def end(self):
        self.__engine.continue_updating = False
        return
