import sys
from functools import cmp_to_key
from sortedcontainers import SortedDict

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
header, lines = data.split("\n\n")
lines = lines.split("\n")

D = {}
for line in lines:
    s = line.split()
    source = s[0]
    dst_l = s[2][1:-1]
    dst_r = s[3][:-1]
    if source not in D:
        D[source] = (dst_l, dst_r)

pos = 'AAA'
print(D)
steps = 0


while True:
    for dir in header:
        print(pos)
        if pos == 'ZZZ':
            print(steps)
            assert(False)
        elif dir == 'R':
            pos = D[pos][1]
        elif dir == 'L':
            pos = D[pos][0]

        else:
            assert(False)
        print(dir)
        steps += 1 