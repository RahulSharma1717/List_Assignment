# Write a program to create a list of 5 strings and print the list after removing all the vowels from the first and last strings in the list.

user_input = input("Enter 5 words separated by spaces: ")
my_list = user_input.split()[:5]
print("\nThe list generated from words entered:", my_list)

def filter_vowels(char):
    vowels = "aeiou"
    consonant_string = ''

    for i in char:
        if i.lower() not in vowels:
            consonant_string = consonant_string + i

    return consonant_string

my_list[0] = filter_vowels(my_list[0])
my_list[-1] = filter_vowels(my_list[-1])

print("\nUpdated list after removing vowels from first and last string:", my_list)


"""Output:
Enter 5 words separated by spaces: Action speaks louder than words

The list generated from words entered: ['Action', 'speaks', 'louder', 'than', 'words']

Updated list after removing vowels from first and last string: ['ctn', 'speaks', 'louder', 'than', 'wrds']
"""

# The above code can be used to filter vowels for any number of words from any length of sentence.

