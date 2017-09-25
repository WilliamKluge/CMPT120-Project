# Holds the DrawTextSystem class
# Author: William Kluge
# Date: 2017-9-21
import textwrap

from Nowhere.EntityFramework.Systems.ISystem import ISystem


class DrawTextSystem(ISystem):
    """Draws text"""

    @property
    def priority(self):
        return 100

    def __init__(self, engine, text, location, format_text=None):
        """
        Draws text to the screen.
        :param engine: Engine controlling the game.
        :param text: Text to draw on the screen.
        :param location: Location (as a tuple in pixels) where the text is to be drawn.
        :param format_text: The text to format the string with. Use this to replace {} with character name in strings.
        This can be a list if multiple data are to be used during formatting.
        """
        self.__engine = engine
        self.__text = text
        self.__location = location

        if format_text:
            self.__text = self.__text.format(format_text)

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        wrapped_text = textwrap.wrap(self.__text, 120)

        text_width, text_height = self.__engine.game_font.size("P")  # Get the height of the font
        for i in range(len(wrapped_text)):
            self.__engine.screen.blit(self.__engine.game_font.render(wrapped_text[i], 1, (0, 0, 0)),
                                      tuple([sum(j) for j in zip(self.__location, (0, text_height * i))]))

        return self.__engine.input_box.value

    def end(self):
        return
