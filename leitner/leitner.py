import random
from card import Card

class Leitner:

    def __init__(self):
        self._deck:list[Card] = []

    def shuffle(self):
        '''Fisher-Yates shuffle of the deck.'''
        current_index = len(self._deck) - 1

        while current_index > 0:
            swap_index = random.randint(0, current_index)

            if swap_index != current_index:
                current_value = self._deck[current_index]
                self._deck[current_index] = self._deck[swap_index]
                self._deck[swap_index] = current_value

            current_index -= 1

