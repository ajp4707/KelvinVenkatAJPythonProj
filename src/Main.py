"""
Created on Jul 15, 2019

@author: Kel N
"""
import GUIcreator
from Menu import *

menu = Menu()
params = menu.run_menu()

game = GUIcreator.GUI(params)
game.run()
