# Write simple structure representing deck of cards. Think of:
# - proper representation of single card (suit, rank)
# - deck sorting mechanism etc.
import random
from functools import total_ordering


def num_rank(rank):
    if rank == 'J':
        return 11
    if rank == 'Q':
        return 12
    if rank == 'K':
        return 13
    if rank == 'A':
        return 1
    return int(rank)


@total_ordering
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def display_card(self):
        return (f'{self.rank} of {self.suit}')

    def __lt__(self, other):
        t1 = self.suit, num_rank(self.rank)
        t2 = other.suit, num_rank(other.rank)
        return t1 < t2

    def __gt__(self, other):
        t1 = self.suit, num_rank(self.rank)
        t2 = other.suit, num_rank(other.rank)
        return t1 > t2

    def __eq__(self, other):
        t1 = self.suit, num_rank(self.rank)
        t2 = other.suit, num_rank(other.rank)
        return t1 == t2


class Deck:
    list_suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    list_ranks = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in self.list_suits for rank in self.list_ranks]

    def show(self):
        for card in self.cards:
            print(card.display_card())

    def card_count(self):
        return len(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            print("No more cards in deck")
            return
        card = self.cards.pop()
        print(f"Draw - {card.display_card()}")

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()
