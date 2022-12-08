import sys

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

grid = []

for line in lines:
    l = [int(t) for t in line]
    grid.append(l)

def get_view_dist(home, tree_line):
    dist = 0
    for tree in tree_line:
        dist += 1
        if tree >= home:
            break
    return dist


def look_right(G, row, col):
    home = G[row][col]

    tree_line = []
    for c_d in range(col + 1, len(G[0])):
        tree_line.append(G[row][c_d])

    return get_view_dist(home, tree_line)

def look_left(G, row, col):
    home = G[row][col]

    tree_line = []
    for c_d in range(col - 1, -1, -1):
        tree_line.append(G[row][c_d])
    return get_view_dist(home, tree_line)

def look_up(G, row, col):
    home = G[row][col]

    tree_line = []
    for r_d in range(row - 1, -1, -1):
        tree_line.append(G[r_d][col])
    return get_view_dist(home, tree_line)

def look_down(G, row, col):
    home = G[row][col]

    tree_line = []
    for r_d in range(row + 1, len(G[0])):
        tree_line.append(G[r_d][col])

    return get_view_dist(home, tree_line)
def is_vis(G, row, col):
    h = G[row][col]
    score = 1
    score *= look_right(G, row, col)

    score *= look_left(G, row, col)

    score *= look_up(G, row, col)

    score *= look_down(G, row, col)
    return score


scores = []
for r in range(1, len(grid) -1):
    for c in range(1, len(grid[0]) - 1):

        scores.append(is_vis(grid, r, c))
        #reak
        
    

print(max(scores))
# print("asdfsadf")
# print(is_vis(grid, 3, 2))

