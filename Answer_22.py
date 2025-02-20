# Write a program to create a list of 5 numbers and print the list after inserting a new number at the beginning of the list and sorting the list in ascending order.

user_input = (input("Enter 5 numbers separated by spaces: "))
my_list = list(map(int, user_input.split()[:5]))
print(f"\nThe numbers input are: {my_list}")

my_list.insert(0, 25)
print("After inserting number at the beginning:", my_list)

my_list.sort()
print(f"After sorting the list:", my_list)


"""Output:
Enter 5 numbers separated by spaces: 23 14 84 56 79 36

The numbers input are: [23, 14, 84, 56, 79]
After inserting number at the beginning: [25, 23, 14, 84, 56, 79]
After sorting the list: [14, 23, 25, 56, 79, 84]
"""
