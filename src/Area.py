import pygame


class Area(pygame.sprite.Group):
    """An ABC for Areas"""
    def __init__(self, width, height, x, y, color, hidden=True):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.move_ip((x, y))
        self.x = x
        self.y = y
        self.hide_cards = hidden

    def flip(self):  # TODO doc this and streamline if necessary
        for card in self:
            card.hidden = self.hide_cards

    def display(self):
        pass

    def update(self, deck):
        """Checks if any cards are inside hand, and adds them to hand Group."""
        for card in deck.cards:
            if (card.rect.colliderect(self.rect) and self.rect.collidepoint(card.rect.x, card.rect.y) and
                    self.rect.collidepoint(card.rect.x + card.width, card.rect.y + card.height)):
                self.add(card)
            else:
                self.remove(card)
        self.flip()
        self.display()
