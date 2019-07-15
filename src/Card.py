
import pygame
from pygame.constants import RLEACCEL

class Card(pygame.sprite.Sprite):
    CARD_WIDTH = 75
    CARD_HEIGHT = 114
    BACK = pygame.image.load(f'cardimages/blue_back.png')
    
    
    def __init__ (self, val, suit, hid, x, y):
        super(Card,self).__init__()
        
        self.value= int(val)
        self.suit = suit
        self.hidden= int(hid)
        
        self.name=""
        self.setName()
        self.image = pygame.transform.scale(pygame.image.load(f'cardimages/{self.name}{self.suit[0]}.png').convert(), (self.CARD_WIDTH, self.CARD_HEIGHT))
        self.image.set_colorkey((0,255,0))
        self.back = pygame.transform.scale(self.BACK.convert(), (self.CARD_WIDTH,self.CARD_HEIGHT))
        self.back.set_colorkey((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        
        self.dragging = False
        
    def getImage(self):
        if self.hidden:
            return self.back
        else:
            return self.image
        
    
    
    def toggleHide(self):
        self.hidden = not self.hidden
        
    def setName(self):
        if self.value == 1:
            self.name = "A"
        elif self.value == 11:
            self.name = "J"
        elif self.value == 12:
            self.name = "Q"
        elif self.value == 13:
            self.name = "K"
        else:
            self.name = str(self.value)
            
    
    
