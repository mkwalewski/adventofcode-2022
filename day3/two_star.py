from pprint import pprint

index = 1
total = 0
mapping = {}

for i in range(ord('a'), ord('z') + 1):
    mapping[chr(i)] = index
    index += 1

for i in range(ord('A'), ord('Z') + 1):
    mapping[chr(i)] = index
    index += 1

with open('input.txt') as file:
    group = []
    group_count = 0
    for line in file:
        group_count += 1
        string = line.rstrip()
        group.append(string)
        if group_count == 3:
            added = {}
            for i in range(0, len(group[0])):
                char = group[0][i]
                if char in group[1] and char in group[2] and char not in added:
                    added[char] = 1
                    total += mapping[char]
            group = []
            group_count = 0

print(total)
