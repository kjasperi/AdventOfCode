import sys


def parse_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines


def check_password_policy(input):
    policy, password = input.split(':')
    min_letters, policy = policy.split('-')

    max_letters, letter = policy.split(' ')

    letter_occ = password.count(letter)

    if letter_occ < int(min_letters):
        return False
    if letter_occ > int(max_letters):
        return False
    
    return True


#Part 2
def check_toboggan_policy(input):
    policy, password = input.split(':')

    index_a, policy = policy.split('-')

    index_b, letter = policy.split(' ')

    #print("-------")
    #print(password)

    letter_a = password[int(index_a)]
    letter_b = password[int(index_b)]

    num_matching_letters = 0

    if letter_a == letter:
        num_matching_letters = num_matching_letters + 1

    if letter_b == letter:
        num_matching_letters = num_matching_letters + 1
    
    #print(num_matching_letters)

    if num_matching_letters == 1:
        return True
    return False


input_lines = parse_file()

num_correct_passwords = 0
for input in input_lines:
    is_valid = check_toboggan_policy(input)

    if is_valid:
        num_correct_passwords = num_correct_passwords + 1
print(num_correct_passwords)