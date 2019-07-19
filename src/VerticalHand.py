'''
Created on Jul 18, 2019

@author: Kel N
'''
from Area import Area

SCREEN_WIDTH, SCREEN_HEIGHT= 1200, 700
VERT_HAND_WIDTH, VERT_HAND_HEIGHT = 176, 400

class verticalHand(Area):
    #An area in which all cards are shown
    def __init__(self, color, location):
        if location=="Left":
            super().__init__(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), color,False)
        else:
            super().__init__(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 1100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), color,False)