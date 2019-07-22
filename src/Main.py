'''
Created on Jul 15, 2019

@author: Kel N
'''
import GUIcreator
from Menu import*
#Color Schemes:
#   ScreenColor,  MiddleColor, HandColor,   Deck,   DiscardColor
#1: DARK_PUCE,    ELEC_BLUE,   MOCCASIN,    GRULLO, DARK_RED
#2: BLACK,        MOCCASIN,    GRULLO,      GREEN,  DARK_RED
#3: MIDNIGHT_BLUE,SILVER,      LIGHT_GRAY,  GREEN,  VIOLET_RED
#4: DARK_BLUE,    HONEYDEW,    SPRING_GREEN,BEIGE,  TEAL

#Joker denotes whether Jokes are present or not
menu = Menu()
params = menu.runMenu(menu.listA)
print(params)
joker = params[0]
numhands = params[1]+1
colorScheme = params[2]
sortHands = params[3]
sortOrder = params[4]
#SortParams denotes whether how you want to sort each hand. The first hand is the bottom hand and the other numbers are given in a counter-clockwise rotations
sortParams= [("Value",False),("Value",False),("Value",True),("Value",True)]
gui=GUIcreator.GUI(numhands,colorScheme, joker, sortParams)
gui.runSim()
