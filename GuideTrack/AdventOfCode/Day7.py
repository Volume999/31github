import sys
from regex import regex
from icecream import ic
import collections
from enum import Enum
from functools import cmp_to_key
sys.stdout = open('output.txt','wt')
sys.stdin = open('input.txt','rt')

ic.disable()

class CardCombo(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    FIVE_OF_A_KIND = 9

def transform_hand(hand):
    res = []
    for c in hand:
        if c == "T":
            res.append(10)
        elif c == "J":
            res.append(-1)
        elif c == "Q":
            res.append(12)
        elif c == "K":
            res.append(13)
        elif c == "A":
            res.append(14)
        else:
            res.append(int(c))
    return res

def parse_input():
    data = sys.stdin.readlines()
    sets = []
    for game in data:
        hand, bid = game.split()
        sets.append((hand, bid))
    return sets

def find_combo(hand):
    ic(hand)
    jokers = hand.count(-1)
    c = collections.Counter(hand)
    del c[-1]
    ic(jokers)
    counts = sorted(c.values(), reverse=True)
    if not counts:
        counts = [0]
    ic(c)
    if counts[0] + jokers == 5:
        return CardCombo.FIVE_OF_A_KIND
    if counts[0] + jokers == 4:
        return CardCombo.FOUR_OF_A_KIND
    if counts[0] + jokers == 3 and counts[1] == 2:
        return CardCombo.FULL_HOUSE
    if counts[0] + jokers == 3:
        return CardCombo.THREE_OF_A_KIND
    if counts[0] == 2 and (jokers or counts[1] == 2):
        return CardCombo.TWO_PAIR
    if counts[0] == 2 or jokers:
        return CardCombo.PAIR
    return CardCombo.HIGH_CARD

def compare_hands(hand1, hand2):
    if find_combo(hand1[0]).value > find_combo(hand2[0]).value:
        return 1
    if find_combo(hand1[0]).value < find_combo(hand2[0]).value:
        return -1
    for (c1, c2) in zip(hand1[0], hand2[0]):
        if c1 > c2:
            return 1
        if c1 < c2:
            return -1
    return 0


def solve():
    sets = parse_input()
    sets = list(map(lambda k: (transform_hand(k[0]), k[1]), sets))
    sets.sort(key=cmp_to_key(compare_hands))
    res = 0
    for i, (hand, bid) in enumerate(sets):
        print(i, hand, bid)
        res += (i + 1) * int(bid)
    print(res)
    # print(list(sorted(sets, key=cmp_to_key(compare_hands))))



def main():
    solve()

if __name__ == "__main__":
    main()