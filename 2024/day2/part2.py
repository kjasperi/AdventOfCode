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

def check_safe(nums):
    prev_n = nums[0]
    incr = False
    if nums[1] > prev_n:
        incr = True
        print("increase")

    for idx, n in enumerate(nums):
        n = int(n)
        if idx == 0:
            
            prev_n = n
            continue
        if incr:
            if prev_n >= n or abs(prev_n - n) > 3:
                return False, idx
        else:
            if prev_n <= n or abs(prev_n - n) > 3:

                return False, idx


        prev_n = n
    return True, 0
    
    
for line in lines:
    nums = [int(n) for n in line.split()]
    safe, idx = check_safe(nums)
    if safe:
        score +=1
        

    else:
        safe = True
        l = len(nums)
        for i in range(l):

            nums2 = []
            for id, n in enumerate(nums):
                if id != i:
                    nums2.append(n)

            safe, k = check_safe(nums2)
            if safe:
                print("safe")
                score += 1
                break


print(score)