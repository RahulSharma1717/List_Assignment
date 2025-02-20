# Write a program to create a list of 5 strings and print the list after reversing each string in the list.

user_input = input("Enter up to 5 words separated by spaces: ")
my_list = user_input.split()[:5]
print("\nThe list generated from words entered:", my_list)

reversed_string = []

for char in my_list:
    reversed_string.append(char[::-1])

print("\nList after reversing the input words:", reversed_string)



"""Output:
Enter up to 5 words separated by spaces: Action speaks louder than words

The list generated from words entered: ['Action', 'speaks', 'louder', 'than', 'words']

List after reversing the input words: ['noitcA', 'skaeps', 'reduol', 'naht', 'sdrow']
"""