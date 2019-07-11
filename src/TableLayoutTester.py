import sys
import pygame
from pygame.locals import*
from Deck import *
from Card import *
from Hand import *
from Middle import *

#Screen Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

MIDDLE_WIDTH = 800
MIDDLE_HEIGHT = 400

HORIZ_HAND_WIDTH = 600
HORIZ_HAND_HEIGHT = 132

VERT_HAND_WIDTH = 176
VERT_HAND_HEIGHT = 400

#Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0, 255)



#initializes pygame module and window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Creates middle area
middle = Middle(MIDDLE_WIDTH, MIDDLE_HEIGHT, SCREEN_WIDTH/2 - MIDDLE_WIDTH/2, SCREEN_HEIGHT/2 - MIDDLE_HEIGHT/2, GREEN )
hand1 = Hand(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 625 - HORIZ_HAND_HEIGHT/2, BLUE)
hand2 = Hand(HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT, int(SCREEN_WIDTH/2 - HORIZ_HAND_WIDTH/2), 75 - HORIZ_HAND_HEIGHT/2, BLUE)
hand3 = Hand(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), BLUE)
hand4 = Hand(VERT_HAND_WIDTH, VERT_HAND_HEIGHT, 1100 - VERT_HAND_WIDTH/2, int(SCREEN_HEIGHT/2 - VERT_HAND_HEIGHT/2), BLUE)


pygame.display.flip()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            
            
            
    screen.fill(BLACK) #background
    screen.blit(middle.surf, (middle.x, middle.y)) #middle
    screen.blit(hand1.surf, (hand1.x, hand1.y))
    screen.blit(hand2.surf, (hand2.x, hand2.y))
    screen.blit(hand3.surf, (hand3.x, hand3.y))
    screen.blit(hand4.surf, (hand4.x, hand4.y))
    pygame.display.flip() 
    
    clock.tick(30)