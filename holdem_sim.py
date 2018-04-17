# -*- coding: utf-8 -*-
import handrank
import math
import random
import itertools
import collections
import pprint

class Player():
    def __init__(self, a, b):
        self.holecard1 = a
        self.holecard2 = b
    def best_ranking_hand(self, community_cards):
        seven_cards = community_cards + [holecard1, holecard2]
        five_cards_comb = list(itertools.combinations(seven_cards, 5))
        
        return handrank.best_ranking_hand(five_cards_comb)

if __name__ == "__main__":
    print("How many time to repeat this simulatation?")
    times = int(input())
    print("How many players? (at least 2)")
    num = int(input())
    player_ls = []
    for i in range(1, num + 1):
        print("Enter player {0}'s first hole card. (e.g. 14C)".format(i))
        Print("Or enter 'rd' to randomly deal player {0}'s first hole card")
        holecard1 = input().upper()
        print("Enter player {0}'s second hole card. (e.g. 14C)".format(i))
        Print("Or enter 'rd' to randomly deal player {0}'s second hole card")
        holecard2 = input().upper()
        player_ls.append(player(holecard1, holecard2))
    print("")
    