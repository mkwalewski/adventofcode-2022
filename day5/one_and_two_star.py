import re
import math
from pprint import pprint

result = ''
two_star = True
boxes = []
boxesDict = {}

with open('input.txt') as file:
    for line in file:
        string = line.rstrip()
        finds = re.findall(r"(\s*)\[(\w+)\]", string)
        if finds:
            row = 0
            total_rest = 0
            for find in finds:
                row += 1
                if row == 1:
                    spaces = len(find[0])
                else:
                    spaces = len(find[0]) - 1
                curr_rest = math.floor(spaces / 4)
                total_rest += curr_rest
                index = (row - 1) + total_rest
                for i in range(0, index + 1):
                    if i not in boxesDict:
                        boxesDict[i] = []
                boxesDict[index].append(find[1])
        if not string:
            for i in boxesDict:
                boxArray = boxesDict[i]
                boxArray.reverse()
                boxes.append(boxArray)
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
