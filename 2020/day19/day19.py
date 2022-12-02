import sys
import itertools


def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]

#print(lines)

all_rules = {}
all_messages = []


class Rule:
    def __init__(self):
        self.branches = []
    
    def add_branch(self, branch_str):
        branch = branch_str.split()
        self.branches.append(branch)



def parse_rule(line):
    rule_num, rule_str = line.split(':')
    
    assert rule_num not in all_rules

    rule = Rule()

    for branch in rule_str.split('|'):
        rule.add_branch(branch)


    all_rules[rule_num] = rule


parsing_rules = True

for line in lines:
    if line == '':
        parsing_rules = False
    elif parsing_rules:
        parse_rule(line)
        #print(line)
    else:
        all_messages.append(line)

max_depth = 500

def is_valid(message, rule_num):
    #print((20-len(message))*'-',"is valid:", message, rule_num)

    if message == '':
        #print(100*"!")
        #print(rule_num)
        return 0
    if not rule_num.isnumeric():     
        if rule_num[1] == message[0]:
            return 1
        #print("No Match")
        return 0
    valid = True
    rule = all_rules[rule_num]
    #print((20-len(message))*'-',rule.branches)

    for branch in rule.branches:
        valid_branch = True
        sub_cnt = 0

        for sub_rule in branch:
            sub_msg = message[sub_cnt:]
            #print(sub_rule, sub_msg)
            match = is_valid(sub_msg, sub_rule)
            if not match:
                valid_branch = False
                break
            sub_cnt += match
        if valid_branch:
            return sub_cnt

    return 0

def generate_rule_8():
    
    all_rule_8 = []
    for i in range(10):
        rule8 = Rule()
        
        rule8.add_branch(i*'42 ')
        print(rule8.branches)
        all_rule_8.append(rule8)
    
    return all_rule_8
   
def generate_rule_11():
    
    all_rule_11 = []
    for i in range(10):
        rule11 = Rule()
        
        rule11.add_branch(i*'42 ' + i*'31 ')
        all_rule_11.append(rule11)
        print(rule11.branches)

    
    return all_rule_11
   




message = all_messages[0]
ans = 0
all_rule_8 = generate_rule_8()

print(all_rules['8'].branches)

all_rule_11 = generate_rule_11()

#print(all_rule_11.branches)

rule_8_11_pairs = []
for idx_8 in range(10):
    for idx_11 in range(10):
        rule_8_11_pairs.append((idx_8, idx_11))
        print(idx_8, idx_11)
print(rule_8_11_pairs)

for message in all_messages:
    active_message = message
    for rule8_11 in rule_8_11_pairs:
        rule8 = all_rule_8[rule8_11[0]]
        all_rules['8'] = rule8

        rule11 = all_rule_11[rule8_11[1]]
        all_rules['11'] = rule11

        valid = is_valid(message, '0')
        print("---------------", valid)
        if valid >= len(message):
            print("Valid", message)
            print(len(message), valid)
            ans += 1
            break
        else:
            print("Not valid", message)
            print(len(message), valid)
            #break

print(ans)


