from Toggle import *
from constants import Color, Dimensions
import pygame


class Menu(object):
    left_margin = 800
    w, h = 200, 50

    joker_btn = Toggle((left_margin, 275), (w, h), ["No", "Yes"])
    num_hands_btn = Toggle((left_margin, 350), (w, h), ["1", "2", "3", "4"])
    color_scheme_btn = Toggle((left_margin, 425), (w, h), ["Dark Puce", "Black", "Midnight Blue", "Dark Blue"])
    sort_hands_btn = Toggle((left_margin, 500), (w, h), ["Value", "Suit"])
    order_btn = Toggle((left_margin, 575), (w, h), ["Ascending", "Descending"])
    begin_btn = Toggle((300, 640), (600, h), ["Begin", ""])
    buttons = [joker_btn, num_hands_btn, color_scheme_btn, sort_hands_btn, order_btn, begin_btn]

    def __init__(self):
        # initializes window
        pygame.init()
        self.screen = pygame.display.set_mode((Dimensions.screen_width, Dimensions.screen_height))
        pygame.display.set_caption('Python Card Simulator v4')
        self.params = None
        self.run_menu()

    @staticmethod  # TODO class method?
    def text_objects(text, font, text_color):
        text_surface = font.render(text, True, text_color)  # TODO what's the difference between this and self.TextSurf?
        return text_surface, text_surface.get_rect()

    def disp_text(self, msg, x, y, w, h, font, text_color):
        text_surf, text_rect = Menu.text_objects(msg, font, text_color)
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen.blit(text_surf, text_rect)

    def draw_labels(self):
        """Draws button descriptions."""
        title_font = pygame.font.Font('freesansbold.ttf', 80)
        font = pygame.font.Font('freesansbold.ttf', 30)
        label_color = Color.BLACK

        x, w, h = 25, 600, 50
        self.disp_text("Python Card Sim v4.0", 200, 100, 800, 100, title_font, label_color)
        self.disp_text("Include Joker", x, 275, w, h, font, label_color)
        self.disp_text("Number of Players", x, 350, w, h, font, label_color)
        self.disp_text("Choose your theme", x, 425, w, h, font, label_color)
        self.disp_text("Sort hands by", x, 500, w, h, font, label_color)
        self.disp_text("Sort order", x, 575, w, h, font, label_color)

    def draw_button(self, button: Toggle):
        """Creates button objects."""
        button_font = pygame.font.Font('freesansbold.ttf', 20)
        mouse = pygame.mouse.get_pos()

        # Buttons the mouse hovers over turn blue, default silver
        if button.x < mouse[0] < button.x + button.w and button.y < mouse[1] < button.y + button.h:
            pygame.draw.rect(self.screen, Color.ELEC_BLUE, (button.x, button.y, button.w, button.h))
        else:
            pygame.draw.rect(self.screen, Color.SILVER, (button.x, button.y, button.w, button.h))

        msg = button.options[button.current_state]
        self.disp_text(msg, button.x, button.y, button.w, button.h, button_font, Color.BLACK)

    # runs game loop and menu
    def run_menu(self):
        clock = pygame.time.Clock()

        while True:
            self.screen.fill(Color.MOCCASIN)
            self.draw_labels()
            # Check for events
            for event in pygame.event.get():
                # Quit conditions
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return None
                elif event.type == pygame.QUIT:
                    return None
                # Check if a button was pressed
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for button in Menu.buttons:
                            if (button.x < event.pos[0] < button.x + button.w and button.y < event.pos[1] <
                                    button.y + button.h):
                                button.rotate()

            # Draw the buttons
            for button in Menu.buttons:
                self.draw_button(button)

            # Start the game?
            if Menu.begin_btn.current_state != 0:
                pygame.quit()
                self.params = {
                    'joker': bool(Menu.joker_btn.current_state),
                    'num_hands': Menu.num_hands_btn.current_state + 1,
                    'color_scheme': Menu.color_scheme_btn.label,
                    'hand_sort': Menu.sort_hands_btn.label,
                    'sort_order': Menu.order_btn.label
                }
                return

            pygame.display.flip()
            clock.tick(30)
