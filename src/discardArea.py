import pygame
# from Card import *
# from Deck import *
from Area import *

HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT = 800, 133
VERT_HAND_WIDTH, VERT_HAND_HEIGHT = 176, 400

class discardArea(Area):
    #Similar to hand properties, but cards in middle are all shown
    def __init__(self, color):
        super().__init__(VERT_HAND_WIDTH,HORIZ_HAND_HEIGHT, 1100 - VERT_HAND_WIDTH/2, 625 - HORIZ_HAND_HEIGHT/2, color,False)
