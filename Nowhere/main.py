# Main file for CMPT120-Project
# Author: William Kluge
# Date: 2017-9-8
from Nowhere.EntityFramework.Entity import Entity
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Systems.Engine import Engine
from Nowhere.EntityFramework.Systems.ImplimentedSystems.DescriptionSystem import DescriptionSystem


def main():

    engine = Engine()

    start = Entity()
    start.add_component(DescriptionNode("Start", "You are in a foggy forest. The landscape around you is hard to see, "
                                                 "but you can make out some structure off in the distance"))

    test = DescriptionSystem()
    test.set_target(start)
    engine.add_system(test, 100)

    while engine.continue_updating:
        engine.update(0)


    # start = Location("Start", ("You are in a foggy forest. The landscape around you is hard to see, but you can make "
    #                            "out some structure off in the distance"))
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
    # print("This game and its contents are all owned by William Kluge. Contact: klugewilliam@gmail.com")


if __name__ == "__main__":
    main()
