# Venkat - citing code from pythonprogramming.net
import sys
import pygame
from pygame.locals import*


class Toggle:
    """A button that loops through states"""
    def __init__(self, x, y, w, h, options: [str]):
        self.options = options
        self.current_state = 0
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.selected = self.options[self.current_state]

    def rotate(self):
        """Rotates around the list one at a time. Returns current state."""
        self.current_state += 1
        self.current_state %= len(self.options)
        self.selected = self.options[self.current_state]
        # return self.options[self.current_state]
