from pprint import pprint

total = 0
cards = ['Rock', 'Paper', 'Scissors']
opponentDict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
strategyDict = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
strategyScoreDict = {'Lose': 0, 'Draw': 3, 'Win': 6}
scoreDict = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

def get_card(number):
    if number < 0:
        return cards[-1]
    if number == len(cards):
        return cards[0]
    return cards[number]

def predict_card(opponent, strategy):
    if strategy == 'Draw':
        return opponent
    elif strategy == 'Lose':
        return get_card(scoreDict[opponent] - 2)
    elif strategy == 'Win':
        return get_card(scoreDict[opponent])

def calc_score(me, strategy):
    score = scoreDict[me]
    score += strategyScoreDict[strategy]
    return score

with open('input.txt') as file:
    for line in file:
        opponent, me = line.rstrip().split()
        myCard = predict_card(opponentDict[opponent], strategyDict[me])
        score = calc_score(myCard, strategyDict[me])
        total += score

print(total)
