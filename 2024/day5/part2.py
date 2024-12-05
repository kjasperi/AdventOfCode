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
    
def check_update(pages):
    correct = True
    for idx, page in enumerate(pages):
        rest = pages[idx + 1:]
        if page in RULES:            
            for p2 in rest:
                if p2 not in RULES[page]:
                    correct = False

        if page in REV_RULES:            
            for p2 in rest:
                if p2 in REV_RULES[page]:
                    correct = False
    return correct


def fix_page(pages):
    new_page = []
    backlog = []
    for idx, page in enumerate(pages):
        rest = pages[idx + 1:]
        correct = True
        if page in RULES:            
            for p2 in rest:
                if p2 not in RULES[page]:
                    correct = False

        if page in REV_RULES:            
            for p2 in rest:
                if p2 in REV_RULES[page]:
                    correct = False

        if correct:
            new_page.append(page)
        else:
            backlog.append(page)
    for page_to_insert in backlog:
        inserted = False
        for pos in range(len(new_page)):
            test_pages = new_page[:]
            test_pages.insert(pos, page_to_insert)
            corr = check_update(test_pages)
            if corr:
                new_page = test_pages[:]
                inserted = True
                break
        if not inserted:
            new_page.append(page_to_insert)
    return new_page


score = 0
for update in updates:
    pages = update.split(',')

    corr = check_update(pages)
    if not corr:
        new_page = fix_page(pages)
        score += int(new_page[(len(new_page) - 1) // 2])
        
print(score)