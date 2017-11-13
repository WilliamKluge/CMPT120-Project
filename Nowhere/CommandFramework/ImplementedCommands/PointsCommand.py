# Holds the NorthCommand class
# Author: William Kluge
# Date: 2017-10-15
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Nodes.ScoreNode import ScoreNode
from Nowhere.EntityFramework.Systems.ImplementedSystems.DrawTextSystem import DrawTextSystem


class PointsCommand(ICommand):
    @property
    def help_string(self):
        return "Displays the user's score until they press a key."

    @property
    def key(self):
        return "points"

    def is_possible(self, engine):
        return True

    def create_system(self, engine, user_input):
        # Get the size of the screen
        w, h = engine.screen.get_size()
        return DrawTextSystem(engine, "Score: " + str(engine.character.components[ScoreNode.__name__].score),
                              (w * 0.90, 0), no_wait=False)
