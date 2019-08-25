# Venkat - citing code from pythonprogramming.net

from Toggle import *
from constants import Color, Dimensions


class Menu(object):
    # Declaring Objects (buttons)
    left_margin = 800
    w, h = 200, 50
    joker_btn = Toggle(left_margin, 275, w, h, ["No", "Yes"])
    num_hands_btn = Toggle(left_margin, 350, w, h, ["One", "Two", "Three", "Four"])
    color_scheme_btn = Toggle(left_margin, 425, w, h, ["Dark Puce", "Black", "Midnight Blue", "Dark Blue"])
    sort_hands_btn = Toggle(left_margin, 500, w, h, ["Value", "Suit"])
    order_btn = Toggle(left_margin, 575, w, h, ["Ascending", "Descending"])
    begin_btn = Toggle(300, 640, 600, h, ["Begin", ""])
    buttons = [joker_btn, num_hands_btn, color_scheme_btn, sort_hands_btn, order_btn, begin_btn]

    def __init__(self):
        # initializes pygame module and window
        pygame.init()
        self.screen = pygame.display.set_mode((Dimensions.screen_width, Dimensions.screen_height))
        pygame.display.set_caption('Python Card Simulator v4')

    def text_objects(self, text, font, color):
        self.textSurface = font.render(text, True, color)
        return self.textSurface, self.textSurface.get_rect()

    def disp_text(self, msg, x, y, w, h, font, color):
        self.TextSurf, self.TextRect = self.text_objects(msg, font, color)
        self.TextRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen.blit(self.TextSurf, self.TextRect)

    # draws button descriptions
    def draw_labels(self):
        font_color = Color.BLACK
        title_font = pygame.font.Font('freesansbold.ttf', 80)
        option_font = pygame.font.Font('freesansbold.ttf', 30)

        self.disp_text("Python Card Sim v4.0", 200, 100, 800, 100, title_font, font_color)
        self.disp_text("Include Joker", 25, 275, 600, 50, option_font, font_color)
        self.disp_text("Number of Players", 25, 350, 600, 50, option_font, font_color)
        self.disp_text("Choose your theme", 25, 425, 600, 50, option_font, font_color)
        self.disp_text("Sort hands by", 25, 500, 600, 50, option_font, font_color)
        self.disp_text("Sort order", 25, 575, 600, 50, option_font, font_color)

    # draws buttons TODO overhaul buttons
    def draw_button(self, button: Toggle):
        button_font = pygame.font.Font('freesansbold.ttf', 20)
        mouse = pygame.mouse.get_pos()
        # toggles options: checks if mouse is over button, then changes color to active color
        if button.x < mouse[0] < button.x + button.w and button.y < mouse[1] < button.y + button.h:
            pygame.draw.rect(self.screen, Color.ELEC_BLUE, (button.x, button.y, button.w, button.h))
            msg = button.options[button.current_state]
        # default option
        else:
            # draws default button parameters
            pygame.draw.rect(self.screen, Color.SILVER, (button.x, button.y, button.w, button.h))
            msg = button.options[button.current_state]
        self.disp_text(msg, button.x, button.y, button.w, button.h, button_font, Color.BLACK)

    # runs game loop and menu
    def run_menu(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            self.screen.fill(Color.MOCCASIN)
            self.draw_labels()
            for event in pygame.event.get():  # checks the queue of events
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False  # TODO return?
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for button in Menu.buttons:
                            if button.x < event.pos[0] < button.x + button.w and button.y < event.pos[1] \
                                    < button.y + button.h:
                                button.rotate()
                elif event.type == QUIT:
                    running = False
            for button in Menu.buttons:
                self.draw_button(button)
            # checks if begin was selected, then closes gui and returns values
            if Menu.begin_btn.current_state != 0:
                pygame.quit()
                return {
                    'joker': bool(Menu.joker_btn.current_state),
                    'num_hands': Menu.num_hands_btn.current_state + 1,
                    'color_scheme': Menu.color_scheme_btn.selected,
                    'hand_sort': Menu.sort_hands_btn.selected,
                    'sort_order': Menu.order_btn.selected
                }

            pygame.display.flip()
            clock.tick(30)
