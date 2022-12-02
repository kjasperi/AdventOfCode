import sys

def get_lines_from_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines


def get_scores(lines):
    temp_cal = 0
    scores = []

    for line in lines:
        if line == '':
            scores.append(temp_cal)
            temp_cal = 0

        else:
            temp_cal += int(line)
    scores.append(temp_cal)
    return scores
lines = get_lines_from_file()

scores = get_scores(lines)
scores.sort()

# Part 1
print(scores[-1:])
# Part 2
print(sum(scores[-3:]))
