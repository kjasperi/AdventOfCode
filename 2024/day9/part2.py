import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

nums = [int(x) for x in lines[0]]

is_lengths = True

disk_map = []
id = 0

for num in nums:
    if is_lengths:
        for i in range(num):
            disk_map.append(str(id))
        id += 1

    else: #space
        for i in range(num):
            disk_map.append('.')

    is_lengths = not is_lengths

def find_block_to_move(disk_map, rev_it, prev_num):
    len_to_move = 0
    num_to_move = '.'

    while True:
        if rev_it == 0:
            return 0, 0
        if disk_map[rev_it] != '.' and disk_map[rev_it] != prev_num:
            num_to_move = disk_map[rev_it]
            break
        rev_it -= 1

    while disk_map[rev_it] == num_to_move and rev_it >= 0:
        len_to_move += 1
        rev_it -= 1
    return num_to_move, len_to_move, rev_it + 1

def find_free_space(disk_map, max_pos, space_need):
    # print(disk_map)

    free_space = 0
    free_pos = 0
    it = 0
    counting = False
    while it < max_pos:
        if disk_map[it] == '.':
            free_space += 1
            if not counting:
                free_pos = it
                counting = True
        else:
            free_space = 0
            free_pos = it
            counting = False
        if free_space >= space_need:
            return free_pos, free_space
        it += 1
    return 0, 0

rev_it = len(disk_map) - 1
it = 0

num_to_move = '.'
while True:
    num_to_move, len_to_move, rev_it = find_block_to_move(disk_map, rev_it, num_to_move)

    free_pos, free_space = find_free_space(disk_map, rev_it, len_to_move)

    if rev_it <= 1:
        break
    if free_space >= len_to_move:
        for i in range(len_to_move):
            disk_map[free_pos + i], disk_map[rev_it + i] = disk_map[rev_it + i], disk_map[free_pos + i]
    # print(disk_map)
    
    




checksum = 0

for idx, num in enumerate(disk_map):
    if num != '.':
        checksum += idx * int(num)
print(checksum)