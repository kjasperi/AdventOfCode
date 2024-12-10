import sys
import cmath 
import copy

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

DIRS = [UP, DOWN, RIGHT, LEFT]

for r_idx, line in enumerate(lines):
    for c_idx, ch in enumerate(line):
        GRID[(r_idx, c_idx)] = int(ch)

dump(GRID)

start_pos = []
end_pos = []
# hiking trail is any path that starts at height 0, ends at height 9,
for pos in GRID:
    if GRID[pos] == 0:
        start_pos.append(pos)
    if GRID[pos] == 9:
        end_pos.append(pos)
    
print(start_pos, end_pos)

def get_pos_neigh(grid, pos):
    neigh = []
    for dir in DIRS:
        test_n = add(pos, dir)
        if test_n in GRID:
            if GRID[test_n] == GRID[pos] + 1:
                neigh.append(test_n)
    return neigh

def search(grid, start_pos):
    visited = []

    to_visit = [start_pos]
    
    while to_visit:
        current_pos = to_visit[0]
        to_visit = to_visit[1:]
        visited.append(current_pos)
        # print(current_pos)
        for neigh in get_pos_neigh(grid, current_pos):
            if neigh not in visited and neigh not in to_visit:
                to_visit.append(neigh)
    score = 0
    for v in visited:
        # print(grid[v])
        if grid[v] == 9:
            score += 1

    return score

score = 0
for p in start_pos:
    score += search(copy.deepcopy(GRID), p)
print(score)