# Write a program to add all the elements of the list. Also find the length of the list using loop.

list_of_numbers = [1, 2, 3, 9, 4, 2, 3, 1, 4, 6, 7, 9, 6, 5]
print(f"Input List: {list_of_numbers}")
print()
sum_of_elements = 0
number_of_elements = 0

for num in list_of_numbers:
    sum_of_elements += num
    number_of_elements += 1

print(f"Sum of elements of list: {sum_of_elements}")
print(f"Number of elements in the list: {number_of_elements}")


"""Output:
Input List: [1, 2, 3, 9, 4, 2, 3, 1, 4, 6, 7, 9, 6, 5]

Sum of elements of list: 62
Number of elements in the list: 14
"""