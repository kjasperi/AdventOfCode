import sys
from functools import cmp_to_key
from sortedcontainers import SortedDict

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

def extrapolate(history):
    history.reverse()
    # print(history)
    diff = 0
    for idx, seq in enumerate(history[1:]):
        diff = seq[0] - diff
        # print(diff)
        history[idx + 1].insert(0, diff)
    return history[-1][0]

def predict(seq): 
    history = [seq]
    pred = []
    while not all(v == 0 for v in seq):
        for idx, val in enumerate(seq):
            if idx + 1 == len(seq):
                seq = pred
                history.append(pred)
                pred = []
                break
            pred.append(seq[idx + 1] - val)
    return extrapolate(history)

ans = 0
for line in lines:
    seq = [int(x) for x in line.split()]
    print(seq)
    ans += predict(seq)
print(ans)