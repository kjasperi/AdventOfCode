import sys
import numpy as np


def get_lines_from_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines


def parse_input():
    input_lines = get_lines_from_file()
    height = len(input_lines)
    width = len(input_lines[0])
    world_map = np.zeros((height, width))

    row = 0
    for line in input_lines:
        col = 0
        for ch in line:
            if ch == '#':
                # trees are represented as 1
                world_map[row][col] = 1
            col = col + 1
        row = row + 1
    return world_map


def traverse_map(world_map, slope):
    start_position = np.array([0, 0])
    check_position = start_position
    num_of_rows = world_map.shape[0]

    num_of_cols = world_map.shape[1]

    total_trees = 0
    while True:
        check_position = check_position + slope

        row = check_position[0]
        col = check_position[1] % num_of_cols

        if row >= num_of_rows:
            return total_trees
        feature = world_map[row][col]

        total_trees = total_trees + feature


world_map = parse_input()

all_slopes = []

# Right 1, down 1.
slope = np.array([1, 1])
all_slopes.append(slope)

# Right 3, down 1. (This is the slope you already checked.)
slope = np.array([1, 3])
all_slopes.append(slope)

# Right 5, down 1.
slope = np.array([1, 5])
all_slopes.append(slope)

# Right 7, down 1.
slope = np.array([1, 7])
all_slopes.append(slope)

# Right 1, down 2.
slope = np.array([2, 1])
all_slopes.append(slope)

trees = []
for slope in all_slopes:
    total_trees = traverse_map(world_map, slope)
    trees.append(total_trees)

print(np.prod(trees))
