# Main file for CMPT120-Project
# Author: William Kluge
# Date: 2017-9-8

# noinspection PyUnresolvedReferences
import SetupPath  # Sets up the system path to import everything from Nowhere

from Nowhere.EndConditionFramework.ImplimentedConditions.MapRiverCondition import MapRiverLossCondition
from Nowhere.EndConditionFramework.ImplimentedConditions.MapTowerWinCondition import MapTowerWinCondition
from Nowhere.EndConditionFramework.ImplimentedConditions.TurnLossCondition import TurnLossCondition
from Nowhere.EntityFramework.Entity import Entity
from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Nodes.InventoryNode import InventoryNode
from Nowhere.EntityFramework.Nodes.ItemNode import ItemNode
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
    start.add_component(NameNode("Start"))
    start.add_component(BackgroundNode("Assets/0-0-0Background.png", engine))
    start.add_component(MapMarkerNode("Assets/0-0-0MapMarker.png", engine))
    start.add_component(InventoryNode([ItemNode("Stick", "This is just a stick"),
                                       ItemNode("Map", "This shows you where things are.")]))

    # Forest large tree location
    forest_large_tree = Entity()
    forest_large_tree.add_component(DescriptionNode("A large tree obscures any sight you had above the trees in the "
                                                    "forest."))
    forest_large_tree.add_component(NameNode("The Large Tree"))
    forest_large_tree.add_component(BackgroundNode("Assets/1-0-0Background.png", engine))
    forest_large_tree.add_component(InventoryNode([]))

    # Forest can location
    forest_can = Entity()
    forest_can.add_component(DescriptionNode("{0}, you proceed in the forest to find an oil drum with a burning fire."))
    forest_can.add_component(NameNode("Burning Drum"))
    forest_can.add_component(BackgroundNode("Assets/0-1-0Background.png", engine))
    forest_can.add_component(InventoryNode([ItemNode("Cloth Scrap", "A small piece of cloth.")]))

    # Watchtower stairs location
    watchtower_stairs = Entity()
    watchtower_stairs.add_component(DescriptionNode("As you make your way up the watchtower you notice the stairs"
                                                    " seem a little loose. You gain more visibility over the "
                                                    "treetops the higher you go."))
    watchtower_stairs.add_component(NameNode("Watchtower Stairs"))
    watchtower_stairs.add_component(BackgroundNode("Assets/0-1-1Background.png", engine))
    watchtower_stairs.add_component(InventoryNode([]))

    # Watchtower side location
    watchtower_side = Entity()
    watchtower_side.add_component(DescriptionNode("Standing next to the watchtower you can't see much, but you seem "
                                                  "to have a decent amount of cover"))
    watchtower_side.add_component(NameNode("Watchtower Side"))
    watchtower_side.add_component(BackgroundNode("Assets/0-1-1Background.png", engine))
    watchtower_side.add_component(InventoryNode([]))

    # Watchtower location
    watchtower_top = Entity()
    watchtower_top.add_component(DescriptionNode("Standing on top of the watchtower you can see out for miles. As far"
                                                 " as you can tell, {0}, there is nothing but dense forest to your"
                                                 " north, west, and south, but there is an open field to you east."))
    watchtower_top.add_component(NameNode("Watchtower Top"))
    watchtower_top.add_component(BackgroundNode("Assets/0-1-2Background.png", engine))
    watchtower_top.add_component(InventoryNode([ItemNode("Flashlight", "This will help illuminate dark areas")]))

    # Dense forest
    dense_forest = Entity()
    dense_forest.add_component(DescriptionNode("You are barley able to get through to this part of the forest it is"
                                               " so dense."))
    dense_forest.add_component(NameNode("Dense Forest"))
    dense_forest.add_component(BackgroundNode("Assets/0--1-0Background.png", engine))
    dense_forest.add_component(InventoryNode([]))

    # Denser forest
    denser_forest = Entity()
    denser_forest.add_component(DescriptionNode("You can't get through to this part of the forest it is"
                                                " so dense. {0}, you can't travel any further in this direction."))
    denser_forest.add_component(NameNode("Denser Forest"))
    denser_forest.add_component(BackgroundNode("Assets/0--1-0Background.png", engine))
    denser_forest.add_component(InventoryNode([]))

    # Hill
    hill = Entity()
    hill.add_component(DescriptionNode("You look down a hill populated by tress with a rushing river at the bottom"))
    hill.add_component(NameNode("Hill to the River"))
    hill.add_component(BackgroundNode("Assets/0--1-0Background.png", engine))
    hill.add_component(InventoryNode([]))

    # River
    river = Entity()
    river.add_component(DescriptionNode("You stand by the side of the river and see that it is perfectly clear."
                                        "Something shimmers at the bottom."))
    river.add_component(NameNode("The River"))
    river.add_component(BackgroundNode("Assets/0--1-0Background.png", engine))
    river.add_component(InventoryNode([]))

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
    player.add_component(InventoryNode([]))

    # Add entities to the game engine
    engine.add_location(start, (0, 0, 0))
    engine.add_location(forest_can, (0, 1, 0))
    engine.add_location(watchtower_stairs, (0, 1, 1))
    engine.add_location(watchtower_top, (0, 1, 2))
    engine.add_location(watchtower_side, (0, 2, 0))
    engine.add_location(forest_large_tree, (1, 0, 0))
    engine.add_location(dense_forest, (0, -1, 0))
    engine.add_location(denser_forest, (0, -2, 0))
    engine.add_location(hill, (0, -1, 0))
    engine.add_location(river, (0, -2, 0))
    engine.add_character(player)
    engine.add_entity(game_map)

    # Add ending conditions
    engine.add_end_condition(TurnLossCondition(engine))
    engine.add_end_condition(MapRiverLossCondition(engine))
    engine.add_end_condition(MapTowerWinCondition(engine))

    # Starts the engine updating process
    engine.update()


if __name__ == "__main__":
    main()
