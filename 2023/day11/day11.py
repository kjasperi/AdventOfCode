import sys
from functools import cmp_to_key
from sortedcontainers import SortedDict
import time

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")
print(data)

def solve(expansion):
    gal_in_rows = set()
    gal_in_cols = set()


    for idx, l in enumerate(lines):
        for cdx, ch in enumerate(l):
            if ch == "#":
                gal_in_rows.add(idx)
                gal_in_cols.add(cdx)

    GAL = []
    row = 0

    for idx, l in enumerate(lines):
        col = 0
        if idx not in gal_in_rows:
            row += expansion
        for cdx, ch in enumerate(l):
            if cdx not in gal_in_cols:
                col += expansion
            if ch == "#":
                GAL.append((row, col))
            col += 1
        row += 1


    sum = 0
    for g1 in range(len(GAL)):
        for g2 in range(g1 + 1, len(GAL)):
            G1 = GAL[g1]
            G2 = GAL[g2]
            dist = abs(G1[0] - G2[0]) + abs(G1[1] - G2[1])
            sum += dist
    return sum
print("P1", solve(1))
print("P2", solve(999999))

