# Holds the QuitSystem class
# Author: William Kluge
# Date: 2017-9-22
from Nowhere.EntityFramework.Systems.ISystem import ISystem


class QuitSystem(ISystem):
    """Draws text"""

    def __init__(self, engine):
        """
        Quits the game
        :param engine: Engine controlling the game
        """
        self.__engine = engine

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        self.__engine.continue_updating = False
        return True

    def end(self):
        return
