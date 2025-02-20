# Write a python program to create a list of numbers. Print the sum of the elements of even index and odd index separately.

user_input = input("Enter up to 10 numbers separated by spaces: ")
my_list = list(map(int, user_input.split()))
print(my_list)

for item in enumerate(my_list):
    print(item, end=' ')
print()

even_sum = 0
odd_sum = 0

for index, number in enumerate(my_list):
    if index % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print()
print(f"Sum of numbers at even indices: {even_sum}")
print(f"Sum of numbers at odd indices: {odd_sum}")



"""Output:
Enter up to 10 numbers separated by spaces: 12 45 32 68 74 19 61 20 59 73 49
[12, 45, 32, 68, 74, 19, 61, 20, 59, 73, 49]
(0, 12) (1, 45) (2, 32) (3, 68) (4, 74) (5, 19) (6, 61) (7, 20) (8, 59) (9, 73) (10, 49) 

Sum of numbers at even indices: 287
Sum of numbers at odd indices: 225
"""