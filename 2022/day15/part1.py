import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

closest_beacon = {}
all_sensors = set()
all_beacons = set()

no_beacon = set()

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

#print(closest_beacon)

def find_blocked(y_coord):
    for sensor in all_sensors:
        x, y = sensor
        dist = get_distance(sensor, closest_beacon[sensor])
        y_diff = abs(y_coord - y) 
        if y_diff <= dist: 
            x_remain = (dist - y_diff)
            #print(sensor, x_remain)
            if (x, y_coord) not in all_beacons:
                no_beacon.add((x, y_coord))

            for dx in range(x_remain + 1):
                if (x - dx, y_coord) not in all_beacons:
                    no_beacon.add((x - dx, y_coord))
                if (x + dx, y_coord) not in all_beacons:
                    no_beacon.add((x + dx, y_coord))

find_blocked(2000000)

print(len(no_beacon))