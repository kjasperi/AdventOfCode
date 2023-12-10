import sys
from functools import cmp_to_key
from sortedcontainers import SortedDict

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")


# Five of a kind, where all five cards have the same label: AAAAA
def isFiveOfKind(hand):
    first = hand[0]

    for card in hand:
        if card != first:
            return False
    return True

# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
def isFourOfKind(hand):
    card_dict = {}
    for card in hand:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    for t in card_dict:
        if card_dict[t] == 4:

            return True
    return False
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
def isFullHouse(hand):
    card_dict = {}
    for card in hand:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    big_house = ''
    small_house = ''
    for t in card_dict:
        if card_dict[t] == 3:
            big_house = t
        if card_dict[t] == 2:
            small_house = t
    if big_house and small_house:
        return True
    return False
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
def isThreeOfKind(hand):
    card_dict = {}
    for card in hand:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    for t in card_dict:
        if card_dict[t] == 3:

            return True
    return False
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
def isTwoPair(hand):
    card_dict = {}
    for card in hand:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    pairs = []
    for t in card_dict:
        if card_dict[t] == 2:
            pairs.append(t)
    if len(pairs) == 2:
        return True
    return False
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
def isOnePair(hand):
    card_dict = {}
    for card in hand:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    pairs = []
    for t in card_dict:
        if card_dict[t] == 2:
            pairs.append(t)
    if len(pairs) == 1:
        return True
    return False
# High card, where all cards' labels are distinct: 23456
def isHighCard(hand):
    card_dict = {}
    for card in hand:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    pairs = []
    singles = []
    for t in card_dict:
        if card_dict[t] == 2:
            pairs.append(t)
        if card_dict[t] == 1:
            singles.append(t)
    if len(singles) == 5:
        return True
    return False





hands_with_score = SortedDict()

for n, line in enumerate(lines):
    hand, bid = line.split()
    bid = int(bid)
    print(hand)
    score = 0
    if isFiveOfKind(hand):
        print("isFiveOfKind")
        score = 1

    elif isFourOfKind(hand):
        print("isFourOfKind")
        score = 2

    elif isFullHouse(hand):
        print("isFullHouse")
        score = 3

    elif isThreeOfKind(hand):
        print("isThreeOfKind")
        score = 4

    elif isTwoPair(hand):
        print("isTwoPair")
        score = 5

    elif isOnePair(hand):
        print("isOnePair")
        score = 6

    elif isHighCard(hand):
        score = 7
        print("isHighCard")
    
    if not score in hands_with_score:
        hands_with_score[score] = []
    hands_with_score[score].append((hand, bid)) 

print(hands_with_score)

priot = {'A' : 1, 'K' : 2, 'Q' : 3, 'J': 4, 'T':5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}

def tie_cmp(h_a, h_b):
    a, bid_a = h_a
    b, bid_b = h_b
    if not a:
        return 0
    if priot[a[0]] > priot[b[0]]:
        return 1
    elif priot[a[0]] < priot[b[0]]:
        return -1
    return tie_cmp((a[1:], 0), (b[1:], 0))
    

cmp_items_py3 = cmp_to_key(tie_cmp)

final_sorted_hands = []
for score in hands_with_score:
    sub_list = hands_with_score[score]
    print(sub_list)
    sub_list.sort(key=cmp_items_py3)
    print(sub_list)
    final_sorted_hands += sub_list
    # sorted(sub_list, key=tie_cmp)
final_sorted_hands.reverse()
print(final_sorted_hands)
tot_score = 0
for idx, hand in enumerate(final_sorted_hands):
    print(hand)
    tot_score += hand[1] * (idx + 1)

print(tot_score)