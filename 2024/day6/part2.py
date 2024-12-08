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

def rotate(current_dir):
    if current_dir == UP:
        current_dir = RIGHT
    elif current_dir == RIGHT:
        current_dir = DOWN

    elif current_dir == DOWN:
        current_dir = LEFT

    elif current_dir == LEFT:
        current_dir = UP
    return current_dir

def find_cand(grid, pos, current_dir):
    vis = set()
    while run:
        vis.add(pos)
        # print(VISITED_DIR)
        # dump(GRID)
        grid[pos] = '.'
        while True:

            test_dir = current_dir
            test_pos = get_next_pos(pos, test_dir)
            # print(POS, test_dir, test_pos)
            if test_pos not in grid:
                return vis
            if grid[test_pos] == '#':
                current_dir = rotate(current_dir)
            else:
                pos = test_pos
                break

def test_grid(grid, pos, current_dir):
    VISITED = set()
    VISITED_DIR = set()


    while run:
        VISITED.add(pos)
        VISITED_DIR.add((pos, current_dir))
        # print(VISITED_DIR)
        # dump(GRID)
        grid[pos] = '.'
        while True:

            test_dir = current_dir
            test_pos = get_next_pos(pos, test_dir)
            # print(POS, test_dir, test_pos)
            if test_pos not in grid:
                return True, len(VISITED)
            if (test_pos, current_dir) in VISITED_DIR:
                print("loop found")
                return False, 0
            if grid[test_pos] == '#':
                current_dir = rotate(current_dir)
            else:
                pos = test_pos
                break
def solve():
    pos = POS
    current_dir = CURRENT_DIR
    loops = 0
    for cand in find_cand(GRID, POS, CURRENT_DIR):
        test_pos = cand
        if GRID[test_pos] == ".":
            grid = copy.deepcopy(GRID)
            grid[test_pos] = '#'
            succ, ans = test_grid(grid, POS, CURRENT_DIR)
            # dump(grid)
            if not succ:
                print(test_pos)
                loops += 1

    print(loops)
    
solve()
# print(len(VISITED))
# print(VISITED)
# for v in VISITED:
#     GRID[v] = 'X'
# dump(GRID)
# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.