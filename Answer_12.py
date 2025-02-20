# Reverse a list without using reverse() function.

user_input = input("Enter numbers separated by spaces: ")
my_list = list(map(int, user_input.split()))

print()
print("List of integers:", my_list)
print()

reversed_list = my_list[::-1]
print(f"The list when reversed {reversed_list}")
