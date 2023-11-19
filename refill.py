import numpy as np

file = open("input.txt", "w")

user_input = input("Enter number of points: ")

for i in range(0, int(user_input)):
    file.write(str(np.random.rand() * 100))
    file.write(' ')

file.write('\n')

for i in range(0, int(user_input)):
    file.write(str(np.random.rand() * 100))
    file.write(' ')

file.close()