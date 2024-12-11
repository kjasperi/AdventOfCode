import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

stones = [int(x) for x in lines[0].split()]

def blink(stones):
    new_stones = []
    # print(stones)
    for stone in stones:
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if stone == 0:
            new_stones.append(1)
        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        elif len(str(stone)) % 2 == 0:
            st_str = str(stone)
            lhs = st_str[:len(st_str) // 2]
            rhs = st_str[len(st_str) // 2:]
            new_stones.append(int(lhs))
            new_stones.append(int(rhs))
        
        else: # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            new_stones.append(2024 * stone)

    return new_stones

for step in range(25):
    print("step", step)
    stones = blink(stones)

# print(stones)
print(len(stones))