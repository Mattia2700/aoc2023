import re

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]

target = {"red": 12, "green": 13, "blue": 14}
valid_games = set()

for game_id, line in enumerate(lines):
    colon_index = line.index(':')
    line = line[colon_index+1:].strip()
    groups = [group.strip() for group in line.split(';')]

    valid = True

    for group in groups:
        cubes = [cube.strip() for cube in group.split(',')]
        for cube in cubes:
            number, color = cube.split(' ')
            number = int(number)
            if number > target[color]:
                valid = False
                break
        
        if not valid:
            break

    if valid:
        valid_games.add(game_id + 1)

print(sum(valid_games))
