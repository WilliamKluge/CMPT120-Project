# Holds the MapMarkerNode class
# Author: William Kluge
# Date: 2017-10-16

import pygame


class MapMarkerNode(object):
    """Holds the data for describing an entity"""

    def __init__(self, path, engine):
        marker_sprite = pygame.image.load(path).convert()
        w, h = engine.screen.get_size()
        self.image_size = (int(w * 0.0325), int(h * 0.0325))
        self.background_screen = pygame.transform.scale(marker_sprite, self.image_size)

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

    def get_image_offset(self, negative=True):
        x = int(-self.image_size[0] / 2) if negative else int(self.image_size[0] / 2)
        y = int(-self.image_size[1] / 2) if negative else int(self.image_size[1] / 2)
        tupley_test = (x, y)
        return tupley_test
