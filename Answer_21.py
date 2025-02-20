# Write a program to create a list of 5 strings and print the list after removing all the vowels from each string.

user_input = input("Enter up to 5 words separated by spaces: ")
my_list = user_input.split()[:5]
print("\nThe list generated from words entered:", my_list)

vowels = "aeiou"
consonant_list = []

for char in my_list:
    consonant_string = ''
    for i in char:
        if i.lower() not in vowels:
            consonant_string = consonant_string + i
    consonant_list.append(consonant_string)


print(f"\nList after removing vowels from words: {consonant_list}")



"""Output:
Enter up to 5 words separated by spaces: Action speaks louder than words

The list generated from words entered: ['Action', 'speaks', 'louder', 'than', 'words']

List after removing vowels from words: ['ctn', 'spks', 'ldr', 'thn', 'wrds']
"""
