# Write a program to create a list of numbers and print the list of numbers after reversing each number in the list.

import random

def reverse_numbers():
    create_number = []
    reverse_num = []
    i = 0

    while i < 10:
        random_number = random.randint(100, 10000)
        create_number.append(random_number)
        i += 1
    print(f"\nThe random number list created is: {create_number}")

    for num in create_number:
        number_reversed = 0

        while num > 0:
            smallest_digit = num % 10
            remaining_digits = num // 10
            num = remaining_digits
            number_reversed = number_reversed * 10 + smallest_digit

        reverse_num.append(number_reversed)
    print(f"\nThe list generated after reversing the numbers: {reverse_num}")



reverse_numbers()



"""Output:

The random number list created is: [9758, 2629, 7659, 8197, 8869, 6038, 8562, 2401, 997, 8382]

The list generated after reversing the numbers: [8579, 9262, 9567, 7918, 9688, 8306, 2658, 1042, 799, 2838]
"""

# The above problem can be solved better by string reversal, but solved to show the logic of number reversal