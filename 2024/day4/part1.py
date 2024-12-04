import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

grid = {}

ROWS = len(lines)
COLS = len(lines[0])


for row, l in enumerate(lines):
    for col, c in enumerate(l):
        grid[(row, col)] = c



WORD = 'XMAS'

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def search_dir(r, c, dir):
    r_d = dir[0]
    c_d = dir[1]

    next_pos = (r, c)
    for i in range(4):
        if next_pos not in grid:
            return False
        
        if grid[next_pos] != WORD[i]:
            return False
        
        next_pos = (next_pos[0] + r_d, next_pos[1] + c_d)

    return True


def search(r, c):
    # This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
    print("search", r, c)
    num_found = 0
    for dir in DIRS:
        if search_dir(r, c, dir):
            num_found += 1

    return num_found


result = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[(r, c)] == 'X':
            result += search(r, c)
print(result)