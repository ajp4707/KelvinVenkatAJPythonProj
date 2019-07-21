import pygame
from pygame.constants import RLEACCEL

class Card(pygame.sprite.Sprite):
    CARD_WIDTH = 75
    CARD_HEIGHT = 114
    BACK = pygame.image.load(f'cardimages/blue_back.png')
    
    
    def __init__ (self, val, suit, x, y):
        super(Card,self).__init__()
        
        self.value= int(val)
        self.suit = suit
        self.hidden= True
        self.setName()
        self.image = pygame.transform.scale(pygame.image.load(f'cardimages/{self.name}{self.suit[0]}.png').convert(), (self.CARD_WIDTH, self.CARD_HEIGHT))
        self.image.set_colorkey((0,255,0), RLEACCEL)
        self.back = pygame.transform.scale(self.BACK.convert(), (self.CARD_WIDTH,self.CARD_HEIGHT))
        self.back.set_colorkey((0,255,0), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        
        self.dragging = False
        
    def getImage(self):
        if self.hidden:
            return self.back
        else:
            return self.image
    def getValue(self):
        return self.value
    def compareSuit(self):
        if self.suit=="Diamonds":
            num1=1
        elif self.suit=="Clubs":
            num1=2
        elif self.suit=="Hearts":
            num1=3
        elif self.suit=="Spades":
            num1=4
        elif self.suit=="Red":
            num1=5
        else:
            num1=6
        return num1

            
    def toggleHide(self):
        self.hidden = not self.hidden
        
    def setName(self):
        if self.value == 14:
            self.name= "Joker"
        elif self.value == 1:
            self.name = "A"
        elif self.value == 11:
            self.name = "J"
        elif self.value == 12:
            self.name = "Q"
        elif self.value == 13:
            self.name = "K"
        else:
            self.name = str(self.value)
