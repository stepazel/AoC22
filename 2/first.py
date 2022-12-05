text = open('input', 'r')
shapeScores = {'X': 1, 'Y': 2, 'Z': 3}

# Rock:     A/X
# Paper:    B/Y
# Scissors: C/Z
# Lose == 0
# Draw == 3
# Win == 6

totalScore = 0


def get_outcome(opponent_shape, my_shape):
    if my_shape == 'X':
        if opponent_shape == 'A':
            return 3
        if opponent_shape == 'B':
            return 0
        if opponent_shape == 'C':
            return 6

    if my_shape == 'Y':
        if opponent_shape == 'A':
            return 6
        if opponent_shape == 'B':
            return 3
        if opponent_shape == 'C':
            return 0

    if my_shape == 'Z':
        if opponent_shape == 'A':
            return 0
        if opponent_shape == 'B':
            return 6
        if opponent_shape == 'C':
            return 3


# First part
while False:
    line = text.readline()
    if not line:
        break

    opponentShape = line[0]
    myShape = line[2]

    outcome = get_outcome(opponentShape, myShape)
    totalScore += shapeScores[myShape] + get_outcome(opponentShape, myShape)

print(totalScore)

# X == LOSE
# Y == DRAW
# Z == WIN

# Rock:     A/X
# Paper:    B/Y
# Scissors: C/Z

from enum import Enum


class Shape(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


class MyShape(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class Tactic(Enum):
    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'


def get_shape_for_tactic(opponent_shape, tactic):
    if tactic == Tactic.LOSE:
        if opponent_shape == Shape.ROCK:
            return MyShape.SCISSORS
        if opponent_shape == Shape.PAPER:
            return MyShape.ROCK
        if opponent_shape == Shape.SCISSORS:
            return MyShape.PAPER

    if tactic == Tactic.DRAW:
        if opponent_shape == Shape.ROCK:
            return MyShape.ROCK
        if opponent_shape == Shape.PAPER:
            return MyShape.PAPER
        if opponent_shape == Shape.SCISSORS:
            return MyShape.SCISSORS

    if tactic == Tactic.WIN:
        if opponent_shape == Shape.ROCK:
            return MyShape.PAPER
        if opponent_shape == Shape.PAPER:
            return MyShape.SCISSORS
        if opponent_shape == Shape.SCISSORS:
            return MyShape.ROCK


tacticScores = {'X': 0, 'Y': 3, 'Z': 6}
shapeScoress = {MyShape.ROCK: 1, MyShape.PAPER: 2, MyShape.SCISSORS: 3}
tactics = {'X': Tactic.LOSE, 'Y': Tactic.DRAW, 'Z': Tactic.WIN}
oponentShapes = {'A': Shape.ROCK, 'B': Shape.PAPER, 'C': Shape.SCISSORS}

score = 0
count = 0
while True:
    count += 1
    line = text.readline()
    if not line:
        break

    opponentShape = line[0]
    tactic = line[2]
    tacticEnum = tactics[tactic]
    tacticScore = tacticScores[tactic]
    shapeEnum = oponentShapes[opponentShape]
    myShape = get_shape_for_tactic(shapeEnum, tacticEnum)
    shapeScore = shapeScoress[myShape]
    score += tacticScore + shapeScore

print(score)
