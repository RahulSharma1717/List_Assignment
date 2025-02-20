# Write a Python program that asks the user to enter a sentence and then prints the words in the sentence in alphabetical order.

user_input = input("Enter a sentence: ").lower()
words_in_sentence = user_input.split()
sorted_sentence = sorted(words_in_sentence)
print(f"The sentence after sorting: {sorted_sentence}")


"""Output:
Enter a sentence: The witty fox jumps over the lazy dog
The sentence after sorting: ['dog', 'fox', 'jumps', 'lazy', 'over', 'the', 'the', 'witty']
"""