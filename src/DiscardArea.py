from Area import *
import Card  # TODO necessary?

HORIZ_HAND_WIDTH, HORIZ_HAND_HEIGHT = 800, 133
VERT_HAND_WIDTH, VERT_HAND_HEIGHT = 176, 400


class DiscardArea(Area):
    # Similar to hand properties, but cards in middle are all shown
    def __init__(self, color):
        super().__init__(VERT_HAND_WIDTH, HORIZ_HAND_HEIGHT,
                         1100 - VERT_HAND_WIDTH / 2,
                         625 - HORIZ_HAND_HEIGHT / 2,
                         color,
                         True
                         )

    def display(self):
        for card in self:
            card.rect.x, card.rect.y = 1100 - Card.width / 2, 625 - Card.height / 2
