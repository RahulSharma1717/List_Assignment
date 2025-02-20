# Write a python program to find the common elements between two lists

def common_elements(list_1, list_2):
    common_list = []
    for element in list_1:
        if element in list_2:
            common_list.append(element)
    return f"The common elements among the two input lists is {common_list}"

user_input_1 = input("Enter items for first list separated by spaces: ")
my_list_1 = user_input_1.split()
print('First List:', my_list_1)
print()

user_input_2 = input("Enter items for second list separated by spaces: ")
my_list_2 = user_input_2.split()
print('Second List:', my_list_2)
print()

common = common_elements(my_list_1, my_list_2)
print(common)


"""Output:
Enter items for first list separated by spaces: There are 28 states and 8 union territories in India in 2025
First List: ['There', 'are', '28', 'states', 'and', '8', 'union', 'territories', 'in', 'India', 'in', '2025']

Enter items for second list separated by spaces: There used to be 25 states and 7 union territories before the start of 21st century
Second List: ['There', 'used', 'to', 'be', '25', 'states', 'and', '7', 'union', 'territories', 'before', 'the', 'start', 'of', '21st', 'century']

The common elements among the two input lists is ['There', 'states', 'and', 'union', 'territories']
"""

"The single quotes in the list, after using split function can be removed. But i am keeping the quotes in this exercise"