# Holds the QuitSystem class
# Author: William Kluge
# Date: 2017-9-22

import textwrap

import pygame

from Nowhere.EntityFramework.Systems.ISystem import ISystem


class QuitSystem(ISystem):
    """Draws text"""

    # TODO update to use new ISystem update due to command framework implimentation

    @property
    def priority(self):
        return 0  # High priority system

    def __init__(self, engine, text):
        """
        Draws end screen of the game
        :param engine: Engine controlling the game
        :param text: Text to draw on the screen
        """
        super().__init__(engine)
        self.__text = text
        self.background = pygame.Surface(self.engine.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((100, 100, 100))

    def update(self, time):  # TODO make this use DrawTextSystem
        # Remove all systems from the engine queue
        self.engine.system_queue.clear()
        # Add self back to the engine queue
        self.engine.system_queue.append(self)

        # Wrap text
        line_length = 120
        wrapped_text = textwrap.wrap(self.__text, line_length)

        # Get sizes
        w, h = self.engine.screen.get_size()
        text_width, text_height = self.engine.game_font.size("P")  # Get the height of the font

        # Blit self's background
        self.engine.screen.blit(self.background, (0, 0))

        for i in range(len(wrapped_text)):
            location = (w * 0.50 - (len(wrapped_text[i]) * text_width) / 2, h * 0.50 + text_height * i)
            self.engine.screen.blit(self.engine.game_font.render(wrapped_text[i], 1, (0, 0, 0)), location)

        self.engine.screen.blit(self.engine.game_font.render("Press any key to quit", 1, (0, 0, 0)),
                                (w * 0.50 - (21 * text_width) / 2, h * 0.90))

        for x in self.engine.events:
            if x.type == pygame.KEYDOWN:
                # Cycles through all events and checks if any are of type KEYDOWN
                return True

        return False  # Occurs if no events were of type KEYDOWN

    def end(self):
        self.engine.continue_updating = False
