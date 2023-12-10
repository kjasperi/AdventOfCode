import sys
from functools import cmp_to_key
from sortedcontainers import SortedDict

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")
print(data)
GRID = {}
S = set()
start = (0,0)
for idx, l in enumerate(lines):
    for cdx, ch in enumerate(l):
        
        GRID[(idx, cdx)] = ch
        if ch == 'S':
            start = (idx, cdx)

VALID_R = ["-", "S", "7", "J"]
VALID_L = ["-", "S", "L", "F"]
VALID_U = ["|", "S", "7", "F"]
VALID_D = ["|", "S", "J", "L"]

pos = start
steps = 0
S.add(pos)
moves = []
tot_r = 0
tot_u = 0
while True:
    right = (pos[0], pos[1] + 1)
    left = (pos[0], pos[1] - 1)
    up = (pos[0] - 1, pos[1])
    down = (pos[0] + 1, pos[1])

    steps += 1
    if (right in GRID) and (GRID[right] in VALID_R) and (GRID[pos] in VALID_L) and (not right in S):
        pos = right
    elif (left in GRID) and (GRID[left] in VALID_L)  and (GRID[pos] in VALID_R) and (not left in S):
        pos = left
    elif (up in GRID) and (GRID[up] in VALID_U) and (GRID[pos] in VALID_D) and (not up in S):
        pos = up
    elif (down in GRID) and (GRID[down] in VALID_D) and (GRID[pos] in VALID_U) and (not down in S):
        pos = down
    else:
        break
    S.add(pos)
    moves.append(pos)

def dump(G):
    rows = len(lines)
    cols = len(lines[0])
    for r in range(rows):
        line = ""
        for col in range(cols):
            line += G[r, col]
        print(line)

prev_move = moves[0]

sys.setrecursionlimit(10000)
moves.append(start)
def fillGrid(to_mark, ch):
    if to_mark in GRID and to_mark not in S:
        GRID[to_mark] = ch
        S.add(to_mark)
    else:
        return
    # print("Fill")
    neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for n in neigh:
        p = (to_mark[0] + n[0], to_mark[1] + n[1])
        fillGrid(p, ch)

for move in moves:
    if prev_move == move:
        continue
    row_diff = move[0] - prev_move[0]
    col_diff = move[1] - prev_move[1]

    to_markX = (move[0] + col_diff, move[1] - row_diff)
    to_markY = (move[0] - col_diff, move[1] + row_diff)
    
    fillGrid(to_markX, "X")
    fillGrid(to_markY, "Y")

    to_markX = (prev_move[0] + col_diff, prev_move[1] - row_diff)
    to_markY = (prev_move[0] - col_diff, prev_move[1] + row_diff)
    
    fillGrid(to_markX, "X")
    fillGrid(to_markY, "Y")
    prev_move = move

    # dump(GRID)
for move in moves:
    GRID[move] = "."
# print(moves)
dump(GRID)
x = 0
y = 0
for pos in GRID:
    if GRID[pos] == "X":
        x += 1
    if GRID[pos] == "Y":
        y += 1
print("Part1:", steps // 2)
print("X:", x)
print("Y:", y)
