import sys
import re
from collections import defaultdict

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

sum = 0
num_copies = defaultdict()
for card, line  in enumerate(lines):
    card_num = card + 1
    if not card_num in num_copies:
        num_copies[card_num] = 0
    num_copies[card_num] += 1

    line = line.split(":")[1:]
    winning_num, own_num = line[0].split('|') 
    winning_num = winning_num.split()
    own_num = own_num.split()
    score = 0
    matching = []

    for win in winning_num:
        if win in own_num:
            matching.append(win)
        
    for n, m in enumerate(matching):
        if not card_num + 1 + n in num_copies:
            num_copies[card_num + 1 + n] = 0
        num_copies[card_num + 1 + n] += num_copies[card_num]

for cop in num_copies:
    sum += num_copies[cop]
print(sum)

