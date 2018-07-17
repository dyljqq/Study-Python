# coding: utf-8

import collections
from random import choice


Card = collections.namedtuple('Card', ['suit', 'rank'])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def score_high(card):
    rank = FranchDeck.ranks.index(card.rank)
    return rank * len(FranchDeck.suits) + suit_values[card.suit]


class FranchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def sort_cards():
    deck = FranchDeck()
    st = sorted(deck, key=score_high)
    for s in st:
        print s


if __name__ == '__main__':
    beer_card = Card('diamonds', '7')
    print beer_card

    deck = FranchDeck()
    print len(deck)

    c = choice(deck)
    print c

    print FranchDeck.ranks.index(c.rank)

    sort_cards()
