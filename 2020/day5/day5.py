import sys


def get_lines_from_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines


all_seats = get_lines_from_file()

largest_id = 0

all_ids = []

for seat in all_seats:
    str_row = seat[:7]
    str_row = str_row.replace('F', '0')
    str_row = str_row.replace('B', '1')

    row = int(str_row, 2)

    str_col = seat[7:]
    str_col = str_col.replace('R', '1')
    str_col = str_col.replace('L', '0')

    col = int(str_col, 2)

    seat_id = row * 8 + col
    all_ids.append(seat_id)
    if seat_id > largest_id:
        largest_id = seat_id

all_ids.sort()

current_digit = all_ids[0] - 1
print(current_digit)
for digit in all_ids:
    if digit != current_digit + 1:
        print("missing digit")
        print(digit - 1)
    current_digit = digit
