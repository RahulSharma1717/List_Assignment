# Create a list of five strings and print the length of each string.

user_input = input("Enter up to 5 words separated by spaces: ")
my_list = list(map(str, user_input.split()[:5]))

print()
print("List of five words:", my_list)
print()

for word in my_list:
    print(f"Number of alphabets in '{word}' are {len(word)}")


"""Output:
Enter up to 5 words separated by spaces: distribution wealth concentrated among powerful people

List of five words: ['distribution', 'wealth', 'concentrated', 'among', 'powerful']

Number of alphabets in 'distribution' are 12
Number of alphabets in 'wealth' are 6
Number of alphabets in 'concentrated' are 12
Number of alphabets in 'among' are 5
Number of alphabets in 'powerful' are 8
"""