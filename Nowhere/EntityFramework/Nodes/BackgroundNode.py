# Holds the BackgroundNode class
# Author: William Kluge
# Date: 2017-9-18

import pygame


class BackgroundNode(object):
    """Holds the data for describing an entity"""

    __background_sprite = None  # Keep this after game is loaded for now
    background_screen = None

    def __init__(self, path):
        self.background_sprite = pygame.image.load(path).convert()

    def scale_image(self, engine):
        w, h = engine.screen.get_size()
        self.background_screen = pygame.transform.scale(self.background_sprite, (int(w * 0.60), int(h * 0.60)))
