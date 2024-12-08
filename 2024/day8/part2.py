import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")
R = len(lines)
C = len(lines[0])

antennas = {}

anti_nodes = {}
anti_set = set()
for r_id, row in enumerate(lines):
    for c_id, ch in enumerate(row):
        if ch == ".":
            continue
        if ch not in antennas:
            antennas[ch] = []
        antennas[ch].append((r_id, c_id))

for ant in antennas:
    positions = antennas[ant]
    if ant not in anti_nodes:
        anti_nodes[ant] = []  
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            p1 = positions[i]
            p2 = positions[j]
            delta = (p1[0] - p2[0], p1[1] - p2[1])

            while p1[0] >= 0 and p1[0] < R and p1[1] >= 0 and p1[1] < C:
                anti_set.add(p1)
                p1 = (p1[0] + delta[0], p1[1] + delta[1])

            while p2[0] >= 0 and p2[0] < R and p2[1] >= 0 and p2[1] < C:
                anti_set.add(p2)
                p2 = (p2[0] - delta[0], p2[1] - delta[1])


print(len(anti_set))

