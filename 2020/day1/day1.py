import sys

input_file = sys.argv[1]

input_numbers = []

with open(input_file) as inf:
    for line in inf:
        input_numbers.append(int(line.strip('\n')))

print(input_numbers)

expense_sum = 2020

number_of_expenses = len(input_numbers)
for expense_A_ind in range(0, number_of_expenses):
    #print(input_numbers[expense_A_ind])
    expense_A = input_numbers[expense_A_ind]

    for expense_B_ind in range(expense_A_ind + 1, number_of_expenses):
        expense_B = input_numbers[expense_B_ind]

        for expense_C_ind in range(expense_B_ind + 1, number_of_expenses):
            #print(input_numbers[expense_B_ind])
            expense_C = input_numbers[expense_C_ind]
            if expense_A + expense_B + expense_C == expense_sum:
                print("Expense A " + str(expense_A))
                print("Expense B " + str(expense_B))
                print("Expense C " + str(expense_C))
                print("answer: " + str(expense_A*expense_B*expense_C))




