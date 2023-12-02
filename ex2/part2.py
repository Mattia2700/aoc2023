import re

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]

total_sum = 0

for game_id, line in enumerate(lines):
    colon_index = line.index(':')
    line = line[colon_index+1:].strip()
    groups = [group.strip() for group in line.split(';')]

    required_colors = {"red": 0, "green": 0, "blue": 0}

    for group in groups:
        cubes = [cube.strip() for cube in group.split(',')]
        for cube in cubes:
            number, color = cube.split(' ')
            number = int(number)
            required_colors[color] = max(required_colors[color], number)

    power = required_colors["red"] * required_colors["green"] * required_colors["blue"]
    total_sum += power

print(total_sum)