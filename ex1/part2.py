import re

with open('input.txt') as f:
    lines = f.readlines()

mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# filter out empty lines
lines = [line.strip() for line in lines if line.strip()]

sum = 0

for line in lines:
    for word in mapping.keys():
        if word in line:
            line = line.replace(word, word[0]+mapping[word]+word[-1])
    print(line)
    numbers = re.findall(r'\d+?', line)
    for n in numbers:
        if n in mapping:
            numbers[numbers.index(n)] = mapping[n]
    if len(numbers) < 2:
        numbers = [numbers[0], numbers[0]]
    else:
        numbers = [numbers[0], numbers[-1]]
    numbers = [int(number) for number in numbers
    ]
    sum += numbers[0] * 10 + numbers[1]

print(sum)
    
