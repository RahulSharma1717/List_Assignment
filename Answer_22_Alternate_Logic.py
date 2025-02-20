# Here i will be adding one number at a time at the beginning with the help of loop and keep sorting the row as it grows

try:
    my_list = []
    i = int(input("Enter how many numbers you want in the list: "))

    while i > 0:
        user_input = int(input("Enter a number: "))
        my_list.insert(0, user_input)
        print(my_list)
        my_list.sort()
        print(my_list)
        i -= 1

    print("The final list received after all the insertion and sorting:", my_list)

except ValueError:
    print("Invalid Input!, Enter a numeric value")


"""Output:
Enter how many numbers you want in the list: 12
Enter a number: 15
Enter a number: 96
Enter a number: 31
Enter a number: 03
Enter a number: 08
Enter a number: 25
Enter a number: 47
Enter a number: 61
Enter a number: 35
Enter a number: 22
Enter a number: 10
Enter a number: 20
The final list received after all the insertion and sorting: [3, 8, 10, 15, 20, 22, 25, 31, 35, 47, 61, 96]
"""

"""Output:
Enter how many numbers you want in the list: 4
Enter a number: 21
[21]
[21]
Enter a number: 10
[10, 21]
[10, 21]
Enter a number: 52
[52, 10, 21]
[10, 21, 52]
Enter a number: 63
[63, 10, 21, 52]
[10, 21, 52, 63]
The final list received after all the insertion and sorting: [10, 21, 52, 63]
"""



