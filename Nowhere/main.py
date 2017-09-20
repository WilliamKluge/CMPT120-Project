# Main file for CMPT120-Project
# Author: William Kluge
# Date: 2017-9-8
from Nowhere.EntityFramework.Entity import Entity
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Nodes.BackgroundNode import BackgroundNode
from Nowhere.EntityFramework.Nodes.PositionNode import PositionNode
from Nowhere.EntityFramework.Systems.Engine import Engine
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DescriptionSystem import DescriptionSystem
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DrawLocationSystem import DrawLocationSystem
import pygame


def main():

    engine = Engine()

    start = Entity()
    start.add_component(DescriptionNode("Start", "You are in a foggy forest. The landscape around you is hard to see, "
                                                 "but you can make out some structure off in the distance"))
    start.add_component(BackgroundNode("Assets/Background.png"))
    start.components[BackgroundNode.__name__].scale_image(engine)
    forest_can = Entity()
    forest_can.add_component(DescriptionNode("Can", "You are getting closer to the structure. You see a tin can on the"
                                                    " ground next to you."))
    forest_can.add_component(BackgroundNode("Assets/1-0-0Background.png"))
    forest_can.components[BackgroundNode.__name__].scale_image(engine)

    player = Entity()
    player.add_component(PositionNode((0, 0, 0)))

    engine.add_location(start, (0, 0, 0))
    engine.add_location(forest_can, (1, 0, 0))
    engine.add_character(player)

    while engine.continue_updating:
        engine.update(0)


    # forest_can = Location("can", ("You are getting closer to the structure. You see a tin can on the ground next to "
    #                               "you."))
    # forest_large_tree = ("The Large Tree", ("The structure is now clearly visible as some sort of watchtower. You also "
    #                                         "notice a very large tree that you could not see before."))
    # watchtower_stairs = ("The Stairs of the Watchtower", ("As you make your way up the watchtower you notice the stairs"
    #                                                       " seem a little loose. You gain more visibility over the "
    #                                                       "treetops the higher you go."))
    # watchtower = ("The Watchtower", ("Standing on top of the watchtower you can see out for miles. As far as you can "
    #                                  "tell, there is nothing but dense forest to your north, west, and south, but there"
    #                                  " is an open field to you east."))

    # player_location = start
    # score = 0

    # print("Nowhere\nYou don't know where you are or how you got there. Unless you can find a way to civilization or"
    #       " figure out how to survive, you will die.")

    # player_location = change_location(start, score)
    # score += 5
    # player_location = change_location(forest_can, score)
    # score += 5
    # player_location = change_location(forest_large_tree, score)
    # score += 5
    # player_location = change_location(watchtower_stairs, score)
    # score += 5
    # player_location = change_location(watchtower, score)
    # score += 5

    # print("\nA helicopter comes and picks you up from the watchtower. You're saved!")
    # print("Final score:", score)
    print("This game and its contents are all owned by William Kluge. Contact: klugewilliam@gmail.com")


if __name__ == "__main__":
    main()
