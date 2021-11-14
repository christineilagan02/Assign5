# Create a program that will ask for grade percentage. 
# Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good
# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed

import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

_grade = float(input("Grade: "))
grade = round_half_up(_grade)

if grade >= 97 and grade <= 100:
    print("Excellent! Your grade is 1.0!")
elif grade >= 94 and grade <= 96:
    print("Excellent! Your grade is 1.25!")
elif grade >= 91 and grade <= 93:
    print("Very Good! Your grade is 1.5!")
elif grade >= 88 and grade <= 90:
    print("Very Good! Your grade is 1.75!")
elif grade >= 85 and grade <= 87:
    print("Good! Your grade is 2.0!")
elif grade >= 82 and grade <= 84:
    print("Good! Your grade is 2.25!")
elif grade >= 79 and grade <= 81:
    print("Satisfactory! Your grade is 2.5!")
elif grade >= 76 and grade <= 78:
    print("Satisfactory! Your grade is 2.75!")
elif grade == 75:
    print("Passing! Your grade is 3.0!")
elif grade >= 65 and grade <= 74:
    print("Failure, better luck next time. Your grade is 5.0.")
else:
    print("Your grade is either Inc. means Incomplete, W means Withdrawn, or D means Dropped")

print("Your grade has been recorded!")