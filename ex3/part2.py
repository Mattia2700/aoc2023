import re
import itertools

def is_number(text):
    return re.match(r'\d', text)

def filter_adjacents(indexes):

    for i, j in indexes:
        for k, l in indexes:
            if i == k and j == l:
                continue
            if i == k and abs(j - l) == 1:
                indexes.remove((k, l))
            if j == l and abs(i - k) == 1:
                indexes.remove((k, l))

    return indexes

def check_around(lines, i, j):
    indexes = []
    count_1, count_2 = [], []
    if i > 0 and is_number(lines[i - 1][j]):
        indexes.append((i - 1, j))
        count_1.append((i - 1, j))
    if i < len(lines) - 1 and is_number(lines[i + 1][j]):
        indexes.append((i + 1, j))
        count_2.append((i + 1, j))
    if j > 0 and is_number(lines[i][j - 1]):
        indexes.append((i, j - 1))
    if j < len(lines[i]) - 1 and is_number(lines[i][j + 1]):
        indexes.append((i, j + 1))
    if i > 0 and j > 0 and is_number(lines[i - 1][j - 1]):
        indexes.append((i - 1, j - 1))
        count_1.append((i - 1, j - 1))
    if i > 0 and j < len(lines[i]) - 1 and is_number(lines[i - 1][j + 1]):
        indexes.append((i - 1, j + 1))
        count_1.append((i - 1, j + 1))
    if i < len(lines) - 1 and j > 0 and is_number(lines[i + 1][j - 1]):
        indexes.append((i + 1, j - 1))
        count_2.append((i + 1, j - 1))
    if i < len(lines) - 1 and j < len(lines[i]) - 1 and is_number(lines[i + 1][j + 1]):
        indexes.append((i + 1, j + 1))
        count_2.append((i + 1, j + 1))

    if len(count_1) > 1 and len(count_2) > 1:
        count_1, count_2 = sorted(count_1), sorted(count_2)
        keep_1, keep_2  = count_1[1], count_2[1]
        extra_indexes = list(itertools.chain.from_iterable([count_1, count_2]))
        extra_indexes.remove(keep_1)
        extra_indexes.remove(keep_2)

        for idx in extra_indexes:
            indexes.remove(idx)

    indexes = filter_adjacents(indexes)

    return indexes

with open('/home/dhilab-mattia/Desktop/aoc2023/ex3/input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]
lines = [list(line) for line in lines]

count = 0

for line in lines:
    for char in line:
        if char == '*':
            count += 1

print(count)

valid_indexes = []
total = 0

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '*':
            new_indexes = check_around(lines, i, j)
            if len(new_indexes) == 2:
                valid_indexes.append(new_indexes)
            # else:
            #     print(''.join(lines[i-1][j-1:j+2]))
            #     print(''.join(lines[i][j-1:j+2]))
            #     print(''.join(lines[i+1][j-1:j+2]))
            #     print()

numbers = {
    (i, j): None
    for i, j in itertools.chain.from_iterable(valid_indexes)
}


for i, line in enumerate(lines):
    accumulator = []
    valid = False
    store_index = None
    for j, char in enumerate(line):
        if is_number(char):
            accumulator.append(char)
            for idx in itertools.chain.from_iterable(valid_indexes):
                if idx == (i, j):
                    store_index = idx
                    valid |= True
                    break
        else:
            if valid:
                numbers[store_index] = int(''.join(accumulator))
            accumulator = []
            valid = False
    
    if valid:
        numbers[store_index] = int(''.join(accumulator))

for pairs in valid_indexes:
    total += numbers[pairs[0]] * numbers[pairs[1]]

print(total)