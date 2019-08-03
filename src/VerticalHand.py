'''
Created on Jul 18, 2019

@author: Kel N
'''
from Area import *

SCREEN_WIDTH, SCREEN_HEIGHT= 1200, 700
VERT_HAND_WIDTH, VERT_HAND_HEIGHT = 176, 400


class VerticalHand(Area):
    # An area in which all cards are shown
    def __init__(self, color, param,location):
        if location == "Left":
            self.handx = 100
        else:
            self.handx = 1100
        super().__init__(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, self.handx - VERT_HAND_WIDTH/2, 
                         int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), color, False)
        if param[0] == 0:
            self.sortParam = "Value"
        else:
            self.sortParam = "Suit"
        self.sortOrder = param[1]

    # https://docs.python.org/3/howto/sorting.html- Refreshed on how to sort with lambda functions
    def display(self):
        if self.sortParam == "Suit":
            temp = sorted(self, key=Card.get_value, reverse=self.sortOrder)
            new_order = sorted(temp, key=Card.compare_suit)
        else:
            temp = sorted(self, key=Card.compare_suit)
            new_order = sorted(temp, key=Card.get_value, reverse=self.sortOrder)
        size = len(new_order)
        if size != 0:
            step = 250/size
        count = 0
        for card in new_order:
            card.rect.x, card.rect.y = self.handx - Card.CARD_WIDTH/2,225 - Card.CARD_HEIGHT/2 + step * count
            count += 1
