from collections import deque

start_numbers = deque()
testinput = [19,0,5,1,10,13]

start_numbers = deque(testinput)


print(start_numbers)

turn = 1
max_turn = 30000000

spoken_numbers = {}

def add_spoken(num, turn):
    if num not in spoken_numbers:
        spoken_numbers[num] = deque()
    spoken_numbers[num].appendleft(turn)


while len(start_numbers):
    num = start_numbers.popleft()
    print(num)
    add_spoken(num, turn)
    last_spoken_number = num
    turn += 1


while turn <= max_turn:
    if len(spoken_numbers[last_spoken_number]) == 1:
        last_spoken_number = 0
    else:
        last_turns = spoken_numbers[last_spoken_number]
        last_spoken_number = last_turns[0] - last_turns[1]
    add_spoken(last_spoken_number, turn)

    turn += 1
print(turn, last_spoken_number)

#print(spoken_numbers)