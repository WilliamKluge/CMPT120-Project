# Holds the BackgroundNode class
# Author: William Kluge
# Date: 2017-9-18

import pygame


class BackgroundNode(object):
    """Holds the data for describing an entity"""

    def __init__(self, path, engine):
        self.background_sprite = pygame.image.load(path).convert()
        w, h = engine.screen.get_size()
        self.background_screen = pygame.transform.scale(self.background_sprite, (int(w * 0.60), int(h * 0.60)))

    def scale_image(self, engine):
        """
        Scales the image of this class to properly fit in the game screen
        :param engine: Engine that the game is running from
        :return: None
        """
        w, h = engine.screen.get_size()
        self.background_screen = pygame.transform.scale(self.background_sprite, (int(w * 0.60), int(h * 0.60)))
