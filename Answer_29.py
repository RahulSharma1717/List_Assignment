# Take a sentence from user and create a list and print the list of first letter of each word in the first list.

user_input = input("Enter words separated by spaces: ")
my_list = user_input.split()
print("\nThe list generated from words entered:", my_list)

first_character_list = []

for word in my_list:
    first_character_list.append(word[0])

print("\nThe first letter of each alphabet of sentence is:", first_character_list)


"""Output:
Enter words separated by spaces: Indian markets are falling as a result of FII's seeling their shares, as the latter wish to invest in more attractive US Bond Market

The list generated from words entered: ['Indian', 'markets', 'are', 'falling', 'as', 'a', 'result', 'of', "FII's", 'seeling', 'their', 'shares,', 'as', 'the', 'latter', 'wish', 'to', 'invest', 'in', 'more', 'attractive', 'US', 'Bond', 'Market']
The first letter of each alphabet of sentence is: ['I', 'm', 'a', 'f', 'a', 'a', 'r', 'o', 'F', 's', 't', 's', 'a', 't', 'l', 'w', 't', 'i', 'i', 'm', 'a', 'U', 'B', 'M']
"""