# Holds the DescriptionSystem class
# Author: William Kluge
# Date: 2017-9-18

from Nowhere.EntityFramework.Nodes.DescriptionNode import DescriptionNode
from Nowhere.EntityFramework.Systems.ISystem import ISystem


class DescriptionSystem(ISystem):
    """Prints the description for an entity"""

    def __init__(self, entity):
        self.target_entity = entity

    def set_target(self, entity):
        self.target_entity = entity

    @staticmethod
    def start(self):
        return True

    def update(self, time):
        print(self.target_entity.get_component(DescriptionNode.__name__).description)  # TODO update this for gui
        return True

    def end(self):
        return
