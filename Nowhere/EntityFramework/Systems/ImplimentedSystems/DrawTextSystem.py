# Holds the DrawTextSystem class
# Author: William Kluge
# Date: 2017-9-21
import textwrap

from Nowhere.EntityFramework.Systems.ISystem import ISystem


class DrawTextSystem(ISystem):
    """Draws text"""

    def __init__(self, engine, text, location):
        """
        Draws text to the screen
        :param engine: Engine controlling the game
        :param text: Text to draw on the screen
        :param location: Location (as a tuple in pixels) where the text is to be drawn
        """
        self.__engine = engine
        self.__text = text
        self.__location = location

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        wrapped_text = textwrap.wrap(self.__text, 120)

        text_width, text_height = self.__engine.game_font.size("P")  # Get the height of the font
        for i in range(len(wrapped_text)):
            self.__engine.screen.blit(self.__engine.game_font.render(wrapped_text[i], 1, (0, 0, 0)),
                                      tuple([sum(j) for j in zip(self.__location, (0, text_height * i))]))

        return True

    def end(self):
        return
