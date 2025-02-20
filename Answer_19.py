# Write a program to create a list of 5 numbers and print the list after replacing all the odd numbers with their squares.

try:
    user_input = input("Enter up to 5 numbers separated by spaces: ")
    my_list = list(map(int, user_input.split()[:5]))
    print(f"\nInput list of 5 numbers: {my_list}")
    new_list = []

    for num in my_list:
        if num % 2 == 0:
            new_list.append(num)
        else:
            new_list.append(num**2)

    print(f"\nThe updated list after squaring odd numbers: {new_list}")

except ValueError:
    print("Invalid Input!, Enter a numeric value")


"""Output:
Enter up to 5 numbers separated by spaces: 52 36 14 89 67 55

Input list of 5 numbers: [52, 36, 14, 89, 67]

The updated list after squaring odd numbers: [52, 36, 14, 7921, 4489]
"""