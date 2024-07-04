import re
import itertools

def range_overlapping(x, y):
    if x.start == x.stop or y.start == y.stop:
        return False
    return x.start <= y.stop and y.start <= x.stop

def get_overlapping_range(x: range, lst: list):
    for y in lst:
        if range_overlapping(x, y):
            return y
    return None

def compute_not_mapped(seeds, mapped):
    not_mapped = []
    for si, seed in enumerate(seeds):
        print(si, seed)
        for mi, m in mapped:
            if si == mi:
                if len(not_mapped) > 0:
                    sd_to_check = get_overlapping_range(m, not_mapped)
                    if sd_to_check is None:
                        sd_to_check = seed
                    else:
                        not_mapped.remove(sd_to_check)
                    lst_to_check = m
                else: 
                    sd_to_check = seed
                    lst_to_check = m
                
                print("Computing new ranges for {} and {}".format(sd_to_check, lst_to_check))
                new_not_mapped = [x for x,y in compute_new_ranges(sd_to_check, lst_to_check) if not y]
                print(new_not_mapped)
                not_mapped.extend(new_not_mapped)
            
    return not_mapped

def compute_new_ranges(x: range, y: range, diff=0):

    if not range_overlapping(x, y):
        return None
    
    new_range = [range(max(x.start, y.start)+diff, min(x.stop, y.stop)+diff)]

    if x.stop > y.stop:
        new_range.append(range(y.stop, x.stop))

    if x.start < y.start:
        new_range.append(range(x.start, y.start))

    return new_range
    
def simplify_ranges(ranges):
    return list(set([x for x in ranges if x.start != x.stop]))

with open('/home/dhilab-mattia/Desktop/aoc2023/ex5/input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]

seeds = []

for start, step in re.findall(r'(\d+) (\d+)', lines[0]):
    seeds.append(range(int(start), int(start) + int(step)))

new_seeds = []
mapped = set()

for mapping in lines[1:]:
    if not any(m.isnumeric() for m in mapping.split()):

        for idx, seed in enumerate(seeds):
            if idx not in mapped:
                new_seeds.append(seed)

        if len(new_seeds) > 0:
            seeds = new_seeds.copy()
            new_seeds = []
            mapped.clear()

        continue

    dest, start, step = re.findall(r'(\d+)', mapping)
    dest, start, step = int(dest), int(start), int(step)

    dst_range = range(dest, dest + step)
    src_range = range(start, start + step)

    for si, seed in enumerate(seeds):
        x = compute_new_ranges(seed, src_range, dst_range.start - src_range.start)
        if x is not None and si not in mapped:
            mapped.add(si)
            new_seeds.extend(x)

for idx, seed in enumerate(seeds):
    if idx not in mapped:
        new_seeds.append(seed)

    if len(new_seeds) > 0:
        seeds = new_seeds.copy()

# remove seeds that start from 0
# seeds = [seed for seed in seeds if seed.start != 0]

# seeds = sorted(seeds, key=lambda x: x.start)

print(min(seeds, key=lambda x: x.start).start)
