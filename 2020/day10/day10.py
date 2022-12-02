import sys
import collections


def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()


adapters = [int(line.rstrip()) for line in get_lines_from_file()]

adapters.insert(0, 0)
adapters.sort()

#### PART 1 #####
start_jolt = 0
max_diff = 3

num_diff = {}
prev_adapt = start_jolt
for adapt in adapters:
    diff = adapt - prev_adapt

    if not diff in num_diff:
        num_diff[diff] = 0
    num_diff[diff] += 1

    prev_adapt = adapt

num_diff[3] += 1

print(num_diff[3]*num_diff[1])

#### PART 2 #####

memo = {}


def get_combos(target_idx):
    if target_idx in memo:
        return memo[target_idx]

    ans = 0

    if target_idx == 0:
        return 1

    for i in range(1, 4):
        new_idx = target_idx - i
        if new_idx >= 0 and adapters[target_idx] - adapters[new_idx] <= max_diff:
            ans += get_combos(new_idx)
    memo[target_idx] = ans
    return ans


print(get_combos(len(adapters) - 1))


##### PART 2 första lösningen ######


class Node:
    def __init__(self):
        self.next_nodes = []
        self.ways_to_get_here = 0

        
def get_num_ways(adapter):
    idx = adapters.index(adapter) + 1

    if idx >= len(adapters):
        return []

    next_adapter = adapters[idx]
    ans = []
    while adapters[idx] - adapter <= max_diff:
        idx += 1
        ans.append(next_adapter)
        if idx >= len(adapters):
            return ans
        next_adapter = adapters[idx]
    return ans


all_nodes = {}
for adapt in adapters:
    node = Node()
    node.next_nodes = get_num_ways(adapt)

    all_nodes[adapt] = node

# Traverse graph
all_nodes[0].ways_to_get_here = 1
for node_id in all_nodes:
    node = all_nodes[node_id]
    for child_node_id in node.next_nodes:
        child_node = all_nodes[child_node_id]
        child_node.ways_to_get_here += node.ways_to_get_here


print(node.ways_to_get_here)