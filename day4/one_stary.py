from pprint import pprint

total = 0

with open('input.txt') as file:
    for line in file:
        string = line.rstrip()
        first, second = string.split(',')
        firstMin, firstMax = [int(n) for n in first.split('-')]
        secondMin, secondMax = [int(n) for n in second.split('-')]
        if firstMin <= secondMin and firstMax >= secondMax or firstMin >= secondMin and firstMax <= secondMax:
            total += 1

print(total)
