from pprint import pprint

length = 4

with open('input.txt') as file:
    for line in file:
        string = line.rstrip()
        for i in range(0, len(string) - 4):
            word = string[i:i+length]
            word_unique = ''.join(set(word))
            if len(word_unique) == length:
                print(i + length)
                break
