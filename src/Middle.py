import pygame
# from Card import *
# from Deck import *
from Area import *

SCREEN_WIDTH, SCREEN_HEIGHT= 1200, 700
MIDDLE_WIDTH, MIDDLE_HEIGHT = 800, 400

class Middle(Area):
    #An area in which all cards are shown
    def __init__(self, color):
        super().__init__(MIDDLE_WIDTH, MIDDLE_HEIGHT, SCREEN_WIDTH/2 - MIDDLE_WIDTH/2, SCREEN_HEIGHT/2 - MIDDLE_HEIGHT/2, color,False)
            
