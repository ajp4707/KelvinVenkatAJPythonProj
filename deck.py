import Card.py
import random
class Deck():
    def __init__(self, joker):
        self.List=list()
        self.Suits= ["clubs", "diamonds", "hearts", "spades"]
        #Creates a standard 52 card deck
        for suit in Suits:
            for val in range(1,14):
                self.List.append(Card(val, suit, 0, "deck"))
        #Jokers have the value 0 and the suit "joker"
        if int(joker):
            self.List.append(Card(0, "joker", 0, "deck"))
        self.shuffle()
    #Shuffles the deck regardless of size
    def shuffle(self):
        size=len(self.List)
        for i in range(0,500):
            idx= random.randint(1,size-1)
            self.List.append(self.List.pop(idx))
    #Returns how ever many top cards and changes their location
    def deal (self, num, loc):
        temp=list()
        for i in range(0,num):
            card=self.List.pop()
            card.location=loc
            temp.append(card)
        return temp
