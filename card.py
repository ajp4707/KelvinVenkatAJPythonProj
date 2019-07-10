import pygame

class Card(pygame.sprite.Sprite):
    def __init__ (self, val, suit, hid, loc):
        super(Card,self).__init__()
        
        self.value= int(val)
        self.suit = suit
        self.hidden= int(hid)
        self.location=loc
        self.name=""
        self.setName()
        self.surf = pygame.surface.Surface((40,40))
        self.image = pygame.transform.scale(pygame.image.load(f'cardimages/{self.name}{self.suit[0]}.png').convert(), (75,113))
        self.back = pygame.transform.scale(pygame.image.load(f'cardimages/blue_back.png').convert(), (75,113))

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
