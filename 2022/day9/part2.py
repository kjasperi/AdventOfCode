import sys

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

print(lines)

rope_x = [0 for x in range(10)]
rope_y = [0 for y in range(10)]

visited = set()

def update_tail(h_x, h_y, t_x, t_y):
    dx = h_x - t_x
    dy = h_y - t_y
    if abs(dx) <= 1 and abs(dy) <= 1:
        #print("touching")
        return t_x, t_y

    sx = 0
    sy = 0

    if dx == 0:
        sy = int(dy / abs(dy))

    elif dy == 0:
        sx = int(dx / abs(dx))
    else: # diagonal
        #print("diagonal")
        sx = int(dx / abs(dx))
        sy = int(dy / abs(dy))

    t_x += sx
    t_y += sy
    #print("test")
    return [t_x, t_y]

def do_steps(rope_x, rope_y, dx, dy, steps):
    for _ in range(steps):
        print("---------------")
        rope_x[0] += dx
        rope_y[0] += dy
        tail = update_tail(rope_x[0], rope_y[0] , rope_x[1], rope_y[1])
        rope_x[1] = tail[0]
        rope_y[1] = tail[1]
            
        for knot_idx in range(1, len(rope_x) - 1):
            h_x = rope_x[knot_idx]
            h_y = rope_y[knot_idx]
            t_x = rope_x[knot_idx + 1]
            t_y = rope_y[knot_idx + 1]
            
            tail = update_tail(h_x, h_y, t_x, t_y)
            #print(tail)
            rope_x[knot_idx] = h_x

            rope_y[knot_idx] = h_y

            rope_x[knot_idx + 1] = tail[0]
            rope_y[knot_idx + 1] = tail[1]
            
            # print("head:",head_x, head_y)
            # print("tail:",tail_x, tail_y)
        print("head: ", rope_x[0], rope_y[0])
        print("tail: ", rope_x[1], rope_y[1])
        visited.add((rope_x[-1], rope_y[-1]))

for line in lines:
    dir, steps = line.split()
    steps = int(steps)
    if dir == 'R':
        do_steps(rope_x, rope_y, 1, 0, steps)
    if dir == 'L':
        do_steps(rope_x, rope_y, -1, 0, steps)
    if dir == 'U':
        do_steps(rope_x, rope_y, 0, 1, steps)
    if dir == 'D':
        do_steps(rope_x, rope_y, 0, -1, steps)
print(len(visited))
#print(visited)