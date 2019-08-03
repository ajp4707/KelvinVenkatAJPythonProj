from Card import*
import random
# I think Deck should be an abstract representation of ALL cards
# I propose a new class called deckArea that extends Area class, but is where all cards initially start
# deckArea would inherit the Group class, which allows iteration over all Sprites (cards) in the group


class Deck():
    def __init__(self, joker, x, y):
        self.List = list()
        self.Suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        
        self.x = x 
        self.y = y
        # Creates a standard 52 Card deck
        for suit in self.Suits:
            for val in range(1,14):
                self.List.append(Card(val, suit, x, y))
        # Jokers have the value 0 and the suit "joker"
        if int(joker):
            self.add_jokers(x, y)
        self.shuffle()

    # Shuffles the deck regardless of size
    def shuffle(self):
        size = len(self.List)
        for i in range(0, 500):
            idx = random.randint(1, size - 1)
            self.List.append(self.List.pop(idx))

    def hide(self):
        for card in self.List:
            card.hidden = 1
    
    # NEEDS WORK. Move selected cards.rect to specific hand locations.
    # Perhaps even stagger cards so you can see them all
    # I propose removing this method from this class and adding it to deckArea class.
    '''
    def deal (self, num, x, y):
        for i in range(0, num):
            
            Card.rect.x = x 
            Card.rect.y = y
            temp.append(Card)
        return temp
    '''
    def undrag(self):
        for card in self.List:
            card.dragging = False
    
    def add_jokers(self, x, y):
        self.List.append(Card(14, "Red", x, y))
        self.List.append(Card(14, "Black", x, y))
