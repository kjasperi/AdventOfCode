import sys
import cmath 

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")
#blocks = data.split("\n")

print(lines)
score = 0
for line in lines:
    prev_n = int(line.split()[0])
    incr = False
    safe = True
    if int(line.split()[1]) > prev_n:
        incr = True
        print("increase")
    l = len(line.split())
    print(line, incr)
    for idx, n in enumerate(line.split()):
        n = int(n)
        if idx == 0:
            
            prev_n = n
            continue
        print(n, prev_n, incr)
        if incr:
            if prev_n >= n or abs(prev_n - n) > 3:
                safe = False
                print("hej")
                break
        else:
            if prev_n <= n or abs(prev_n - n) > 3:
                safe = False
                print("hej2", prev_n, n)

                break



        prev_n = n
    
    if safe:
        score +=1
        print(safe)
print(score)