# Suppose a list contains 20 integers generated randomly. Receive a number from the keyboard and report position of all occurrences of this number in the list.

import random

i = 0
random_number_list = []

while i < 20:
    random_numbers = random.randint(1, 50)
    random_number_list.append(random_numbers)
    i += 1

print("\nRandom number list:", random_number_list)

try:
    index_values = []
    user_input = int(input("\nEnter a number from 1 to 50: "))
    for index, value in enumerate(random_number_list):
        if user_input == value:
            index_values.append(index)

    print(f"\nInput number is present in random list at position {index_values}")

except ValueError:
    print("Invalid Input!, Enter numeric value")


"""Output:
Random number list: [39, 26, 17, 11, 39, 30, 28, 28, 43, 17, 45, 17, 21, 48, 7, 38, 14, 32, 22, 3]

Enter a number from 1 to 50: 17

Input number is present in random list at position [2, 9, 11]
"""


"""Output:
Random number list: [12, 48, 17, 9, 13, 31, 34, 30, 1, 1, 43, 32, 10, 29, 21, 20, 39, 14, 45, 40]

Enter a number from 1 to 50: a
Invalid Input!, Enter numeric value
"""
