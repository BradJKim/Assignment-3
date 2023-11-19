import numpy as np



# take input file, extract values and store into arrays

file = open("input.txt", "r")

x_arr = []
y_arr = []

line = file.readline()
for number in line.split():
    x_arr.append(float(number))

line = file.readline()
for number in line.split():
    y_arr.append(float(number))

file.close()

# Recursively take n-orders to get top derivative value

derivatives = []
derivatives.append(y_arr[0])

initial_derv_arr = []

for i in range(0, len(y_arr) - 1):
    initial_derv_arr.append(( y_arr[i+1] - y_arr[i] ) / ( x_arr[i+1] - x_arr[i] ))

derivatives.append(initial_derv_arr[0])

def get_derivatives(derv_arr):
    results = []

    for i in range(0, len(derv_arr) - 1):
        results.append(( derv_arr[i+1] - derv_arr[i] ) / ( x_arr[i  + (len(x_arr) - len(derv_arr)) + 1] - x_arr[i] ))

    derivatives.append(results[0])

    if (len(results) != 1):
        get_derivatives(results)

get_derivatives(initial_derv_arr)

# Prompt user for value and evaluate polynomial from array values, print and repeat until quit

user_input = input("Enter a value for evaluation: ")

while(user_input != 'q'):

    solution = 0

    for derv in derivatives:
        product = derv

        for i in range(0, derivatives.index(derv)):
            product *= float(user_input) - x_arr[i]

        solution += product

    print("Solution: " + str(solution))

    user_input = input("Enter a value for evaluation: ")

print("Qutting")
