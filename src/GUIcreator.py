import sys
import pygame
from pygame.locals import*
from Area import *
from VerticalHand import verticalHand
from HorizontalHand import horizontalHand
from Middle import *
from DeckArea import deckArea
from discardArea import discardArea
from pygame.constants import K_s
#Screen and Area Constants
SCREEN_WIDTH, SCREEN_HEIGHT= 1200, 700

#Color Constants
colors={"WHITE":(255,255,255),"BLACK":(0,0,0),"RED":(255,0,0),"DARK_RED":(232,23,23),"LIME":(0,255,0),"BLUE":(0,0,255),
"DARK_PUCE":(72,61,63),"ELEC_BLUE":(5,142,217),"MOCCASIN":(244,235,217),"GRULLO":(163,154,146),"DARK_MAGENTA":(139,0,139),
"BEIGE":(245,245,220),"LIGHT_GRAY":(119,136,153),"GREEN":(0,128,0),"SILVER":(192,192,192),"DARK_BLUE":(0,0,139),
"MIDNIGHT_BLUE":(25,25,112),"VIOLET_RED":(219,112,147),"HONEYDEW":(240,255,240),"TEAL":(0,128,128),"SPRING_GREEN":(0,250,154)}

#Color Schemes
colorSchemes=[(colors["DARK_PUCE"],colors["ELEC_BLUE"],colors["MOCCASIN"],colors["GRULLO"],colors["DARK_RED"]),
              (colors["BLACK"],colors["MOCCASIN"],colors["GRULLO"],colors["GREEN"],colors["DARK_RED"]),
              (colors["MIDNIGHT_BLUE"],colors["SILVER"],colors["LIGHT_GRAY"],colors["GREEN"],colors["VIOLET_RED"]),
              (colors["DARK_BLUE"],colors["HONEYDEW"],colors["SPRING_GREEN"],colors["BEIGE"],colors["TEAL"])]

class GUI(object):
    def __init__(self,numHands, scheme, joker, params):
        self.scheme= scheme-1
        self.clock = pygame.time.Clock()
        self.middle,self.screen= self.createScreen()
        self.hands= self.createHands(numHands, params)
        self.deck,self.deckarea= self.makeDeck(joker)
        self.discardarea= self.createDiscard()    
        #mouse variables
        self.mouse_x, self.mouse_y = 0,0
    #initializes pygame module and window
    def createScreen(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Python Card Simulator v4    "Spacebar": Deal Cards     Keys "1-4": Player 1-4\'s Turn    Key "s": Reshuffle')
        middle = Middle( colorSchemes[self.scheme][1] )
        return middle,screen
    
    def createDiscard(self):
        discardarea = discardArea(colorSchemes[self.scheme][4])
        return discardarea
        #Creates middle area and hands. 
    def createHands(self, handNum, params):
        hands = []
        color=colorSchemes[self.scheme][2]
        #1, 2, 3, and 4 are the only accepted arguments for the number of hands
        hands.append(horizontalHand( color,params))
        if (handNum==2):
            hands.append(horizontalHand(color, params,"Top"))
        elif (handNum==3):
            hands.append(verticalHand(color,params,"Right"))
            hands.append(verticalHand(color, params,"Left"))        
        elif (handNum==4):
            hands.append(verticalHand(color, params,"Right"))
            hands.append(horizontalHand(color, params,"Top"))
            hands.append(verticalHand(color, params,"Left"))
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
                
    def updateAreas(self):
        self.deck.hide()
        self.deckarea.update(self.deck) 
        for hand in self.hands:
            hand.update(self.deck)
        self.middle.update(self.deck)
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
                        self.updateAreas()
                    elif event.key == K_1:
                        for hand in self.hands:
                            hand.hideCards = True
                        self.hands[0].hideCards = False
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == K_2:
                        for hand in self.hands:
                            hand.hideCards = True
                        self.hands[1%len(self.hands)].hideCards = False
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == K_3:
                        for hand in self.hands:
                            hand.hideCards = True
                        self.hands[2%len(self.hands)].hideCards = False
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == K_4:
                        for hand in self.hands:
                            hand.hideCards = True
                        self.hands[3%len(self.hands)].hideCards = False
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == K_s:
                        for card in self.deck.List:
                            card.rect.x, card.rect.y=100 - Card.CARD_WIDTH/2, 75 - Card.CARD_HEIGHT/2
                        self.deck.shuffle()
                        self.updateAreas()
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
                    self.updateAreas()
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
