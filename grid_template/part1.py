import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

R = len(lines)
C = len(lines[0])

GRID = {}

def dump(grid):
    lines = []
    for r in range(R):
        line = ""
        for c in range(C):
            line += str(GRID[(r, c)])
        lines.append(line)
        print(line)

def add(posA, posB):
    return (posA[0] + posB[0], posA[1] + posB[1])

def sub(posA, posB):
    return (posA[0] - posB[0], posA[1] - posB[1])

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

UP_RIGHT = (-1, 1)
UP_LEFT = (-1, -1)
DOWN_RIGHT = (1, 1)
DOWN_LEFT = (1, -1)

DIRS = [UP, DOWN, RIGHT, LEFT, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT]

for r_idx, line in enumerate(lines):
    for c_idx, ch in enumerate(line):
        GRID[(r_idx, c_idx)] = ch

dump(GRID)
