#Venkat - citing code from pythonprogramming.net
import sys
import pygame
from pygame.locals import*
from Toggle import *


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
labelFont = BLACK

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
        self.titleFont = pygame.font.Font('freesansbold.ttf', 80)
        self.buttonFont = pygame.font.Font('freesansbold.ttf', 20)
        self.optionFont = pygame.font.Font('freesansbold.ttf', 30)

    #Declaring Objects (buttons)
    joker = Toggle(800, 275, 200, 50, ["No", "Yes"])
    numHands = Toggle(800, 350, 200, 50, ["One", "Two", "Three", "Four"])
    colorScheme = Toggle(800, 425, 200, 50, ["Dark Puce", "Black", "Midnight Blue", "Dark Blue"])
    sortHands = Toggle(800, 500, 200, 50, ["Value", "Suit"])
    scend = Toggle(800, 575, 200, 50, ["Ascending", "Descending"])
    begin = Toggle(300, 640, 600, 50, ["Begin"])
    listA = [joker, numHands, colorScheme, sortHands, scend, begin]


    def text_objects(self, text, font, color):
        self.textSurface = font.render(text, True, color)
        return self.textSurface, self.textSurface.get_rect()

    #displays text
    def dispText(self, msg, x, y, w, h, font, color):
        self.TextSurf, self.TextRect = self.text_objects(msg, font, color)
        self.TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen.blit(self.TextSurf, self.TextRect)

    #draws button descriptions
    def drawLabels(self):
        self.dispText("Python Card Sim v4.0", 200, 100, 800, 100, self.titleFont, labelFont)
        self.dispText("Include Joker", 25, 275, 600, 50, self.optionFont, labelFont)
        self.dispText("Number of Players", 25, 350, 600, 50, self.optionFont, labelFont)
        self.dispText("Choose your theme", 25, 425, 600, 50, self.optionFont, labelFont)
        self.dispText("Sort hands by", 25, 500, 600, 50, self.optionFont, labelFont)
        self.dispText("Sort order", 25, 575, 600, 50, self.optionFont, labelFont)

    #draws buttons
    def drawButton(self, toggle):
        mouse = pygame.mouse.get_pos()
        #toggles options
        if toggle.x < mouse[0] < toggle.x + toggle.w and toggle.y < mouse[1] < toggle.y + toggle.h or toggle.attr % len(toggle.mod) != 0:  # checks if mouse is over button, then changes color to active color
            pygame.draw.rect(self.screen, ELEC_BLUE, (toggle.x, toggle.y, toggle.w, toggle.h))
            msg = toggle.mod[toggle.attr%(len(toggle.mod))]

        #default option
        else:
            pygame.draw.rect(self.screen, SILVER, (toggle.x, toggle.y, toggle.w, toggle.h))  # draws default button parameters
            msg = toggle.mod[0]


        self.dispText(msg, toggle.x, toggle.y, toggle.w, toggle.h, self.buttonFont, BLACK)

    #runs game loop and menu
    def runMenu(self, list):
        running = True
        clock = pygame.time.Clock()

        while running:

            self.screen.fill(MOCCASIN)
            self.drawLabels()

            for event in pygame.event.get():  # checks the queue of events
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for i in list:
                            if i.x < event.pos[0] < i.x + i.w and i.y < event.pos[1] < i.y + i.h:
                                i.attr += 1
                elif event.type == QUIT:
                    running = False

            for i in range(len(list)):
                self.drawButton(list[i])

            #checks if begin was selected, then closes gui and returns values
            if list[5].attr > 0:
                pygame.quit()
                returnList = []
                returnList.append(list[0].attr%len(list[0].mod))
                returnList.append(list[1].attr%len(list[1].mod))
                returnList.append(list[2].attr%len(list[2].mod))
                returnList.append(list[3].attr%len(list[3].mod))
                returnList.append(list[4].attr%len(list[4].mod))
                return returnList

            #self.drawButton(self.toggle1)
            #print(self.toggle1.attr)
             #print(self.toggle1.mod[self.toggle1.attr%2])
            #self.dispText("Do you want jokers", 200, 125, 200, 200)
            pygame.display.flip()

            clock.tick(60)



c = Menu()
c.runMenu(c.listA)


