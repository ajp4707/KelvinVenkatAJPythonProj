import sys
import pygame
from pygame.locals import*

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#initializes pygame module and window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

surf = pygame.Surface((50,50))
surf.fill((100,200,200))
rect = surf.get_rect()
screen.blit(surf, (375,275))
pygame.display.flip()

#Game loop - keeps the window open 
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
