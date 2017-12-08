# Holds the EndScreenSystem class
# Author: William Kluge
# Date: 2017-12-8

import textwrap

import pygame

from Nowhere.EntityFramework.Systems.ISystem import ISystem


class EndScreenSystem(ISystem):
    """Print the ending message and prompts the user if they would like to play again"""

    @property
    def priority(self):
        return 0  # High priority system

    def __init__(self, engine):
        """
        Draws end screen of the game
        :param engine: Engine controlling the game
        """
        super().__init__(engine)
        self.background = pygame.Surface(self.engine.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((100, 100, 100))

    def update(self, time):
        # Remove all systems from the engine queue
        self.engine.system_queue.clear()
        # Add self back to the engine queue
        self.engine.system_queue.append(self)

        # Wrap text
        line_length = 120
        wrapped_text = textwrap.wrap(self.using, line_length)

        # Get sizes
        w, h = self.engine.screen.get_size()
        text_width, text_height = self.engine.game_font.size("P")  # Get the height of the font

        # Blit self's background
        self.engine.screen.blit(self.background, (0, 0))

        for i in range(len(wrapped_text)):
            location = (w * 0.50 - (len(wrapped_text[i]) * text_width) / 2, h * 0.50 + text_height * i)
            self.engine.screen.blit(self.engine.game_font.render(wrapped_text[i], 1, (0, 0, 0)), location)

        self.engine.screen.blit(self.engine.game_font.render("Press Y to play again, any other key to quit",
                                                             1, (0, 0, 0)),
                                (w * 0.50 - (21 * text_width) / 2, h * 0.90))

        for x in self.engine.events:
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_y:
                    # If the pressed key was y, spawn a new main process
                    import Nowhere.main as new
                    new.main()
                # Cycles through all events and checks if any are of type KEYDOWN
                return True

        return False  # Occurs if no events were of type KEYDOWN

    def end(self):
        self.engine.continue_updating = False
