# Holds the DrawTextSystem class
# Author: William Kluge
# Date: 2017-9-21

from Nowhere.EntityFramework.Systems.ISystem import ISystem


class UpdateCommandSystem(ISystem):
    """Draws text"""

    @property
    def priority(self):
        return 100

    def __init__(self, engine):
        """
        Updates the commands the user has available
        :param engine: Engine controlling the game
        """
        self.__engine = engine

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        # Update user input (also draws possible commands to the screen)
        self.__engine.update_commands()

        return False

    def end(self):
        return
