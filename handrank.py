# -*- coding: utf-8 -*-
import collections
import functools
import itertools
import math
import pprint
import random

def is_straight_flush(cards): 
    '''
    Input should be a 5-element list
    
    Including royal flushij
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    if len(set(suits)) == 1 and ranks == list(range(ranks[0], ranks[0] + 5)):
        return True
    elif len(set(suits)) == 1 and ranks == [2,3,4,5,14]:
        return True
    else:
        return False

def is_4_of_a_kind(cards):
    '''
    Input should be a 5-element list
    
    1. Excluding Royal Flush & Straight Flush (By its nature)
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    return ranks[0] == ranks[3] or ranks[1] == ranks[4]
        
def is_fullhouse(cards):
    '''
    Input should be a 5-element list
    
    1. Excluding Royal Flush & Straight Flush (By its nature)
    2. Excluding Four of a Kind (By its nature)
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    if ranks[0] == ranks[2] and ranks[3] == ranks[4]:
        return True
    elif ranks[0] == ranks[1] and ranks[2] == ranks[4]:
        return True
    else:
        return False
    
def is_flush(cards):
    '''
    Input should be a 5-element list
    
    1. Excluding Royal Flush & Straight Flush
    2. Excluding Four of a Kind (By its nature)
    3. Excluding Full House (By its nature)
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    if ranks == list(range(ranks[0], ranks[0] + 5)):
        return False
    elif ranks == [2,3,4,5,14]:
        return False
    elif len(set(suits)) == 1:
        return True
    else:
        return False
        
def is_straight(cards):
    '''
    Input should be a 5-element list
    
    1. Excluding Royal Flush & Straight Flush
    2. Excluding Four of a Kind (By its nature)
    3. Excluding Full House (By its nature)
    4. Excluding flush (Because it has excluded straight flush)
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    if len(set(suits)) == 1:
        return False
    elif ranks == list(range(ranks[0], ranks[0] + 5)):
        return True
    elif ranks == [2,3,4,5,14]:
        return True
    else:
        return False
        
def is_3_of_a_kind(cards):
    '''
    Input should be a 5-element list
    
    1. Excluding Royal Flush & Straight Flush (By its nature)
    2. Excluding Four of a Kind
    3. Excluding Full House
    4. Excluding Flush (By its nature)
    5. Excluding Straight (By its nature)
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    counter = collections.Counter(ranks)
    if [1,1,3] == sorted(counter.values()):
        return True
    else:
        return False

def is_two_pair(cards):
    '''
    Input should be a 5-element list
    
    1. Excluding Royal Flush & Straight Flush (By its nature)
    2. Excluding Four of a Kind
    3. Excluding Full House
    4. Excluding Flush (By its nature)
    5. Excluding Straight (By its nature)
    6. Excluding Three of a Kind
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    counter = collections.Counter(ranks)
    if [1,2,2] == sorted(counter.values()):
        return True
    else:
        return False
        
def is_one_pair(cards):
    '''
    Input should be a 5-element list
    
    1. Excluding Royal Flush & Straight Flush (By its nature)
    2. Excluding Four of a Kind
    3. Excluding Full House
    4. Excluding Flush (By its nature)
    5. Excluding Straight (By its nature)
    6. Excluding Three of a Kind
    7. Excluding Two Pair
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    counter = collections.Counter(ranks)
    if [1,1,1,2] == sorted(counter.values()):
        return True
    else:
        return False

def is_high_card(cards):
    '''
    Input should be a 5-element list
    
    1. Excluding Royal Flush & Straight Flush
    2. Excluding Four of a Kind
    3. Excluding Full House
    4. Excluding Flush
    5. Excluding Straight
    6. Excluding Three of a Kind
    7. Excluding Two Pair
    8. Excluding One Pair
    '''
    suits = [i[-1] for i in cards]
    ranks = sorted([int(i[:-1]) for i in cards])
    counter = collections.Counter(ranks)
    if len(set(suits)) == 1:
        return False
    elif ranks == list(range(ranks[0], ranks[0] + 5)):
        return False
    elif ranks == [2,3,4,5,14]:
        return False
    elif [1,1,1,1,1] == sorted(counter.values()):
        return True
    else:
        return False

def eval_rank(cards):
    '''
    Input should be a 5-element list
    '''
    if is_high_card(cards):
        return 1
    elif is_one_pair(cards):
        return 2
    elif is_two_pair(cards):
        return 3
    elif is_3_of_a_kind(cards):
        return 4
    elif is_straight(cards):
        return 5
    elif is_flush(cards):
        return 6
    elif is_fullhouse(cards):
        return 7
    elif is_4_of_a_kind(cards):
        return 8
    elif is_straight_flush(cards):
        return 9
    else:
        print("Error in eval_diff_rank()")

def eval_straight_flush(a, b):
    '''
    Input should be two 5-element lists.
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a])
    ranks_b = sorted([int(i[:-1]) for i in b])
    if ranks_a[1] > ranks_b[1]:
        return a
    elif ranks_a[1] < ranks_b[1]:
        return b
    else:
        return "equal rank"
        
def eval_4_of_a_kind(a, b):
    '''
    Input should be two 5-element lists.
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a])
    ranks_b = sorted([int(i[:-1]) for i in b])
    if ranks_a[0] == ranks_a[3]:
        a_4 = ranks_a[0]
        a_kicker = ranks_a[4]
    else:
        a_4 = ranks_a[4]
        a_kicker = ranks_a[0]

    if ranks_b[0] == ranks_b[3]:
        b_4 = ranks_b[0]
        b_kicker = ranks_b[4]
    else:
        b_4 = ranks_b[4]
        b_kicker = ranks_b[0]

    if a_4 > b_4:
        return a
    elif a_4 < b_4:
        return b
    elif a_kicker > b_kicker:
        return a
    elif a_kicker < b_kicker:
        return b
    else:
        return "equal rank"

def eval_fullhouse(a, b):
    '''
    Input should be two 5-element lists.
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a])
    ranks_b = sorted([int(i[:-1]) for i in b])
    counter_a = collections.Counter(ranks_a)
    counter_b = collections.Counter(ranks_b)
    for k, v in counter_a.items():
        if v == 2:
            a_2 = k
        else:
            a_3 = k
    for k, v in counter_b.items():
        if v == 2:
            b_2 = k
        else:
            b_3 = k
    if a_3 > b_3:
        return a
    elif a_3 < b_3:
        return b
    elif a_2 > b_2:
        return a
    elif a_2 < b_2:
        return b
    else:
        return "equal rank"
    
def eval_flush(a, b):
    '''
    Input should be two 5-element lists.
    This is identical function of eval_high_card
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a], reverse=True)
    ranks_b = sorted([int(i[:-1]) for i in b], reverse=True)
    for i in range(5):
        if ranks_a[i] > ranks_b[i]:
            return a
        elif ranks_a[i] < ranks_b[i]:
            return b
        elif i == 4:
            return "equal rank"
        else:
            print("Error in eval_flush")

def eval_straight(a, b):
    '''
    Input should be two 5-element lists.
    This is identical function of eval_straight_flush
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a])
    ranks_b = sorted([int(i[:-1]) for i in b])
    if ranks_a[1] > ranks_b[1]:
        return a
    elif ranks_a[1] < ranks_b[1]:
        return b
    else:
        return "equal rank"
    
def eval_3_of_a_kind(a, b):
    '''
    Input should be two 5-element lists.
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a])
    ranks_b = sorted([int(i[:-1]) for i in b])
    counter_b = collections.Counter(ranks_b)
    a_ls = collections.Counter(ranks_a).most_common()
    b_ls = collections.Counter(ranks_b).most_common()
    a_3 = a_ls[0][0]
    b_3 = b_ls[0][0]
    a_kicker1, a_kicker2 = a_ls[1][0], a_ls[2][0]
    b_kicker1, b_kicker2 = b_ls[1][0], b_ls[2][0]
    if a_3 > b_3:
        return a
    elif a_3 < b_3:
        return b
    elif max(a_kicker1, a_kicker2) > max(b_kicker1, b_kicker2):
        return a
    elif max(a_kicker1, a_kicker2) < max(b_kicker1, b_kicker2):
        return b
    elif min(a_kicker1, a_kicker2) > min(b_kicker1, b_kicker2):
        return a
    elif min(a_kicker1, a_kicker2) < min(b_kicker1, b_kicker2):
        return b
    else:
        print("Error in eval_3_of_a_kind")
    
def eval_two_pair(a, b):
    '''
    Input should be two 5-element lists.
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a])
    ranks_b = sorted([int(i[:-1]) for i in b])
    a_ls = collections.Counter(ranks_a).most_common()
    b_ls = collections.Counter(ranks_b).most_common()
    if a_ls[1][0] > b_ls[1][0]:
        return a
    elif a_ls[1][0] < b_ls[1][0]:
        return b
    elif a_ls[0][0] > b_ls[0][0]:
        return a
    elif a_ls[0][0] < b_ls[0][0]:
        return b
    elif a_ls[2][0] > b_ls[2][0]:
        return a
    elif a_ls[2][0] < b_ls[2][0]:
        return b
    else:
        return "equal rank"
    
def eval_one_pair(a, b):
    '''
    Input should be two 5-element lists.
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a])
    ranks_b = sorted([int(i[:-1]) for i in b])
    a_ls = collections.Counter(ranks_a).most_common()
    b_ls = collections.Counter(ranks_b).most_common()
    if a_ls[0][0] > b_ls[0][0]:
        return a
    elif a_ls[0][0] < b_ls[0][0]:
        return b
    elif a_ls[3][0] > b_ls[3][0]:
        return a
    elif a_ls[3][0] < b_ls[3][0]:
        return b
    elif a_ls[2][0] > b_ls[2][0]:
        return a
    elif a_ls[2][0] < b_ls[2][0]:
        return b
    elif a_ls[1][0] > b_ls[1][0]:
        return a
    elif a_ls[1][0] < b_ls[1][0]:
        return b
    else:
        return "equal rank"

def eval_high_card(a, b):
    '''
    Input should be two 5-element lists.
    Output will be the bigger hand, or "equal rank"
    '''
    ranks_a = sorted([int(i[:-1]) for i in a], reverse=True)
    ranks_b = sorted([int(i[:-1]) for i in b], reverse=True)
    for i in range(5):
        if ranks_a[i] > ranks_b[i]:
            return a
        elif ranks_a[i] < ranks_b[i]:
            return b
        elif i == 4:
            return "equal rank"

def best_ranking_hand(list_of_hands):
    '''
    Input should be a multi-element list.
    Each element itself should be a list of 5 elements.

    Should be re-write
    '''
    fuct_ls = [eval_high_card,
               eval_one_pair,
               eval_two_pair,
               eval_3_of_a_kind,
               eval_straight,
               eval_flush,
               eval_fullhouse,
               eval_4_of_a_kind,
               eval_straight_flush]

    var1 = sorted(map(eval_rank, list_of_hands), reverse=True)
    var2 = sorted(list_of_hands, key=eval_rank, reverse=True)
    num = var1.count(var1[0])
    function = fuct_ls[var1[0] - 1]
    ranks = list(var2[:num])
    for i in range(len(ranks) - 1):
        if function(ranks[i], ranks[i + 1]) == ranks[i]:
            ranks[i], ranks[i + 1] = ranks[i + 1], ranks[i]
    return ranks[-1]

if __name__ == "__main__":
    def new_deck():
        '''
        Creat a standard deck of cards.
        Use 11,12,13,14 to replace J,Q,K,A respectively.
        Use "C" for club, ♣;
        Use "D" for diamond, ♦;
        Use "H" for heart, ♥;
        Use "S" for spade, ♠.
        '''
        rank = [i for i in range(2, 15)][::-1]
        suit = ['C', 'D', 'H', 'S']
        standard_deck = [str(i) + j for i in rank for j in suit]

        return tuple(standard_deck)

    def test_eval_rank(number):
        t_num = number
        counter = [0 for _ in range(9)]
        for _ in range(t_num):
            rank = eval_rank(random.sample(new_deck(), 5))
            counter[rank - 1] += 1
        pprint.pprint(counter, width = 5)
        print("----------")
        print(sum(counter))

    def test_eval_high_card(number):
        tmp = [random.sample(new_deck(), 5) for _ in range(number)]
        ls = filter(is_high_card, tmp)
        pprint.pprint(ls)
        print("")
        print("")
        for _ in range(len(ls)):
            for i in range(len(ls) - 1):
                if eval_high_card(ls[i], ls[i + 1]) == ls[i]:
                    ls[i], ls[i + 1] = ls[i + 1], ls[i]
            biggest = ls[-1]
            print(sorted(biggest, key=lambda x: int(x[:-1])))
            ls.pop()

    def test_best_ranking_hand(number):
        ls_of_hands = [random.sample(new_deck(), 5) for _ in range(number)]
        for _ in range(t_num):
            tmp = best_ranking_hand(ls_of_hands)
            print(tmp)
            ls_of_hands.remove(tmp)

    # test_eval_rank(10**4)
    # test_eval_straight_flush(10**5)
    test_eval_high_card(10)
    # test_best_ranking_hand(10**2)