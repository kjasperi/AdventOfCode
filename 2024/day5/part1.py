import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
blocks = data.split("\n\n")


rules = blocks[0].split('\n')
updates = blocks[1].split('\n')

RULES = {}
REV_RULES = {}
for rule in rules:
    p1, p2 = rule.split('|')
    if p1 not in RULES:
        RULES[p1] = []
    RULES[p1].append(p2)

    if p2 not in REV_RULES:
        REV_RULES[p2] = []
    REV_RULES[p2].append(p1)
    
def check_update(update):
    pages = update.split(',')
    l = len(pages)
    correct = True

    for idx, page in enumerate(pages):
        # print(page)
        rest = pages[idx + 1:]
        if page in RULES:            
            for p2 in rest:
                if p2 not in RULES[page]:
                    correct = False

        if page in REV_RULES:            
            for p2 in rest:
                if p2 in REV_RULES[page]:
                    correct = False
    return pages, correct




score = 0
for update in updates:
    page, corr = check_update(update)
    if corr:
        score += int(page[(len(page) - 1) // 2])
    # break
print(score)