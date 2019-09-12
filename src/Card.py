import pygame
from pygame.constants import RLEACCEL as RLE


class Card(pygame.sprite.Sprite):
    """A representation of a card."""
    width, height = 75, 114
    back_img = pygame.image.load(f'../cardimages/blue_back.png')
    
    def __init__(self, val, suit, x, y):
        super(Card, self).__init__()
        
        self.value = val
        self.name = Card.set_name(self.value)
        self.suit = suit
        self.hidden = True
        # Initialize images
        self.front_img = pygame.transform.scale(
            pygame.image.load(f'../cardimages/{self.name}{self.suit[0]}.png').convert(),
            (self.width, self.height)
        )
        self.front_img.set_colorkey((0, 255, 0), RLE)
        self.back_img = pygame.transform.scale(self.back_img.convert(), (self.width, self.height))
        self.back_img.set_colorkey((0, 255, 0), RLE)
        self.rect = self.front_img.get_rect()
        self.rect.x, self.rect.y = x, y
        self.draggable = False
        
    def get_image(self):
        return self.back_img if self.hidden else self.front_img

    def get_value(self):  # TODO replace with @property
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
