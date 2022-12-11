import sys

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
blocks = data.split("\n\n")

monkeys = {}
cache = {}

magic_number = 1

def update_worry_level(item, operation):
    #print(item, operation)
    c = (item, operation) 
    if c in cache:
        return cache[c]

    val1, op, val2 = operation.split()
    if val1 == 'old':
        val1 = item
    if val2 == 'old':
        val2 = item
    val1 = int(val1)
    val2 = int(val2)
    if op == '*':
        res = val1 * val2
        cache[c] = res
        return res
    if op == '+':
        res = val1 + val2
        cache[c] = res

        return res

def throw(item, to_id):
    monkeys[to_id].receive_item(item)

class Monkey:
    def __init__(self, start_items, op_str, test_val, true_id, false_id):
        self.items = start_items
        self.operation = op_str
        self.test_val = test_val
        self.true_to_id = true_id
        self.false_to_id = false_id
        self.inspected = 0
    
    def turn(self):
        global t_worry
        global t_throw
        #print("hej")
        for item in self.items:
            self.inspected += 1
            if item > magic_number:
                item = item % magic_number

            item = update_worry_level(item, self.operation)

            if item % self.test_val == 0:
                #print("throw to: ", self.true_to_id)
                throw(item, self.true_to_id)
            else:
                #print("throw to: ", self.false_to_id)
                throw(item, self.false_to_id)
        self.items = []

    def receive_item(self, item):
        self.items.append(item)

def create_monkey(block):
    lines = block.split("\n")
    id = int(lines[0].split()[1].split(":")[0])

    items = lines[1].split("items:")[1].split(",")
    items = [int(item.strip()) for item in items]

    op_str = lines[2].split("=")[1].strip()
    test_val = int(lines[3].split("divisible by")[1].strip())

    true_id = int(lines[4].split("monkey")[1])
    false_id = int(lines[5].split("monkey")[1])
    monkey = Monkey(items, op_str, test_val, true_id, false_id)
    monkeys[id] = monkey

def do_round():
    for id in monkeys:
        monkeys[id].turn()

for block in blocks:
    create_monkey(block)

for id in monkeys:
    magic_number *= monkeys[id].test_val

for id in range(10000):
    do_round()

inspected = [monkeys[id].inspected for id in monkeys]
inspected.sort()
print(inspected[-1] * inspected[-2])