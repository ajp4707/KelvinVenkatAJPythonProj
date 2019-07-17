'''
Created on Jul 15, 2019

@author: Kel N
'''
import GUIcreator
#for testing

#Color Schemes:
#ScreenColor,MiddleColor,HandColor,Deck, DiscardColor
#1: DARK_PUCE, ELEC_BLUE, MOCCASIN,GRULLO, DARK_RED
numhands, joker=4,0
gui=GUIcreator.GUI(numhands,1, joker)
gui.runSim()
