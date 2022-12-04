import sys

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

    

lines = [line.rstrip() for line in get_lines_from_file()]

def expand(section):
    expand_set = set()
    start, stop = section.split('-')
    for i in range(int(start), int(stop) + 1):
        expand_set.add(i)
    return expand_set

p1 = 0
p2 = 0

for line in lines:
    group1, group2 = line.split(',')
    set1 = expand(group1)
    set2 = expand(group2)
    if set1.issubset(set2):
        p1 += 1
    elif set2.issubset(set1):
        p1 += 1
    
    inter = set1.intersection(set2)
    if len(inter):
        p2 += 1

print(p1)
print(p2)
