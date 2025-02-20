# Create a list of ten numbers and print only the even numbers in the list.

user_input = input("Enter up to 10 numbers separated by spaces: ")
my_list = list(map(int, user_input.split()[:10]))

print("List of integers:", my_list)

numbers = ""

for number in my_list:
    if number % 2 == 0:
        numbers += str(number) + ' '

print(f"Even numbers among the input are {numbers}")



"""Output:
Enter up to 10 numbers separated by spaces: 12 45 78 16 96 31 45 87 20 119 52
List of integers: [12, 45, 78, 16, 96, 31, 45, 87, 20, 119]
Even numbers among the input are 12 78 16 96 20 
"""