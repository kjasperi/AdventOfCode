import sys

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

print(lines)

grid = []

for line in lines:
    l = [int(t) for t in line]
    grid.append(l)

print(grid[1][2])

def is_vis(G, row, col):
    h = G[row][col]
    #print(h)
    vr = True
    vl = True
    vd = True
    vu = True
    for r_d in range(row - 1, -1, -1):
        h_d = G[r_d][col]
        # print("'")
        # print(h_d)
        if h_d >= h:
            vl = False

    
    for r_d in range(row + 1, len(G), 1):
        h_d = G[r_d][col]
        if h_d >= h:
            vr = False
    for c_d in range(col - 1, -1, -1):
        h_d = G[row][c_d]
        if h_d >= h:
            vd = False
    #print("---")
    for c_d in range(col + 1, len(G[0]), 1):
        h_d = G[row][c_d]
        #print(h_d)
        if h_d >= h:
            vu = False
    # print(vl)
    # print(vr)
    # print(vd)
    # print(vu)
    # print("VIS: " + str(r) + " " + str(c))
    # if vl or vr or vd or vu :
    #     print("VIS: " + str(r) + " " + str(c))
    return vl or vr or vd or vu 

p1 = 0
for r in range(1, len(grid) -1):
    for c in range(1, len(grid[0]) - 1):

        if (is_vis(grid, r, c)):
            p1 += 1
print(len(grid) * 4 - 4)
print(p1 + len(grid) * 4 - 4)