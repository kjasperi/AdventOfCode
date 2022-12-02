import sys
import numpy as np

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]
#print(lines)

d_east = [1, 0]
d_west = [-1, 0]
d_north = [0, 1]
d_south = [0, -1]

headings = [d_east, d_south, d_west, d_north]
rotations = 0

current_position = [0, 0]
current_head = headings[rotations]

## PART 1
for line in lines:
    action = line[0]
    value = int(line[1:])

    # Action F means to move forward by the given value in the direction the ship is currently facing
    if action == 'F':
        current_position[0] += current_head[0]*value
        current_position[1] += current_head[1]*value
    # Action N means to move north by the given value.
    elif action == 'N':
        current_position[0] += d_north[0]*value
        current_position[1] += d_north[1]*value
    # Action S means to move south by the given value.
    elif action == 'S':
        current_position[0] += d_south[0]*value
        current_position[1] += d_south[1]*value
    # Action E means to move east by the given value.
    elif action == 'E':
        current_position[0] += d_east[0]*value
        current_position[1] += d_east[1]*value
    # Action W means to move west by the given value.
    elif action == 'W':
        current_position[0] += d_west[0]*value
        current_position[1] += d_west[1]*value
    # Action L means to turn left the given number of degrees.
    elif action == 'L':
        rotations -= int(value / 90)
    # Action R means to turn right the given number of degrees.
    elif action == 'R':
        rotations += int(value / 90)
    current_head = headings[rotations % len(headings)]

print(abs(current_position[0]) + abs(current_position[1]))

print("PART 2")
current_position = [0, 0]

waypoint = [10, 1]

for line in lines:
    #print("-"*80)
    action = line[0]
    value = int(line[1:])
    #print(action, value)

    rotations = 0

    # Action F means to move forward by the given value in the direction the ship is currently facing
    if action == 'F':
        current_position[0] += waypoint[0]*value
        current_position[1] += waypoint[1]*value
    # Action N means to move north by the given value.
    elif action == 'N':
        waypoint[0] += d_north[0]*value
        waypoint[1] += d_north[1]*value
    # Action S means to move south by the given value.
    elif action == 'S':
        waypoint[0] += d_south[0]*value
        waypoint[1] += d_south[1]*value
    # Action E means to move east by the given value.
    elif action == 'E':
        waypoint[0] += d_east[0]*value
        waypoint[1] += d_east[1]*value
    # Action W means to move west by the given value.
    elif action == 'W':
        waypoint[0] += d_west[0]*value
        waypoint[1] += d_west[1]*value
    # Action L means to turn left the given number of degrees.
    elif action == 'L':
        rotations = -int(value/ 90)
        
    # Action R means to turn right the given number of degrees.
    elif action == 'R':
        rotations = int(value / 90)
        
    for _ in range(rotations % 4):
        waypoint = [waypoint[1], -waypoint[0]]


    #print(turn)
    #print(current_position)
    #print("waypoint", waypoint)

print(abs(current_position[0]) + abs(current_position[1]))