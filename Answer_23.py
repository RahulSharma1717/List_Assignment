# Take a sentence from user and print each word separated by ,

user_input = input("Enter a sentence: ")
words = ', '.join(user_input.split())
print("\nWords of sentence separated by , are:", words)


"""Output:
Enter a sentence: Sweet are the fruits of adversity

Words of sentence separated by , are: Sweet, are, the, fruits, of, adversity
"""