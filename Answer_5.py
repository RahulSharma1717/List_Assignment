# Take a sentence from user and print only those words which are of even length.

user_input = input("Enter a sentence: ")
words = user_input.split()

selected_words = []

for i in words:
    if len(i) % 2 == 0:
        selected_words.append(i)

print(f"The words with even number of alphabets are {selected_words}")



"""Output:
Enter a sentence: the scholarship provided to the student was enough to cover his tuition fee and hostel expenses
The words with even number of alphabets are ['provided', 'to', 'enough', 'to', 'tuition', 'hostel', 'expenses']
"""