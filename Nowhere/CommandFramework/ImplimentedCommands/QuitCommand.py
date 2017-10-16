# Holds the NorthCommand class
# Author: William Kluge
# Date: 2017-10-15
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Systems.ImplimentedSystems.QuitSystem import QuitSystem


class QuitCommand(ICommand):
    @property
    def help_string(self):
        return "Quits the game."

    @property
    def key(self):
        return "quit"

    def is_possible(self, engine):
        return True

    def create_system(self, engine, using=None, target=None):
        return QuitSystem(engine, "This game and its contents are all owned by William Kluge. Contact: "
                                  "klugewilliam@gmail.com")
