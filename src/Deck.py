from Card import *
from random import shuffle


# I think Deck should be an abstract representation of ALL cards
# I propose a new class called deckArea that extends Area class, but is where all cards initially start
# deckArea would inherit the Group class, which allows iteration over all Sprites (cards) in the group


class Deck:
    def __init__(self, joker, x, y):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]  # TODO class var?

        self.x = x
        self.y = y

        # Creates a standard 52 card deck
        self.cards = [Card(val, suit, x, y) for suit in self.suits for val in range(1, 14)]

        # Creates a standard 52 Card deck
        if joker:
            self.add_jokers(x, y)
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)

    def hide(self):
        """Turns all cards in the deck face-down."""
        for card in self.cards:
            card.hidden = True

    # def deal (self, num, x, y):
    #     for i in range(0, num):
    #
    #         Card.rect.x = x
    #         Card.rect.y = y
    #         temp.append(Card)
    #     return temp

    def undrag(self):
        for card in self.cards:
            card.dragging = False

    def add_jokers(self, x, y):
        self.cards.append(Card(14, "Red", x, y))
        self.cards.append(Card(14, "Black", x, y))
