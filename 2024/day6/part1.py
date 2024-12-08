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
VISITED = set()

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

POS = ()
CURRENT_DIR = UP
for r_idx, line in enumerate(lines):
    for c_idx, ch in enumerate(line):
        GRID[(r_idx, c_idx)] = ch
        if ch == '^':
            POS = (r_idx, c_idx)

def dump(grid):
    lines = []
    for r in range(R):
        line = ""
        for c in range(C):
            line += GRID[(r, c)]
        lines.append(line)
        print(line)
    # print(lines)
    print("**********************************")
# print(GRID)
dump(GRID)
run = True

def get_next_pos(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

def rotate():
    global CURRENT_DIR

    if CURRENT_DIR == UP:
        CURRENT_DIR = RIGHT
    elif CURRENT_DIR == RIGHT:
        CURRENT_DIR = DOWN

    elif CURRENT_DIR == DOWN:
        CURRENT_DIR = LEFT

    elif CURRENT_DIR == LEFT:
        CURRENT_DIR = UP
    print(CURRENT_DIR)


def solve():
    global POS
    while run:
        VISITED.add(POS)
        # print(POS)
        # dump(GRID)
        GRID[POS] = '.'
        find_next_pos = True
        while True:

            test_dir = CURRENT_DIR
            test_pos = get_next_pos(POS, test_dir)
            # print(POS, test_dir, test_pos)
            if test_pos not in GRID:
                return
            if GRID[test_pos] == '#':
                rotate()
            else:
                POS = test_pos
                break
        GRID[POS] = '^'
solve()
print(len(VISITED))
# print(VISITED)
for v in VISITED:
    GRID[v] = 'X'
# dump(GRID)
# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.