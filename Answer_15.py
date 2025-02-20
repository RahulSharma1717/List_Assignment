# Write a program to store average marks of 10 students in a list and print the number of students falling the following categories in two columns:
#         Average Marks                                                     Number of Students
#            1 - 30                                                                 xx
#            31 - 50                                                                xx
#            51 - 70                                                                xx
#            71 - 85                                                                xx
#            86 - 100                                                               xx

import sys

try:
    user_input = input("Enter the average marks of 10 students separated by spaces: ")
    my_list = list(map(int, user_input.split()[:10]))
    grade_A = 0
    grade_B = 0
    grade_C = 0
    grade_D = 0
    grade_E = 0

    for marks in my_list:
        if 1 <= marks <= 30:
            grade_E += 1
        elif 31 <= marks <= 50:
            grade_D += 1
        elif 51 <= marks <= 70:
            grade_C += 1
        elif 71 <= marks <= 85:
            grade_D += 1
        elif 86 <= marks <= 100:
            grade_A += 1
        else:
            print("Please enter marks in between 1-100")
            sys.exit()

    print(f"""             Average Marks             Number of Students
                1 - 30                           {grade_E}
                31 - 50                          {grade_D}
                51 - 70                          {grade_C}
                71 - 85                          {grade_B}
                86 - 100                         {grade_A}""")

except ValueError:
    print("Invalid Input, Enter numeric values")



"""Output:
Enter the average marks of 10 students separated by spaces: 85 21 33 47 56 89 64 45 82 76 51 63
             Average Marks             Number of Students
                1 - 30                           1
                31 - 50                          6
                51 - 70                          2
                71 - 85                          0
                86 - 100                         1
"""

"""Output:
Enter the average marks of 10 students separated by spaces: 52 34 78 96 456 65 159 53 75 423
Please enter marks in between 1-100
"""