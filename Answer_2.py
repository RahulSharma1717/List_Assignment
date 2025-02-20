# Take name of five fruit from user through loop and store into a bucket made by list and print name of each fruit in the bucket.

i = 0
bucket = []

while i < 5:
    user_input = input("Enter the name of a fruit: ")
    bucket.append(user_input)
    i += 1

print()
print(f"The fruits entered by user are {bucket}")
print()

fruits = ""
for fruit in bucket:
    fruits += fruit + ' '

print(f"Fruits extracted from bucket are {fruits}")


"""Output:
Enter the name of a fruit: banana
Enter the name of a fruit: apple
Enter the name of a fruit: mango
Enter the name of a fruit: guava
Enter the name of a fruit: orange

The fruits entered by user are ['banana', 'apple', 'mango', 'guava', 'orange']

Fruits extracted from bucket are banana apple mango guava orange 
"""
