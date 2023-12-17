from random import shuffle

from classes.card import Card

COLORS = ["blue", "red", "green", "yellow"]
MAX_NUM = 10
COLORED_SPECIAL = ["<-", "-->", "+2"]
BLACK_SPECIAL = ["+4", "color"]


class Deck:
    """
    This class holds the game state in terms of the draw pile and the out pile.
    Players can take from this object and give to this object.
    """

    def __init__(self, mult=1):
        """
        Creates the deck. Mult gives how many multipliers of decks are necessary.
        Default 108 cards are in the deck.
        """

        self.draw_pile = []
        self.play_pile = []

        for color in COLORS:
            # add numbered cards
            for number in range(0, MAX_NUM):
                self.draw_pile.append(
                    Card(cardType="number", color=color, number=number)
                )

            # add colored special cards
            for ability in COLORED_SPECIAL:
                self.draw_pile.append(
                    Card(cardType="special", color=color, ability=ability)
                )

        # add special black cards
        for _ in range(4):
            # maybe add more?
            for ability in BLACK_SPECIAL:
                self.draw_pile.append(
                    Card(cardType="special", color="black", ability=ability)
                )

    def shuffle(self, pile=None):
        """
        Simply shuffles the order of the given deck.
        """
        if pile is None:
            shuffle(self.draw_pile)
        else:
            shuffle(pile)

    def re_deck(self, n=0):
        """
        Necessary to call when the required number of cards is greater than the
        length of the draw_pile. Simply shuffles the cards that were below the
        top `N` of cards.
        """
        top = self.draw_pile[n:]
        bot = self.draw_pile[:n]
        shuffle(bot)
        self.draw_pile = bot + top

    def draw_first(self):
        self.play_pile.append(self.draw())

    def draw(self, num=1):
        if num == 1:
            return self.draw_pile.pop()
        else:
            return [self.draw_pile.pop() for _ in range(num)]

    def get_top(self):
        return self.play_pile[-1]

    def play_card(self, card):
        match card.cardType:
            case "special":
                if card.color == "black":
                    # check abilities
                    pass
                elif card in COLORS:
                    # check top of play
                    pass
            case "number":
                # check top of play
                # check if matching number or color
                pass
        self.play_pile.append(card)

    def __str__(self):
        return_str = "> play pile:\n"
        for card in self.play_pile:
            return_str += f"{card}, "
        return_str += "\n> draw pile:\n"
        for card in self.draw_pile:
            return_str += f"{card}, "
        return return_str
