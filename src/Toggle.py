# Venkat - citing code from pythonprogramming.net
import sys
import pygame
from pygame.locals import*


class Toggle:
    """A button that loops through various states."""
    def __init__(self, coords: tuple, w_h: tuple, options: [str]):
        self.options = options
        self.current_state = 0
        self.x, self.y = coords
        self.w, self.h = w_h
        self.label = self.options[self.current_state]

    def rotate(self):
        """Rotates around the list one at a time."""  # Returns current state."""
        self.current_state += 1
        self.current_state %= len(self.options)
        self.label = self.options[self.current_state]
        # return self.options[self.current_state]
