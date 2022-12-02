import sys

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()


lines = [line.rstrip() for line in get_lines_from_file()]

cubes = {}
active_cubes = set()

min_x = 0
min_y = 0
min_z = 0
min_w = 0

max_x = 8
max_y = 8
max_z = 0
max_w = 0

dimensions = 4

#print(lines)
z = 0
w = 0
for y, line in enumerate(lines):
    #print(y, line)
    for x, cube in enumerate(line):
        state = False
        if cube == "#":
            state = True
            active_cubes.add((x,y,z,w))
        cubes[(x,y,z,w)] = state


def get_neighbors(coord):
    x, y, z, w = coord

    neighbors = []
    for d_x in [-1, 0, 1]:
        for d_y in [-1, 0, 1]:
            for d_z in [-1, 0, 1]:
                for d_w in [-1, 0, 1]:
                    c = (x+d_x, y+d_y, z+d_z, w+d_w)
                    if c != coord:
                        neighbors.append(c)
    return neighbors


def num_active_neighboors(coord):
    x, y, z, w = coord
    #print("-----")
    #print(x, y, z)
    neighbors = get_neighbors(coord)
    num_active = 0
    for c in neighbors:
        if c in cubes:
            #print(c)
            #print(cubes[c])
            if cubes[c]:
                num_active += 1
                #print(coord, num_active)

    return num_active


def expand_space():
    global min_x
    global min_y
    global min_z
    global min_w

    global max_x
    global max_y
    global max_z
    global max_w

    min_x -= 1
    min_y -= 1
    min_z -= 1
    min_w -= 1

    max_x += 1
    max_y += 1
    max_z += 1
    max_w += 1

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                for w in range(min_w, max_w + 1):
                    if (x, y, z, w) not in cubes:
                        cubes[(x, y, z, w)] = False

    #for x in range(min_x, max_x):


def update_cube_states():
    global cubes
    expand_space()

    cubes_to_change = {}
    cubes_to_check = set()
    for cube in active_cubes:
        cubes_to_check.add(cube)

    for cube in active_cubes:
        neighbors = get_neighbors(cube)
        for c in neighbors:
            cubes_to_check.add(c)

    for cube_coord in cubes_to_check:
        cube_active = cubes[cube_coord]
        #print(cube_coord, cube)
        
        num_active = num_active_neighboors(cube_coord)
        #print(cube_coord, num_active)
        if cube_active:
            if not (num_active == 2 or num_active == 3):
                cubes_to_change[cube_coord] = False
                #print(cube_coord, "Becomes inactive")
                active_cubes.remove(cube_coord)

        else: #inactive
            if num_active == 3:
                #print(cube_coord, "Becomes active")
                cubes_to_change[cube_coord] = True
                active_cubes.add(cube_coord)

    for coord in cubes_to_change:
        cubes[coord] = cubes_to_change[coord]

#print(cubes)
for i in range(6):
    print(i)
    update_cube_states()

print(len(active_cubes))

