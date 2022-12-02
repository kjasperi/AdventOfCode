import sys

def get_lines_from_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines


ROCK = 1
PAPER = 2
SCISSOR = 0 #3

lines = get_lines_from_file()

tot_score = 0

def elf_choice(abc):
    if abc == 'A':
        return ROCK
    elif abc == 'B':
        return PAPER
    elif abc == 'C':
        return SCISSOR

def my_points(elf, xyz):
    if xyz == 'X': # lose
        if elf == ROCK:
            return SCISSOR + 3
        elif elf == PAPER:
            return ROCK
        return PAPER
    if xyz == 'Y': # draw
        if elf == 0:
            return 3 + 3
        return elf + 3
    if xyz == 'Z': # win
        if elf == ROCK:
            return 2 + 6
        elif elf == PAPER:
            return 3 + 6
        return 1 + 6

tot_points = 0
for line in lines:
    abc, xyz = line.split() 
    elf = elf_choice(abc)
    points = my_points(elf, xyz)

    tot_points += points

print(tot_points)