# Holds the NorthCommand class
# Author: William Kluge
# Date: 2017-10-15
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawTextSystem import DrawTextSystem


class HelpCommand(ICommand):
    @property
    def help_string(self):
        return "Prints help to the user."

    @property
    def key(self):
        return "help"

    def is_possible(self, engine):
        return True

    def create_system(self, engine, using=None, target=None):
        return DrawTextSystem(engine, "Commands are located on the left of the screen.\nEach direction command moves"
                                      " you in that direction. The quit command exits the game.", (50, 20),
                              no_wait=False)
