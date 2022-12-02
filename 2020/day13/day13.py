import sys
import numpy as np

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]

print(lines)

earliest_dep = int(lines[0])

bus_ids = lines[1].split(",")



wait_times = {}
best_res = (0, 999999999)
for bus in bus_ids:
    if bus == 'x':
        continue
    bus_id = int(bus)
    shortest_wait = bus_id - earliest_dep % bus_id
    wait_times[bus_id] = shortest_wait
    if shortest_wait < best_res[1]:
        best_res = (bus_id, shortest_wait)

best_bus = min(wait_times, key=wait_times.get)

print(wait_times[best_bus])
print(best_res)
print(best_res[0] * best_res[1])

print(bus_ids)

remainders = {}
print("------")
for rest, id in enumerate(bus_ids):
    if id != 'x':
        remainders[int(id)] = rest
        print(id, rest)

print(max(remainders))
max_id = max(remainders)
test_num = max_id - remainders[max_id]
print(test_num)

found_ans = False
print("------------")
def valid_bus(bus_rest, test_num, bus_id):
    #print(bus_rest, test_num, bus_id)
    mod = test_num % bus_id
    #print(mod)
    if mod == 0 and bus_rest == 0:
        return True
    if mod + bus_rest == bus_id:
        return True
    return False
        
while not found_ans:
    found_ans = True
    for bus in remainders:
        bus_rest = remainders[bus]
        #print(bus, bus_rest)
        if not valid_bus(bus_rest, test_num, bus):
            #print(test_num % bus)
            found_ans = False
            break
    if not found_ans:
        test_num += max_id
        print(test_num)
    if test_num > 1000000000000:
        print(test_num)
    # if test_num > 2068781:
    #     break
print(test_num)

bus_id = 7
print("-------------------")
for bus_id in remainders:
    print(valid_bus(remainders[bus_id], 1068781, bus_id))