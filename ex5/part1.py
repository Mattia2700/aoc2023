import re

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]

seeds = [int(n) for n in re.findall(r'(\d+)', lines[0])]

new_seeds = []
mapped = set()
not_mapped = []

for mapping in lines[1:]:
    if not any(m.isnumeric() for m in mapping.split()):
        for s in seeds:
            if s in not_mapped:
                new_seeds.append(s)

        if len(new_seeds) != 0:
            seeds = new_seeds
            new_seeds = []
            mapped.clear()

        continue

    dest, start, step = re.findall(r'(\d+)', mapping)
    dest, start, step = int(dest), int(start), int(step)


    for s in seeds:
        if 0 <= s - start < step:
            new_seeds.append(s + dest - start)
            mapped.add(s)

    not_mapped = [s for s in seeds if s not in mapped]

for s in seeds:
    if s in not_mapped:
        new_seeds.append(s)

    if len(new_seeds) != 0:
        seeds = new_seeds

print(min(seeds))