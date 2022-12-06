from pprint import pprint

data = []
total = 0

with open('input.txt') as file:
    for line in file:
        string = line.rstrip()
        if string:
            total += int(string)
        else:
            data.append(total)
            total = 0
    if total > 0:
        data.append(total)
    data.sort(reverse=True)
    total = data[0] + data[1] + data[2]
    print(total)
