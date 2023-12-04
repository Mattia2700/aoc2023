import re

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]

total = 0

for line in lines:
    cards = line.split(':')[1]
    winning, your = cards.split('|')
    winning = [int(card) for card in re.findall(r'\d+', winning)]
    your = [int(card) for card in re.findall(r'\d+', your)]
    count = 0
    for card in winning:
        if card in your:
            count += 1

    if count > 0:
        total += 2 ** (count - 1)

print(total)
    