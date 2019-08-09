import pygame
from pygame.constants import RLEACCEL as RLE


class Card(pygame.sprite.Sprite):
    width = 75
    height = 114
    back_img = pygame.image.load(f'cardimages/blue_back.png')
    
    def __init__(self, val, suit, x, y):
        super(Card, self).__init__()
        
        self.value = val
        self.name = Card.set_name(self.value)
        self.suit = suit
        self.hidden = True
        # Initialize images
        self.image = pygame.transform.scale(
            pygame.image.load(f'cardimages/{self.name}{self.suit[0]}.png').convert(),
            (self.width, self.height)
        )
        self.image.set_colorkey((0, 255, 0), RLE)
        self.back = pygame.transform.scale(self.back_img.convert(), (self.width, self.height))
        self.back.set_colorkey((0, 255, 0), RLE)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.dragging = False
        
    def get_image(self):
        if self.hidden:
            return self.back
        else:
            return self.image

    def get_value(self):
        """Used as a key for sorting the Hands by value."""
        return self.value

    def get_suit_value(self):
        """Used as a key for sorting the Hands by suit."""

        suits = {
            'Spades': 4,
            'Hearts': 3,
            'Diamonds': 2,
            'Clubs': 1
        }
        return suits[self.suit]

    # Currently unused
    # def toggle_hide(self):
    #     self.hidden = not self.hidden

    @classmethod
    def set_name(cls, value):
        """Handles naming of face cards and number cards."""
        face_cards = {
            14: 'Joker',
            13: 'K',
            12: 'Q',
            11: 'J',
            1: 'A'
        }
        try:
            return face_cards[value]
        except KeyError:
            return str(value)
