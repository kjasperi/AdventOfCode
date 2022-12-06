import sys

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.read()

line = get_lines_from_file().strip()

def solve(length):
    for idx in range(length - 1, len(line)):
        if len(set(line[idx - length + 1 : idx + 1])) == length:
            return idx + 1

print(solve(4))
print(solve(14))
    