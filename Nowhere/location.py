# Holds the location class
# Author: William Kluge
# Date: 2017-9-18


class Location:
    """
    The location class for Nowhere.
    This class is responsible for creating a general shell that can be used to store the information for any location
    in the game. This includes its description, name, any items located there, etc.
    """

    def __init__(self, location_name, location_description):
        self.__location_name = location_name
        self.__location_description = location_description

    def get_name(self):
        return self.__location_name

    def get_description(self):
        return self.__location_description

    visited = False
    __location_name = ""
    __location_description = ""
