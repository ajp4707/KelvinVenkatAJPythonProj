import pygame

class Card(pygame.sprite.Sprite):
    def __init__ (self, val, suit, hid, loc):
        super(Card,self).__init__()
        self.value= int(val)
        self.suit = suit
        self.hidden= int(hid)
        self.location=loc
        self.surf = pygame.surface.Surface((40,40))
        self.image = pygame.image.load(f'{val}of{suit}.png').convert()
