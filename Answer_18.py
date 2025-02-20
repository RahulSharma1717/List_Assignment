# Write a program to create two lists of 5 numbers each and print the list after adding corresponding elements of the two lists.

try:
    user_input = input("Enter up to 10 numbers separated by spaces: ")
    my_list = list(map(int, user_input.split()[:10]))
    print(f"\nInput list of 10 numbers: {my_list}")

    my_list_1 = my_list[:5]
    my_list_2 = my_list[5:10]

    new_list = my_list_1 + my_list_2
    print("\nList after adding elements of 2 segregated lists:", new_list)

except ValueError:
    print("Invalid Input!, Enter Numeric Values")



"""Output:
Enter up to 10 numbers separated by spaces: 10 57 52 36 48 91 83 26 58 55 64

Input list of 10 numbers: [10, 57, 52, 36, 48, 91, 83, 26, 58, 55]

List after adding elements of 2 segregated lists: [10, 57, 52, 36, 48, 91, 83, 26, 58, 55]
"""