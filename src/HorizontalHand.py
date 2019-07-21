'''
Created on Jul 18, 2019

@author: Kel N
'''
from Area import *

SCREEN_WIDTH, SCREEN_HEIGHT= 1200, 700
HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT = 800, 133

class horizontalHand(Area):
    #An area in which all cards are shown
    def __init__(self, color, param, location="Bottom"):
        if location=="Top":
            self.handy=75
        else:
            self.handy=625
        super().__init__(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2),
                          self.handy - HORIZ_HAND_HEIGHT/2, color,False)
        self.sortParam=param
    
#https://docs.python.org/3/howto/sorting.html- Refreshed on how to sort with key functions
    def display(self):
        if self.sortParam[0] == "Suit":
            temp=sorted(self,key=Card.getValue, reverse=self.sortParam[1])
            newOrder=sorted(temp,key=Card.compareSuit)
        else:
            temp=sorted(self,key=Card.compareSuit)
            newOrder=sorted(temp,key=Card.getValue, reverse=self.sortParam[1])
        size=len(newOrder)
        if size !=0:
            step=660/size
        count=0
        for card in newOrder:   
            card.rect.x, card.rect.y= int(275 - Card.CARD_WIDTH/2 +step*count), self.handy - Card.CARD_HEIGHT/2
            count+=1
