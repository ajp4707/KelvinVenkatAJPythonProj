#Venkat - citing code from pythonprogramming.net
import sys
import pygame
from pygame.locals import*


class Toggle:
    def __init__(self, x, y, w, h, mod):
        self.mod = mod
        self.attr = 0
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.state = mod[self.attr%2]
