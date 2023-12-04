import sys
import re

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

sum = 0
for row, line  in enumerate(lines):
    line = line.split(":")[1:]
    winning_num, own_num = line[0].split('|') 
    winning_num = winning_num.split()
    own_num = own_num.split()
    score = 0
    for win in winning_num:
        if win in own_num:
            if score == 0:
                score = 1
            else:
                score *= 2
    sum += score
print(sum)

