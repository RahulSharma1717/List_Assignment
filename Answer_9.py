# Given a list of integers, write a program to find the sum of all even numbers in the list.

input_list = list(range(1, 25))
sum_even = 0

for i in input_list:
    if i % 2 == 0:
        sum_even += i

print(f"The input list is: {input_list}")
print(f"The sum of even numbers in the list: {sum_even}")



"""Output:
The input list is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
The sum of even numbers in the list: 156
"""