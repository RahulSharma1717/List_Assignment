# Create a list of ten numbers and print the largest number in the list.

user_input = input("Enter up to 10 numbers separated by spaces: ")
my_list = list(map(int, user_input.split()[:10]))

print("List of integers:", my_list)

largest_number = 0

for num in my_list:
    if num > largest_number:
        largest_number = num

print(f"The largest number among the integers entered is {largest_number}")


"""Output:
Enter up to 10 numbers separated by spaces: 2 45 78 16 96 31 45 87 20 119 52
List of integers: [2, 45, 78, 16, 96, 31, 45, 87, 20, 119]
The largest number among the integers entered is 119
"""