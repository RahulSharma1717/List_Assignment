# Given a list of strings, write a program to find the longest string in the list.

input_string = input("Enter a sentence: ").split()
longest_string = input_string[0]

for item in input_string:
    if len(item) > len(longest_string):
        longest_string = item

print(f"Longest word in the input sentence is '{longest_string}'")


"""Output:
Enter a sentence: the scholarship provided to the student was enough to cover his tuition fee and hostel expenses
Longest word in the input sentence is 'scholarship'
"""