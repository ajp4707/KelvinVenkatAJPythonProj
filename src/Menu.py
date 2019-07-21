#Venkat - citing code from pythonprogramming.net
import sys
import pygame
from pygame.locals import*
"""from Deck import *
from Card import *
from VerticalHand import *
from HorizontalHand import horizontalHand
from Middle import *
from DeckArea import *
from discardArea import discardArea"""


class Menu(object):
    def __init__(self):
        # Screen and Hand Constants
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 700
        # initializes pygame module and window
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.largeText = pygame.font.Font('freesansbold.ttf', 80)
        self.smallText = pygame.font.Font('freesansbold.ttf', 20)
        self.TextSurf, self.TextRect = self.text_objects("Welcome to Card Simulator", self.largeText)


    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, (20,255,150))
        return self.textSurface, self.textSurface.get_rect()






    def button(self, x, y, w, h, ic, ac, im, am):
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x+w and y < mouse[1] < y+h:  #checks if mouse is over button, then changes color to active color
            pygame.draw.rect(self.screen, ac, (x,y,w,h))
            msg = am
        else:
            pygame.draw.rect(self.screen, ic, (x,y,w,h)) #draws default button parameters
            msg = im
        self.TextSurf, self.TextRect = self.text_objects(msg, self.smallText)
        self.TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen.blit(self.TextSurf, self.TextRect)



    def runMenu(self):
        running = True
        while running:
            clock = pygame.time.Clock()
            for event in pygame.event.get():  # checks the queue of events
                print(event)
                if event.type == KEYDOWN:  # we can add many more commands here if we want
                    if event.key == K_ESCAPE:
                        running = False
            self.screen.fill((255,255,255))

            self.TextRect.center = ((self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2))
            self.screen.blit(self.TextSurf, self.TextRect)

            #pygame.draw.rect(screen, (0,255,0), (200, 450, 100, 50))
            pygame.draw.rect(self.screen, (255,0,0), (900, 450, 100, 50))
            self.button(200, 450, 100, 50, (0,255,0), (255,0,0), "inactive", "active",)
            pygame.display.flip()


            clock.tick(30)


a = Menu()
a.runMenu()
