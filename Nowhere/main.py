# Main file for CMPT120-Project
# Author: William Kluge
# Date: 2017-9-8
from Nowhere.EntityFramework.Entity import Entity
from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.Engine import Engine


def main():
    # Game engine TODO keep track of score
    engine = Engine()
    # Start location
    start = Entity()
    start.add_component(DescriptionNode("Start", "You are in a foggy forest. The landscape around you is hard to see, "
                                                 "but you can make out some structure off in the distance"))
    start.add_component(BackgroundNode("Assets/0-0-0Background.png", engine))
    # Forest can location
    forest_can = Entity()
    forest_can.add_component(DescriptionNode("Can", "You are getting closer to the structure. You see a tin can on the"
                                                    " ground next to you."))
    forest_can.add_component(BackgroundNode("Assets/1-0-0Background.png", engine))
    # Forest large tree location
    forest_large_tree = Entity()
    forest_large_tree.add_component(DescriptionNode("The Large Tree", "The structure is now clearly visible as some "
                                                                      "sort of watchtower. You also notice a very large"
                                                                      " tree that you could not see before."))
    forest_large_tree.add_component(BackgroundNode("Assets/0-1-0Background.png", engine))
    # Watchtower starts location
    watchtower_stairs = Entity()
    watchtower_stairs.add_component(DescriptionNode("The Stairs of the Watchtower",
                                                    "As you make your way up the watchtower you notice the stairs"
                                                    " seem a little loose. You gain more visibility over the "
                                                    "treetops the higher you go."))
    watchtower_stairs.add_component(BackgroundNode("Assets/0-1-1Background.png", engine))
    # Watchtower location
    watchtower = Entity()
    watchtower.add_component(DescriptionNode("The Watchtower",
                                             "Standing on top of the watchtower you can see out for miles. As far as "
                                             "you can tell, there is nothing but dense forest to your north, west, and"
                                             " south, but there is an open field to you east."))
    watchtower.add_component(BackgroundNode("Assets/0-1-2Background.png", engine))
    # Player
    player = Entity()
    player.add_component(PositionNode((0, 0, 0)))
    # Add entities to the game engine
    engine.add_location(start, (0, 0, 0))
    engine.add_location(forest_can, (1, 0, 0))
    engine.add_location(forest_large_tree, (0, 1, 0))
    engine.add_location(watchtower_stairs, (0, 1, 1))
    engine.add_location(watchtower, (0, 1, 2))
    engine.add_character(player)
    # Basic game loop
    while engine.continue_updating:
        engine.update(0)

    # score = 0

    # print("Nowhere\nYou don't know where you are or how you got there. Unless you can find a way to civilization or"
    #       " figure out how to survive, you will die.")

    print("This game and its contents are all owned by William Kluge. Contact: klugewilliam@gmail.com")


if __name__ == "__main__":
    main()
