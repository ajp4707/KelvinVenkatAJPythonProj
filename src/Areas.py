import pygame
from constants import Dimensions
from Card import Card


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


HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT = 800, 133
VERT_HAND_WIDTH, VERT_HAND_HEIGHT = 176, 400


class DeckArea(Area):

    def __init__(self, color, handlist):
        super().__init__(VERT_HAND_WIDTH, HORIZ_HAND_HEIGHT,
                         100 - VERT_HAND_WIDTH / 2,
                         75 - HORIZ_HAND_HEIGHT / 2,
                         color,
                         True
                         )
        self.handList = handlist

    # n is number of cards to deal to each hand
    def deal(self, n):
        handnum = len(self.handList)
        if len(self) < n * handnum:
            print("Not enough cards!")
            return
        cardlist = self.sprites()
        for i in range(0, n * handnum):
            cardlist[i].rect.x = self.handList[i % handnum].x + 5 * i
            cardlist[i].rect.y = self.handList[i % handnum].y + 5

    def display(self):
        for card in self:
            card.rect.x, card.rect.y = 100 - Card.width / 2, 75 - Card.height / 2


MIDDLE_WIDTH, MIDDLE_HEIGHT = 800, 400


class Middle(Area):
    """Represents the main playing field where all cards are visible."""

    def __init__(self, color):
        super().__init__(MIDDLE_WIDTH,
                         MIDDLE_HEIGHT,
                         Dimensions.screen_width / 2 - MIDDLE_WIDTH / 2,
                         Dimensions.screen_height / 2 - MIDDLE_HEIGHT / 2,
                         color,
                         False
                         )


class VerticalHand(Area):
    """An area with a vertical shape in which cards are placed (and hidden from opponents)"""
    width = 176
    height = 400

    def __init__(self, color, params, location):
        self.handx = 100 if location == 'Left' else 1100

        super().__init__(VerticalHand.width, VerticalHand.height, self.handx - VerticalHand.width / 2,
                         int(Dimensions.screen_height / 2 - VerticalHand.height / 2), color, False)

        self.sortParam = params['hand_sort']
        self.descending_order = False if params['sort_order'] == 'Ascending' else True

    def display(self):
        order = sorted(self, key={
                'Suit': Card.get_suit_value,
                'Value': Card.get_value
            }[self.sortParam],
                       reverse=self.descending_order)

        size = len(order)
        step = 250 / size
        count = 0
        for card in order:
            card.rect.x = self.handx - Card.width / 2
            card.rect.y = 225 - Card.height / 2 + step * count
            count += 1


class HorizontalHand(Area):
    """An area with a horizontal shape in which cards are placed (and hidden from opponents)"""
    width = 800
    height = 133

    def __init__(self, color, params, location):  # TODO Doesn't need all the params, only hand_sort and sort_order. Group them?
        self.handy = 75 if location == 'Top' else 625

        super().__init__(HorizontalHand.width, HorizontalHand.height, int(Dimensions.screen_width
                                                                          / 2 - HorizontalHand.width / 2),
                         self.handy - HorizontalHand.height / 2, color, False)

        self.sortParam = params['hand_sort']
        self.descending_order = False if params['sort_order'] == 'Ascending' else True

    def display(self):
        # TODO I don't understand how this sorts the cards but ok
        order = sorted(self, key={
                'Suit': Card.get_suit_value,
                'Value': Card.get_value
            }[self.sortParam],
                       reverse=self.descending_order)

        size = len(order)
        if size:
            step = 660 / size
        count = 0
        for card in order:
            card.rect.x = int(275 - Card.width / 2 + step * count)
            card.rect.y = self.handy - Card.height / 2
            count += 1


class DiscardArea(Area):
    # Similar to hand properties, but cards in middle are all shown
    def __init__(self, color):
        super().__init__(VERT_HAND_WIDTH, HORIZ_HAND_HEIGHT,
                         1100 - VERT_HAND_WIDTH / 2,
                         625 - HORIZ_HAND_HEIGHT / 2,
                         color,
                         True
                         )

    def display(self):
        for card in self:
            card.rect.x, card.rect.y = 1100 - Card.width / 2, 625 - Card.height / 2
