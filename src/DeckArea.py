from Area import *
from Card import Card

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
