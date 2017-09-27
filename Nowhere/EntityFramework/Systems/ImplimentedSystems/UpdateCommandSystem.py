# Holds the UpdateCommandSystem class
# Author: William Kluge
# Date: 2017-9-25
from Nowhere.EntityFramework.Nodes.ScoreNode import ScoreNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawTextSystem import DrawTextSystem


class UpdateCommandSystem(ISystem):
    """Updates the commands the user has available and draws the users score"""

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
        self.__engine.update_commands()

        w, h = self.__engine.screen.get_size()  # Gets the size of the screen

        # Draws the user's score
        self.__engine.add_system(DrawTextSystem(self.__engine,
                                                "Score: "
                                                + str(self.__engine.character.components[ScoreNode.__name__].score),
                                                (w * 0.90, 0)))

        return False

    def end(self):
        return
