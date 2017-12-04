# Demo of how a game would use a traditional matrix for movement
# Author: William Kluge
# Date: 2017-11-13


def main():
    beach = 0
    hall = 1
    room = 2
    roof = 3
    long_hall = 4
    locations = [[beach, None, None, None],
                 [hall, room, long_hall, None],
                 [None, None, roof, None],
                 [None, None, beach, None]]

    x = 0
    y = 1

    location_description = ["beach", "hall", "room", "roof", "long_hall"]

    while True:
        print(location_description[locations[y][x]])

        movement = input("enter north, south, east, or west")

        new_x = x
        new_y = y

        if movement == "north":
            new_y -= 1
        elif movement == "south":
            new_y += 1
        elif movement == "east":
            new_x += 1
        elif movement == "west":
            new_x -= 1
        else:
            print("invalid input")

        if locations[new_y][new_x] is not None:
            y = new_y
            x = new_x
            print("Player moved")


if __name__ == "__main__":
    main()
