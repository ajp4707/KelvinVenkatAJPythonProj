import sys
import pygame
from pygame.locals import*
from Deck import *
from Card import *
from Hand import *
from Middle import *
from DeckArea import *

#Screen and Hand Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

MIDDLE_WIDTH = 800
MIDDLE_HEIGHT = 400

HORIZ_HAND_WIDTH = 800
HORIZ_HAND_HEIGHT = 133

VERT_HAND_WIDTH = 176
VERT_HAND_HEIGHT = 400

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


#initializes pygame module and window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Creates middle area and hands. 
middle = Middle(MIDDLE_WIDTH, MIDDLE_HEIGHT, SCREEN_WIDTH/2 - MIDDLE_WIDTH/2, SCREEN_HEIGHT/2 - MIDDLE_HEIGHT/2, ELEC_BLUE )
hands = []
hands.append(Hand(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 625 - HORIZ_HAND_HEIGHT/2, MOCCASIN))
hands.append(Hand(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 1100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), MOCCASIN))
hands.append(Hand(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 75 - HORIZ_HAND_HEIGHT/2, MOCCASIN))
hands.append(Hand(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), MOCCASIN))

#initialize deck. In the future, determine whose turn it is?

deck = Deck(0, 100 - Card.CARD_WIDTH/2, 75 - Card.CARD_HEIGHT/2)
deckarea = DeckArea(VERT_HAND_WIDTH,HORIZ_HAND_HEIGHT, 100 - VERT_HAND_WIDTH/2, 75 - HORIZ_HAND_HEIGHT/2, GRULLO, hands)
deckarea.update(deck)

#clock controls FPS of game
clock = pygame.time.Clock()
#mouse vars are important for card motion
mouse_x = 0
mouse_y = 0

#Game loop - keeps the window open 
running = True
while running:
    for event in pygame.event.get(): #checks the queue of events
        if event.type == KEYDOWN:    #we can add many more commands here if we want
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                deckarea.deal(7)
                print("check space")
        elif event.type == QUIT:
            running = False
        
        #MOUSEBUTTONDOWN 3 is a right click, drags all of the cards. button 1 is a left click, drags one card
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:                   
                for card in deck.List:
                    if card.rect.collidepoint(event.pos):
                        card.dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = card.rect.x - mouse_x
                        offset_y = card.rect.y - mouse_y
            elif event.button == 1:
                for i in range(len(deck.List)-1, -1, -1 ):
                    if deck.List[i].rect.collidepoint(event.pos):
                        deck.List[i].dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = deck.List[i].rect.x - mouse_x
                        offset_y = deck.List[i].rect.y - mouse_y
                        deck.List.append(deck.List.pop(i)) #Put grabbed cards at the end of the deck, they will blit on top
                        break
        #For efficiency, Hands only check if cards have been added to them after MOUSEBUTTONUP 
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                deck.undrag()
            elif event.button == 1:
                deck.undrag()
            
            deck.hide()
            deckarea.update(deck)
            for hand in hands:
                hand.update(deck)
                hand.flip()
            middle.update(deck)
            middle.flip()
            #if event.button == 2:
                
                
        elif event.type == pygame.MOUSEMOTION:
            for card in deck.List:
                if card.dragging:
                    mouse_x, mouse_y = event.pos
                    card.rect.x = mouse_x + offset_x
                    card.rect.y = mouse_y + offset_y
                
    
    screen.fill(DARK_PUCE)
    screen.blit(middle.surf, (middle.x, middle.y))
    screen.blit(deckarea.surf, (deckarea.x, deckarea.y))
    for hand in hands:
        screen.blit(hand.surf, (hand.x, hand.y))
    for card in deck.List:
        screen.blit(card.getImage(), (card.rect.x, card.rect.y))
    pygame.display.flip() 
    
    clock.tick(30)
