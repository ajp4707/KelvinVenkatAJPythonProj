from pygame.locals import *
# from VerticalHand import VerticalHand
# from HorizontalHand import HorizontalHand
from HandAreas import *
from Middle import *
from DeckArea import DeckArea
from DiscardArea import DiscardArea
from pygame.constants import K_s
from constants import Schemes

# Screen and Area Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700


class GUI(object):
    def __init__(self, params):
        self.scheme = Schemes.get(params['color_scheme'])
        self.clock = pygame.time.Clock()
        self.middle, self.screen = self.create_screen()
        self.hands = self.create_hands(params['num_hands'], params)
        self.deck, self.deckarea = self.make_deck(params['joker'])
        self.discardarea = self.create_discard()
        # mouse variables
        self.mouse_x, self.mouse_y = 0, 0

    # initializes pygame module and window
    def create_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(
            'Python Card Simulator:   [SPACE] Deal Cards,   [1-4] Player 1-4\'s Turn,   [S] Reshuffle')
        middle = Middle(self.scheme[1])
        return middle, screen

    def create_discard(self):
        return DiscardArea(self.scheme[4])

        # Creates middle area and hands.

    def create_hands(self, hand_num, params):
        hands = []
        color = self.scheme[2]
        # 1, 2, 3, and 4 are the only accepted arguments for the number of hands
        hands.append(HorizontalHand(color, params))
        if hand_num == 2:
            hands.append(HorizontalHand(color, params, "Top"))
        elif hand_num == 3:
            hands.append(VerticalHand(color, params, "Right"))
            hands.append(VerticalHand(color, params, "Left"))
        elif hand_num == 4:
            hands.append(VerticalHand(color, params, "Right"))
            hands.append(HorizontalHand(color, params, "Top"))
            hands.append(VerticalHand(color, params, "Left"))
        return hands

    # initialize Deck accepting parameters for whether you want jokers and the previously created hands.
    # In the future, determine whose turn it is?
    def make_deck(self, joker):
        deck = Deck(joker, 100 - Card.width / 2, 75 - Card.height / 2)
        deckarea = DeckArea(self.scheme[3], self.hands)
        deckarea.update(deck)
        return deck, deckarea

    def blit_screen(self):
        self.screen.fill(self.scheme[0])
        self.screen.blit(self.middle.surf, (self.middle.x, self.middle.y))
        self.screen.blit(self.deckarea.surf, (self.deckarea.x, self.deckarea.y))
        self.screen.blit(self.discardarea.surf, (self.discardarea.x, self.discardarea.y))
        for hand in self.hands:
            self.screen.blit(hand.surf, (hand.x, hand.y))
        for card in self.deck.cards:
            self.screen.blit(card.get_image(), (card.rect.x, card.rect.y))

    def update_areas(self):
        self.deck.hide()
        self.deckarea.update(self.deck)
        for hand in self.hands:
            hand.update(self.deck)
        self.middle.update(self.deck)
        self.discardarea.update(self.deck)

    # Game loop - keeps the window open
    def run_sim(self):
        running = True
        while running:
            for event in pygame.event.get():  # checks the queue of events
                if event.type == KEYDOWN:  # we can add many more commands here if we want
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_SPACE:
                        self.deckarea.deal(7)
                        self.update_areas()
                    elif event.key == K_1:
                        for hand in self.hands:
                            hand.hide_cards = True
                        self.hands[0].hide_cards = False
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == K_2:
                        for hand in self.hands:
                            hand.hide_cards = True
                        self.hands[1 % len(self.hands)].hide_cards = False
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == K_3:
                        for hand in self.hands:
                            hand.hide_cards = True
                        self.hands[2 % len(self.hands)].hide_cards = False
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == K_4:
                        for hand in self.hands:
                            hand.hide_cards = True
                        self.hands[3 % len(self.hands)].hide_cards = False
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == K_s:
                        for card in self.deck.cards:
                            card.rect.x, card.rect.y = 100 - Card.width / 2, 75 - Card.height / 2
                        self.deck.shuffle()
                        self.update_areas()
                elif event.type == QUIT:
                    running = False

                # MOUSEBUTTONDOWN 3 is a right click, drags all of the cards. button 1 is a left click, drags one Card
                # Logic and some code to drag and drop cards came from this website
                # https://stackoverflow.com/questions/41332861/click-and-drag-a-rectangle-with-pygame
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        for card in self.deck.cards:
                            if card.rect.collidepoint(event.pos):
                                card.dragging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = card.rect.x - mouse_x
                                offset_y = card.rect.y - mouse_y
                    elif event.button == 1:
                        for i in range(len(self.deck.cards) - 1, -1, -1):
                            if self.deck.cards[i].rect.collidepoint(event.pos):
                                self.deck.cards[i].dragging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = self.deck.cards[i].rect.x - mouse_x
                                offset_y = self.deck.cards[i].rect.y - mouse_y
                                self.deck.cards.append(self.deck.cards.pop(
                                    i))  # Put grabbed cards at the end of the Deck, they will blit on top
                                break
                # For efficiency, Hands only check if cards have been added to them after MOUSEBUTTONUP
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        self.deck.undrag()
                    elif event.button == 1:
                        self.deck.undrag()
                    self.update_areas()
                    # if event.button == 2:

                elif event.type == pygame.MOUSEMOTION:
                    for card in self.deck.cards:
                        if card.dragging:
                            mouse_x, mouse_y = event.pos
                            card.rect.x = mouse_x + offset_x
                            card.rect.y = mouse_y + offset_y

            self.blit_screen()
            pygame.display.flip()

            self.clock.tick(30)
