from pprint import pprint

total = 0

with open('input.txt') as file:
    for line in file:
        string = line.rstrip()
        first, second = string.split(',')
        firstMin, firstMax = [int(n) for n in first.split('-')]
        secondMin, secondMax = [int(n) for n in second.split('-')]
        if firstMin <= secondMax and firstMax >= secondMin:
            total += 1
        elif firstMin >= secondMax and firstMax <= secondMin:
            total += 1

print(total)
