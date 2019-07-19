'''
Created on Jul 15, 2019

@author: Kel N
'''
import GUIcreator
#for testing

#Color Schemes:
#   ScreenColor,  MiddleColor, HandColor,   Deck,   DiscardColor
#1: DARK_PUCE,    ELEC_BLUE,   MOCCASIN,    GRULLO, DARK_RED
#2: BLACK,        MOCCASIN,    GRULLO,      GREEN,  DARK_RED
#3: MIDNIGHT_BLUE,SILVER,      LIGHT_GRAY,  GREEN,  VIOLET_RED
#4: DARK_BLUE,    HONEYDEW,    SPRING_GREEN,BEIGE,  TEAL

numhands, joker=4,0
gui=GUIcreator.GUI(numhands,4, joker)
gui.runSim()
