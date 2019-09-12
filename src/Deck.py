from Card import *
from random import shuffle


class Deck:
    """Represents the Deck of Cards. A standard deck of 52 playing cards, but can be
    customized to a custom deck. Handles shuffling."""
    def __init__(self, joker, x, y):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.x, self.y = x, y

        # Creates a standard 52 card deck
        self.cards = [Card(val, suit, x, y) for suit in self.suits for val in range(1, 14)]

        # Add the jokers if necessary
        if joker:
            self.add_jokers(x, y)
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)

    def hide(self):
        """Turns all cards in the deck face-down."""
        for card in self.cards:
            card.hidden = True

    def undrag(self):
        for card in self.cards:
            card.draggable = False

    def add_jokers(self, x, y):
        self.cards.append(Card(14, "Red", x, y))
        self.cards.append(Card(14, "Black", x, y))
