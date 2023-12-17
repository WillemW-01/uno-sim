import random

from classes.deck import COLORS


class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.deck = []
        self.strategy = strategy

    def deal(self, card):
        self.deck.append(card)

    def card_matches(self, card, target):
        if card.cardType == "number":
            if card.number == target.number or (
                card.color in COLORS and card.color == target.color
            ):
                return True

        elif card.cardType == "special":
            if target.color in COLORS and card.color == target.color:
                return True

        return False

    def can_play_number(self, target):
        possible_cards = []
        for card in self.deck:
            if card.cardType == "number":
                if self.card_matches(card, target):
                    possible_cards.append(card)

        if len(possible_cards) != 0:
            return random.choice(possible_cards)
        else:
            return None

    def can_play_special(self, target):
        possible_cards = []
        for card in self.deck:
            if card.cardType == "special":
                if self.card_matches(card, target):
                    possible_cards.append(card)
                elif card.color == "black":
                    possible_cards.append(card)

        if len(possible_cards) != 0:
            return random.choice(possible_cards)
        else:
            return None

    def get_best_card(self, target):
        match self.strategy:
            case "special-first":
                best_special = self.can_play_special(target)
                if best_special is not None:
                    return best_special

                best_number = self.can_play_number(target)
                if best_number is not None:
                    return best_number

            case "number-first":
                # check if has a number card that can be played, then checks for special
                best_number = self.can_play_number(target)
                if best_number is not None:
                    return best_number

                best_special = self.can_play_special(target)
                if best_special is not None:
                    return best_special

        return None

    def play(self, target):
        card = self.get_best_card(target)
        if card is not None:
            self.deck.remove(card)
            return card

    def get_deck(self):
        return_str = ""
        for card in self.deck:
            return_str += f"{card}, "
        return return_str

    def __str__(self):
        return f"Player {self.name}'s"
