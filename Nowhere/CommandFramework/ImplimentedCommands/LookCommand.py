# Holds the LookCommand class
# Author: William Kluge
# Date: 2017-11-8
from Nowhere.CommandFramework.ICommand import ICommand
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Nodes.LocationsVisitedNode import LocationsVisitedNode
from Nowhere.EntityFramework.Nodes.NameNode import NameNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.ImplementedSystems.DrawTextSystem import DrawTextSystem


class LookCommand(ICommand):

    @property
    def help_string(self):
        return "Prints the long description of the user's current location."

    @property
    def key(self):
        return "look"

    def is_possible(self, engine):
        """
        Returns the opposite condition of that used in DrawLocationSystem to decide if the long description should be
        printed.
        This command can only be run if the long description was not normally printed
        :param engine: Game engine
        :return: If the command can be run
        """
        player = engine.character
        player_location = player.components[PositionNode.__name__].location
        player_path = player.components[LocationsVisitedNode.__name__].visited_locations

        return player_path.index(player_location) != len(player_path) - 1

    def create_system(self, engine, user_input):
        # Get sizes
        w, h = engine.screen.get_size()
        # Get location
        location = engine.locations[engine.character.components[PositionNode.__name__].location]
        # Get player name
        player_name = engine.character.components[NameNode.__name__].name

        return DrawTextSystem(engine,
                              location.components[DescriptionNode.__name__].description,
                              (w * 0.05, w * 0.05),
                              player_name,
                              False)
