from Card import *
import random


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

    # Shuffles the deck regardless of size
    def shuffle(self):
        size = len(self.cards)
        for i in range(0, 500):
            idx = random.randint(1, size - 1)
            self.cards.append(self.cards.pop(idx))

    def hide(self):
        for card in self.cards:
            card.hidden = 1

    # NEEDS WORK. Move selected cards.rect to specific hand locations.
    # Perhaps even stagger cards so you can see them all
    # I propose removing this method from this class and adding it to deckArea class.

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
