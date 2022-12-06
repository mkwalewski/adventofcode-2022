import re
from pprint import pprint

result = ''
two_star = True
boxes_small_input = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]
boxes_input = [
    ['B', 'W', 'N'],
    ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
    ['Q', 'H', 'Z', 'W', 'R'],
    ['W', 'D', 'V', 'J', 'Z', 'R'],
    ['S', 'H', 'M', 'B'],
    ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
    ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
    ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
    ['Z', 'W', 'M', 'S', 'C', 'D', 'J']
]

with open('input.txt') as file:
    if 'sample' in file.name:
        boxes = boxes_small_input
    else:
        boxes = boxes_input
    for line in file:
        string = line.rstrip()
        # finds = re.findall(r"(\s*)\[(\w+)\]", string)
        finds = re.findall(r"move (\d+) from (\d+) to (\d+)", string)
        if finds:
            how_many = int(finds[0][0])
            from_box = int(finds[0][1])
            to_box = int(finds[0][2])
            boxes_to_move = []
            for i in range(0, how_many):
                box = boxes[from_box - 1].pop(-1)
                boxes_to_move.append(box)
            if two_star:
                boxes_to_move.reverse()
            for i in range(0, len(boxes_to_move)):
                item = boxes_to_move[i]
                boxes[to_box - 1].append(item)
    for i in range(0, len(boxes)):
        result += boxes[i][-1]
    print(result)
