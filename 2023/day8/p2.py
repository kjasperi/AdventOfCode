import sys
from functools import cmp_to_key

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

def test_start(start):
    visited = set()
    steps = 0
    pos = start
    while True:
        for idx, dir in enumerate(header):
            # print(pos)

            if dir == 'R':
                pos = D[pos][1]
            elif dir == 'L':
                pos = D[pos][0]

            else:
                assert(False)
            # print(dir)
            steps += 1
            if pos[-1] == 'Z':
                return steps
            # if (pos, idx) in visited:
                # print(pos)
                # print(visited)
                # print(len(visited))
                # return steps 
            # visited.add((pos, idx))
import math
from functools import reduce
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
def part2(starts):

    positions = starts
    steps_to_end = {}
    sol = {}
    to_test = {}
    for s in starts:
        sol[s] = test_start(s)
        to_test[s] = test_start(s)
    print(to_test)
    while list(to_test.values())[:-1] != list(to_test.values())[1:]:
        smallest = ''
        temp_smallest = 99999999999999
        for d in to_test:
            if to_test[d] < temp_smallest:
                smallest = d
                temp_smallest = to_test[d]
        to_test[smallest] += sol[smallest]
        # print(to_test)
    print(to_test)
        



starts = []
for d in D:
    if d[-1] == 'A':
        starts.append(d)
print("***********************")
print(starts)
res = part2(starts)
print(res)