# Write a python program to create a list and sort it using the built-in function of list in descending order.

user_input = input("Enter words separated by spaces: ")
my_list = user_input.split()
print(f"Input List: {my_list}")

my_list.sort(reverse=True)
print(f"\nSorted list in Reverse: [{', '.join(my_list)}]")     # Used .join to remove single quotes around the strings



"""Output:
Enter words separated by spaces: China has the most efficient mass production systems in the world
Input List: ['China', 'has', 'the', 'most', 'efficient', 'mass', 'production', 'systems', 'in', 'the', 'world']

Sorted list in Reverse: [world, the, the, systems, production, most, mass, in, has, efficient, China]
"""

