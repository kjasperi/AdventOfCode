import sys

def get_lines_from_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines



def get_top_score(lines):
    temp_cal = 0
    top_score = 0
    for line in lines:
        if line == '':
            if temp_cal > top_score:
                top_score = temp_cal
            temp_cal = 0
        else:
            temp_cal += int(line)

    if temp_cal > top_score:
        top_score = temp_cal
    return top_score

lines = get_lines_from_file()
print(get_top_score(lines))