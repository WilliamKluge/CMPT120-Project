# Holds the UseItemSystem class
# Author: William Kluge
# Date: 2017-12-4
from Nowhere.EntityFramework.Systems.ISystem import ISystem


class UseItemSystem(ISystem):
    """Uses an item"""

    @property
    def priority(self):
        return 100

    def __init__(self, engine):
        """
        Moves the character by the specified amount
        :param engine: Engine controlling the game
        """
        super().__init__(engine)
        self.using = None

    def set_using(self, using):
        self.using = using

    def update(self, time):
        self.using.use_command()
        return True
