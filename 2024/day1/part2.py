import sys
import cmath

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

# print(lines)
locationA = []
locationB = []
for line in lines:
    a, b = line.split()
    locationA.append(int(a))
    locationB.append(int(b))


result = 0

for idx, a in enumerate(locationA):
    count = 0
    for b in locationB:
        if a == b:
            count += 1
    result += count * a
print(result)