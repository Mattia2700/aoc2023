import re

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]

times = [int(t) for t in re.findall(r'(\d+)', lines[0])]
spaces = [int(t) for t in re.findall(r'(\d+)', lines[1])]

results=[]

for time,space in zip(times,spaces):
    partial = []

    for t in range(time):
        speed = t
        runtime = time - t
        space = speed*runtime
        partial.append(space)

    results.append(partial)

total = 1

for index, r in enumerate(results):
    # count elements that are greater than the space
    count = len([x for x in r if x > spaces[index]])
    total *= count

print(total)