import random

from classes.deck import Deck
from classes.player import Player

NUM_PLAYERS = 4

DEBUG = True


def debug(message):
    if DEBUG:
        print(message)


# create and shuffle uno deck
deck = Deck()
print(deck)
deck.shuffle()
deck.draw_first()
print(deck)

# deal to players
players = [Player(index + 1, "number-first") for index in range(NUM_PLAYERS)]

for card_num in range(7):
    for player in players:
        player.deal(deck.draw())

for player in players:
    print(f"> {player.name} deck:")
    print(player.get_deck())

# decide who to start
index = random.choice(list(range(NUM_PLAYERS)))
player_order = list(range(index, NUM_PLAYERS)) + list(range(index))
print(player_order)

# play in rounds until someone wins
print("Play will now commence!\n")
while True:
    curr_player = players[index]
    print(f"It is {curr_player} turn")
    target = deck.get_top()
    debug(f"  Top of play pile is: {target}")
    debug(f"  Player's deck: {curr_player.get_deck()}")
    best_card = curr_player.play(target)
    if best_card is not None:
        print(f"  Player could play a card: {best_card}")
        deck.play_card(best_card)
        debug(f"  Player's deck: {curr_player.get_deck()}")
    else:
        drawn_card = deck.draw()
        print(f"  Player has to draw, drew {drawn_card}")
        curr_player.deal(drawn_card)
        debug(f"  Player's deck: {curr_player.get_deck()}")
        best_card = curr_player.play(target)
        if best_card is not None:
            print(f"  Player could play drawn card")
            deck.play_card(best_card)
            debug(f"  Player's deck: {curr_player.get_deck()}")
        else:
            print("  Player had to pass")
            index = (index + 1) % NUM_PLAYERS
            input()
            continue

    index = (index + 1) % NUM_PLAYERS
    input()

# can play?
# yes - play card and do resulting effects
# no - pick up and see if can play
