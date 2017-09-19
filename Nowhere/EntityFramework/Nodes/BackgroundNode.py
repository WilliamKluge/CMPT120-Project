# Holds the BackgroundNode class
# Author: William Kluge
# Date: 2017-9-18

import pygame


class BackgroundNode(object):
    """Holds the data for describing an entity"""

    background_sprite = None

    def __init__(self, path):
        self.background_sprite = pygame.image.load(path)
