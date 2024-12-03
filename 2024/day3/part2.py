import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()

posible_all = data.split('mul')

possible = posible_all[1:]

mul_enabled = True

do = 'do()'

dont = r"don't()"

if dont in posible_all:
    mul_enabled = True


def test_word(word):
    if word[0] != '(':
        return 0
    word = word[1:]

    if ')' not in word:
        return 0
    

    word = word.split(')')[0]

    words = word.split(',')
    if len(words) != 2:
        return 0 
    lhs, rhs = word.split(',')

    try:
        return int(lhs) * int(rhs)
    except:
        print("fel", lhs, rhs)
        return 0
    


result = 0
for w in possible:
    if mul_enabled:
        result += test_word(w)

    if do in w:
        print("do")
        mul_enabled = True
    if dont in w:
        print("dont")
        mul_enabled = False
print(result)