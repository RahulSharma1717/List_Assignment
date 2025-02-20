# Write a program to create a list of 5 strings and print the list after removing all the strings which have a length less than the average length of all the strings in the list.

user_input = input("Enter words separated by spaces: ")
my_list = user_input.split()
print("\nThe list generated from words entered:", my_list)

word_length = 0

for words in my_list:
    word_length = word_length + len(words)

average_len = word_length / len(my_list)      # After making code work for 5 words, now have modified the code to run on sentence of any length

filtered_list = []

for words in my_list:
    if len(words) >= average_len:
        filtered_list.append(words)

print("\nWords with length greater than average word length are: ", filtered_list)


"""Output:
Enter up to 5 words separated by spaces: Action speaks louder than words

The list generated from words entered: ['Action', 'speaks', 'louder', 'than', 'words']

Words with length greater than average word length are:  ['Action', 'speaks', 'louder']
"""

"""Output:
Enter words separated by spaces: China has the most efficient mass production systems in the world

The list generated from words entered: ['China', 'has', 'the', 'most', 'efficient', 'mass', 'production', 'systems', 'in', 'the', 'world']

Words with length greater than average word length are:  ['China', 'efficient', 'production', 'systems', 'world']
"""

