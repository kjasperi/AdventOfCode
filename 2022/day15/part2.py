import sys
import cmath 
from sortedcontainers import SortedDict
import random

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

closest_beacon = {}
all_sensors = set()
all_beacons = set()

for line in lines:
    sensor, beacon = line.split(":")
    sensor = sensor.split("Sensor at")[1]
    x, y = sensor.split(",")
    x = int(x.split("=")[1])
    y = int(y.split("=")[1])
    sensor_pos = (x, y)

    beacon = beacon.split("at")[1]
    x, y = beacon.split(",")
    x = int(x.split("=")[1])
    y = int(y.split("=")[1])
    beacon_pos = (x, y)
    closest_beacon[sensor_pos] = beacon_pos
    all_sensors.add(sensor_pos)
    all_beacons.add(beacon_pos)

#print(all_sensors)

def get_distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

def get_score(pos):
    score = -9999999
    for sensor in all_sensors:
        test_dist = get_distance(sensor, pos)
        closest_dist = get_distance(sensor, closest_beacon[sensor])
        temp_score = closest_dist - test_dist
        if temp_score > score:
            score = temp_score
    return score

visited = set()
#max_size = 20
max_size = 4000000


def get_neighbours(pos, score):
    x = pos[0]
    y = pos[1]
    neigh = []
    for dx, dy in [(-1 ,0), (1, 0), (0, -1), (0, 1)]:
        n = ((x + dx * (score // 2 + 1)) % max_size, (y + dy * (score // 2 + 1)) % max_size)
        neigh.append(n)
    return neigh

def get_next_position(current_pos, current_score):
    temp_score = 5555555555555
    temp_pos = (-1, -1)
    for neigh in get_neighbours(current_pos, current_score):
        if get_score(neigh) < temp_score and neigh not in visited:
            temp_pos = neigh
            temp_score = get_score(neigh)
    return temp_pos



def part2():
    position = (0, 0)

    prev_score = 0

    for step in range(60000000):
        if get_score(position) > prev_score or position in visited:
            x = random.randint(0, max_size)
            y = random.randint(0, max_size)
            print("In local minima testing random pos", x, y)
            position = (x, y) 

        print("Step", step, position, get_score(position))

        visited.add(position)
        score = get_score(position)
        prev_score = score

        if score < 0: # Found beacon
            print(position[0] * 4000000 + position[1])
            return True

        position = get_next_position(position, score)
part2()