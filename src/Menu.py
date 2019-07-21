#Venkat - citing code from pythonprogramming.net
import sys
import pygame
from pygame.locals import*
from Deck import *
from Card import *
from VerticalHand import *
from HorizontalHand import horizontalHand
from Middle import *
from DeckArea import *
from discardArea import discardArea


class Menu:
    # Screen and Hand Constants
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 700 

    def text_objects(text, font):
        textSurface = font.render(text, True, (20,255,150))
        return textSurface, textSurface.get_rect()

    # initializes pygame module and window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects("Welcome to Card Simulator", largeText)


    def button(self, x, y, w, h, ic, ac, func):
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x+w and y < mouse[1] < y+h:  #checks if mouse is over button, then changes color to active color
            pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        else:
            pygame.draw.rect(gameDisplay, ic, (w,y,w,h)) #draws default button parameters




    running = True
    while running:
        clock = pygame.time.Clock()
        for event in pygame.event.get():  # checks the queue of events
            print(event)
            if event.type == KEYDOWN:  # we can add many more commands here if we want
                if event.key == K_ESCAPE:
                    running = False
        screen.fill((255,255,255))

        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen, (0,255,0), (200, 450, 100, 50))
        pygame.draw.rect(screen, (255,0,0), (900, 450, 100, 50))

        pygame.display.flip()

        clock.tick(30)


