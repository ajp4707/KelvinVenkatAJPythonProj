import pygame
from Card import *
from Deck import *


class Area(pygame.sprite.Group):

    def __init__(self, width, height, x, y, color, hidden=True):
        super().__init__()
        self.surf = pygame.Surface((width,height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.move_ip((x,y))
        self.x = x 
        self.y = y
        
        #if True, cards in a hand will not be shown
        self.hideCards = hidden
        
    def flip(self):
        for i in self:
            i.hidden = self.hideCards
    
    #checks if any cards are inside hand. if so, Card is added to hand Group.
    def update(self, deck):
        for card in deck.List:
            if card.rect.colliderect(self.rect) and self.rect.collidepoint(card.rect.x, card.rect.y)\
            and self.rect.collidepoint(card.rect.x + card.CARD_WIDTH, card.rect.y + card.CARD_HEIGHT):
                self.add(card)
            else:
                self.remove(card)
