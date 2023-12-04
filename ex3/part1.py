import re

def check_symbol(text):
    if re.match(r'[^a-zA-Z\d\.]', text):
        return True
    return False

def is_number(text):
    return re.match(r'\d', text)

def check_around(lines, i, j):
    valid = False
    if i > 0:
        valid |= check_symbol(lines[i - 1][j])
    if i < len(lines) - 1:
        valid |= check_symbol(lines[i + 1][j])
    if j > 0:
        valid |= check_symbol(lines[i][j - 1])
    if j < len(lines[i]) - 1:
        valid |= check_symbol(lines[i][j + 1])
    if i > 0 and j > 0:
        valid |= check_symbol(lines[i - 1][j - 1])
    if i > 0 and j < len(lines[i]) - 1:
        valid |= check_symbol(lines[i - 1][j + 1])
    if i < len(lines) - 1 and j > 0:
        valid |= check_symbol(lines[i + 1][j - 1])
    if i < len(lines) - 1 and j < len(lines[i]) - 1:
        valid |= check_symbol(lines[i + 1][j + 1])
    return valid

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]
lines = [list(line) for line in lines]

total = 0

for i, line in enumerate(lines):
    accumulator = []
    valid = False
    for j, char in enumerate(line):
        if is_number(char):
            accumulator.append(char)
            valid |= check_around(lines, i, j)
        else:
            if valid:
                total += int(''.join(accumulator))
            accumulator = []
            valid = False
    
    if valid:
        total += int(''.join(accumulator))

print(total)