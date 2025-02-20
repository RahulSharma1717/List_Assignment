# Suppose a list contains positive and negative numbers. Write a program to create two lists - one containing positive numbers and another containing negative numbers.

import random

i = 0
random_number_list = []

while i < 30:
    random_numbers = random.randint(-50, 50)
    random_number_list.append(random_numbers)
    i += 1

print("Random number list:", random_number_list)

positive_numbers = []
negative_numbers = []
neutral_number = 0

for num in random_number_list:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    else:
        print("\nThe list also contains a", neutral_number)

print("\nList of positive numbers:", positive_numbers)
print("\nList of negative numbers:", negative_numbers)


"""Output:
Random number list: [-26, 13, 15, 47, 15, -10, -22, 11, -16, -41, 19, -44, -37, -8, 47, -13, -23, 23, 33, 41, -24, -20, -38, 19, -32, -19, -15, -39, -35, -46]

List of positive numbers: [13, 15, 47, 15, 11, 19, 47, 23, 33, 41, 19]

List of negative numbers: [-26, -10, -22, -16, -41, -44, -37, -8, -13, -23, -24, -20, -38, -32, -19, -15, -39, -35, -46]
"""


"""Output:
Random number list: [21, -49, -16, -25, -32, 8, 0, -49, -33, 44, -31, -42, 14, 13, 28, 35, 43, 41, -50, 8, -2, 21, 40, 9, -12, 1, -9, -10, -14, 26]

The list also contains a 0

List of positive numbers: [21, 8, 44, 14, 13, 28, 35, 43, 41, 8, 21, 40, 9, 1, 26]

List of negative numbers: [-49, -16, -25, -32, -49, -33, -31, -42, -50, -2, -12, -9, -10, -14]
"""
