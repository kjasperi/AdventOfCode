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

anti_set = set()
for r_id, row in enumerate(lines):
    for c_id, ch in enumerate(row):
        # print(ch)
        if ch == ".":
            continue
        if ch not in antennas:
            antennas[ch] = []
        antennas[ch].append((r_id, c_id))

for ant in antennas:
    positions = antennas[ant]

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            p1 = positions[i]
            p2 = positions[j]
            delta = (p1[0] - p2[0], p1[1] - p2[1])
            anti_A = (p1[0] + delta[0], p1[1] + delta[1])
            anti_B = (p2[0] - delta[0], p2[1] - delta[1])
            if anti_A[0] >= 0 and anti_A[0] < R and anti_A[1] >= 0 and anti_A[1] < C:
                anti_set.add(anti_A)
            if anti_B[0] >= 0 and anti_B[0] < R and anti_B[1] >= 0 and anti_B[1] < C:
                anti_set.add(anti_B)

print(len(anti_set))

