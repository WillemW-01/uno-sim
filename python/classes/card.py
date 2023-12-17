colors = {
    "black": "\033[30m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "green": "\033[92m",
    "blue": "\033[96m",
    None: "\033[00m",
}


class Card:
    def __init__(self, cardType=None, color=None, number=None, ability=None):
        self.cardType = cardType
        self.color = color
        self.number = number
        self.ability = ability

    def __str__(self):
        if self.number is not None:
            return f"{colors[self.color]}{self.number}{colors[None]}"
        elif self.ability is not None:
            return f"{colors[self.color]}{self.ability}{colors[None]}"
