import sys
import cmath

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

print(lines)

OPERATIONS = ['mult', 'add']

def test(test_val, numbers, total):
    concat = ""
    concat = concat + str(total) + str(numbers[0])
    add_total = total + numbers[0]
    mult_total = total * numbers[0]

    if len(numbers) == 1:
        if total * numbers[0] == test_val:
            return True
        if total + numbers[0] == test_val:
            return True

        if int(concat) == test_val:
            return True
        return False


    if test(test_val, numbers[1:], add_total):
        return True
    elif test(test_val, numbers[1:], mult_total):
        return True
    elif test(test_val, numbers[1:], int(concat)):
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