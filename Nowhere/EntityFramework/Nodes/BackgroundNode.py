# Holds the BackgroundNode class
# Author: William Kluge
# Date: 2017-9-18

import pygame


class BackgroundNode(object):
    """Holds the picture for a background of a scene"""

    def __init__(self, path, engine):
        background_sprite = pygame.image.load(path).convert()
        w, h = engine.screen.get_size()
        self.background_screen = pygame.transform.scale(background_sprite, (int(w * 0.65), int(h * 0.65)))

    def scale_image(self, engine):
        """
        Scales the image of this class to properly fit in the game screen
        :param engine: Engine that the game is running from
        :return: None
        """
        # Get sizes
        w, h = engine.screen.get_size()
        # Scale background to new size
        self.background_screen = pygame.transform.scale(self.background_screen, (int(w * 0.65), int(h * 0.65)))
