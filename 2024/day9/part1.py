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

rev_it = len(disk_map) - 1
it = 0
while it < rev_it:
    while True:
        if disk_map[it] == '.':
            break
        it += 1
    while True:
        if disk_map[rev_it] != '.':
            break
        rev_it -= 1
    # print(it, rev_it)
    if it >= rev_it:
        break
    disk_map[it], disk_map[rev_it] = disk_map[rev_it], disk_map[it]
    # print(disk_map)

checksum = 0

for idx, num in enumerate(disk_map):
    if num == '.':
        break
    checksum += idx * int(num)
print(checksum)