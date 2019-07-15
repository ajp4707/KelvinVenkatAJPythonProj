
from Card import*
import random

#I think Deck should be an abstract representation of ALL cards
#I propose a new class called DeckArea that extends Hand class, but is where all cards initially start
#DeckArea would inherit the Group class, which allows iteration over all Sprites (cards) in the group
class Deck():
    def __init__(self, joker, x, y):
        self.List=list()
        self.Suits= ["Clubs", "Diamonds", "Hearts", "Spades"]
        
        self.x = x 
        self.y = y
        #Creates a standard 52 card deck
        for suit in self.Suits:
            for val in range(1,14):
                self.List.append(Card(val, suit, 1, x, y))
        #Jokers have the value 0 and the suit "joker"
        if int(joker):
            self.addJoker(1, x, y)
        self.shuffle()
        
        
    #Shuffles the deck regardless of size
    def shuffle(self):
        size=len(self.List)
        for i in range(0,500):
            idx= random.randint(1,size-1)
            self.List.append(self.List.pop(idx))

    def hide(self):
        for card in self.List:
            card.hidden = 1
    
    #NEEDS WORK. Move selected cards.rect to specific hand locations. Perhaps even stagger cards so you can see them all
    #I propose removing this method from this class and adding it to DeckArea class.
    '''
    def deal (self, num, x, y):
        for i in range(0, num):
            
            card.rect.x = x 
            card.rect.y = y
            temp.append(card)
        return temp
    '''
    def undrag(self):
        for card in self.List:
            card.dragging = False
    
    def addJoker(self, hid, x, y):
        self.List.append(Card(0, "Joker", hid, (x,y)))
