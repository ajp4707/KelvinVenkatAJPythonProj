import Hand
class deckArea(Hand.Hand):

    def __init__(self, width, height, x, y, color, handlist):
        super().__init__(width, height, x, y, color,True)
        self.handList = handlist
    #n is number of cards to deal to each hand
    def deal(self, n):
        handnum = len(self.handList)
        if len(self) < n*handnum:
            print("Not enough cards!")
            return
        cardlist = self.sprites()
        for i in range(0,n*handnum):
            cardlist[i].rect.x = self.handList[i % handnum].x + 5 * i
            cardlist[i].rect.y = self.handList[i % handnum].y + 5 
        
                
                
                
            
        
