# Main file for CMPT120-Project
# Author: William Kluge
# Date: 2017-9-8

# noinspection PyUnresolvedReferences
import SetupPath  # Sets up the system path to import everything from Nowhere

from Nowhere.EntityFramework.Entity import Entity
from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Nodes.LocationsVisitedNode import LocationsVisitedNode
from Nowhere.EntityFramework.Nodes.MapMarkerNode import MapMarkerNode
from Nowhere.EntityFramework.Nodes.NameNode import NameNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Nodes.ScoreNode import ScoreNode
from Nowhere.EntityFramework.Systems.Engine import Engine
from Nowhere.EntityFramework.Systems.ImplementedSystems.TitleScreenSystem import TitleScreenSystem


def main():
    # Game engine
    engine = Engine()

    # Adds the title screen to the game
    engine.add_system(TitleScreenSystem(engine,
                                        "Nowhere",
                                        "You don't know where you are or how you got there. Unless you can find a way "
                                        "to civilization or figure out how to survive, you will die."))

    # Start location
    start = Entity()
    start.add_component(DescriptionNode("{0}, you are in a foggy forest. The landscape around you is hard to see, but "
                                        "you can make out some structure off in the distance"))
    start.add_component(BackgroundNode("Assets/0-0-0Background.png", engine))
    start.add_component(MapMarkerNode("Assets/0-0-0MapMarker.png", engine))

    # Forest large tree location
    forest_large_tree = Entity()
    forest_large_tree.add_component(DescriptionNode("A large tree obscures any sight you had above the trees in the "
                                                    "forest."))
    forest_large_tree.add_component(BackgroundNode("Assets/1-0-0Background.png", engine))

    # Forest can location
    forest_can = Entity()
    forest_can.add_component(DescriptionNode("{0}, you proceed in the forest to find an oil drum with a burning fire."))
    forest_can.add_component(BackgroundNode("Assets/0-1-0Background.png", engine))

    # Watchtower stairs location
    watchtower_stairs = Entity()
    watchtower_stairs.add_component(DescriptionNode("As you make your way up the watchtower you notice the stairs"
                                                    " seem a little loose. You gain more visibility over the "
                                                    "treetops the higher you go."))
    watchtower_stairs.add_component(BackgroundNode("Assets/0-1-1Background.png", engine))

    # Watchtower location
    watchtower_top = Entity()
    watchtower_top.add_component(DescriptionNode("Standing on top of the watchtower you can see out for miles. As far"
                                                 " as you can tell, {0}, there is nothing but dense forest to your"
                                                 " north, west, and south, but there is an open field to you east."))
    watchtower_top.add_component(BackgroundNode("Assets/0-1-2Background.png", engine))

    # Dense forest
    dense_forest = Entity()
    dense_forest.add_component(DescriptionNode("You are barley able to get through to this part of the forest it is"
                                               "is dense. {0}, you can't travel any further in this direction."))
    dense_forest.add_component(BackgroundNode("Assets/0--1-0Background.png", engine))

    # Map
    game_map = Entity()
    game_map.add_component(BackgroundNode("Assets/MapBackground.png", engine))
    game_map.add_component(MapMarkerNode("Assets/ErrorLocationMarker.png", engine))

    # Player
    player = Entity()
    player.add_component(LocationsVisitedNode())
    player.add_component(PositionNode((0, 0, 0), player))
    player.add_component(ScoreNode())
    player.add_component(NameNode())

    # Add entities to the game engine
    engine.add_location(start, (0, 0, 0))
    engine.add_location(forest_can, (0, 1, 0))
    engine.add_location(forest_large_tree, (1, 0, 0))
    engine.add_location(watchtower_stairs, (0, 1, 1))
    engine.add_location(watchtower_top, (0, 1, 2))
    engine.add_location(dense_forest, (0, -1, 0))
    engine.add_character(player)
    engine.add_entity(game_map)

    # Starts the engine updating process
    engine.update()


if __name__ == "__main__":
    main()
