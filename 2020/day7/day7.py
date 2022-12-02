import sys
import re
import time


def lines_from_arg():
    with open(sys.argv[1]) as inf:
        return inf.readlines()


class Bag:
    def __init__(self):
        self.parents = []
        self.children = []

    def add_child(self, child, qty):
        if child not in self.children:
            for _ in range(qty):
                self.children.append(child)

    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)


def parse_line(line):
    parent_col = re.match(r'(.+) bags contain', line)[1]

    if parent_col not in all_bags:
        parent_bag = Bag()
        all_bags[parent_col] = parent_bag

    child_pattern = re.compile(r'(\d) (.+?) bag')

    for qty, col in child_pattern.findall(line):
        if col not in all_bags:
            bag = Bag()
            bag.add_parent(parent_col)
            all_bags[col] = bag
        else:
            bag = all_bags[col]
            bag.add_parent(parent_col)

        all_bags[parent_col].add_child(col, int(qty))


all_bags = {}
lines = lines_from_arg()

for line in lines:
    parse_line(line)

##### PART 1 ######
current_bag = all_bags["shiny gold"]

parents = current_bag.parents

all_parents = []
while len(parents) > 0:
    next_parent = parents.pop().strip()
    all_parents.append(next_parent)
    current_bag = all_bags[next_parent]
    parents += current_bag.parents

print(len(set(all_parents)))

##### PART 2 ######
start_time = time.perf_counter()
current_bag = all_bags["shiny gold"]

children = current_bag.children.copy()

num_of_bags = 0
while len(children) > 0:
    next_child = children.pop()
    current_bag = all_bags[next_child]
    children += current_bag.children

    num_of_bags += 1
    
print(num_of_bags)
print((time.perf_counter() - start_time) * 1000)
##### PART 2 recursive ######
start_time = time.perf_counter()

def get_bag_size(bag):
    size = 1
    for child in bag.children:
        size += get_bag_size(all_bags[child])
    return size


target_bag = all_bags["shiny gold"]

print(get_bag_size(target_bag) - 1)
print((time.perf_counter() - start_time) * 1000)
