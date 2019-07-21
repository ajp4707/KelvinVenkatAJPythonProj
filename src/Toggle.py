#Venkat - citing code from pythonprogramming.net
import sys
import pygame
from pygame.locals import*
"""from Deck import *
from Card import *
from VerticalHand import *
from HorizontalHand import horizontalHand
from Middle import *
from DeckArea import *
from discardArea import discardArea"""

#colors and list form GUI creator
#Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_RED = (232, 23, 23)
LIME = (0,255,0)
BLUE = (0,0, 255)
DARK_PUCE = (72, 61, 63)
ELEC_BLUE = (5, 142, 217)
MOCCASIN = (244, 235, 217)
GRULLO = (163, 154, 146)
DARK_MAGENTA = (139,0,139)
BEIGE=(245,245,220)
LIGHT_GRAY=(119,136,153)
GREEN=(0,128,0)
SILVER=(192,192,192)
DARK_BLUE=(0,0,139)
MIDNIGHT_BLUE=(25,25,112)
VIOLET_RED=(219,112,147)
HONEYDEW=(240,255,240)
TEAL=(0,128,128)
SPRING_GREEN=(0,250,154)

#Color Schemes
colorSchemes=[[DARK_PUCE, ELEC_BLUE,MOCCASIN, GRULLO, DARK_RED],
              [BLACK, MOCCASIN, GRULLO, GREEN, DARK_RED],
              [MIDNIGHT_BLUE,SILVER,LIGHT_GRAY, GREEN, VIOLET_RED ],
              [DARK_BLUE,HONEYDEW,SPRING_GREEN, BEIGE, TEAL]]

class Toggle:
    def __init__(self, x, y, w, h, im, am, mod):
        self.state = 0
        self.attr = 0
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic = DARK_RED
        self.ac = GREEN
        self.im = im
        self.am = am
        self.mod = mod
        #self.smallText = pygame.font.Font('freesansbold.ttf', 20)



    def tester(self):
        self.attr += 14

