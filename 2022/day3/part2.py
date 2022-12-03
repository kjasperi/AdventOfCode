import sys

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]

common = []

def get_common(ruck1, ruck2, ruck3):
    com = set()
    for let in ruck1:
        if let in ruck2 and let in ruck3:
            com.add(let)
    return com



for idx in range(0, len(lines), 3):
    com = get_common(lines[idx], lines[idx + 1], lines[idx + 2])
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