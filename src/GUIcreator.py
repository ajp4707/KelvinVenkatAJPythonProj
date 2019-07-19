import sys
import pygame
from pygame.locals import*
from Deck import *
from Card import *
from VerticalHand import verticalHand
from HorizontalHand import horizontalHand
from Middle import *
from deckArea import deckArea
from discardArea import discardArea
#Screen and Area Constants
SCREEN_WIDTH, SCREEN_HEIGHT= 1200, 700

#Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_RED = (232, 23, 23)
LIME = (0,255,0)
BLUE = (0,0, 255)
DARK_PUCE = (72, 61, 63)
ELEC_BLUE = (5, 142, 217)
MOCCASIN = (244, 235, 217)
GRULLO = (163, 154, 146)
DARK_MAGENTA = (139,0,139)
BEIGE=(245,245,220)
LIGHT_GRAY=(119,136,153)
GREEN=(0,128,0)
SILVER=(192,192,192)
DARK_BLUE=(0,0,139)
MIDNIGHT_BLUE=(25,25,112)
VIOLET_RED=(219,112,147)
HONEYDEW=(240,255,240)
TEAL=(0,128,128)
SPRING_GREEN=(0,250,154)

#Color Schemes
colorSchemes=[[DARK_PUCE, ELEC_BLUE,MOCCASIN, GRULLO, DARK_RED],
              [BLACK, MOCCASIN, GRULLO, GREEN, DARK_RED],
              [MIDNIGHT_BLUE,SILVER,LIGHT_GRAY, GREEN, VIOLET_RED ],
              [DARK_BLUE,HONEYDEW,SPRING_GREEN, BEIGE, TEAL]]

class GUI(object):
    def __init__(self,numHands, scheme, joker):
        self.scheme= scheme-1
        self.clock = pygame.time.Clock()
        self.middle,self.screen= self.createScreen()
        self.hands= self.createHands(numHands)
        self.deck,self.deckarea= self.makeDeck(joker)
        self.discardarea= self.createDiscard()    
        #mouse variables
        self.mouse_x, self.mouse_y = 0,0
    #initializes pygame module and window
    def createScreen(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        middle = Middle( colorSchemes[self.scheme][1] )
        return middle,screen
    
    def createDiscard(self):
        discardarea = discardArea(colorSchemes[self.scheme][4])
        return discardarea
        #Creates middle area and hands. 
    def createHands(self, handNum):
        hands = []
        color=colorSchemes[self.scheme][2]
        #1, 2, 3, and 4 are the only accepted arguments for the number of hands
        hands.append(horizontalHand( color))
        if (handNum==2):
            hands.append(horizontalHand(color,"Top"))
        elif (handNum==3):
            hands.append(verticalHand(color,"Right"))
            hands.append(verticalHand(color, "Left"))        
        elif (handNum==4):
            hands.append(verticalHand(color, "Right"))
            hands.append(horizontalHand(color, "Top"))
            hands.append(verticalHand(color, "Left"))
        return hands
    #initialize Deck accepting parameters for whether you want jokers and the previously created hands. In the future, determine whose turn it is? 
    def makeDeck(self, joker):
        deck = Deck(joker, 100 - Card.CARD_WIDTH/2, 75 - Card.CARD_HEIGHT/2)
        deckarea = deckArea(colorSchemes[self.scheme][3], self.hands)
        deckarea.update(deck)
        return deck,deckarea
    
    def blitScreen(self):
            self.screen.fill(colorSchemes[self.scheme][0])
            self.screen.blit(self.middle.surf, (self.middle.x, self.middle.y))
            self.screen.blit(self.deckarea.surf, (self.deckarea.x, self.deckarea.y))
            self.screen.blit(self.discardarea.surf, (self.discardarea.x, self.discardarea.y))
            for hand in self.hands:
                self.screen.blit(hand.surf, (hand.x, hand.y))
            for card in self.deck.List:
                self.screen.blit(card.getImage(), (card.rect.x, card.rect.y))
                
    def updateHands(self):
        self.deck.hide()
        self.deckarea.update(self.deck) 
        for hand in self.hands:
            hand.update(self.deck)
            hand.flip()
        self.middle.update(self.deck)
        self.middle.flip()
        self.discardarea.update(self.deck)
    #Game loop - keeps the window open 
    def runSim(self):
        running = True
        while running:
            for event in pygame.event.get(): #checks the queue of events
                if event.type == KEYDOWN:    #we can add many more commands here if we want
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_SPACE:
                        self.deckarea.deal(7)
                        print("check space")
                elif event.type == QUIT:
                    running = False
                
                #MOUSEBUTTONDOWN 3 is a right click, drags all of the cards. button 1 is a left click, drags one Card
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:                   
                        for card in self.deck.List:
                            if card.rect.collidepoint(event.pos):
                                card.dragging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = card.rect.x - mouse_x
                                offset_y = card.rect.y - mouse_y
                    elif event.button == 1:
                        for i in range(len(self.deck.List)-1, -1, -1 ):
                            if self.deck.List[i].rect.collidepoint(event.pos):
                                self.deck.List[i].dragging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = self.deck.List[i].rect.x - mouse_x
                                offset_y = self.deck.List[i].rect.y - mouse_y
                                self.deck.List.append(self.deck.List.pop(i)) #Put grabbed cards at the end of the Deck, they will blit on top
                                break
                #For efficiency, Hands only check if cards have been added to them after MOUSEBUTTONUP 
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        self.deck.undrag()
                    elif event.button == 1:
                        self.deck.undrag()
                    self.updateHands()
                    #if event.button == 2:
                        
                        
                elif event.type == pygame.MOUSEMOTION:
                    for card in self.deck.List:
                        if card.dragging:
                            mouse_x, mouse_y = event.pos
                            card.rect.x = mouse_x + offset_x
                            card.rect.y = mouse_y + offset_y
                        
            
            self.blitScreen()
            pygame.display.flip() 
            
            self.clock.tick(30)
