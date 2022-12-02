import sys
import numpy as np

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]


all_rules = []
valid_tickets = []

def get_range(range_):
    # print("get range")
    # print(range_)
    min_r, max_r = range_.split("-")

    return range(int(min_r), int(max_r) + 1)

class TicketRange:
    def __init__(self, range1, range2):
        self.range1 = get_range(range1)
        self.range2 = get_range(range2)
        self.possible_ids = []
        self.id = -1

        # print("TicketRange")
        # print(self.range1)
        # print(self.range2)
    def in_range(self, ticket_value):
        if ticket_value in self.range1:
            return True
        elif ticket_value in self.range2:
            return True
        return False 


def parse_range(line):
    if line == "":
        return
    #print("RANGES")
    range1, range2 = line.split(" or ")
    _, range1 = range1.split(": ")
    ticket_range = TicketRange(range1.strip(), range2.strip())

    all_rules.append(ticket_range)


def is_valid(ticket_value):
    for ticket_rule in all_rules:
        if ticket_rule.in_range(ticket_value):
            return True

    return False

def parse_ticket(line):
    words = line.split(",")
    ticket = []
    for w in words:
        ticket.append(int(w))
    return ticket

def parse_nearby_ticket(line):
    valid = False
    valid_ticket = True
    ticket = parse_ticket(line)

    for ticket_value in ticket:
        valid = is_valid(ticket_value)
        if not valid: 
            print(ticket_value, valid)
            invalid_values.append(ticket_value)
            valid_ticket = False
    if valid_ticket:
        valid_tickets.append(ticket)


RANGES = 1
YOUR_TICKET = 2
NEARBY_TICKET = 3
parse_mode = RANGES

invalid_values = []
p2 = True
your_ticket = []
for line in lines:
    if line == "":
        continue
    elif line == "your ticket:":
        parse_mode = YOUR_TICKET
    elif line == "nearby tickets:":
        parse_mode = NEARBY_TICKET
    else:
        if parse_mode == RANGES:
            parse_range(line)

        elif parse_mode == YOUR_TICKET:
            if p2:
                your_ticket = parse_ticket(line)
                
                #parse_ticket(line)
            # print("YOUR_TICKET")
            #print(line)
        elif parse_mode == NEARBY_TICKET:
            # print("NEARBY_TICKET")
            # print(line)
            parse_nearby_ticket(line)
            
        else:
            assert(False)


#print(lines)

print(sum(invalid_values))

print(your_ticket)

for idx in range(len(your_ticket)):
    print()
    print(idx)
    test_values = []
    for nearby_ticket in valid_tickets:
        test_values.append(nearby_ticket[idx])

    for rule in all_rules:
        correct_rule = True
        print(test_values)
        for test in test_values:
            if not rule.in_range(test):
                correct_rule = False
                print("hallå")
                break
        if correct_rule:

            rule.possible_ids.append(idx)
            print("correct rule")

print()
determined = 0

def remove_from_possible(rule_id):
    print("remove ", rule_id)
    
    for rule in all_rules:
        if rule_id in rule.possible_ids:
            rule.possible_ids.remove(rule_id)
            
        

while determined < len(your_ticket):
    for rule in all_rules:
        print(rule.possible_ids)
        print(len(rule.possible_ids))
        if len(rule.possible_ids) == 1:
            rule.id = rule.possible_ids[0]
            remove_from_possible(rule.id)
            determined += 1

print()
mult_id = []
for rule in all_rules[0:6]:
    mult_id.append(rule.id)
    print(rule.id)

print()
prod = 1
for dep in mult_id:
    prod *= your_ticket[dep]
    print(your_ticket[dep]) 
print(prod)