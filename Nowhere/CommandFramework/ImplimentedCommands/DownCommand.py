# Holds the NorthCommand class
# Author: William Kluge
# Date: 2017-10-15
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ImplimentedSystems.MoveSystem import MoveSystem


class DownCommand(ICommand):

    @property
    def help_string(self):
        return "Moves the character to the location below their current location."

    @property
    def key(self):
        return "down"

    def is_possible(self, engine):
        character_location = engine.character.components[PositionNode.__name__].location
        return engine.vertical_add(character_location, (0, 0, -1)) in engine.locations

    def create_system(self, engine, using=None, target=None):
        return MoveSystem(engine, using, 0, (0, 0, -1))
