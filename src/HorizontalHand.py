'''
Created on Jul 18, 2019

@author: Kel N
'''
from Area import Area

SCREEN_WIDTH, SCREEN_HEIGHT= 1200, 700
HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT = 800, 133

class horizontalHand(Area):
    #An area in which all cards are shown
    def __init__(self, color,location="Bottom"):
        if location=="Top":
            super().__init__(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 75 - HORIZ_HAND_HEIGHT/2, color,False)
        else:
            super().__init__(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 625 - HORIZ_HAND_HEIGHT/2, color,False)
