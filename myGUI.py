import sys
import pygame
from pygame.locals import*
import Deck
import Card
from Card import *


#Screen Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

MIDDLE_WIDTH = 400
MIDDLE_HEIGHT = 400

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
middle = pygame.Surface((MIDDLE_WIDTH,MIDDLE_HEIGHT))
middle.fill(GREEN)
middlerect = middle.get_rect()
pygame.display.flip()

#REPLACE with card objects .... pygame.rect.Rect((x,y), (len, height))
cardimage = Card(13,"Cpades",0,"deck").getImage()
cardrect = cardimage.get_rect()
card_dragging = False

#clock controls FPS of game
clock = pygame.time.Clock()

#Game loop - keeps the window open 
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if cardrect.collidepoint(event.pos):
                    card_dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = cardrect.x - mouse_x
                    offset_y = cardrect.y - mouse_y
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                card_dragging = False
                
        elif event.type == pygame.MOUSEMOTION:
            if card_dragging:
                mouse_x, mouse_y = event.pos
                cardrect.x = mouse_x + offset_x
                cardrect.y = mouse_y + offset_y
                
    #if card collides with certain areas, update card status below
    '''
    for i in range(0,len(deck)):
        if card[i].collidepoint(middle.pos):
            card[i].setVisible()
    '''
    screen.fill(BLACK) #background
    screen.blit(middle, (SCREEN_WIDTH/2 - MIDDLE_WIDTH/2, SCREEN_HEIGHT/2 - MIDDLE_HEIGHT/2)) #middle
    screen.blit(cardimage, (cardrect.x, cardrect.y)) #card
    pygame.display.flip() 
    
    clock.tick(30)
