# -*- coding: utf-8 -*-
import math
import random
import collections
import pprint

def standard_deck():
    '''
    Creat a standard, 52-card deck of cards.
    Use 11,12,13,14 to replace J,Q,K,A respectively.
    Use "C" for club, ♣;
    Use "D" for diamond, ♦;
    Use "H" for heart, ♥;
    Use "S" for spade, ♠.
    '''
    rank = [i for i in range(2, 15)][::-1]
    suit = ['C', 'D', 'H', 'S']
    standard_deck = [str(i) + j for i in rank for j in suit]

    return standard_deck

class DeckOfCards():
    def __init__(self):
        self.deck = standard_deck()

    def deal_holecards(self, a, b):
        if a.upper() == "RD" and b.upper() == "RD":
            a = random.choice(self.deck)
            self.deck.remove(a)
            b = random.choice(self.deck)
            self.deck.remove(b)
            return [a, b]
        elif a.upper() == "RD" and b.upper() != "RD":
            self.deck.remove(b)
            a = random.choice(self.deck)
            self.deck.remove(a)
            return [a, b]
        elif a.upper() != "RD" and b.upper() == "RD":
            self.deck.remove(a)
            b = random.choice(self.deck)
            self.deck.remove(b)
            return [a, b]
        else:
            self.deck.remove(a)
            self.deck.remove(b)
            return [a, b]

    def deal_the_flop(a, b, c):
        pass
        if a.upper() == "RD" and b.upper() == "RD" and c.upper() == "RD":
            a = random.choice(self.deck)
            self.deck.remove(a)
            b = random.choice(self.deck)
            self.deck.remove(b)
            c = random.choice(self.deck)
            return [a, b]
        elif a.upper() == "RD" and b.upper() != "RD":
            self.deck.remove(b)
            a = random.choice(self.deck)
            self.deck.remove(a)
            return [a, b]
        elif a.upper() != "RD" and b.upper() == "RD":
            self.deck.remove(a)
            b = random.choice(self.deck)
            self.deck.remove(b)
            return [a, b]
        else:
            self.deck.remove(a)
            self.deck.remove(b)
            self.deck.remove(c)
            return [a, b, c]
        
    def deal_the_turn():
        pass
    def deal_the_river():
        pass

if __name__ == '__main__':
    sample = DeckOfCards()
    holecards = sample.deal_holecards("RD", "2S")
    print(sample.deck)
    print(holecards)
    print(len(sample.deck))
