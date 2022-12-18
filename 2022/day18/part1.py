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


def exposed_faces(all_cubes):
    exposed = 0

    for cube in all_cubes:
        for dx in [-1, 1]:
            if (cube[0] + dx, cube[1], cube[2]) not in all_cubes:
                exposed += 1
        for dy in [-1, 1]:
            if (cube[0], cube[1] + dy, cube[2]) not in all_cubes:
                exposed += 1

        for dz in [-1, 1]:
            if (cube[0], cube[1], cube[2] + dz) not in all_cubes:
                exposed += 1
    print(exposed)

exposed_faces(all_cubes)