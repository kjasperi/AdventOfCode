import sys
from functools import cmp_to_key
import time

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data().strip()

def hash(str):
    val = 0
    for ch in str:
        # Determine the ASCII code for the current character of the string.
        # print(ord(ch))
        # Increase the current value by the ASCII code you just determined.
        val += ord(ch)
        # Set the current value to itself multiplied by 17.
        val *= 17
        # Set the current value to the remainder of dividing itself by 256.
        val = val % 256
    return val
seq = data.split(",")

sum = 0
BOXES = {}
LABELS = {}
# If the operation character is a dash (-), go to the relevant box and remove the lens with the given 
# label if it is present in the box. Then, move any remaining lenses as far forward in the box as they 
# can go without changing their order, filling any space made by removing the indicated lens. 
# (If no lens in that box has the given label, nothing happens.)
def dash(label, box_num):
    if label not in LABELS:
        return
    box_num = LABELS[label]

    if box_num == -1:
        return
    contents = BOXES[box_num]
    new_content = []
    for l in contents:
        if l[0] != label:
            new_content.append(l)
    BOXES[box_num] = new_content
    LABELS[label] = -1

def op_eq(label, focal, box_num):
    if box_num not in BOXES:
        BOXES[box_num] = []
    contents = BOXES[box_num]
    new_content = []
    added = False
    for l in contents:
        if l[0] != label:
            new_content.append(l)
        else:
            new_content.append((label, focal))
            added = True
    if not added:
        new_content.append((label, focal))
    BOXES[box_num] = new_content
    LABELS[label] = box_num

  
for step in seq:
    if "=" in step:
        label, focal = step.split("=")
        focal = int(focal)
        box_num = hash(label)
        op_eq(label, focal, box_num)

    else: 
        label, focal = step.split("-")
        dash(label, box_num)

# PART 1
sum = 0
for step in seq:
    sum += hash(step)
print("Part1:", sum)
# PART 2
sum = 0
for box_num in BOXES:
    box = BOXES[box_num]
    for slot in range(len(box)):
        sum += (box_num + 1) * (slot + 1) * box[slot][1]
print("Part2:", sum)