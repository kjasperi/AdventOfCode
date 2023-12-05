import sys
import re

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n\n")

sum = 0
seeds = [int(x) for x in lines[0].split(":")[1].split()]
lines = lines[1:]

def to_range(raw):
    src, dest = raw[0].split(" map")[0].split("-to-")
    s_d_key = (src, dest)
    res_ranges = []
    raw = raw[1:]

    for line in raw:
        res_range = {}

        dest_start, src_start, l = line.split()
        dest_start = int(dest_start)
        src_start = int(src_start)
        res_range["src"] = src_start
        res_range["dst"] = dest_start
        res_range["l"] = int(l)
        res_ranges.append(res_range)

    return s_d_key, res_ranges

all_ranges = {}

for n, line in enumerate(lines):
    seed_to_soil = line.split("\n")
    k, seed_to_soil = to_range(seed_to_soil)
    all_ranges[n] = seed_to_soil

res = []
for seed in seeds:
    loc = seed
    for r in all_ranges:
        for a_range in all_ranges[r]:
            print(a_range)
            src = a_range['src']
            dst = a_range['dst']
            l = a_range['l']

            if loc >= src and loc < src + l:
                loc = dst + loc - src 
                break

    res.append(loc)
    
print(min(res))


