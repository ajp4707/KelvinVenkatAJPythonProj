import pygame
# from Card import *
# from Deck import *
from Area import *
from constants import Dimensions

MIDDLE_WIDTH, MIDDLE_HEIGHT = 800, 400


class Middle(Area):
    """Represents the main playing field where all cards are visible."""

    def __init__(self, color):
        super().__init__(MIDDLE_WIDTH,
                         MIDDLE_HEIGHT,
                         Dimensions.screen_width / 2 - MIDDLE_WIDTH / 2,
                         Dimensions.screen_height / 2 - MIDDLE_HEIGHT / 2,
                         color,
                         False
                         )
