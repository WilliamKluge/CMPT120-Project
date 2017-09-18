# Holds the DescriptionData class
# Author: William Kluge
# Date: 2017-9-18


class DescriptionData:
    """Holds the data for describing an entity"""

    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description
