import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()

posible = data.split('mul')[1:]


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
for w in posible:
    result += test_word(w)
print(result)