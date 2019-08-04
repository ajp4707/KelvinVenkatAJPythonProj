"""Constants of the project"""


class Color:
    """Common colors used in the GUI."""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    DARK_RED = (232, 23, 23)
    LIME = (0, 255, 0)
    BLUE = (0, 0, 255)
    DARK_PUCE = (72, 61, 63)
    ELEC_BLUE = (5, 142, 217)
    MOCCASIN = (244, 235, 217)
    GRULLO = (163, 154, 146)
    DARK_MAGENTA = (139, 0, 139)
    BEIGE = (245, 245, 220)
    LIGHT_GRAY = (119, 136, 153)
    GREEN = (0, 128, 0)
    SILVER = (192, 192, 192)
    DARK_BLUE = (0, 0, 139)
    MIDNIGHT_BLUE = (25, 25, 112)
    VIOLET_RED = (219, 112, 147)
    HONEYDEW = (240, 255, 240)
    TEAL = (0, 128, 128)
    SPRING_GREEN = (0, 250, 154)


class Schemes:
    """Groups of colors."""
    DARK_PUCE = (Color.DARK_PUCE, Color.ELEC_BLUE, Color.MOCCASIN, Color.GRULLO, Color.DARK_RED)
    BLACK = (Color.BLACK, Color.MOCCASIN, Color.GRULLO, Color.GREEN, Color.DARK_RED)
    MIDNIGHT_BLUE = (Color.MIDNIGHT_BLUE, Color.SILVER, Color.LIGHT_GRAY, Color.GREEN, Color.VIOLET_RED)
    DARK_BLUE = (Color.DARK_BLUE, Color.HONEYDEW, Color.SPRING_GREEN, Color.BEIGE, Color.TEAL)

    @classmethod
    def get(cls, scheme):
        if scheme == 'Dark Puce':
            return cls.DARK_PUCE
        elif scheme == 'Black':
            return cls.BLACK
        elif scheme == 'Midnight Blue':
            return cls.MIDNIGHT_BLUE
        elif scheme == 'Dark Blue':
            return cls.DARK_BLUE
        else:
            raise KeyError('Did not receive proper scheme:', scheme)
