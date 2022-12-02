import sys


def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()


lines = get_lines_from_file()
memory = []
for line in lines:
    operation = line[0:3]
    arg = int(line[3:].rstrip())

    memory.append((operation, arg))



def gameboy():
    program_counter = 0
    instructions_run = []
    accumulator = 0

    while True: 
        if program_counter >= len(memory):
            print("Terminated succeful")
            print("Accumulator: " + str(accumulator))

            return True

        elif program_counter in instructions_run:
            print("break")
            print(program_counter)
            print("Accumulator: " + str(accumulator))
            return False

        instr, arg = memory[program_counter]
        
        instructions_run.append(program_counter)
        if instr == "acc":
            accumulator += arg
            program_counter += 1
        elif instr == "jmp":
            program_counter += arg
        elif instr == "nop":
            program_counter += 1
        else:
            print("Invalid instruction: " + instr)
            break


gameboy()

# original_memory = memory.copy()
# for idx, line in enumerate(memory):
#     memory = original_memory.copy()
#     changed = False
#     if line[0] == "nop":
#         memory[idx] = ("jmp", line[1])
#         changed = True
#     elif line[0] == "jmp":
#         memory[idx] = ("nop", line[1])
#         changed = True

#     if changed:
#         if gameboy():
#             break

