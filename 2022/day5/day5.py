import sys
from dataclasses import dataclass

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line for line in get_lines_from_file()]


divider = 0
for idx, line in enumerate(lines):
    if line == "\n":
        divider = idx

def parse_header(head_lines):
    nums = {}
    stacks = {}
    for idx, let in enumerate(head_lines[-1]):
        if let.isnumeric():
            nums[int(let)] = idx

    for n in nums:
        for line in head_lines[:-1]:
            crate = line[nums[n]].strip()
            if crate:
                s = int(n)
                if not stacks.get(s):
                    stacks[s] = []
                stacks[s].append(crate)
    return stacks

def parse_instruction(lines):
    instructions = []
    for line in lines:
        instr, cmd = line.split("from")
        qnt = int(instr.rstrip().split()[-1])
        s_from, s_to = cmd.split("to")
        s_from = int(s_from.strip())
        s_to = int(s_to.strip())
        instructions.append([qnt, s_from, s_to])
    return instructions
start_stacks = parse_header(lines[:divider])
instructions = parse_instruction(lines[divider + 1:])

def solve_p1(stacks, instructions):
    for instr in instructions:

        qnt, from_s, to_s = instr
        for i in range(qnt):
            crate = stacks[from_s][0]
            stacks[from_s] = stacks[from_s][1:]

            stacks[to_s] = [crate] + stacks[to_s][:]

    return stacks
end_stacks = solve_p1(start_stacks, instructions)

ans = ''
for s in end_stacks:
    ans += end_stacks[s][0]
print(ans)


start_stacks = parse_header(lines[:divider])
instructions = parse_instruction(lines[divider + 1:])

def solve_p2(stacks, instructions):
    for instr in instructions:

        qnt, from_s, to_s = instr
        crates = stacks[from_s][0:qnt]
        stacks[from_s] = stacks[from_s][qnt:]
        stacks[to_s] = crates + stacks[to_s][:]

    return stacks
end_stacks = solve_p2(start_stacks, instructions)

ans = ''
for s in end_stacks:
    ans += end_stacks[s][0]
print(ans)