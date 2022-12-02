import sys


def get_lines_from_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines


declaration_forms = get_lines_from_file()

group_dict = {}
all_dicts = []
people_in_group = 0

for declaration in declaration_forms:
    if declaration == '':
        all_dicts.append((group_dict, people_in_group))
        people_in_group = 0
        group_dict = {}

        continue
    people_in_group += 1
    for letter in declaration:
        if letter in group_dict:
            group_dict[letter] += 1
        else:
            group_dict[letter] = 1
all_dicts.append((group_dict, people_in_group))

answer_p1 = 0
answer_p2 = 0

for (declaration, group_size) in all_dicts:
    answer_p1 += len(declaration)
    for answer in declaration:
        print(answer)
        if declaration[answer] == group_size:
            answer_p2 += 1


print("Part 1:")
print(answer_p1)
print("Part 2:")
print(answer_p2)