# Write a python program to remove duplicates from a list.

list_numbers = [1, 2, 3, 9, 4, 2, 3, 1, 4, 6, 7, 9, 6, 5]
print(f"Input list: {list_numbers}")
print()
filtered_list = []

for i in list_numbers:
    if i not in filtered_list:
        filtered_list.append(i)

print(f"List of numbers after removing duplicates is {filtered_list}")
