import sys


def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()


numbers = [int(line.rstrip()) for line in get_lines_from_file()]

preamble_size = 25


def valid(idx):
    num = numbers[idx]
    preamble = numbers[idx - preamble_size: idx]
    for idx_x in range(0, preamble_size):
        x = preamble[idx_x]
        for idx_y in range(idx_x, preamble_size):
            y = preamble[idx_y]
            if x + y == num:
                return True
    return False


invalid_num = 0
for idx in range(preamble_size, len(numbers)):
    if not valid(idx):
        invalid_num = numbers[idx]
        break

print(invalid_num)

### PART 2 ###
# for idx, num in enumerate(numbers):
#     check_sum = num

#     add_idx = idx
#     while check_sum < invalid_num:
#         add_idx += 1

#         check_sum += numbers[add_idx]

#     if check_sum == invalid_num:
#         min_in_range = min(numbers[idx: add_idx + 1])
#         max_in_range = max(numbers[idx: add_idx + 1])
#         print(max_in_range + min_in_range)
#         break
