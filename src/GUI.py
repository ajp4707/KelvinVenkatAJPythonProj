import pygame
from Areas import *
from constants import Schemes, Dimensions
from Deck import Deck

"""The number of cards dealt to players when [space] is pressed"""
deal_num = 1


class GUI:
    """Runs the main game loop. Handles logic and graphics."""

    # For memory efficiency
    __slots__ = ('scheme', 'clock', 'middle', 'screen', 'hands', 'deck',
                 'deckarea', 'discardarea', 'mouse_x', 'mouse_y')

    def __init__(self, params):
        self.scheme = Schemes.get(params['color_scheme'])
        self.clock = pygame.time.Clock()
        self.middle, self.screen = self.create_screen()
        self.hands = self.create_hands(params)
        self.deck, self.deckarea = self.make_deck(params['joker'])
        self.discardarea = DiscardArea(self.scheme[4])
        self.mouse_x, self.mouse_y = 0, 0

        self.run()

    def create_screen(self):
        """Initializes window."""
        pygame.init()
        screen = pygame.display.set_mode((Dimensions.screen_width, Dimensions.screen_height))
        pygame.display.set_caption(
            'Python Card Simulator:   [SPACE] Deal,   [1-4] Player 1-4\'s Turn,   [S] Reshuffle')
        # Create the middle area, since it never changes.
        middle = Middle(self.scheme[1])
        return middle, screen

    def create_hands(self, params):
        """Creates a number of HandAreas based on num_hands."""
        hands = []
        num_hands = params['num_hands']
        scheme = self.scheme[2]
        # Add the bottom hand
        hands.append(HorizontalHand(scheme, params, 'Bottom'))
        # Add the top and/or side hands
        if num_hands == 2:
            hands.append(HorizontalHand(scheme, params, "Top"))
        elif num_hands >= 3:
            hands.append(VerticalHand(scheme, params, "Right"))
            hands.append(VerticalHand(scheme, params, "Left"))
        # Finally, add the top hand (if four players)
        if num_hands == 4:
            hands.append(HorizontalHand(scheme, params, "Top"))
        return hands

    def make_deck(self, joker):
        """Initialize the deck with the joker parameter."""
        deck = Deck(joker, 100 - Card.width / 2, 75 - Card.height / 2)
        deck_area = DeckArea(self.scheme[3], self.hands)
        deck_area.update(deck)
        return deck, deck_area

    def blit_screen(self):
        """Draws textures onto shapes, areas, cards, everything!"""
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

    def run(self):
        """The main game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    num_keys = {pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2, pygame.K_4: 3}
                    if event.key == pygame.K_ESCAPE:  # Quits game
                        running = False
                    elif event.key == pygame.K_SPACE:  # Deals cards
                        self.deckarea.deal(deal_num)
                        self.update_areas()
                    elif event.key in num_keys:  # Changes player number (Flips other hands)
                        for hand in self.hands:
                            hand.cards_hidden = True
                        try:
                            self.hands[num_keys[event.key]].cards_hidden = False
                        except IndexError:
                            print('That player doesn\'t exist!')
                        for hand in self.hands:
                            hand.update(self.deck)
                    elif event.key == pygame.K_s:  # Reshuffles the deck
                        for card in self.deck.cards:
                            card.rect.x, card.rect.y = 100 - Card.width / 2, 75 - Card.height / 2
                        self.deck.shuffle()
                        self.update_areas()
                elif event.type == pygame.QUIT:
                    running = False

                # MOUSEBUTTONDOWN 3 is a right click, drags all of the cards. button 1 is a left click, drags one Card
                # Logic to drag and drop cards from:
                # https://stackoverflow.com/questions/41332861/click-and-drag-a-rectangle-with-pygame
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        for card in self.deck.cards:
                            if card.rect.collidepoint(event.pos):
                                card.draggable = True
                                mouse_x, mouse_y = event.pos
                                offset_x = card.rect.x - mouse_x
                                offset_y = card.rect.y - mouse_y
                    elif event.button == 1:
                        for i in range(len(self.deck.cards) - 1, -1, -1):  # TODO what is this loop doing?
                            if self.deck.cards[i].rect.collidepoint(event.pos):
                                self.deck.cards[i].draggable = True
                                mouse_x, mouse_y = event.pos
                                offset_x = self.deck.cards[i].rect.x - mouse_x
                                offset_y = self.deck.cards[i].rect.y - mouse_y
                                # Put grabbed cards at the end of the Deck, they will blit on top
                                self.deck.cards.append(self.deck.cards.pop(i))
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
                        if card.draggable:
                            mouse_x, mouse_y = event.pos
                            card.rect.x = mouse_x + offset_x
                            card.rect.y = mouse_y + offset_y

            self.blit_screen()
            pygame.display.flip()

            self.clock.tick(30)
