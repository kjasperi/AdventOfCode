import sys

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

def print_layout(layout):
    print()
    for line in layout:
        print("".join(line))
    print()


layout = [list(line.rstrip()) for line in get_lines_from_file()]

ROWS = len(layout)
COLS = len(layout[0])

#print_layout(layout)


class Seat:
    def __init__(self):
        self.occupied = False
        self.next_state = False
        self.adjecant_seats = []

    def set_next_state(self):
        #         If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        num_occ_adj = self.num_adjecant_occupied()
        if not self.occupied and num_occ_adj == 0:
            self.next_state = True
            
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        elif self.occupied and num_occ_adj >= 5:
            self.next_state = False
        # Otherwise, the seat's state does not change.
        else:
            self.next_state = self.occupied
        
    def num_adjecant_occupied(self):
        num_occ = 0
        for adj in self.adjecant_seats:
            if adj.occupied:
                num_occ += 1
        return num_occ

def print_all_seats(seats):
    print("\n")
    for row in range(ROWS):
        line_to_print = ""
        for col in range(COLS):
            char_to_add = "."
            seat_id = (row, col)
            if seat_id in seats:
                if seats[seat_id].occupied:
                    char_to_add = "#"
                else:
                    char_to_add = "L"
            line_to_print += char_to_add

        print(line_to_print)


all_seats = {}

for row_idx, row in enumerate(layout):
    for col_idx, seat in enumerate(row):
        if seat == 'L':
            #print(row_idx, col_idx)
            all_seats[(row_idx, col_idx)] = Seat()

# set adjecant seats
def set_adjecant_p1():
    adjecant_ids = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]
    for seat in all_seats:
        for adjecant in adjecant_ids:
            adj_seat_id = (seat[0] + adjecant[0], seat[1] + adjecant[1])
            #print(adj_seat_id)

            if adj_seat_id in all_seats:
                #print(adj_seat_id)
                all_seats[seat].adjecant_seats.append(all_seats[adj_seat_id])

def set_adjecant_p2():
    adjecant_matrix = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]
    for seat in all_seats:
        for adjecant in adjecant_matrix:
            adj_seat_id = seat
            while 0 <= adj_seat_id[0] < ROWS and 0 <= adj_seat_id[1] < COLS:
                adj_seat_id = (adj_seat_id[0] + adjecant[0], adj_seat_id[1] + adjecant[1])

                if adj_seat_id in all_seats:
                    #print(adj_seat_id)
                    all_seats[seat].adjecant_seats.append(all_seats[adj_seat_id])
                    break


def apply_rules():
    changed = False
    for seat_id in all_seats:
        seat = all_seats[seat_id]
        seat.set_next_state()

    for seat_id in all_seats:
        seat = all_seats[seat_id]
        if seat.occupied != seat.next_state:
            seat.occupied = seat.next_state
            changed = True
        
    
    return changed

set_adjecant_p2()

while apply_rules():
    None
    #print_all_seats(all_seats)

num_occ = 0
for seat_id in all_seats:
    seat = all_seats[seat_id]
    if seat.occupied:
        num_occ += 1

print(num_occ)