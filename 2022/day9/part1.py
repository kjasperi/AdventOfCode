import sys

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

print(lines)

head_x = 0
head_y = 0

tail_x = 0
tail_y = 0
visited = set()

def update_tail():
    global tail_x
    global tail_y
    dx = head_x - tail_x
    dy = head_y - tail_y
    if abs(dx) <= 1 and abs(dy) <= 1:
        print("touching")
        return 

    sx = 0
    sy = 0

    if dx == 0:
        sy = int(dy / abs(dy))

    elif dy == 0:
        sx = int(dx / abs(dx))
    else: # diagonal
        print("diagonal")
        sx = int(dx / abs(dx))
        sy = int(dy / abs(dy))

    tail_x += sx
    tail_y += sy

def do_steps(dx, dy, steps):
    global head_x
    global head_y
    for _ in range(steps):
        head_x += dx
        head_y += dy
        print("---------------")
        update_tail()
        visited.add((tail_x, tail_y))
        print("head:",head_x, head_y)
        print("tail:",tail_x, tail_y)


for line in lines:
    dir, steps = line.split()
    steps = int(steps)
    if dir == 'R':
        do_steps(1, 0, steps)
    if dir == 'L':
        do_steps(-1, 0, steps)
    if dir == 'U':
        do_steps(0, 1, steps)
    if dir == 'D':
        do_steps(0, -1, steps)
print(len(visited))