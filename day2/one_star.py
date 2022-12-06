from pprint import pprint

total = 0
opponentDict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
myDict = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
scoreDict = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

def get_winner(o, m):
    if (o + 1) % 3 == m:
        return 6 #me win
    elif o == m:
        return 3 #draw
    else:
        return 0 #opponent win

def get_score(opponent, me):
    score = scoreDict[me]
    score += get_winner(scoreDict[opponent] - 1, scoreDict[me] - 1)
    return score

with open('input.txt') as file:
    for line in file:
        opponent, me = line.rstrip().split()
        score = get_score(opponentDict[opponent], myDict[me])
        total += score

print(total)
