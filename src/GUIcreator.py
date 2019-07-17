import sys
import pygame
from pygame.locals import*
from Deck import *
from Card import *
from Hand import *
from Middle import *
from deckArea import deckArea
#Screen and Hand Constants
SCREEN_WIDTH, SCREEN_HEIGHT= 1200, 700

MIDDLE_WIDTH, MIDDLE_HEIGHT = 800, 400

HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT = 800, 133

VERT_HAND_WIDTH, VERT_HAND_HEIGHT = 176, 400

#Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_RED = (232, 23, 23)
GREEN = (0,255,0)
BLUE = (0,0, 255)
DARK_PUCE = (72, 61, 63)
ELEC_BLUE = (5, 142, 217)
MOCCASIN = (244, 235, 217)
GRULLO = (163, 154, 146)

#Color Schemes
colorSchemes=[[DARK_PUCE, ELEC_BLUE,MOCCASIN, GRULLO, DARK_RED],
              [DARK_PUCE]]

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
        middle = Middle(MIDDLE_WIDTH, MIDDLE_HEIGHT, SCREEN_WIDTH/2 - MIDDLE_WIDTH/2, SCREEN_HEIGHT/2 - MIDDLE_HEIGHT/2, colorSchemes[self.scheme][1] )
        return middle,screen
    
    def createDiscard(self):
        discardarea = Hand(VERT_HAND_WIDTH,HORIZ_HAND_HEIGHT, 1100 - VERT_HAND_WIDTH/2, 625 - HORIZ_HAND_HEIGHT/2, colorSchemes[self.scheme][4])
        return discardarea
        #Creates middle area and hands. 
    def createHands(self, handNum):
        hands = []
        color=colorSchemes[self.scheme][2]
        #1, 2, 3, and 4 are the only accepted arguments for the number of hands
        hands.append(Hand(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 625 - HORIZ_HAND_HEIGHT/2, color))
        if (handNum==2):
            hands.append(Hand(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 75 - HORIZ_HAND_HEIGHT/2, color))
        elif (handNum==3):
            hands.append(Hand(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 1100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), color))
            hands.append(Hand(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), color))        
        elif (handNum==4):
            hands.append(Hand(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 1100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), color))
            hands.append(Hand(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 75 - HORIZ_HAND_HEIGHT/2, color))
            hands.append(Hand(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), color))
        return hands
    #initialize Deck accepting parameters for whether you want jokers and the previously created hands. In the future, determine whose turn it is? 
    def makeDeck(self, joker):
        deck = Deck(joker, 100 - Card.CARD_WIDTH/2, 75 - Card.CARD_HEIGHT/2)
        deckarea = deckArea(VERT_HAND_WIDTH,HORIZ_HAND_HEIGHT, 100 - VERT_HAND_WIDTH/2, 75 - HORIZ_HAND_HEIGHT/2,colorSchemes[self.scheme][3], self.hands)
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
