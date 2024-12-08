import sys
import cmath

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

def test(test_val, numbers, total):
    if len(numbers) == 1:
        if total * numbers[0] == test_val:
            return True
        if total + numbers[0] == test_val:
            return True
        return False

    add_total = total + numbers[0]
    mult_total = total * numbers[0]
    if test(test_val, numbers[1:], add_total):
        return True
    elif test(test_val, numbers[1:], mult_total):
        return True
    return False

p1 = 0
for line in lines:
    test_value, numbers = line.split(":")
    test_value = int(test_value)
    numbers = [int(x) for x in numbers.split()]
    if test(test_value, numbers[1:], numbers[0]):
        p1 += test_value
print(p1)