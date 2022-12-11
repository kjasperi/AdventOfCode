import sys
import cmath 
from collections import defaultdict
import queue

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

X = 1
cycle = 0
X_hist = []
for line in lines:
    X_hist.append(X)

    if line == 'noop':
        cycle += 1
    else:
        X_hist.append(X)

        _, val = line.split()
        cycle += 2
        X += int(val)


def draw(X_hist):
    row = 0
    line = []
    width = 40

    for pixel_idx, x in enumerate(X_hist):
        if pixel_idx >= width * row:
            row += 1
            print(''.join(line))
            line = []
        hor_pixel_pos = pixel_idx % width
        if abs(hor_pixel_pos - x) <= 1:
            line.append('#')
        else:

            line.append('.')
    print(''.join(line))



s_20th = 20 * X_hist[20 - 1] 
s_60th = 60 * X_hist[60 - 1] 
s_100th = 100 * X_hist[100 - 1] 
s_140th = 140 * X_hist[140 - 1] 
s_180th = 180 * X_hist[180 - 1] 
s_220th = 220 * X_hist[220 - 1]


ans = s_20th + s_60th + s_100th + s_140th + s_180th + s_220th

print(ans)
draw(X_hist)
