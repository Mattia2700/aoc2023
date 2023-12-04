import re

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]
copies = {}
for index, line in enumerate(lines, 1):
    copies[index] = 1

for index, line in enumerate(lines, 1):
    cards = line.split(':')[1]
    winning, your = cards.split('|')
    winning = [int(card) for card in re.findall(r'\d+', winning)]
    your = [int(card) for card in re.findall(r'\d+', your)]
    count = 0
    for card in winning:
        if card in your:
            count += 1

    for i in range(index + 1, index + count + 1):
        for _ in range(copies[index]):
            copies[i] += 1
    
print(sum(copies.values()))