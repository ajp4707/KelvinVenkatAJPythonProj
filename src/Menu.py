#Venkat - citing code from pythonprogramming.net
import sys
import pygame
from pygame.locals import*
from Toggle import *
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

    toggle1 = Toggle(800, 200, 100, 50, "No", "Yes", 2)
    toggle2 = Toggle(800, 400, 100, 50, "No", "Yes", 4)
    toggle3 = Toggle(800, 600, 100, 50, "No", "Yes", 4)
    listA= [toggle1, toggle2, toggle3]

    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, (0, 0, 0))
        return self.textSurface, self.textSurface.get_rect()

    def dispText(self, msg, x, y, w, h):
        self.TextSurf, self.TextRect = self.text_objects(msg, self.smallText)
        self.TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen.blit(self.TextSurf, self.TextRect)

    def drawButton(self, toggle):
        mouse = pygame.mouse.get_pos()
        if toggle.x < mouse[0] < toggle.x + toggle.w and toggle.y < mouse[1] < toggle.y + toggle.h or toggle.attr % toggle.mod == 1:  # checks if mouse is over button, then changes color to active color
            pygame.draw.rect(self.screen, toggle.ac, (toggle.x, toggle.y, toggle.w, toggle.h))
            msg = toggle.am

        else:
            pygame.draw.rect(self.screen, toggle.ic, (toggle.x, toggle.y, toggle.w, toggle.h))  # draws default button parameters
            msg = toggle.im


        self.dispText(msg, toggle.x, toggle.y, toggle.w, toggle.h)

    def runMenu(self, list):
        running = True
        clock = pygame.time.Clock()
        while running:
            #print("in loop")
            self.screen.fill(BEIGE)
            for event in pygame.event.get():  # checks the queue of events
                print(event)
                if event.type == KEYDOWN:  # we can add many more commands here if we want
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for i in range(len(list)):
                            if list[0].x < event.pos[0] < list[0].x + list[0].w and list[0].y < event.pos[1] < list[0].y + list[0].h:
                                self.toggle1.attr += 1
            #print("end loop")
            for i in range(len(list)):
                self.drawButton(list[i])
            self.drawButton(self.toggle1)
            print(self.toggle1.attr)
            #self.dispText("Do you want jokers", 200, 125, 200, 200)
            pygame.display.flip()

            clock.tick(30)



c = Menu()
c.runMenu(c.listA)


"""class Menu(object):
    def __init__(self):
        # Screen and Hand Constants
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 700
        self.bool = False

        # initializes pygame module and window
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.largeText = pygame.font.Font('freesansbold.ttf', 80)
        self.smallText = pygame.font.Font('freesansbold.ttf', 20)
        #self.TextSurf, self.TextRect = self.text_objects("Welcome to Card Simulator", self.largeText)

    #this is a little messy right now, I'll have to clean up how text works
    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, (0,0,0))
        return self.textSurface, self.textSurface.get_rect()

    def dispText(self,msg,x,y,w,h):
        self.TextSurf, self.TextRect = self.text_objects(msg, self.smallText)
        self.TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen.blit(self.TextSurf, self.TextRect)

    def tester(self):
        self.dispText("qwertuip", 200, 400, 200, 200)
        self.bool = True

    #easily creates buttons
    def button(self, x, y, w, h, ic, ac, im, am, func):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x+w and y < mouse[1] < y+h:  #checks if mouse is over button, then changes color to active color
            pygame.draw.rect(self.screen, ac, (x,y,w,h))
            msg = am
            if click[0] == 1:
                func()

        else:
            pygame.draw.rect(self.screen, ic, (x,y,w,h)) #draws default button parameters
            msg = im
        self.dispText(msg, x, y, w, h)


    #draws the buttons to the menu
    def drawButtons(self):
        self.button(800, 200, 100, 50, RED, GREEN, "No", "Yes", self.tester )
        self.button(800, 300, 100, 50, RED, GREEN, "inactive", "active", self.tester )


    #runs the menu
    def runMenu(self):
        running = True
        while running:
            clock = pygame.time.Clock()
            self.screen.fill(BEIGE)
            for event in pygame.event.get():  # checks the queue of events
                print(event)
                if event.type == KEYDOWN:  # we can add many more commands here if we want
                    if event.key == K_ESCAPE:
                        running = False





            #self.screen.blit(self.TextSurf, self.TextRect)

            #pygame.draw.rect(screen, (0,255,0), (200, 450, 100, 50))
            self.drawButtons()
            self.dispText("Do you want jokers", 200, 125, 200, 200)
            pygame.display.flip()


            clock.tick(30)
        print(self.bool)


a = Menu()
a.runMenu()
"""
