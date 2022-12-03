import sys

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]

common = []

for line in lines:
    com = set()

    comp1 = line[0:int(len(line)/2)]

    comp2 = line[int(len(line)/2) : ]

    for let in comp1:
        if let in comp2:
            com.add(let)
    for let in com:
        common.append(let)

def calc_points(let):

    if let.islower():
        return ord(let)-96
    else:
        return ord(let) - 64 + 26

points = 0
for let in common:
    points += calc_points(let)
print(points)