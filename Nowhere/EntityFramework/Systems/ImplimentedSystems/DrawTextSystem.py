# Holds the DrawTextSystem class
# Author: William Kluge
# Date: 2017-9-21
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
import pygame


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
        # TODO fix text going off screen
        rendered_text = self.__engine.game_font.render(self.__text, 1, (0, 0, 0))
        self.__engine.screen.blit(rendered_text, self.__location)
        return True

    def end(self):
        return
