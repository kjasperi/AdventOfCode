import sys

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]

def expand(section):
    start, stop = section.split('-')
    return {s for s in range(int(start), int(stop) + 1)}

p1 = 0
p2 = 0

for line in lines:
    group1, group2 = line.split(',')
    set1 = expand(group1)
    set2 = expand(group2)
    if set1.issubset(set2) or set2.issubset(set1):
        p1 += 1
    
    if set1.intersection(set2):
        p2 += 1

print(p1)
print(p2)
