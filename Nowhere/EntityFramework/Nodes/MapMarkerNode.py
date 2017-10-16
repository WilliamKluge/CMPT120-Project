# Holds the MapMarkerNode class
# Author: William Kluge
# Date: 2017-10-16

import pygame


class MapMarkerNode(object):
    """Holds the data for describing an entity"""

    def __init__(self, path, engine):
        marker_sprite = pygame.image.load(path).convert()
        w, h = engine.screen.get_size()
        self.background_screen = pygame.transform.scale(marker_sprite, (int(w * 0.0325), int(h * 0.0325)))

    def scale_image(self, engine):
        """
        Scales the image of this class to properly fit in the game screen
        :param engine: Engine that the game is running from
        :return: None
        """
        # Get sizes
        w, h = engine.screen.get_size()
        # Scale background to new size
        self.background_screen = pygame.transform.scale(self.background_screen, (int(w * 0.0325), int(h * 0.0325)))
