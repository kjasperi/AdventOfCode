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

DIRS_A = [(1, 1), (-1, -1)]
DIRS_B = [(-1, 1), (1, -1)]

def search_dir(r, c, dir):
    r_d = dir[0]
    c_d = dir[1]

    found = True
    back_pos = (r - r_d, c - c_d)
    for_pos = (r + r_d, c + c_d)

    if for_pos in grid:
        if grid[for_pos] != 'S':
            found = False
    else:
        return 0
    if back_pos in grid:
        if grid[back_pos] != 'M':
            found = False
    else:
        return 0

    return found


def search(r, c):
    # This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
    num_found_a = 0
    num_found_b = 0
    
    for dir in DIRS_A:
        if search_dir(r, c, dir):
            num_found_a += 1
    for dir in DIRS_B:
        if search_dir(r, c, dir):
            num_found_b += 1

    return num_found_a > 0 and num_found_b > 0


result = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[(r, c)] == 'A':
            if search(r, c):
                result += 1

print(result)