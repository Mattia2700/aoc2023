import itertools
import functools

with open('/home/dhilab-mattia/Desktop/aoc2023/ex7/input.txt') as f:
    lines = f.readlines()

strength = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J','Q', 'K', 'A']

def value(hands, card1, card2):
    hand1 = hands[card1[0]]
    hand2 = hands[card2[0]]

    for c1, c2 in zip(hand1,hand2):
        if strength.index(c1) < strength.index(c2):
            return -1
        elif strength.index(c1) > strength.index(c2):
            return 1
        
    return 0

def is_pair(counts):
    # check if there is a pair (not two pair)
    pairs = 0
    for card in counts:
        if counts[card] == 2:
            pairs += 1
    return pairs == 1

def is_two_pair(counts):
    # check if there are two pairs
    pairs = 0
    for card in counts:
        if counts[card] == 2:
            pairs += 1
    return pairs == 2

def is_three_of_a_kind(counts):
    # check if there is three of a kind
    for card in counts:
        if counts[card] == 3:
            return True
    return False

def is_full_house(counts):
    # check if there is a full house
    return is_pair(counts) and is_three_of_a_kind(counts)

def is_four_of_a_kind(counts):
    # check if there is four of a kind
    for card in counts:
        if counts[card] == 4:
            return True
    return False

def is_five_of_a_kind(counts):
    # check if there is five of a kind
    for card in counts:
        if counts[card] == 5:
            return True
    return False

def check(counts):
    if is_five_of_a_kind(counts):
        return 6
    elif is_four_of_a_kind(counts):
        return 5
    elif is_full_house(counts):
        return 4
    elif is_three_of_a_kind(counts):
        return 3
    elif is_two_pair(counts):
        return 2
    elif is_pair(counts):
        return 1
    else:
        return 0

# filter out empty lines
lines = [line.strip() for line in lines]

hands = {}
ranks = {}
bids = {}

for idx, line in enumerate(lines):
    hand, bid = line.split(' ')
    counts = {}
    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    hands[idx] = hand
    ranks[idx] = check(counts)
    bids[idx] = int(bid)

ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)

# group by value
groups = {}
for rank, group in itertools.groupby(ranks, lambda x: x[1]):
    groups[rank] = list(group)

cmp = functools.partial(value, hands)

# compare
for k,v in groups.items():
    # order by value
    groups[k] = sorted(v, key=functools.cmp_to_key(cmp))

total = 0
rank = idx + 1

for group in groups.values():
    for hand in reversed(group):
        idx = hand[0]
        total += (rank*bids[idx])
        rank -= 1

print(total)
