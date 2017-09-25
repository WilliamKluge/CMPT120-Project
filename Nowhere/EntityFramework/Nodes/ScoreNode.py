# Holds the ScoreNode class
# Author: William Kluge
# Date: 2017-9-22


class ScoreNode(object):
    """Holds the data for an entity's score"""

    def __init__(self):
        self.score = 0

    def change_score(self, value):
        """
        Change the score held in this node
        :param value: Amount to change the score by
        :return: None
        """
        self.score += value
