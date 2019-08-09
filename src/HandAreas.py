'''
Created on Jul 18, 2019

@author: Kel N
'''
from Area import Area
from Card import Card

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700  # TODO move to constants


class VerticalHand(Area):
    """An area with a vertical shape in which cards are placed (and hidden from opponents)"""
    width = 176
    height = 400

    def __init__(self, color, params, location):
        self.handx = 100 if location == 'Left' else 1100

        super().__init__(VerticalHand.width, VerticalHand.height, self.handx - VerticalHand.width / 2,
                         int(SCREEN_HEIGHT / 2 - VerticalHand.height / 2), color, False)

        self.sortParam = params['hand_sort']
        self.descending_order = False if params['sort_order'] == 'Ascending' else True

    def display(self):
        order = sorted(self, key={
                'Suit': Card.get_suit_value,
                'Value': Card.get_value
            }[self.sortParam],
                       reverse=self.descending_order)

        size = len(order)
        if size != 0:
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

        super().__init__(HorizontalHand.width, HorizontalHand.height, int(SCREEN_WIDTH / 2 - HorizontalHand.width / 2),
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
