"""
Created on Jul 15, 2019

@author: Kel N
"""
from Menu import *
import GUI

menu = Menu()
params = menu.params

if params is not None:  # params will only be None if a player quits the game from the main menu
    game = GUI.GUI(params)
