import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

all_cubes = set()
for line in lines:
    x, y, z = [int(el) for el in line.split(",")]

    coord = (x, y, z)
    all_cubes.add(coord)


def exposed_faces(all_cubes, water_cubes):
    exposed = 0

    for cube in all_cubes:
        for dx in [-1, 1]:
            if (cube[0] + dx, cube[1], cube[2]) not in all_cubes and (cube[0] + dx, cube[1], cube[2])  in water_cubes:
                exposed += 1
        for dy in [-1, 1]:
            if (cube[0], cube[1] + dy, cube[2]) not in all_cubes and (cube[0], cube[1] + dy, cube[2])  in water_cubes:
                exposed += 1

        for dz in [-1, 1]:
            if (cube[0], cube[1], cube[2] + dz) not in all_cubes and (cube[0], cube[1], cube[2] + dz) in water_cubes:
                exposed += 1
    print(exposed)

def get_min_max(all_cubes):
    min_x = 99
    min_y = 99
    min_z = 99

    max_x = 0
    max_y = 0
    max_z = 0
    for cube in all_cubes:
        x, y, z = cube
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if z < min_z:
            min_z = z
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z
    min_coord = (min_x - 1, min_y - 1, min_z - 1)
    max_coord = (max_x + 1, max_y + 1, max_z + 1)
    assert min_coord not in all_cubes
    assert max_coord not in all_cubes

    return min_coord, max_coord


def fill_with_water(all_cubes, min_coord, max_coord):
    water_cubes = set()
    cubes_to_check = []
    cubes_to_check.append(min_coord)
    while cubes_to_check:
        active_cube = cubes_to_check.pop()

        if active_cube not in all_cubes and active_cube not in water_cubes:
            water_cubes.add(active_cube)

            for dx in [-1, 1]:
                new_x = active_cube[0] + dx
                if  new_x <= max_coord[0] and new_x >= -1:
                    cubes_to_check.append((new_x, active_cube[1], active_cube[2]))

            for dy in [-1, 1]:
                new_y = active_cube[1] + dy
                if  new_y <= max_coord[1] and new_y >= -1:
                    cubes_to_check.append((active_cube[0], new_y, active_cube[2]))
            for dz in [-1, 1]:
                new_z = active_cube[2] + dz 
                if new_z <= max_coord[2] and new_z>= -1:
                    cubes_to_check.append((active_cube[0], active_cube[1], new_z))
    return water_cubes

min_coord, max_coord = get_min_max(all_cubes)
water_cubes = fill_with_water(all_cubes, min_coord, max_coord)
exposed_faces(all_cubes, water_cubes)
