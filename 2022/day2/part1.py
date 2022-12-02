import sys

def get_lines_from_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines


a_rock = 'A'
a_paper = 'B'
a_sciss = 'C'

rock = 'X'
paper = 'Y'
scissor = 'Z'

def get_shape_score(move_A, move):
    shape = 0
    won = 0
    if (move_A == a_paper) and move == paper:
        won = 3
    if (move_A == a_rock) and move == rock:
        won = 3
    if (move_A == a_sciss) and move == scissor:
        won = 3
    print("'")

    print()
    if move == rock:
        shape = 1
        print(move)


        if move_A == a_sciss:
            won = 6

    if move == paper:
        shape = 2
        if move_A == a_rock:
            won = 6
    if move == scissor:
        shape = 3
        if move_A == a_paper:
            won = 6
    print(move)
    print(move_A)
    print(scissor)
    print(shape)
    print(won)
    return shape + won

def get_score(line):
    move_A, move_B = line.split()
    print(move_A)
    print(move_B)
    return get_shape_score(move_A.strip(), move_B.strip())
    print(score)

lines = get_lines_from_file()

tot_score = 0

for line in lines:
    score = get_score(line)
    tot_score += score
    print(tot_score)