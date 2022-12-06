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
    for line in file:
        string = line.rstrip()
        half = int(len(string) / 2)
        first = string[0:half]
        second = string[half:]
        added = {}
        for i in range(0, len(first)):
            char = first[i]
            if first[i] in second and char not in added:
                added[char] = 1
                total += mapping[char]

print(total)
