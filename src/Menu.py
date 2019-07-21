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

#colors and list form GUI creator
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
        self.textSurface = font.render(text, True, (0,0,0))
        return self.textSurface, self.textSurface.get_rect()

    def dispText(self,msg,x,y,w,h):
        self.TextSurf, self.TextRect = self.text_objects(msg, self.smallText)
        self.TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen.blit(self.TextSurf, self.TextRect)



    def button(self, x, y, w, h, ic, ac, im, am):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x+w and y < mouse[1] < y+h:  #checks if mouse is over button, then changes color to active color
            pygame.draw.rect(self.screen, ac, (x,y,w,h))
            msg = am
        else:
            pygame.draw.rect(self.screen, ic, (x,y,w,h)) #draws default button parameters
            msg = im
        self.dispText(msg, x, y, w, h)

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


            self.screen.blit(self.TextSurf, self.TextRect)

            #pygame.draw.rect(screen, (0,255,0), (200, 450, 100, 50))
            self.button(200, 450, 100, 50, RED , GREEN , "inactive", "active",)
            pygame.display.flip()


            clock.tick(30)


a = Menu()
a.runMenu()
