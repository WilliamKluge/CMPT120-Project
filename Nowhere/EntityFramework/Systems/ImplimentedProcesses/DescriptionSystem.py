# Holds the DescriptionSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Systems.SystemInterface import ISystem
from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode


class DescriptionSystem(ISystem):
    """Prints the description for an entity"""

    target_entity = None

    def set_target(self, entity):
        self.target_entity = entity

    @staticmethod
    def start():
        return True

    def update(self, time):
        print(self.target_entity.get_component(DescriptionNode.__name__).description)
        return True

    def end(self):
        return
