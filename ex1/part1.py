import re

with open('input.txt') as f:
    lines = f.readlines()

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]

sum = 0

for line in lines:
    numbers = re.findall(r'\d+?', line)
    if len(numbers) < 2:
        numbers = [numbers[0], numbers[0]]
    else:
        numbers = [numbers[0], numbers[-1]]
    numbers = [int(number) for number in numbers
    ]
    sum += numbers[0] * 10 + numbers[1]

print(sum)
    
