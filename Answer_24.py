# Write a program to create a list of 10 numbers and print the list after replacing each number with the difference between itself and the previous number in the list. The first number should remain the same.

user_input = input("Enter up to 10 numbers separated by spaces: ")
my_list = list(map(int, user_input.split()[:10]))
print("\nInput numbers", my_list)

new_list = list(range(10))
new_list[0] = my_list[0]
i = 0

while i < 9:
    new_list[i+1] = my_list[i+1] - my_list[i]
    i += 1

print("\nModified List: ", new_list)


"""Output:
Enter up to 10 numbers separated by spaces: 45 23 15 24 85 93 52 86 74 38 63

Input numbers [45, 23, 15, 24, 85, 93, 52, 86, 74, 38]

Modified List:  [45, -22, -8, 9, 61, 8, -41, 34, -12, -36]
"""