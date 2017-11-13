# Holds the NorthCommand class
# Author: William Kluge
# Date: 2017-10-15
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ImplementedSystems.MoveSystem import MoveSystem


class EastCommand(ICommand):

    @property
    def help_string(self):
        return "Moves the character to the location east of their current location."

    @property
    def key(self):
        return "east"

    def is_possible(self, engine):
        character_location = engine.character.components[PositionNode.__name__].location
        return engine.vertical_add(character_location, (0, 1, 0)) in engine.locations

    def create_system(self, engine, user_input):
        return MoveSystem(engine, engine.character, 0, (0, 1, 0))
