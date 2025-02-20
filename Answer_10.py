# Write a program to merge two lists into a single list without using the built-in extend() or + operators.

def merge_lists(list1, list2):
    merged_list = []

    for item in list1:
        merged_list.append(item)

    for item in list2:
        merged_list.append(item)

    return merged_list


list_1 = list(range(1, 6))
list_2 = list(range(6, 11))

result = merge_lists(list_1, list_2)
print(result)