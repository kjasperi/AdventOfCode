import sys
from functools import cmp_to_key
import time

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")
# print(data)



GRID = {}

num_rows = len(lines)
min_y = 1
max_y = num_rows
max_x = len(lines[0])
min_x = 0

def dump(G):
    for r in range(0, num_rows):
        line = ""
        for col in range(max_x):
            line += G[col, max_y - r]
        print(line)

for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        GRID[(col, max_y - row)] = ch

dump(GRID)
D = {"n": (0, 1), "w": (-1, 0), "s": (0, -1), "e":(1, 0)}

MEMO = {}

def tilt(G, dir):
    moved = True
    while moved:
        moved = False
        for coord in G:
            if G[coord] == "O":
                prev_coord = coord
                sliding = True
                while sliding:
                    new_coord = (prev_coord[0] + dir[0], prev_coord[1] + dir[1])

                    if new_coord not in G:
                        sliding = False
                    elif G[new_coord] == ".":
                        G[new_coord] = "O"
                        G[prev_coord] = "."
                        moved = True
                    else:
                        sliding = False
                    prev_coord = new_coord
    return G
    

def do_cycle(G):
    for dir in D:
        # print(D[dir])
        G = tilt(G, D[dir])
    return G

def calc_weight(G):
    weight = 0
    for coord in G:
        if G[coord] == "O":
            weight += coord[1]
    print(weight)

# Part1
G1 = tilt(GRID, D["n"])
calc_weight(G1)

# Part2
G = GRID
for i in range(1000):
    G = do_cycle(G)
    key = frozenset(G.items())
    if key in MEMO:
        diff = i - MEMO[key]
        if (1000000000 - i) % diff == 1:
            calc_weight(G)
            break
    MEMO[key] = i
