import re

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip().replace(" ", "") for line in lines if line.strip()]

time = int(re.findall(r'(\d+)', lines[0])[0])
space = int(re.findall(r'(\d+)', lines[1])[0])

results=[]

for t in range(time):
    speed = t
    runtime = time - t
    s = speed*runtime
    if s > space:
        results.append(space)

# count elements that are greater than the space
print(len(results))

