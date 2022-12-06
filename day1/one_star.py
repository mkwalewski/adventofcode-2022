from pprint import pprint

max = 0
total = 0

with open('input.txt') as file:
    for line in file:
        string = line.rstrip()
        if string:
            total += int(string)
        else:
            if total > max:
                max = total
            total = 0
    if total > 0 and total > max:
        max = total
    print(max)
